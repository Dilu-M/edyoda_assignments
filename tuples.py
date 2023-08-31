def sort_tuples_by_last_element(input_list):
    sorted_list = sorted(input_list, key=lambda x: x[-1])
    return sorted_list
num_tuples = int(input("Enter the number of tuples: "))
input_tuples = []
for _ in range(num_tuples):
    tuple_str = input("Enter a tuple (comma-separated elements): ")
    tuple_elements = tuple(map(int, tuple_str.split(',')))
    input_tuples.append(tuple_elements)
sorted_tuples = sort_tuples_by_last_element(input_tuples)
print("Sorted Tuples:", sorted_tuples)


