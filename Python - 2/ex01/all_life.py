from load_csv import load_csv
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data, filter for a country, and display a line graph.
    The graph includes a title, axis labels, legend, and grid.
    """
    dataset = load_csv("life_expectancy_years.csv")
    country_data = dataset[dataset['country'] == 'Afghanistan']
    years = country_data.columns[1:]
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy, label='Afghanistan')
    plt.title('Life Expectancy in this country over the years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
