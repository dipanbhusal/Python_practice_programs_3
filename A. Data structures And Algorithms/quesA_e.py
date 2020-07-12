#e. Linear Search

def linear_search(list_of_items, item_to_find):
    for index in range(0,len(list_of_items)):
        if item_to_find == list_of_items[index]:
            return index 

result = linear_search([4,6,8,5,1,4,7], 5)
print(result) 