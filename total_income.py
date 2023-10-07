"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    report = generate_report(num_months, incomes)
    print_report(report)


def generate_report(num_months, incomes):
    """Generate the income report as a list of formatted strings."""
    report = []
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        report_line = f"Month {month:2} - Income: ${income:10.2f}"
        report.append(report_line)
    return report


def print_report(report):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for line in report:
        total += float(line.split()[-1].replace('$', ''))
        print(line + f" Total: ${total:10.2f}")


main()
