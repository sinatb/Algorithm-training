# The Solution

Well The backtracking part is pretty easy and self-explanatory.But There where 2 optimizations that were cool.The first one was that if a character used in the word is less than the amount of that character in the table,We automatically return False.The second one reverses the order of the string if the last character repeats less than the first character.This is for solving test cases like "`AAAAAAAAABB`".
