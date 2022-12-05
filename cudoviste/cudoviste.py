import sys

def is_valid(x, y, r, c):
    return x < r and x >= 0 and y < c and y >= 0


def main():
    first = True
    positions = [(0,0), (0, 1), (1, 0), (1, 1)]
    for arg in sys.stdin:
        if(first):
            first=False
            parameters = arg.split()
            r = int(parameters[0])
            c = int(parameters[1])
            n = r
            map = []
            result = [0,0,0,0,0]
        else:
            n-=1
            map.append(arg.strip())
            if(n == 0):
                for i in range(0, r-1):
                    for j in range(0, c-1):
                        items = []
                        for pos in positions:
                            pos_x, pos_y = pos
                            x = i + pos_x
                            y = j + pos_y
                            if(is_valid(x, y, r, c)):
                                items.append(map[x][y])
                        if(len(items) == 4 and not '#' in items):
                                result[items.count('X')] += 1
                for d in result:
                    print(d)
                
if __name__ == "__main__":
    main()
