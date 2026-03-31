from typing import Optional
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

from config import BASE_URL, TECHNOLOGIES, LEVEL_MAP, CITIES, headers
from models import Vacancy


def parse_single_vacancy(vacancy_soup: Tag) -> Vacancy | None:
    title_tag = vacancy_soup.select_one("h2 a")
    if not title_tag:
        return None
    title = title_tag.text.strip()

    company_tag = vacancy_soup.select_one("div.mt-xs span.strong-600")
    company = company_tag.text.strip() if company_tag else ""

    location_block = vacancy_soup.select_one("div.mt-xs")
    location_text = (
        location_block.get_text(separator=" ", strip=True)
        if location_block else ""
    )
    location = extract_location(location_text)

    url = urljoin(BASE_URL, title_tag.get("href"))

    salary = parse_salary(vacancy_soup)

    detail_soup = get_vacancy_soup(url)
    description = parse_description(detail_soup)

    tech_block = extract_tech_block(detail_soup)
    technologies = extract_technologies(description, tech_block)

    level = extract_level(title, description)

    return Vacancy(
        title=title,
        company=company,
        location=location,
        url=url,
        description=description,
        technologies=technologies,
        salary=salary,
        level=level,
    )


def extract_location(block_text: str) -> str:
    for city in CITIES:
        if city in block_text:
            return city
    return ""


def get_vacancy_soup(url: str) -> BeautifulSoup:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def parse_description(soup: Tag) -> str:
    description = soup.select_one("div.company-description").text.strip()
    return description if description else ""


def parse_salary(vacancy_soup: Tag) -> Optional[float]:
    # in this function we get the average value of the salary range

    salary_tag = vacancy_soup.select_one("div > span.strong-600")

    if not salary_tag:
        return None

    text = salary_tag.text.lower()

    # defense if it is not a salary, but some text or something else,
    # we try to find "грн"
    if "грн" not in text:
        return None
    # we delete all the spaces - ordinary and non-breaking space, using \u202f
    text = text.replace(" ", "").replace("\u202f", "")
    # using lib re we are finding all numbers in this text
    numbers = re.findall(r"\d+", text)

    if not numbers:
        return None

    nums = list(map(int, numbers))
    return sum(nums) / len(nums)


def extract_tech_block(vacancy_soup: Tag) -> list[str]:
    tech_elements = vacancy_soup.select("ul.toggle-block li span.ellipsis")
    return [el.text.strip() for el in tech_elements]


def extract_technologies(description: str, tech_block: list[str]) -> list[str]:
    description_lower = description.lower()

    # we're searching technologies in the description
    # if the technology is in the description we add it to the set
    found_from_text = set()
    for tech in TECHNOLOGIES:
        if tech.lower() in description_lower:
            found_from_text.add(tech)

    # we're searching technologies from the block in a TECHNOLOGIES list
    # and creating a set
    found_from_block = {
        tech for tech in tech_block
        if tech in TECHNOLOGIES
    }
    # we merge two sets and make a list from them
    return list(sorted(found_from_text | found_from_block))


def extract_level(title: str, description: str) -> str:
    text = f"{title} {description}".lower()

    for key, value in LEVEL_MAP.items():
        if key in text:
            return value

    return ""
