ascii_dict = {}
for letter in range(ord('a'), ord('z') + 1):
    ascii_dict[chr(letter)] = letter
keys = input("Enter alphabet letters (a-z) without spaces: ")
print("Corresponding ASCII Values:")
for key in keys:
    if key.isalpha() and key.lower() in ascii_dict:
        print(f"{key}: {ascii_dict[key.lower()]}")
    else:
        print(f"{key}: Not a valid alphabet letter.")


