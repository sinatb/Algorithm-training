# The Solution

For solving the problem we need to have a delayed start when iterating over the linked list.This means after iterating over first n elements we need to start and move the secondary pointer.When we get to the end of the linked list this pointer will be on the element before the element that needs to be deleted.