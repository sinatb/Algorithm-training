# The Solution

The Solution for this problem consists of 2 parts.The first part is finding the index of the pivot.For finding the pivot The intuitive way is to iterate the array until we find an element that is more than its right neighbor.This will make the order for finding the pivot `O(n)` that violates the main condition.The second way is to find the pivot with binary search.

At each Iteration we compare the middle point of array with the rightmost element.If The middle point is more than the rightmost element,The pivot is at the right half of the array and if it is less,The pivot is at left.You can figure this out with an example.

For The second step we can either do 2 binary searches at each side of the pivot,or we can do 1 binary search but with regard to the shift.At each iteration of standard binary search we need to shift the mid point with regards to the middle point.
