// LeetCode, Remove Duplicate from Sorted Array
// time: O(n)	space: O(1)
// 关键在于可以看成是不断在增长的一个数组，主要维持的
// 就是index，然后将A[index]置为下一个值
class Solution {
public:
	int removeDuplicates(int A[], int n) {
		if (n == 0) return 0;
		index = 0;
		for (int i = 1; i < n; i++) {
			if (A[index] != A[i]) {
				// A[index+1] = A[i];
				// index = index + 1;
				A[++index] = A[i]
			}
		}
	}
}