class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_cost(self):
        return self.cost

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


def main():
    guitars = []
    print("My guitars!")

    # For testing, using predefined data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    # User input commented out for testing purposes
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitars.append(Guitar(name, year, cost))
    #     print(f"{name} ({year}) : ${cost:.2f} added.\n")

    print("\nThese are my guitars:")
    current_year = 2023
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {i}: {guitar.get_name()} ({guitar.get_year()}), worth ${guitar.get_cost():8.2f}{vintage}")


if __name__ == '__main__':
    main()
