#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ A function that draws the pascal's triangle """
    ans = []
    if n <= 0:
        return []
    res = [1]
    ans.append(res)
    for i in range(n):
        res = []
        temp = [0] + res + [0]
        for j in range(len(temp) - 1):
            res.append(temp[j] + temp[j + 1])
        ans.append(res)
    return ans
