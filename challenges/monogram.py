import sys


# file = sys.stdin.read()
file = """
2
2
Franklin Delano Roosevelt
h ross perot
4
Dwight David Eisenhower
Warren Gamaliel Harding
Harry S Truman
John Fitzgerald Kennedy
"""

file = ''.join([i for i in file if not i.isdigit()]) # removes digits
file = file.split("\n") # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

monogrammed = []
for line in file:
    line = line.split(" ")
    monogrammed.append(f"{line[0][0]}{line[2][0]}{line[1][0]}".upper())

print(''.join([i + '\n' for i in monogrammed[:-1]]) + monogrammed[-1])