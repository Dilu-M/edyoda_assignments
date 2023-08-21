# Get a series of numbers from the user, separated by spaces
numbers = input("Enter a series of numbers separated by spaces: ")

# Split the input into individual numbers
number_list = numbers.split()

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Initialize lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the numbers using a while loop
i = 0
while i < len(number_list):
    num = int(number_list[i])
    if num % 2 == 0:
        even_count += 1
        even_numbers.append(num)
    else:
        odd_count += 1
        odd_numbers.append(num)
    i += 1

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)