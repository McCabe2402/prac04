class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


# Program
if __name__ == "__main__":
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    # Creating a list of existing ProgrammingLanguage objects
    programming_languages = [python, ruby, visual_basic]

    # Printing the list
    for language in programming_languages:
        print(language)

    # Printing dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)
