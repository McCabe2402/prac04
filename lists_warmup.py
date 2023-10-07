"""

numbers = [3, 1, 4, 1, 5, 9, 2]
What values do the following expressions have?

"""

# 1. numbers[0]
# 2. numbers[-1]
# 3. numbers[3]
# 4. numbers[:-1]
# 5. numbers[3:4]
# 6. 5 in numbers
# 7. 7 in numbers
# 8. "3" in numbers
# 9. numbers + [6, 5, 3]

# 1. The first element of the list "numbers" is 3.
# 2. The last element of the list "numbers" is 2.
# 3. The fourth element of the list "numbers" is 1.
# 4. It will be [3, 1, 4, 1, 5, 9].
# 5. It will be [1].
# 6. The value 5 is present in the list "numbers," so this expression evaluates to True.
# 7. The value 7 is not present in the list "numbers," so this expression evaluates to False.
# 8. The string "3" is not present in the list "numbers," so this expression evaluates to False.
# 9. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

"""
In the same Python file, write statements to achieve the following:

Change the first element of numbers to "ten" (the string, not the number 10)
Change the last element of numbers to 1
Print all the elements from numbers except the first two (slice)
Print whether 9 is an element of numbers
"""

# Given list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
