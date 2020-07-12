# f) Interpolation Search

def interpolation_search(list_of_items, lower, higher, item_to_find):
    
    
    if (lower <= higher and item_to_find >= list_of_items[lower]  and item_to_find <= list_of_items[higher]):
        

        position = lower + ((higher - lower) // (list_of_items[higher] - list_of_items[lower]) * (item_to_find - list_of_items[lower]))
        if list_of_items[position] == item_to_find:
            return position
        elif list_of_items[position] < item_to_find:
            return interpolation_search(list_of_items,position +1, higher, item_to_find )
        else:
            return interpolation_search(list_of_items,lower,  position-1, item_to_find)
    return -1 

input_list = [2,3,5,6,8,10,12,13]
lower = 0
higher = len(input_list) - 1 
result = interpolation_search(input_list,lower, higher, 13)
print(result)  
    