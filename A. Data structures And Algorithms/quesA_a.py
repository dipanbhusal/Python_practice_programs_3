# a) Bubble Sort

def bubble_sort(unsorted_list):
    len_of_list = len(unsorted_list)
    for i in range(len_of_list):
        for j in range(0,len_of_list-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list
unsorted_list = [5,4,3,2,1,0]
res = bubble_sort(unsorted_list)

print(res)
