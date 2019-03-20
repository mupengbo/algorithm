#!/bin/env python3
# 求一个序列的连续子序列。
# 比如 [1, 2, 3]的子序列有：
# [1], [2], [3]
# [1, 2], [2, 3]
# [1, 2, 3]


def sub_seq(seq):
    """
        sub_length 就好像一个窗口，这个窗口的大小反映了
        子序列的长度。然后来滑动窗口释放子序列。
    """
    sub_length = 1  # 定义子序列的长度
    while sub_length <= len(seq):
        index = 0
        while index + sub_length <= len(seq): 
              # index + sub_length - 1 <= len(seq) - 1
            yield seq[index:index+sub_length]
            index += 1
        sub_length += 1


def sum_sub_seq_less_than_threshold(seq, threshold):
    sub_length = len(seq)
    while sub_length >= 1:
        index = 0
        while index + sub_length <= len(seq):
            sub_seq = seq[index: index+sub_length]
            if sum(sub_seq) <= threshold:
                yield sub_seq
            index += 1
        sub_length -= 1


if __name__ == '__main__':
    for sub in sub_seq([1, 2, 3, 4]):
        print(sub)

    print('------------ I\'m separator --------------')
    for sub in sum_sub_seq_less_than_threshold([2, 4, 1, 4, 2, 3, 1], 10):
        print(sub)
