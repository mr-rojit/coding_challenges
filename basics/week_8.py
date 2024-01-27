'''
Q1. Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","floight"]

Output: "fl"
'''

def get_longest_common_prefix(s):

    com = ""
    s.sort()
    print(s)
    first = s[0]
    last = s[-1]

    for i in range(len(first)):
        if first[i] == last[i]:
            com = com+first[i]
        else:
            break
    return com

# print(get_longest_common_prefix(["flower","flowez","flaight"]))

'''
Q2. Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]

Output: 3
'''

def majorityElement(nums):
    half = len(nums)/2
    nums_dict = {}
    ans = None
    for i in nums:
        if i not in nums_dict:
            nums_dict[i] = 1
        else:
            nums_dict[i] +=1
    for k,v in nums_dict.items():
        if v > half:
            ans = k
            break
    return ans
# print(majorityElement([3,2,3]))



