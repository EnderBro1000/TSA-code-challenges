import sys
import math

# file = sys.stdin.read()
file = """
10
5 4 -4
-4 4 5
200
1 1 -100
-35 -100 -100
30
-15.0 15.0 15
15 -15.0 -15
"""
file = file.split('\n') # splits lines into list of strings
file = [i for i in file if i != ""] # removes blank lines

def reverseSignArray(array):
    return [-i for i in array]

def printCoordinate(coord):
    return f"({coord[0]}, {coord[1]}, {coord[2]})"

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
        print("This surface shouldn't happen") # TODO Remove before submission

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

# Cartesian distance, where start and end are 2D points on the same plane
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

# return 0,1,2 for surface xyz face
def surfaceToAxis(surface):
    for i, value in enumerate(surface):
        if value != 0:
            return i
    print("This surface integer shouldn't happen") # TODO Remove before submission

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

# TODO make absolute with L-shift. 
# this is only for adjacent surfaces. TODO support same and opposite surface
def getFlatPoints(startPoint: Point, endPoint: Point):

    startCoords = [0, 0] # (a, c). 2D coordinates of endPoint
    endCoords = [0, 0] # (a, c). 2D coordinates of endPoint
    
    axis1, axis2 = missingAxes(surfaceToAxis(startPoint.surface))
    
    if startPoint.surface == endPoint.surface: # handle same surface case
        
        startCoords[0] = startPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        startCoords[1] = startPoint.xyzCoord[axis2]

        endCoords[0] = endPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        endCoords[1] = endPoint.xyzCoord[axis2]

    elif startPoint.surface == reverseSignArray(endPoint.surface): # handle opposite surface case
        
        startCoords[0] = startPoint.xyzCoord[axis1]
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        startCoords[1] = startPoint.xyzCoord[axis2]

        endCoords[0] = -endPoint.xyzCoord[axis1] # flipping axis 1 TODO Add two length
        # remove bAxis for startCoords, because its already on that surface (and doesn't change)
        endCoords[1] = endPoint.xyzCoord[axis2]

    else: # handle adjacent surface case
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
        
        endCoords[0] = -endPoint.xyzCoord[bAxis] * startPoint.surfaceSign() # TODO this might break # TODO Add (sign) 1 length
        endCoords[1] = endPoint.xyzCoord[cAxis]

    return startCoords, endCoords

# returns 2D relative coords of a point by removing the surface component
def flattenStaticPoint(point):
    pass
    


sideLength = 2
startPoint = Point(1, .5, .25)
endPoint = Point(1, .5, .25)

print(f"Start: {startPoint}")
print(f"End: {endPoint}")

startFlat, endFlat = getFlatPoints(startPoint, endPoint)
print(f"start: {startFlat}\nend: {endFlat}")





        

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