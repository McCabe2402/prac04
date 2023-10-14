import csv


def read_csv_data(filename):
    champions_count = {}
    countries = set()
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        try:
            headers = next(reader)  # Skipping the header
            for row in reader:
                country = row[1]
                if country not in champions_count:
                    champions_count[country] = 0
                champions_count[country] += 1
                countries.add(country)
        except StopIteration:
            print("The CSV file is empty.")
    return champions_count, countries


def display_champions(champions_count):
    print("Wimbledon Champions: ")
    for champion, wins in champions_count.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    country_string = ", ".join(sorted(countries))
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(country_string)


def main():
    champions_count, countries = read_csv_data('champions.csv')
    if champions_count and countries:
        display_champions(champions_count)
        display_countries(countries)


if __name__ == "__main__":
    main()
