import sys
for arg in sys.stdin:
    params = inp.split()
    height = int(params[0])
    node = (2 ** (height + 1)) - 1
    print(node)
    print(height)

