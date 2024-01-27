"""
Write a Python program to find all the numbers from 0-9 from a string:

input: '89ADFRE41'

Output :[8941]
"""

def find_numbers_from_str(s):
    number = 0
    for i in s:
        try:
            n = int(i)
            number = number * 10 + n
        except Exception as e:
            pass
    return [number]

# print(find_numbers_from_str('89ADFRE41'))



"""
Write a Python program to find two elements once in a list where every element appears exactly n times in the list. 
Input : [1, 2, 1, 3, 2, 5], 2    (n=2)
Output :[5, 3]
"""


"""
 Write a Python program to reverse the digits of an integer. 
Input : 234
Input : -234
Output: 432
Output : -432
"""

def reverse_digit(num):

    is_negetive = num < 0 
    if is_negetive:
        num *= -1
    rev = 0
    while num > 0:
        last = num % 10
        num //= 10
        rev = rev * 10 + last
    if is_negetive:
        return rev * -1
    return rev

# print(reverse_digit(-234))