import sys, math


def main():

    for arg in sys.stdin:
        parameters = arg.split()
        length = int(parameters[0])
        weight = int(parameters[1])
        max_weight = length*26
        min_weight = length
        if(max_weight < weight or weight < min_weight):
            print("impossible")
        else:
            a = int((weight/length))
            characters = length
            word_weight = 0
            result = ""
            if(a == 26):
                result = "z"*length
            else:
                for i in range(characters-1):
                    if(a > 20):
                        result = result + chr(a + 97)
                        word_weight = word_weight + (a + 1)
                    else: 
                        result = result + chr(a + 96)
                        word_weight = word_weight + a
                result = result + chr(96 + (weight - word_weight))
                word_weight = word_weight + (weight - word_weight)
            print(result)

if __name__ == "__main__":
    main()