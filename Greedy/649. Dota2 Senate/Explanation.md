# The Solution

For solving this problem we first need a count of radiant and dire senators. At any point if any of the 2 sides is completely banned we know that the other side is victorious. The greedy part of the Solution is that at each step we ban the enemy senator or we unban our own senator. If we are banning another senator there is a chance that we can cast a vote in the next round so we need to add ourself to the end of the list.
