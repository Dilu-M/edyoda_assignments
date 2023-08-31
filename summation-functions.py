def sum_list_numbers():
    num_list = input("Enter a list of numbers separated by commas: ").split(',')
    num_list = [int(num) for num in num_list]
    total_sum = sum(num_list)
    return total_sum
result = sum_list_numbers()
print("Sum of the numbers:", result)
