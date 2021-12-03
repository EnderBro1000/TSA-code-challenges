import sys
import math

file = sys.stdin.read()
# file = """
# 10
# 5 4 -4
# -4 4 5
# 200
# 1 1 -100
# -35 -100 -100
# 30
# -15.0 15.0 15
# 15 -15.0 -15
# """
file = file.split('\n') # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

def reverseSignArray(array):
    return [-i for i in array]

def printCoordinate(coord):
    return f"({coord[0]}, {coord[1]}, {coord[2]})"

# Cartesian distance, where start and end are 2D points
def distance(start, end):
    # d=sqrt((x1-x2)^2+(y1-y2)^2)
    return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

def findShortestPath(sideLength, start, end):
    # startSurface = findSurface(sideLength, start)
    # endSurface = findShortestPath(sideLength, end)

    # if startSurface == endSurface:
    #     return distance(start, end)
    # elif startSurface == reverseSignArray(endSurface):
    #     oppositeSurface = True
    # else:
    #     adjacentSurface = True
    pass

class Point:
    def findSurface(self):
        global sideLength
        axis = 0
        side = [0, 0, 0] # example output: +x side= [1, 0, 0]; -y side= [-1, 0, 0]
        for component in self.xyzCoord:
            if abs(component)*2 == sideLength:
                side[axis] = component // abs(component)
                return side
            axis += 1
        print("This shouldn't happen") ## Remove before submission

    def findSurfaceCoord(self):
        for component in range(len(self.surface)):
            if self.surface[component] != 0:
                temp = self.xyzCoord.copy()
                temp.pop(component)
                return temp
    
    def __init__(self, x, y, z):
        # global sideLength
        self.xyzCoord = [x, y, z] # 3D coordinates
        self.surface = self.findSurface() # Starting surface
        self.surfaceCoord = self.findSurfaceCoord() # surface 2D coordinates

    def __str__(self):
        return f"{self.xyzCoord}, surface: {self.surface}, surfaceCoord: {self.surfaceCoord}"

sideLength = 10
point1 = Point(4, 5, -4)

print(point1)


        

"""
help me please

pos = 0
for i in range(len(file)//3):
    sideLength = file[pos]
    pos += 1
    start = [float(i) for i in file[pos].split(' ')]
    pos += 1
    end = [float(i) for i in file[pos].split(' ')]
    pos += 1
    print(findShortestPath(sideLength, start, end))

"""