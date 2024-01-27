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

def find_square_root(n) -> int:
    """
    function will accept a number assuming it is a perfect square (since it is returning a integer)
    returns None if not a perfect square
    return n**0.5
    """
    if n <= 0:
        raise Exception('Please provide number greater than 0')

    if n == 1:
        return 1

    for i in range(n):
        if i*i == n:
            return i

# print(find_square_root(15))


 
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

# print(check_geometric_progression([2, 6, 18, 54]))