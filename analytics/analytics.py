import pandas as pd
import matplotlib.pyplot as plt

# top 20 technologies bar graph
# pie graph by cities
# salary depending on level
# quantity of vacancies depending on level
# correlation analysis
# top companies by quantity of vacancies

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv("../data/vacancies.csv")
    return df.dropna(subset=["technologies"]) # we make dataframe without NaN

# we create a function that converts str in technologies into
# a python list with technologies
def prepare_technologies(df: pd.DataFrame) -> pd.DataFrame:
    def parse_technologies(tech_str: str) -> list[str]:
        tech_str = tech_str.strip("[]")     # remove []
        tech_str = tech_str.replace("'", "")      # remove quotes
        # in return, we are creating a list with these technologies with help of
        # list generator
        return [t.strip() for t in tech_str.split(",") if t.strip()]

    # we convert every line of our technology dataframe
    df["technologies"] = df["technologies"].apply(parse_technologies)
    # we expand the list in every line into a column
    return df.explode("technologies")

# we count how many techonlogies we have in vacancies (top 20)
# it creates, in a result we get, object Series with index - name of
#technology and value counts of these technologies
def plot_top_technologies(df: pd.DataFrame):
    tech_counts = df["technologies"].value_counts().head(20)

    # we create a bar diagram
    # we can make it with this shortcut - tech_counts.plot(kind="bar")
    # but to make everything crear

    fig, ax = plt.subplots()

    ax.bar(tech_counts.index, tech_counts.values)

    ax.set_title("Top 20 Technologies")
    ax.set_xlabel("Technology")
    ax.set_ylabel("Count")

    ax.tick_params(axis="x", rotation=90)

    plt.tight_layout()
    plt.show()


def main():
    df = load_data("../data/vacancies.csv")
    df_exploded = prepare_technologies(df)
    plot_top_technologies(df_exploded)


if __name__ == "__main__":
    main()