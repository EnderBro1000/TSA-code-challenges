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

def reverseSignArray(array, sign=-1):
    return [i*sign for i in array]

def printCoordinate(coord):
    return f"({coord[0]}, {coord[1]}, {coord[2]})"

def sign(num):
    if num == 0:
        return 1
    return num // abs(num)

def minArray(array):
    minimum = array[0]
    for value in array[1:]:
        minimum = min(minimum, value)
    return minimum

class Point:
    def findSurface(self):
        global sideLength
        axis = 0
        side = [0, 0, 0] # example output: +x side= [1, 0, 0]; -y side= [0, -1, 0]
        for component in self.xyzCoord:
            if abs(component)*2 == sideLength:
                side[axis] = component // abs(component)
                return side
            axis += 1
        # print("This surface shouldn't happen") # TODO Remove before submission

    # return -1 if negative surface, 1 if positive surface
    def surfaceSign(self):
        for value in self.surface:
            if value != 0:
                return value
    
    def __init__(self, x, y, z):
        # global sideLength
        self.xyzCoord = [x, y, z] # 3D coordinates
        self.surface = self.findSurface() # Starting surface

    def __str__(self):
        return f"{self.xyzCoord}\tsurface: {self.surface}"

    def copy(self):
        return Point(self.xyzCoord[0], self.xyzCoord[1], self.xyzCoord[2])

# Cartesian distance, where start and end are 2D points on the same plane
def calculateDistance(start, end):
    # d=sqrt((x1-x2)^2+(y1-y2)^2)
    return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

# return 0,1,2 for surface xyz face
def surfaceToAxis(surface):
    for i, value in enumerate(surface):
        if value != 0:
            return i
    #print("This surface integer shouldn't happen") # TODO Remove before submission

# return 0,1,2 for whichever is missing in xyz 0,1,2 axis
# must pass in different axis
def missingAxis(axis1, axis2):
    combo = axis1 + axis2
    if combo == 1:
        return 2
    if combo == 3:
        return 0
    return 1 # combo == 2

def missingAxes(axis):
    if axis == 0:
        return 1, 2
    elif axis == 1:
        return 2, 0
    return 0, 1

# rotate coordinates +/- 90deg on a plane about its normal 
def rotateCoords(coords, direction):
    return [-coords[1] * direction, coords[0] * direction]

def rotateCoordsAmountDirection(coords, amount, direction):
    for i in range(amount):
        coords = rotateCoords(coords, direction)
    return coords

def rotateCoordsAmount(coords, amount):
    if amount == 0:
        return coords
    direction = amount//abs(amount)
    return rotateCoordsAmountDirection(coords, abs(amount), direction)

# return a list of the different test cases for endpoint 
def createAdjCases(relativeCoords, sideLength, sign):
    cases = [0, 0, 0, 0, 0]

    for i in range(-2,3):
        temp = relativeCoords.copy()
        temp = rotateCoordsAmount(temp, i)
        temp[0] += sideLength * sign
        temp[1] += sideLength * (i) * sign
        cases[i+2] = temp

    return cases

def createOppCases(relativeCoords, sideLength):
    cases = [0, 0, 0, 0]
    sign = 1
    for i in range(4):
        temp = relativeCoords.copy()
        temp = rotateCoordsAmount(temp, -i*2)
        if i > 1:
            sign = -1
        temp[i%2] += sideLength * 2 * sign

        cases[i] = temp
    return cases

# returns the lowest distance from startCoords and each endCoordCase
def testCases(startCoords, endCoordCases):
    distance = calculateDistance(startCoords, endCoordCases[0])
    #print(f"\ndistance: {distance}")
    for case in endCoordCases[1:]:
        newDist = calculateDistance(startCoords, case)
        distance = min(distance, newDist)
        #print(f"distance: {distance}\tnew distance: {newDist}")
    return distance

