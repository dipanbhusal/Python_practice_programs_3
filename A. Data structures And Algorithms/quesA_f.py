# f) Binary Search

def binary_search(list_of_items, lower, upper, item_to_find):
    if upper >= 1:
        mid = (lower + upper) // 2

        if list_of_items[mid] == item_to_find:
            return mid 
        elif list_of_items[mid] > item_to_find:
            return binary_search(list_of_items, lower, mid -1, item_to_find )
        else:
            return binary_search(list_of_items, mid + 1, upper, item_to_find)

input_list = [3,5,6,7,8,10,25,18]
upper = len(input_list) - 1 

result = binary_search(input_list, 0, upper, 8)
print(result)