# The Solution

So my solution for this problem is really slow.Because at each character of the larger string,I create a substring with the length of the smaller string and make a map from that string.The better thing to do is to make a map from the first s1 chars of the larger string and then modify it as the window slides.
