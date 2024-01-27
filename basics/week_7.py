"""
Q1 )

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


def check_palindrome_number(num):
    temp = num
    rev = 0
    while temp > 0:
        last = temp % 10
        temp = temp // 10
        rev = rev * 10 + last
    if rev == num:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

check_palindrome_number(121)


"""
Q2)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"

Output: 3

Explanation: III = 3.

Input: s = "LVIII"

Output: 58

Explanation: L = 50, V= 5, III = 3.

MMMDCX -> 3610
"""

def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for a, b in zip(s, s[1:]):
        if roman[a] < roman[b]:
            ans -= roman[a]
        else:
            ans += roman[a]

    return ans + roman[s[-1]]

# print(roman_to_int('MMMDCX'))

