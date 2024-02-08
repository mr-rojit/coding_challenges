"""
1-Write a Python program to check a sequence of numbers is an arithmetic progression or not. 
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
"""

def check_arethmetic_progression(lst):
    diff = lst[1] - lst[0]
    for i in range(len(lst) -1):
        if not lst[i+1] - lst[i] == diff:
            return False
    return True

print(check_arethmetic_progression([5, 7, 9, 11, 14]))

 
"""
2-Write a Python program to check whether a given number is an ugly number. 
Input : 12
Output : True
Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers.
Note: 1 is typically treated as an ugly number
"""

def find_prime_factors(n):
    pass

def find_ugly_number(n):
    print()

find_ugly_number(12)


## Alternate method

def isUgly(self,n):
    prime_factors=[]
    div=2

    if(n<=0):
        return False
    while(n>1):
        if(n%2==0):
            n=n/2
        elif (n%3==0):
            n=n/3
        elif (n%5==0):
            n=n/5
        else:
            return False
    return True

isUgly(6)

 
"""
3-Write a Python Function to find the single number in a list that doesn't occur n times.
Input : [5, 3,3,4, 4, 3, 4], N=3
Output : 5
"""

def does_not_coocur_n_times(lst, n) -> int:
    count_dict = dict()
    for i in lst:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    for k,v in count_dict.items():
        if v != n:
            return k

# print(does_not_coocur_n_times([5, 3, 3, 4, 4, 3, 4], 3))