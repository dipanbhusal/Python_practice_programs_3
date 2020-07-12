# b) Insertion Sort

def insertion_sort(list_of_items):
    len_of_list = len(list_of_items)
    for i in range(0,len_of_list):
        key = list_of_items[i]
        j = i - 1
        while j >= 0 and list_of_items[j] > key:
            list_of_items[j+1] = list_of_items[j]
            j = j - 1
        list_of_items[j + 1] = key 
    return list_of_items

result = insertion_sort([2,5,4,3,1,9,0])
print(result)