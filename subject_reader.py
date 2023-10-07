"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from a file formatted like: subject,lecturer,number of students."""
    FILENAME = "subject_data.txt"  # Replace with the actual file name
    data_list = []

    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data_list.append(parts)

    return data_list


def display_subject_details(data):
    for subject_info in data:
        subject, lecturer, students = subject_info
        print(f"{subject} is taught by {lecturer} and has {students} students")


main()
