"""

In this exercise, print an alphabetically sorted list of all the functions in the re module containing the word find.

import re

# Your code goes here
find_members = []

"""

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))