# The Solution

For solving this problem we need to use somthing like bfs and a min heap.So at the start we have 1 pointer at the start of each list.At each iteration of the while loop we add the 2 different combinations of number selection the heap(i+1 , j and i , j+1).In the min heap we store the sum of i and j.It is important that we check the combinations are not duplicate.

So overall the min heap stores : `(nums1[i]+nums2[j]=>This is used to heapify , i, j)`.

We will also use a set to store `i,j` combinations.
