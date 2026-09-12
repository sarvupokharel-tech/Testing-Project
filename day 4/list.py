# list.py
# Lists are ordered, changeable, and allow duplicates.

numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

print(numbers)
print(names)

print(numbers[0])
print(names[1])

numbers.append(6)
print(numbers)

numbers.remove(3)
print(numbers)

print(len(numbers))