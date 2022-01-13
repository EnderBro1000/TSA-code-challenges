import sys

file = sys.stdin.read()

file = ''.join([i for i in file if not i.isdigit()]) # removes digits
file = file.split("\n") # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

monogrammed = []
for line in file:
    line = line.split(" ") # split full name into each word
    monogrammed.append(f"{line[0][0]}{line[2][0]}{line[1][0]}".upper()) # get uppercase monogram

[print(i) for i in monogrammed]
