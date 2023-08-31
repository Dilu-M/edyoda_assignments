def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
user_input = input("Enter a string: ")
upper_result, lower_result = count_upper_lower(user_input)
print("Number of uppercase letters:", upper_result)
print("Number of lowercase letters:", lower_result)