# TODO make absolute with L-shift. 
def findShortestPath(startPoint: Point, endPoint: Point, sideLength):
    startCoords = [0, 0] # (a, c). 2D coordinates of endPoint
    endCoords = [0, 0] # (a, c). 2D coordinates of endPoint
    
    axis1, axis2 = missingAxes(surfaceToAxis(startPoint.surface))
    
    if startPoint.surface == endPoint.surface: # handle same surface case
        # print("same surface case")
        startCoords[0] = startPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        startCoords[1] = startPoint.xyzCoord[axis2]

        endCoords[0] = endPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        endCoords[1] = endPoint.xyzCoord[axis2]

        return calculateDistance(startCoords, endCoords)

    elif startPoint.surface == reverseSignArray(endPoint.surface): # handle opposite surface case
        #print("opposite surface case")
        startCoords[0] = startPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        startCoords[1] = startPoint.xyzCoord[axis2]

        endCoords[0] = -endPoint.xyzCoord[axis1] # flipping axis 1 TODO add length additions after creating different cases
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        endCoords[1] = endPoint.xyzCoord[axis2]

        oppositeCases = createOppCases(endCoords, sideLength) # TODO Test with sign
        # print(oppositeCases)
        return testCases(startCoords, oppositeCases)

    else: # handle adjacent surface case
        # print("adjacent surface case")
        # moving face 
        # # [a -> b]
        # relative coordinate = 3D coord input
        # a = -b
        # c = c
        aAxis = surfaceToAxis(endPoint.surface) # moving start axis
        bAxis = surfaceToAxis(startPoint.surface) # static end axis
        cAxis = missingAxis(aAxis, bAxis) # missing axis
        
        startCoords[0] = startPoint.xyzCoord[aAxis]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        startCoords[1] = startPoint.xyzCoord[cAxis]
        
        endCoords[0] = -endPoint.xyzCoord[bAxis] * startPoint.surfaceSign()
        endCoords[1] = endPoint.xyzCoord[cAxis]

        adjacentCases = createAdjCases(endCoords, sideLength, startPoint.surfaceSign())
        # print(adjacentCases)
        return testCases(startCoords, adjacentCases)

    #print("This really shouldn't happen")
    return None

# this handles points that are on multiple surfaces.
# return start, end point. If multiple surfaces, return [startpoints], [endpoints] with individually set surfaces
def getAllSurfacePoints(point: Point):
    points = [point]
    if point.xyzCoord[0] == point.xyzCoord[1] and point.xyzCoord[0] != 0:
        newStartPoint = point.copy()
        newStartPoint.surface = [0, sign(point.xyzCoord[1]), 0]
        points.append(newStartPoint)

    if point.xyzCoord[1] == point.xyzCoord[2] and point.xyzCoord[1] != 0:
        newStartPoint = point.copy()
        newStartPoint.surface = [0, 0, sign(point.xyzCoord[2])]
        points.append(newStartPoint)

    elif point.xyzCoord[0] == point.xyzCoord[2] and point.xyzCoord[0] != 0:
        newStartPoint = point.copy()
        newStartPoint.surface = [0, 0, sign(point.xyzCoord[2])]
        points.append(newStartPoint)

    return points



# myPoint = Point(100, 1, 100)

# sideLength = 30
# startPoint = Point(-15.0, 15.0, 15)
# endPoint = Point(15, -15.0, -15)

# sideLength = 1
# startPoint = Point(.5, .5, 0)
# endPoint = Point(-.5, -.5, 0)




#print(f"single check:\t{findShortestPath(startPoint, endPoint, sideLength)}")

# startPoints = getAllSurfacePoints(startPoint)
# endPoints = getAllSurfacePoints(endPoint)

# distances = []
# for startPoint in startPoints:
# print("".join([f"{i}\n" for i in endPoints]))
# for endPoint in endPoints:
#     print(f"startPoint: {startPoint}")
#     print(f"endPoint: {endPoint}")
#     distances.append(findShortestPath(startPoint, endPoint, sideLength))
#     print("\n\n")

# print(f"Answer: {minArray(distances)}") # TODO remove "Answer" formatting

#print(f"Start: {startPoint}")
#print(f"End: {endPoint}")

# print(distance)
#print(f"start: {startFlat}\nend: {endFlat}")


def takePointOffEdge(startPoint: Point, endPoint: Point, sideLength):
    if startPoint.surface == endPoint.surface or startPoint.surface == reverseSignArray(endPoint.surface):
        return endPoint
    epsilon = .000000000000000000001
    mellowPoint = endPoint.copy()
    foundSide = False
    for i, component in enumerate(endPoint.xyzCoord):
        if component == sideLength//2:
            foundSide = True
        if foundSide:
            mellowPoint.xyzCoord[i] -= epsilon
    return mellowPoint

pos = 0
for i in range(len(file)//3):
    # Parse input
    sideLength = float(file[pos])
    pos += 1
    start = [float(i) for i in file[pos].split(' ')]
    startPoint = Point(start[0], start[1], start[2])
    pos += 1
    end = [float(i) for i in file[pos].split(' ')]
    endPoint = Point(end[0], end[1], end[2])
    pos += 1

    #endPoint = takePointOffEdge(startPoint, endPoint, sideLength)

    endPoints = getAllSurfacePoints(endPoint)
    
    # Test
    distances = []
    for endPoint in endPoints:
    # print(f"startPoint: {startPoint}")
    # print(f"endPoint: {endPoint}")
        distances.append(findShortestPath(startPoint, endPoint, sideLength))
    print(round(minArray(distances),4))

