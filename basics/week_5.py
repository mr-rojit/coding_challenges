"""
You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.
"""

s='10'
beautiful = False
output=0

def check_beautiful(s):
    if(len(s)==2):
        if s[0]!=s[1]:
            return False
    else:
        for i in range (1, len(s)):
            if s[i] != s[0]:
                print(s[i])
                return False
    return True
    


def make_beautiful(s,output):
    if(len(s))<=2:
        output +=1
    else:
        for i in range(0,len(s)-1,2):
            if(s[i]!=s[i+1]):
                output += 1
    return (output)
    

        
if not check_beautiful(s):
    print(f'Output: {make_beautiful(s,output)}')
else:
    print(f'Output: {output}')
    
        


        
    
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