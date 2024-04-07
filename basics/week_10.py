"""
Q1) Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:

Input: num1 = "2", num2 = "3"

Output: "6"

"""

def long_multipication(num1, num2):
    if num1 ==0 or num2 == 0:
        return 0
    res = [0 for _ in range(len(num1) + len(num2)) ]
    m = len(num1)
    n = len(num2)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            p1, p2 =i+j, i+j+1
            sum = res[p2] + int(num1[i]) * int(num2[j])
            res[p2] = sum %10
            res[p1]+= sum//10

    return res

# long_multipication('12', '34')


"""
Q2) The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

"""

def count_and_say(n):
    res = '1'
    for _ in range(1, n):
        prev, count = '.', 0
        curr_str = ""
        for char in res:
            if char == prev or prev == '.':
                count += 1
            else:
                curr_str += str(count) + prev
                count = 1
            prev = char
        curr_str += str(count) + prev
        res = curr_str
    return res

print(count_and_say(5))