# The Solution

So the main idea behind the solution of this problem is that the `GCD(l, a-l) = GCD(l, a)` With this fact in mind we
know that for each number in the area between l and r if we can find the gcd of l then we can return l and l-gcd as an
answer.