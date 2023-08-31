def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
user_input = input("Enter a string: ")
reversed_result = reverse_string(user_input)
print("Reversed string:", reversed_result)
