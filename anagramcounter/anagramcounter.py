import sys
import math

def main():
    for arg in sys.stdin:
        array = [0 for _ in range(200)]
        parameters = arg.split()
        word = parameters[0]
        for char in word:
            array[ord(char)] += 1
        answer = int(math.factorial(len(word)))
        for i in array:
            if(i > 1):
                answer = answer//(math.factorial(i))
        print(answer)
        
if __name__ == "__main__":
    main()    