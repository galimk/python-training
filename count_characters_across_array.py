from array import array

test_array = ["ab", "c", "def", "ghij"]


def count_number_of_characters(arr: list):
    if len(arr) == 1:
        return len(arr[0])
    else:
        return len(arr[0]) + count_number_of_characters(arr[1:len(arr)])


print(f'Number of characters across the array is {count_number_of_characters(test_array)}')
