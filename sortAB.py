class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.value)


class LinkedList:
    def __init__(self, sequence):
        self.sequence = sequence
        self.head = _next = Node(sequence[0])
        for i in sequence[1:]:
            node = Node(i)
            _next.next = node
            _next = node
        self.linkedlist = self.head

    def __getitem__(self, index):
        return self.sequence[index]

    def __len_(self):
        return len(self.sequence)

    def __repr__(self):
        return '-->'.join(str(i) for i in self.sequence)


def find_binary_insert_index(seq, n):   # O(logn)
    """
        二分查找：找出将n插入到seq中的下标
    """
    hi, lo = len(seq) - 1, 0
    while hi >= lo:
        middle = (lo + hi) // 2
        if seq[middle - 1] <= n < seq[middle]:
            return middle
        if seq[middle] > n:
            hi = middle - 1
        else:
            lo = middle + 1
    return middle


def sort(A, B):
    """
        给定A， B两数组，都是乱序，排序A数组，保证A数组对应到B数组每一项（a1-->b1, a2-->b2）
        A元素大于B元素的次数最多
    """
    A.sort()
    result = []
    for i in range(len(B)):
        if B[i] >= A[-1]:
            result.append(A[0])
            A.remove(A[0])
        else:
            index = find_binary_insert_index(A, B[i])
            result.append(A[index])
            A.remove(A[index])
    return result


a1 = [2, 4, 3, 5, 7, 6]
b1 = [6, 2, 4, 3, 7, 1] 

a2 = [5, 4, 7, 3, 2, 6]
b2 = [7, 2, 6, 8, 4, 3]

a3 = [6, 2, 4, 7 ,5, 3]
b3 = [10, 4, 5, 6, 2, 1]
