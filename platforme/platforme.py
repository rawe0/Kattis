import sys
def main():
    first = True
    platforms = []
    for arg in sys.stdin:
        parameters = arg.split()
        if(first):
            n = int(parameters[0])
            first = False
        else:
            if(n != 0):
                z = int(parameters[0])
                x = int(parameters[1])
                y = int(parameters[2])
                new_platform = [z, x, y]
                # Sort on insertions
                if(len(platforms) == 0):
                    platforms.insert(0, new_platform)
                else:
                    i = 0
                    for i in range(len(platforms)):
                        if(new_platform[0] > platforms[i][0]):
                            platforms.insert(i, new_platform)
                            break
                        if(len(platforms) - 1 ==  i):
                            platforms.append(new_platform)
                n-=1
            if(n == 0):
                pillar_size = 0
                # For each platform in the platforms
                for platform in platforms:
                    # x and y is not found for the platform
                    x_not_found = True
                    y_not_found = True
                    # Start at the next platform (we know all the rest of the platforms are under or equal height)
                    j = platforms.index(platform) + 1
                    while ((x_not_found or y_not_found)):
                        if (j == len(platforms)):
                            if(x_not_found and y_not_found):
                                pillar_size += (platform[0]) * 2
                            else:
                                pillar_size += platform[0]
                            x_not_found = False
                            y_not_found = False
                        else:
                            current_platform = platforms[j]
                            if (platform[1] >= current_platform[1] and platform[1] < current_platform[2] and x_not_found):
                                x_not_found = False
                                pillar_size += platform[0] - current_platform[0]
                            if (platform[2] > current_platform[1] and platform[2] <= current_platform[2] and y_not_found):
                                y_not_found = False
                                pillar_size += platform[0] - current_platform[0]

                        j+=1 
                print(pillar_size)

if __name__ == "__main__":
    main()