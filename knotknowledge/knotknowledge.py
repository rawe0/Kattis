import sys

def main():
    first = True
    second = True
    first_array = None
    second_array = None
    for arg in sys.stdin:
        parameters = arg.split()
        if (first):
            n = int(parameters[0])
            first = False
        else:
            if(second):
                second = False
                first_array = parameters
            else:
                second_array = parameters
                print(list(filter(lambda x: x not in second_array, first_array))[0])
                first = True
                second = True
        
if __name__ == "__main__":
    main()    
