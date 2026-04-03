def digital_root(n):
    """
    
    Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

    16  -->  1 + 6 = 7
    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
    493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
    
    """

    n_lst = []

    for i in str(n):
        n_lst.append(int(i))

    n_lst_sum = sum(n_lst)
    n_lst_sum_len = len(str(n_lst_sum))

    while n_lst_sum_len >= 2:
        n = n_lst_sum
        n_lst = []
        for i in str(n):
            n_lst.append(int(i))
            if len(str(n_lst)) >= 2:
                n_lst_sum = sum(n_lst)
                n = n_lst_sum
                n_lst_sum_len = len(str(n_lst_sum))
            elif len(str(n_lst)) == 1:
                n_lst_sum = sum(n_lst)
                n = n_lst_sum
                n_lst_sum_len = len(str(n_lst_sum))
            
    if n_lst_sum_len == 1:
        return n_lst_sum


"""

### Code Test Block ###

n = 493193
n_lst = []

for i in str(n):
    n_lst.append(int(i))

n_lst_sum = sum(n_lst)

n_lst_sum_len = len(str(n_lst_sum))

# print(n_lst_sum)
# print(n_lst_sum_len)



while n_lst_sum_len >= 2:
    n = n_lst_sum
    n_lst = []
    for i in str(n):
        n_lst.append(int(i))
        # print(n_lst)
        if len(str(n_lst)) >= 2:
            n_lst_sum = sum(n_lst)
            n = n_lst_sum
            n_lst_sum_len = len(str(n_lst_sum))
            # print(n_lst_sum)
            # print(n)
        elif len(str(n_lst)) == 1:
            n_lst_sum = sum(n_lst)
            n = n_lst_sum
            n_lst_sum_len = len(str(n_lst_sum))
            # print(n_lst_sum)
            # print(n)

if n_lst_sum_len == 1:
    print(n_lst_sum)

"""