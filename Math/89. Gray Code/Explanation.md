# The Solution

So for solving the problem we need to create the sequence from a base sequence of `[0,1]`. For that we can either use recursion or the bottom-up approach.At each level we have a right and left sequence, The left sequence is created by adding 0 behind the characters in the base sequence and the right one is created by adding 1 to the left of the base.After this the base is updated to left + right.
