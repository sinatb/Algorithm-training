# The Solution

So The first solution that i thought of was a very easy solution.We know that the answer is at least k+1 and at most the length of the string.So we check all the substrings with the length of k+2 to length of s and check the largest available length.

The Second solution which is a lot faster defines a right and left pointer.At each iteration if the current window(The window between the right and left pointers) is valid, we increase the right pointer value by 1 and if it is not valid we increase the left pointer value by 1 to decrease the size of the window.A great explanation for this problem is at [Neetcode](https://www.youtube.com/watch?v=gqXU1UyA8pk).
