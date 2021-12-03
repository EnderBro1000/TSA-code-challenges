import sys
"""***READ BELOW***"""
# IMPORTANT: Requires python 3.0+
"""***READ ABOVE***"""

def inputToTestCaseMatrix(file):
    testCases = int(file[0])
    file = file[1:] # Remove testCase line
    pos = 0
    cases = []
    for case in range(testCases):
        cases.append([])
        for i in range(file[pos]):
            cases[case].append(file[i + pos + 1])
        pos += file[pos] + 1
    return cases

def sumArray(array):
    fin = 0
    for i in array:
        fin += i # Python supports arbitrarily long integers
    return fin

file = sys.stdin.read()
file = file.split('\n') # splits lines into list of strings
file = [int(i) for i in file if i != ""] # removes blank lines

for case in inputToTestCaseMatrix(file):
    print(sumArray(case))
    