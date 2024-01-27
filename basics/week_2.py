"""
A-Write a Python program to check if a number is a perfect square
"""

def find_perfect_square():

    def check(n):

        i = 0
        while i < n:
            if i*i == n:
                return True
            i+=1
        return False
    if check(36):
        print('It is a perfect square')
    else:
        print('It is NOT a perfect square')

find_perfect_square()

"""
B- Write a Python program to find a missing number from a list. 
Input : [1,2,3,4,6,7,8]
Output : 5
"""

def find_missing_number():

    lst = [1,2,3,4,6,7,8]
    missing_number = None 
    for i in range(len(lst)-1):
        if lst[i+1] != lst[i] + 1:
            missing_number = lst[i] + 1

    print(missing_number)

# find_missing_number()

"""
C- Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5
"""

def find_single_occurence():

    lst = [5, 3, 4, 3, 4]
    count_dict = dict()

    for i in lst:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1

    for k,v in count_dict.items():
        if v == 1:
            print(k)


# find_single_coourence()
