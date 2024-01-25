"""
Write a Python program to find the single element in a list where every element appears multiple times except for one.
Input : [5, 3, 4, 3, 5, 5, 3],
Output : 4
"""

def find_single_occurence(lst):

    count_dict = dict()

    for i in lst:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1

    for k,v in count_dict.items():
        if v == 1:
            print(k)


# find_single_occurence([5, 3, 4, 3, 5, 5, 3])


"""
Write a Python program to compute and return the square root of a given 'integer'. 
Input : 16
Output : 4
Note : The returned value will be an 'integer', do not use square root functions from python.
"""




 
"""
Write a Python program to check a sequence of numbers is a geometric progression or not. 
Input : [2, 6, 18, 54]
Output : True
"""

def check_geometric_progression(lst):
    diff = 0
    for i in range(len(lst) -1):
        if diff == 0:
            diff = lst[i+1] // lst[i]
        else:
            if not lst[i+1] // lst[i] == diff:
                return False
    return True

print(check_geometric_progression([2, 6, 18, 54]))