"""
Q1: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"

Output: false

Explanation: "raceacar" is not a palindrome.
"""
import re
def keep_alpha_neumeric(s):
    s = s.lower()
    return re.sub(r'[^a-z0-9]+', '', s)
    

def check_palindrome(s):
    s = keep_alpha_neumeric(s)
    if s == s[::-1]:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

# check_palindrome('race a car')

 
"""
Q2 Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]

Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]

Output: 2
"""

def find_majority(lst):
    i, votes = 0, 0
    candidate = -1
    for item in lst:
        if votes == 0:
            candidate = item
            votes += 1
        else:
            if item == candidate:
                votes +=1
            else:
                votes -=1
    
    if lst.count(candidate) > len(lst) // 2:
        return candidate
    else:
        return None


# print(find_majority([2,2,1,1,1,2,2]))




"""
Q3 Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 Example 1:

Input: n = 19

Output: true

Explanation:

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

Example 2:

Input: n = 2

Output: false
"""
