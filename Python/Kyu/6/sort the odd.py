# test code

source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def sort_array(source_array):

    """
    You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.


    Examples

    [7, 1]  =>  [1, 7]
    [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
    """
    odd_lst = []

    for i in source_array:
        if i % 2 !=0:
            odd_lst.append(i)
    
    for index, value in enumerate(source_array):
        if value % 2 != 0:
            source_array[index] = 'pos'
    
    odd_lst.sort()

    replacement_odd_sort = iter(odd_lst)

    new_source_array = [x if x != 'pos' else next(replacement_odd_sort) for x in source_array]

    return new_source_array

print(sort_array(source_array))

"""

source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

odd_lst = []

for i in source_array:
    # print(f"ith pos: {source_array[i]} with val {i}")
    if i % 2 !=0:
        odd_lst.append(i)

for index, value in enumerate(source_array):
    if value % 2 !=0:
        source_array[index] = 'pos'

print(source_array)
print(odd_lst)
odd_lst.sort()
print(odd_lst)

replacement_odd_sort = iter(odd_lst)

new_source_array = [x if x != 'pos' else next(replacement_odd_sort) for x in source_array]

print(new_source_array)

"""