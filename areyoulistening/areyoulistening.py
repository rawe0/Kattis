import sys, math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to_point(self, point):
        x_diff = (point.x - self.x)
        y_diff = (point.y - self.y)
        return math.sqrt((x_diff * x_diff) + (y_diff * y_diff))
    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False
    def __str__(self):
        return "x : " + str(self.x) + " y : " + str(self.y)

def find_longest_radius(matrix, c):
    radius_increases = True
    radius = 0
    circles_touched = []
    # As long as we want to increase radius
    while(radius_increases):
        # Start top left of box
        x_start = c.x - radius
        y_start = c.y - radius
        #print("x_start : " + str(x_start))
        #print("y_start : " + str(x_start))
        # For all points in box
        for x in range(x_start, x_start + 2*radius):
            #print("x : " + str(x))
            for y in range (y_start, y_start + 2*radius):
                #print("y : " + str(y))
                distance_to_point = c.distance_to_point(Point(x, y))
                #print("Distance to point : " + str(distance_to_point))
                if(distance_to_point <= radius):
                    print("Distance was less than radius")   
                    if(matrix[x][y]):
                        print(matrix[x][y])
                        for location in matrix[x][y]:
                            if not location in circles_touched:
                                print(location, end="")
                                print(" Was not in matrix")
                                if(len(circles_touched) > 1):
                                    print("We returned..")
                                    return radius
                                circles_touched.append(location)

        if(radius_increases):
            radius += 1



def main():
    first = True
    locations = []
    matrix = [[0 for x in range(1000)] for y in range(1000)]
    input = 0
    com = Point(0, 0)
    for arg in sys.stdin:
        parameters = arg.split()
        
        if(first):
            com = Point(int(parameters[0]), int(parameters[1]))            
            n = int(parameters[2])
            inputs = n
            first = False
        else:
            n -=1
            location = {"p": Point(int(parameters[0]), int(parameters[1])),  "r": (int(parameters[2]))}        
            locations.append(location)
            if n == 1: 
                for r in range(1000):
                    for c in range(1000):
                        matrix[r][c] = []
                        for location in locations:
                            if(location["p"].distance_to_point(Point(c, r)) <= location["r"]):
                                #print(location["p"])
                                matrix[r][c].append(location["p"])
                print(find_longest_radius(matrix, com))
if __name__ == "__main__":
    main()  