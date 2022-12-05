import sys
def main():
    for arg in sys.stdin:
        parameters = arg.split()
        n = int(parameters[0])
        if n <= 2:
            print("1")
        else:
            print(f"{n-2}")
if __name__ == "__main__":
    main()