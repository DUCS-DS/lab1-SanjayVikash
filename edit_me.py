
def find_max(lst):
    """return the maximum element"""

    current_max = lst[0]
    for number in lst :
        if number > current_max :
            current_max = number

    

    return current_max

test_list = [2112*i % 2024 for i in range(10000)]
print("apple")
print(find_max(test_list))
