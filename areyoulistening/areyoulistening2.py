import sys, math, time
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
def find_longest_radius(com, locations):
    d = []
    radius = 0
    checked_points = []
    print(com.x)
    print(com.y)
    for location in locations:
        print(location["p"])
        print(location["r"])
    while(len(d) < 3):
        for r in range(com.x-radius, com.x+radius + 1):
            for c in range(com.y-radius, com.y+radius + 1):
                point = Point(r, c)
                if ((com.distance_to_point(point) <= radius) and (not point in checked_points)):
                    checked_points.insert(0, point)
                    for location in locations:
                        if(location["p"].distance_to_point(point) <= location["r"]):
                            if not location["p"] in d:
                                print("hej")
                                d.append(location["p"])
                            if(len(d) > 2):
                                return radius
        radius +=1
        print(radius)

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
            if n == 0:
                print(find_longest_radius(com, locations))

                
if __name__ == "__main__":
    main()  