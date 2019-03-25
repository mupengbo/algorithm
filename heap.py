# parent = (i - 1) // 2
# c1 = 2 * i + 1
# c2 = 2 * i + 2


class Heap:

    def __init__(self, arr):
        self.arr = arr
        self.__heapify()

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        return '{!r}'.format(self.arr)

    def __heapify(self):
        last_not_leaf_node = (len(self) - 1) // 2
        for i in range(last_not_leaf_node, 0-1, -1):
            Heap.heapify(self.arr, i)

    def heappush(self, element):
        self.arr.append(element)
        self.__heapify()

    def heappop(self):
        vertex = self.arr.pop(0)
        self.__heapify()
        return vertex

    @staticmethod
    def heapify(arr, index):

        if index >= len(arr):
            return

        c1 = 2 * index + 1
        c2 = 2 * index + 2
        index_of_max = index
        if c1 < len(arr) and arr[c1] > arr[index_of_max]:
            index_of_max = c1
        if c2 < len(arr) and arr[c2] > arr[index_of_max]:
            index_of_max = c2
        if index != index_of_max:
            arr[index], arr[index_of_max] = arr[index_of_max], arr[index]
            Heap.heapify(arr, index_of_max)


if __name__ == '__main__':
    heap = Heap([3, 5, 2, 5, 6, 1])
    print(heap)
