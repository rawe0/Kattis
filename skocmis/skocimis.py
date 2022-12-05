import sys

def main():
    for arg in sys.stdin:
        parameters = arg.split()
        x = int(parameters[0])
        y = int(parameters[1])
        z = int(parameters[2])
        ans = max(y-x, z-y) - 1
        print(ans)
if __name__ == "__main__":
    main()
