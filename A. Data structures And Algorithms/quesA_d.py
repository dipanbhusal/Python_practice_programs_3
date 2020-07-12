# d) Merge Sort

def merge_sort(list_of_items):
    if len(list_of_items) > 1:
        mid_value = len(list_of_items) // 2
        left_half = list_of_items[:mid_value]
        right_half = list_of_items[mid_value:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_of_items[k] = left_half[i]
                i += 1
            else:
                list_of_items[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list_of_items[k] = left_half[i]
            i += 1
            k += 1 
        while j < len(right_half):
            list_of_items[k] = right_half[j]
            j += 1
            k += 1 
    
list_input = [8,7,5,3,7,9,4,1,0]
merge_sort(list_input)
print(list_input)