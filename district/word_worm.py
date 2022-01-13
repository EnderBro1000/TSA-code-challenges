import sys

def printMatrix(mat):
    out = ""
    for array in mat:
        out += f"{array}\n"
    print(out)

# file = sys.stdin.read()
file = """
2
6 7
A D E K H E Q
B X E H K J R
J I L O C K D
R P I G N A H
T E N E F H M
J U O P L N T
4
LOCKHEED
PLANE
JET
ENGINE
2 3
A D E 
B X E
3
AD
PLANE
JET
"""


file = file.split('\n') # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

def inputToTestCaseMatrix(file):
    testCases = int(file[0])
    file = file[1:] # Remove testCase line
    pos = 0
    cases = []
    for case in range(testCases):
        print(f"case: {case}")
        cases.append([])

        # get rows and cols
        rowColString = file[pos].split(" ")
        rows = int(rowColString[0])
        cols = int(rowColString[1])

        pos += 1

        # get word search map
        for i in range(rows):
            line = file[i + pos]
            cases[case].append(line.split(" "))
        pos += rows

        # get word bank
        wordAmount = int(file[pos])
        for i in range(wordAmount + 1):
            line = file[i + pos]
            cases[case].append(line)

        pos += wordAmount + 1
    return cases


caseMatrix = inputToTestCaseMatrix(file)

print(caseMatrix)