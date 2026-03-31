from pathlib import Path

TECHNOLOGIES = [
    "Python", "Django", "Flask", "HTML", "CSS",
    "FastAPI", "Django Rest", "REST API",
    "C++", "JavaScript", "React", "asyncio", "Angular",
    "CI/CD", "Odoo", "TypeScript", "SOLID Principles",
    "Pandas", "NumPy", "Matplotlib", "TensorFlow", "PyTorch",
    "Selenium", "Beautiful Soup", "Scrapy",
    "SQL", "SQLAlchemy", "PostgreSQL", "SQLite", "MongoDB",
    "Redis", "Oracle", "NoSQL", "RabbitMQ", "GraphQL",
    "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Laravel",
    "Git", "GitHub", "Linux", "Ubuntu", "Raspberry Pi", "nginx",
    "Spark", "Hadoop", "OOP principles", "Celery", "PyTest",
    "LangChain", "LangGraph", "Alembic", "Agile", "Swagger",
]

LEVEL_MAP = {
    "intern": "Intern",
    "trainee": "Intern",
    "junior": "Junior",
    "jr": "Junior",
    "middle": "Middle",
    "mid": "Middle",
    "senior": "Senior",
    "sr": "Senior",
}

CITIES = [
    "Київ", "Харків", "Львів", "Одеса", "Дніпро", "Запоріжжя", "Вінниця",
    "Полтава", "Чернігів", "Черкаси", "Хмельницький", "Суми", "Луцьк",
    "Рівне", "Івано-Франківськ", "Тернопіль", "Житомир", "Миколаїв",
    "Херсон", "Кропивницький", "Ужгород", "Біла Церква", "Краматорськ",
    "Маріуполь", "Сєвєродонецьк", "Кам’янець-Подільський", "Бровари",
    "Слов’янськ", "Нікополь", "Кременчук"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

SEARCH_URL = "https://www.work.ua/jobs-python/" # this is search url where we get all the vacancies
BASE_URL = "https://www.work.ua"

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

PATH_CSV = DATA_DIR / "vacancies.csv"
PATH_GRAPH = DATA_DIR / "graph.png"
