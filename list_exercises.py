# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
user_input = input("Enter your username: ")

# Check if the entered username is in the list of authorized users
if user_input in usernames:
    print("Access granted")

    # Initialize an empty list to store the numbers
    numbers = []

    # Prompt the user for 5 numbers and add them to the list
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Calculate the required information
    min_num = min(numbers)
    max_num = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Output the information
    print(f"Numbers: {numbers}")
    print(f"Minimum: {min_num}")
    print(f"Maximum: {max_num}")
    print(f"Sum: {total}")
    print(f"Average: {average}")

else:
    print("Access denied")
