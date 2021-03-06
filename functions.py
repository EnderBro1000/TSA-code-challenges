def printMatrix(mat):
    out = ""
    for idxi, i in enumerate(mat):
        for idxj, j in enumerate(i):
            out += f"{mat[idxi][idxj]} "
        out += '\n'
    print(out)

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