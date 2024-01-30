"""
1-Write a Python program to find 4 numbers from an array such that the sum of 4 numbers equal to a given number.
Input : [1, 0, -1, 0, -2, 2,10,11], 0)
Output : [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""

def find_four_numbers(nums, target):
    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    print(result)

# find_four_numbers([1, 0, -1, 0, -2, 2,10,11], 0)

"""
2-Write a Python program to find the single element appears once in a list where every element appears multiple times except for one. 
Input : [1, 1, 1, 2, 2, 2, 3]
Output : 3
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


# find_single_occurence([1, 1, 1, 2, 2, 2, 3])


"""
3-Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit. 
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5
"""

def find_single_digit(n):
    new_num = 0
    while n > 9:
        while n > 0:
            last = n % 10
            new_num += last
            n //= 10
        
        n = new_num
        new_num = 0

    print(n)


find_single_digit(59)