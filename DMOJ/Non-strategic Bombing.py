n, m = [int(x) for x in input().split()]
listOfCities = []
listOfPlans = []
for i in range(n):
    listOfCities.append([int(x) for x in input().split()])
for i in range(m):
    listOfPlans.append([int(x) for x in input().split()])

def areaOfTriangle(myInput):
    x1, y1, x2, y2, x3, y3 = myInput
    return(abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2))
def checkIfInside(triangleCoords, pointToCheck):
    # calc total area of triangle
    triangleA = areaOfTriangle(triangleCoords)

    # now calc areas of 3 triangles formed if pointToCheck were inside triangle
    # format: x1, y1, x2, y2, x3, y3
    # points 1 and 2

    A1 = areaOfTriangle(triangleCoords[0:4] + pointToCheck)
    # points 2 and 3
    A2 = areaOfTriangle(triangleCoords[2:] + pointToCheck)
    # points 1 and 3
    A3 = areaOfTriangle(triangleCoords[0:2] + triangleCoords[4:] + pointToCheck)
    if triangleA == (A1 + A2 + A3):
        return True
    else:
        return False

#print(checkIfInside([1, 1, 3, 3, 0, 5], [99, 99]))
for plan in listOfPlans:
    numCitiesBombed = 0
    for city in listOfCities:
        if checkIfInside(plan, city) == True:
            numCitiesBombed += 1
    print(numCitiesBombed)
