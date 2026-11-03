from load_csv import load_csv
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Preprocesses the population string to convert it into a float value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    Loads population data from a CSV file,
    filters it for specific countries, preprocesses the population values,
    """
    data = load_csv("population_total.csv")

    campus = "France"
    country = "Norway"

    campus_data = data[data['country'] == campus].iloc[:, 1:]
    country_data = data[data['country'] == country].iloc[:, 1:]

    campus_pop = campus_data.values.flatten()
    country_pop = country_data.values.flatten()
    years = campus_data.columns.astype(int)

    campus_pop = [preprocess_population(pop) for pop in campus_pop]
    country_pop = [preprocess_population(pop) for pop in country_pop]
    plt.plot(years, campus_pop, label=campus)
    plt.plot(years, country_pop, label=country)

    plt.title("Population in {} and {}".format(campus, country))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(campus_pop), max(country_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()
