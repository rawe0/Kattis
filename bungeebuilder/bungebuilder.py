import sys

def main():
    first = True
    for arg in sys.stdin:
        parameters = arg.split()
        if (first):
            n = int(parameters[0])
            first = False
        else:
            can_build = True
            first = True
            heights = list(map(lambda x : int(x), parameters))
            max_height = 0
            for i in range (0, n):
                start_height = heights[i]
                for j in range (i, n):
                    can_build = True
                    end_height = heights[j]
                    for k in range (i+1, j):
                        between = heights[k]
                        if(between >= end_height or between >= start_height):
                            can_build = False
                            break
                    if(can_build and j != i):
                        maximum = min(start_height, end_height)
                        minimum = min(heights[i:j])
                        potential = maximum - minimum
                        if(maximum - minimum > max_height):
                            max_height = potential
            print(max_height)

        
if __name__ == "__main__":
    main()    