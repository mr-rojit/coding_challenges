"""
Q1Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123

Output: 321

Q2 You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

"""
MATRIX = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]

def rotate_matrix_90(M):
    new_arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
    for i in range(len(M)):
        x = len(M[i]) -1
        for j in range(len(M[i])):
            new_arr[i][j] = M[x][i]
            x-=1
    return new_arr
        

print(rotate_matrix_90(MATRIX))