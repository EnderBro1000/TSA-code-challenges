import sys


file = sys.stdin.read()

file = ''.join([i for i in file if not i.isdigit()]) # removes digits
file = file.split("\n") # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

monogrammed = []

for line in file:
    line = line.split(" ")
    monogrammed.append()

print(file)