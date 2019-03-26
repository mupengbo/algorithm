#include<stdio.h>


void swap(int *nums, int index1, int index2) {
	int temp = nums[index1];
	nums[index1] = nums[index2];
	nums[index2] = temp;
}

void heapify(int nums[], int length, int index) {
	
	if (index >= length) 
		return;

	int c1 = 2 * index + 1;
	int c2 = 2 * index + 2;

	int max_value_index = index;
	if (c1 < length && nums[c1] > nums[max_value_index])   max_value_index = c1;
	if (c2 < length && nums[c2] > nums[max_value_index])   max_value_index = c2;

	if (max_value_index != index) {
		swap(nums, max_value_index, index);
		heapify(nums, length, max_value_index);
	}
}


void build_heap(int nums[], int length) {
	int last_not_leaf_node = (length - 1 - 1) / 2;
	for (int i=last_not_leaf_node; i>=0; i--) {
		heapify(nums, length, i);
	}
}


int main() {

	int nums[] = {4, 2, 5, 6, 7, 2, 3, 1};
	build_heap(nums, 8);
	for(int i=0; i<8; i++) {
		printf("%d  ", nums[i]);
	}
	printf("\n");
	return 0;
}
