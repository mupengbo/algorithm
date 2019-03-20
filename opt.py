#!/bin/env python3
# 给出一个数组列表，从中选取元素，所选元素不能相邻，判断所能选出的最大和。

def rec_opt(arr, index):
    if index == 0:
        return arr[0]
    elif index == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, index - 2) + arr[index] # Choose it
        B = rec_opt(arr, index - 1)  # Do not choose it
        return max(A, B)


def opt(arr, i):
    pass


if __name__ == '__main__':
    arr = [int(i) for i in input('Input an array: ').split()]
    print(rec_opt(arr, len(arr) - 1))
