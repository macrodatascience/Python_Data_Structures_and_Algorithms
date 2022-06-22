"""
Python Data Structures - A Game-Based Approach
Stack challenge
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

for each in string:
    s.push(each)

while not s.is_empty():
    reversed_string+=s.pop()
# Your solution here.

print(reversed_string)
print(string[::-1])
