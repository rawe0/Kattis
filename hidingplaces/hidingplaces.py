import sys
from functools import cmp_to_key

first = True

def translate(input): 
    dictionary = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4,
        "f" : 5,
        "g" : 6,
        "h" : 7,
        0 : 'a',
        1 : 'b',
        2 : 'c',
        3 : 'd',
        4 : 'e',
        5 : 'f',
        6 : 'g',
        7 : 'h'  
    }
    return dictionary.get(input, input)

def all_nodes_are_visited(node_array):
    all_nodes_are_visited = True
    for row in node_array:
        for node in row:
            if(node["visited"] == False):
                all_nodes_are_visited = False
    return all_nodes_are_visited

def get_min_distance_node(node_array):
    min = -1
    x = -1
    y = -1
    for r in range(8):
        for c in range(8):
            elem = node_array[r][c]
            if(elem["visited"] == False):
                if(not elem["dist"] == -1):
                    if(elem["dist"] < min or min == -1 ):
                        min = elem["dist"]
                        x = r
                        y = c
    return {"x" : x, "y": y}


            

def search(x, y):

    positions = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    jumps = [[{"dist": -1, "visited": False} for _ in range(8)] for _ in range(8)]
    jumps[x][y]["dist"] = 0

    while(not all_nodes_are_visited(jumps)):

        node = get_min_distance_node(jumps)
        jumps[node["x"]][node["y"]]["visited"] = True

        for pos in positions:

            next_x = node["x"]+pos[0]
            next_y = node["y"]+pos[1]
            if(next_x >= 0 and next_y >= 0 and next_y < 8 and next_x < 8):

                alt_distance = jumps[node["x"]][node["y"]]["dist"] + 1
                distance = jumps[next_x][next_y]["dist"]

                if(jumps[next_x][next_y]["visited"] == False and (alt_distance < distance or distance == -1) and jumps[node["x"]][node["y"]]["dist"] != -1):
                    
                    jumps[next_x][next_y]["dist"] = jumps[node["x"]][node["y"]]["dist"] + 1
    return jumps


def compare(item1, item2):
    if (item1[1] < item2[1]):
        return 1
    elif (item1[1] > item2[1]):
        return -1
    else:
        if (item1[0] < item2[0]):
            return -1
        elif (item1[0] > item2[0]):
            return 1
        else:
            return 0


for arg in sys.stdin:
    if(first):
        first=False
        continue
    parameters = arg.split()
    input = parameters[0]
    jumps = search(translate(input[0]), int(input[1])-1)
    far = 0

    for i in range(8):
        for j in range (8):
            far = max(far, jumps[i][j]["dist"])
    result = []
    for i in range(8):
        for j in range(8):
            if(jumps[i][j]["dist"] == far):
                result.append(f"{translate(i)}{str(j+1)}")
    result.sort(key=cmp_to_key(compare))
    print(f"{far}", end="")
    for res in result:
        print(f" {res}", end="")
    print("")