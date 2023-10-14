"""
Program to count the occurrences of words in a string.

Time expected to finish: 10 minutes
Actual time taken: ~20 minutes
"""


def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def main():
    user_input = input("Please enter a string: ")
    word_count = count_word_occurrences(user_input)

    sorted_word_count = sorted(word_count.items())

    max_word_length = max(len(word) for word, _ in sorted_word_count)

    print("Text:", user_input)
    for word, count in sorted_word_count:
        print(f"{word:>{max_word_length}} : {count}")


if __name__ == '__main__':
    main()

