import sys


def add_one(a):
    a.insert(0, 1)
    return a
def add_two(a):
    a.insert(0, 2)
    return a
def add_three(a):
    a.insert(0, 3)
    return a

def recursive_func(array):
    
    if (len(array) == 0):
        return []
    elif (len(array) == 1):
        result = [[1]]
    elif (len(array) == 2):
        result = [[1, 1],[2]]
    elif (len(array) == 3):
        result =  [[1, 1, 1,], [2, 1], [2, 1], [3]]
    elif(len(array) > 3):
        # Recursive case starting with 1
        results_one = recursive_func(array[1:])
        # Recursive case starting with 2
        results_two = recursive_func(array[2:])
        # Recursive case starting with 3
        results_three = recursive_func(array[3:])
        final_one = map(add_one, results_one)
        final_two = map(add_two, results_two)
        final_three = map(add_three, results_three)
        result = list(final_one) + list(final_two) + list(final_three)
    print(result)
    return result

def main():
        for arg in sys.stdin:
            parameters = arg.split()
            length = int(parameters[0])
            array = [1]*length
            result = recursive_func(array)
            print(len(result))

if __name__ == "__main__":
    main()
