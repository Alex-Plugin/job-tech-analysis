import csv
from dataclasses import astuple, fields
import time
from urllib.parse import urljoin
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

from config import SEARCH_URL, BASE_URL, headers, PATH_CSV
from models import Vacancy
from vacancy_parser import parse_single_vacancy


VACANCY_FIELDS = [field.name for field in fields(Vacancy)]


def parse_single_page(page_soup: Tag) -> list[Vacancy]:
    vacancies = page_soup.select("div.card")
    result = []
    for vacancy in vacancies:
        parsed = parse_single_vacancy(vacancy)
        if parsed:
            result.append(parsed)

    return result


def write_vacancies_to_csv(vacancies: list[Vacancy], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(VACANCY_FIELDS)
        writer.writerows([astuple(vacancy) for vacancy in vacancies])
        # потом функция оркестратор вызовет write_vacancies_to_csv()
        # и передаст туда PATH_CSV и список vacancies


def get_all_page_vacancies() -> list[Vacancy]:
    all_vacancies = []
    next_url = SEARCH_URL
    visited = set()

    while next_url and next_url not in visited:
        visited.add(next_url) # this is a defense from infinite loop
        response = requests.get(next_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        all_vacancies.extend(parse_single_page(soup))
        print(f"Parsing page: {next_url}, found {len(all_vacancies)} total vacancies")

        next_href = get_next_page(soup)
        next_url = urljoin(BASE_URL, next_href) if next_href else None

        time.sleep(0.5)

    return all_vacancies


def get_next_page(soup) -> str | None:
    buttons = soup.select("ul.pagination a")

    for btn in buttons:
        if "Наступна" in btn.text:
            return btn.get("href")

    return None


def main():
    vacancies = get_all_page_vacancies()
    write_vacancies_to_csv(vacancies, PATH_CSV)


if __name__ == "__main__":
    main()
