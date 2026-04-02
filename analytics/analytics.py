import pandas as pd
import matplotlib.pyplot as plt

from config import PLOTS_DIR

# salary depending on level
# quantity of vacancies depending on level
# correlation analysis
# top companies by quantity of vacancies

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv("../data/vacancies.csv")
    return df.dropna(subset=["technologies"]) # we make dataframe without NaN

# # we create a function that converts str in technologies into
# # a python list with technologies
# def prepare_technologies(df: pd.DataFrame) -> pd.DataFrame:
#     def parse_technologies(tech_str: str) -> list[str]:
#         tech_str = tech_str.strip("[]")     # remove []
#         tech_str = tech_str.replace("'", "")      # remove quotes
#         # in return, we are creating a list with these technologies with help of
#         # list generator
#         return [t.strip() for t in tech_str.split(",") if t.strip()]
#
#     # we convert every line of our technology dataframe
#     df["technologies"] = df["technologies"].apply(parse_technologies)
#     # we expand the list in every line into a column
#     return df.explode("technologies")
#
# # we count how many techonlogies we have in vacancies (top 20)
# # it creates, in a result we get, object Series with index - name of
# #technology and value counts of these technologies
# def plot_top_technologies(df: pd.DataFrame):
#     tech_counts = df["technologies"].value_counts().head(20)
#
#     # we create a bar diagram
#     # we can make it with this shortcut - tech_counts.plot(kind="bar")
#     # but to make everything crear
#
#     fig, ax = plt.subplots()
#
#     ax.bar(tech_counts.index, tech_counts.values)
#
#     ax.set_title("Top 20 Technologies")
#     ax.set_xlabel("Technology")
#     ax.set_ylabel("Count")
#
#     ax.tick_params(axis="x", rotation=90)
#
#     plt.tight_layout()
#     plt.savefig(PLOTS_DIR / "top_technologies.png")
#     plt.show()


# def plot_vacancies_by_city(df: pd.DataFrame) -> None:
#     """
#     Builds the pie diagram and plots the vacancies by city.
#     """
#     # We count the quantity of vacancies in every city
#     city_counts = df["location"].value_counts()
#
#     # Create a figure
#     fig, ax = plt.subplots(figsize=(8, 8))
#     ax.pie(
#         city_counts.values,
#         labels=city_counts.index,
#         autopct='%1.1f%%',  # result in percents
#         startangle=90,      # we rotate the pie graph to start from the top
#         pctdistance=0.85
#     )
#     ax.set_title("Vacancies distribution by city")
#
#     # Save the graph
#     plt.savefig(PLOTS_DIR / "vacancies_by_cities.png")
#     print(f"Saved pie chart to {PLOTS_DIR}")


def plot_salary_from_level_dep(df: pd.DataFrame) -> None:
    """
    Counts average salary depending on the level and plots bar chart
    """
    # Clean data from NaN
    df_clean = df.dropna(subset=["salary", "level"])

    # Group by level and calculate average salary
    salary_level = df_clean.groupby("level")["salary"].mean()

    # Set correct order of levels
    order = ["Intern", "Junior", "Middle", "Senior"]
    salary_level = salary_level.reindex(order).dropna()

    # Build the graph
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(salary_level.index, salary_level.values)

    ax.set_title("Average Salary by Level")
    ax.set_xlabel("Level")
    ax.set_ylabel("Average salary")

    # Add values above bars
    for i, v in enumerate(salary_level.values):
        ax.text(i, v, f"{int(v)}", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "average_salary_by_level.png")
    plt.show()


def main():
    df = load_data("../data/vacancies.csv")
    # df_exploded = prepare_technologies(df)
    # plot_top_technologies(df_exploded)

    # df = df.dropna(subset=["location"])  # we delete all Nan from df
    # plot_vacancies_by_city(df)

    plot_salary_from_level_dep(df)



if __name__ == "__main__":
    main()