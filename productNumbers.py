def product_of_all_other_numbers(arr):
    # Numbers returned are the product of all numbers in array except the number at that index
    #check if there is one built in function to multiply all elements in array
    #loop through array to acces each number
    #variable to hold the current index
    
    final_array = []
    for index, number in enumerate(arr): #O(n)
        product = 1
        for index2, number2 in enumerate(arr): #O(n)
            if not index2 == index:
                product = product * arr[index2]
        final_array.append(product)

    return final_array

arr = [1, 3, -1, -3, 5, 3, 6, 7]
arr2 = [2,1,4]
print(product_of_all_other_numbers(arr2))