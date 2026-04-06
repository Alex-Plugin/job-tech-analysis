# 🚀 Python Job Market Analysis — Ukraine Edition

## Description
Discover the current landscape of Python-related jobs in Ukraine!  
This project analyzes the most in-demand technologies for Python specialists using data  
from one of Ukraine's leading job websites: [work.ua](https://www.work.ua)

We collect job postings with web scraping and perform data analysis to identify trends in  
required skills, developer levels, salaries, and hiring companies.

## Stack
- requests – for making HTTP requests
- BeautifulSoup – for parsing HTML pages
- pandas – for data manipulation and aggregation
- matplotlib – for visualization

⚠️ Note: Job market data changes constantly, so insights may not reflect the full current state.

## 🔍 Key Insights at a Glance

## 📊 Top 20 Technologies

**Insight:**  
According to the results of this graph, we can conclude that most of the vacancies are for backend Python  
developers, since we see in the top 10 technologies such as Django, REST API, FastAPI, Docker, JavaScript,  
Flask, Redis and PostgreSQL, which are typical for backend developer positions.

<img src="data/plots/top_technologies.png" width="600">


## 📊 Vacancies by City

**Insight:**  
The distribution of Python vacancies across Ukrainian cities follows the expected pattern for major urban  
centers: Kyiv, Kharkiv, Lviv, and Dnipro occupy the top spots. These are the largest cities by population  
and business activity.  
However, there are some unusual observations: over 50% of developers are concentrated in Kyiv, and  
surprisingly, Ternopil ranks fifth. Ivano-Frankivsk and Uzhgorod occupy the sixth and seventh positions,  
respectively. This can be explained by the relocation of many IT companies from eastern regions such as  
Kharkiv and Dnipro to western Ukraine and Kyiv, as these areas are safer and further from the conflict  
zones. Consequently, cities like Lviv, Ivano-Frankivsk, and Ternopil have seen an increase in IT  
opportunities.

<img src="data/plots/vacancies_by_cities.png" width="600">

## Average Salary by Level

**Insight:**

Weak correlation observed
Likely caused by:
- mixed Python roles (backend, data analytics, data science, education)
- inconsistent level labeling
- small sample size per level

<img src="data/plots/average_salary_by_level.png" width="600">

## Number of Vacancies by Developer Level

**Insight:**
Data is available for only 22 out of 70 vacancies, as most job postings do not specify the level required.  
Nevertheless, it shows that the market roughly requires developers across all levels: from Intern to Senior.

⚠️ Note: The data is incomplete, so the chart and table reflect only the available subset of the market.

<img src="data/plots/vacancies_quantity_by_level.png" width="600">

## Top 10 companies by number of vacancies

**Insight:**

Most of the companies in Ukraine looking for specialists with Python as a main skill are software development  
companies, which explains the high demand for backend developers.  
Additionally, we can see that one EdTech company is searching for Python teachers, totaling 3 vacancies.  
However, it is difficult to identify the demand for data analytics and data science roles from this top stack,  
because technologies like Pandas, Matplotlib, NumPy, PowerBI, and Tableau do not appear in the top 20.

<img src="data/plots/top_companies.png" width="600">
