# The Solution

So the backtracking part is pretty easy and understandable, The part that finds the answers with the same frequency is the fun part.So Python has a function named Counter that stores the count of each element in a list, we can use this and a for loop to delete the answers with the same frequency.

The problem of the solution is that it is very slow.Some of the other solutions use a start index in the backtrack function that is set to the value of `i`, the current index that is used for making the new combination.In this way we will be sure that a previously used element will not be present and no duplicate combinations will be created.
