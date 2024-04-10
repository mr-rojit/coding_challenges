"""

Q1 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 Example 1:

Input: digits = [1,2,3]

Output: [1,2,4]

Explanation: The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.

Thus, the result should be [1,2,4].

"""

def increase_large_int(lst):
    n = len(lst)
    for i in range(n-1, -1, -1):
        lst[i] += 1
        lst[i] %= 10
        if lst[i] != 0:
            return lst
    return [1] + lst

# print(increase_large_int([1,2,9]))


"""

Q2 Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 Example 1:

Input: ransomNote = "a", magazine = "b"

Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"

Output: false

"""

def ransome(ransomeNote, magazine):
    dictionary = {}
    for char in magazine:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    for char in ransomeNote:
        if char in dictionary and dictionary[char] > 0:
            dictionary[char] -= 1
        else:
            return False
    return True

# print(ransome('aab', 'baa'))


