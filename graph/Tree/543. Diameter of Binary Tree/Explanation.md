# The Solution

So at first I tried to solve the problem with a top down approach,Meaning at each level I will calculate the max diameter of the left subtree and the right subtree and add these 2 numbers together.This Solution proved a bit hard as I got 88/104 and was not able to find the bug.The bottom up approach however seems to be a lot easier.In this Solution we traverse the tree to the leaves and give the leaves a diameter of 0 and from there to up we add 1 to the diameter of the side that is longer.
