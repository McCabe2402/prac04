class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2023  # Assuming the current year is 2023
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


# Testing the Guitar class
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar1)
print(f"The guitar is {guitar1.get_age()} years old.")
print(f"Is the guitar vintage? {guitar1.is_vintage()}")
