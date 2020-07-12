# c) Quick Sort
def swap(a, b):
    a, b = b, a
    return (a,b)
def partition(list_of_items, lower, upper):
    pivot = list_of_items[upper]
    start = lower  - 1 
    for i in range(lower, upper):
        if (list_of_items[i] <= pivot):
            start += 1
        
            list_of_items[start], list_of_items[i] = list_of_items[i], list_of_items[start]
    list_of_items[start + 1 ], list_of_items[upper] =  swap(list_of_items[start+1], list_of_items[upper])
    return start + 1 

def quick_sort(list_of_items, lower, upper):
    if lower < upper:
        location  = partition(list_of_items, lower, upper)
        quick_sort(list_of_items, lower, location-1)
        quick_sort(list_of_items, location + 1, upper)
input_list = [9,6,5,0,3,1,6,4]
upper = len(input_list) 
lower = 0
quick_sort(input_list, lower, upper-1)
print(input_list)