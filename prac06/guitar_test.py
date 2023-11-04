class Guitar:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


# Test scenario
if __name__ == '__main__':
    # Create an instance of the Guitar class
    guitar1 = Guitar("My Guitar", 1923)

    # Test the is_vintage() method
    current_year = 2023
    expected_result = True
    actual_result = guitar1.is_vintage(current_year)

    print(f"{guitar1.get_age(current_year)}-year old guitar is_vintage() - Expected {expected_result}. Got {actual_result}")
