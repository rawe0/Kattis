import sys

for arg in sys.stdin:
    parameters = arg.split()
    height = int(parameters[0])
    label = (2 ** (height+1)) - 1
    
    if len(parameters) == 1:
        print(label)
        continue
    
    l = 1
    r = 2
    for direction in parameters[1]:
        if direction == 'L':
            label = label - l
            l = l*2
            r = r*2-1
        if direction == 'R':
            label = label - r
            l = l*2+1
            r = r*2
    print(label)
