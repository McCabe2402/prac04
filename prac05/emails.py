"""
Program to count the occurrences of words in a string.

Time expected to finish: 15 minutes
Actual time taken: ~20 minutes
"""




def extract_name(email):
    name = email.split('@')[0]
    name = ' '.join(name.split('.') + name.split('_'))
    name = name.title()
    return name


def main():
    user_dict = {}
    email = input("Please enter your email (or leave blank to exit): ")
    while email:
        name = extract_name(email)
        confirm_name = input(f"Is your name {name}? (Y/n) ")
        if confirm_name.lower() != 'y':
            name = input("Please enter your name: ")
        user_dict[email] = name
        email = input("Please enter your email (or leave blank to exit): ")

    print("Results:")
    for email, name in user_dict.items():
        print(f"{name} ({email})")


if __name__ == '__main__':
    main()