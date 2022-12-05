import sys


def is_valid(x, y, r, c):
    return x >= 0 and y >= 0 and y < c and x < r

def add_items(x, y, t, s, r, c):
    items = []
    if(is_valid(x + t, y, r, c)):
        items.append((x + t, y, s + 1))
    if(is_valid(x - t, y, r, c)):
        items.append((x - t, y, s + 1))
    if(is_valid(x, y + t, r, c)):
        items.append((x, y + t, s + 1))
    if(is_valid(x, y - t, r, c)):
        items.append((x, y - t, s + 1))
    return items

def solve(r,c,grid):
    found = False
    queue = []
    visited = []
    queue.append((0, 0, 0))
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[0][0] == 1

    while(len(queue) != 0):
        x, y, s = queue.pop(0)
        if(x == r-1 and y == c-1):
            print(s)
            found = True
            break
        else:
            t = int(grid[x][y])
            items = add_items(x, y, t, s, r, c)
            for item in items:
                x_item, y_item, _ = item
                if(visited[x_item][y_item] == 0):
                    queue.append(item)
                    visited[x_item][y_item] = 1

    if(not found):
        print("-1")

def main():
    first = True
    for arg in sys.stdin:
        parameters = arg.split()
        if (first):
            r = int(parameters[0])
            c = int(parameters[1])
            n=r
            grid = []
            first = False
        else:
            n-=1
            grid.append(parameters[0])
            if(n == 0):
                solve(r, c, grid)

        
if __name__ == "__main__":
    main()    