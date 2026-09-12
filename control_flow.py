# control_flow.py
# Shows if/elif/else, for, while, and a list comprehension.

x = int(input("Enter an integer: "))

# if / elif / else
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# for loop
print("Numbers 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

# while loop
count = 0
while count < 3:
    print("Count is", count)
    count += 1

# list comprehension
squares = [n * n for n in range(6)]
print("Squares:", squares)
