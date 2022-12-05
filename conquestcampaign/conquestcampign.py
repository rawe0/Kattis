import sys

first = True

def update_current(array):
    
    for row in array:
        for item in row:
            item["current"] = item["next"]
            item["next"] = 0

def get_next_gen(array, r, c):

    positions = [[0, 1] ,[1, 0], [-1, 0], [0, -1]]

    for i in range(r):
        for j in range(c):
            if(array[i][j]["current"] == 1):
                array[i][j]["next"] = 1
                for pos in positions:
                    next_x = pos[0] + i
                    next_y = pos[1] + j
                    if(next_x >= 0 and next_x < r and next_y >= 0 and next_y < c):
                        array[next_x][next_y]["next"] = 1

def is_country_conquered(array):
    
    country_is_conquered = True
    
    for row in array:
        for item in row:
            if(item["current"] == 0):
                country_is_conquered = False

    return country_is_conquered

r = 0
c = 0
n = 0
items = []
day = 0

for arg in sys.stdin:
    
    parameters = arg.split()
    
    if(first):
        first=False
        r = int(parameters[0])
        c = int(parameters[1])
        n = int(parameters[2])
        items = [[{"current": 0, "next": 0} for _ in range(c)] for _ in range(r)]
        continue
    else:
        n-=1
        x = int(parameters[0]) - 1 
        y = int(parameters[1]) - 1
        items[x][y]["current"] = 1
        if(n == 0):
            day = 0
            while(not is_country_conquered(items)):
                day += 1
                get_next_gen(items, r, c)
                update_current(items)
            print(str(day+1))
