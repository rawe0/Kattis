import sys

for arg in sys.stdin:
    
    parameters = arg.split()
    found = False    
    f = int(parameters[0])
    s = int(parameters[1])
    g = int(parameters[2])
    u = int(parameters[3])
    d = int(parameters[4])

    queue = []
    queue.append((s, 0))

    visited = [0 for _ in range(f+1)]
    visited[s] = 1
    
    while(not len(queue) == 0 and not found):
        floor, steps = queue.pop(0)
        if(floor == g):03303asdasd
            found = True
            print(steps)
        if floor + u <= f and visited[floor + u] == 0 and not found:
            visited[floor + u] = 1
            queue.append((floor + u, steps + 1))
        if floor - d > 0 and visited[floor - d] == 0 and not found:
            visited[floor - d] = 1
            queue.append((floor - d, steps + 1))
    if not found:
        print("use the stairs")