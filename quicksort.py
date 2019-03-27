# quick sort algorithm implemented in python

def quicksort(nums):
    if len(nums) <= 0:
        return []

    pivot = nums[0]
    less, greater = [], []
    for i in nums[1:]:
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)

    return quicksort(less) + [pivot] + quicksort(greater)



if __name__ == '__main__':
    nums = [4, 2, 1, 5, 2, 5, 2, 1]
    sorted_nums = quicksort(nums)
    print(nums)
    print(sorted_nums)
