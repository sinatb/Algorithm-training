# The Solution

For solving the problem we need to store the sum of all nodes in the same height in the binary tree. after that for each node we need to replace its value with the sum of nodes in a level - sum of the childs with the same parent as him (his brother).

## The code

For storing nodes in the stack (for the bfs) we store the node and its parent together.

* `child_sum` : A dictionary that stores sum of children nodes for each parent. The key of this dictionary is parent and the value is sum. The reason for making it a `defaultdict` is that it might have `None` as a key.

* `p` : A dictionary holding the parent element of each node. Withe the use of this and `child_sum` we can find the sum of a specific part of the tree and reduce it from the sum of a level.

* `curr` : The sum of all nodes in 1 level.

The first loop is for calculating the sum in a level and the second loop is for calculatin the new values.
