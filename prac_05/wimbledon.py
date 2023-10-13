import csv


def read_wimbledon_data(filename):
    wimbledon_data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            year = row["Year"]
            champion = row["Champion"]
            wimbledon_data.append((year, champion))

    return wimbledon_data


def count_wimbledon_champions(data):
    champion_count = {}

    for _, champion in data:
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1

    return champion_count


def list_countries(data):
    countries = set()

    for _, champion in data:
        country = champion.split()[-1]
        countries.add(country)

    return sorted(countries)


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)

    champion_count = count_wimbledon_champions(wimbledon_data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    countries = list_countries(wimbledon_data)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)


if __name__ == "__main__":
    main()
