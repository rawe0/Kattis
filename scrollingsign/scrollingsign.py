
import sys

def main():
    first = True
    second_first = True
    words = []
    n = 0
    for arg in sys.stdin:
        parameters = arg.split()
        if(first):
            first = False
            continue
        else:
            if(second_first):
                second_first = False
                n = int(parameters[1])
                words = []
            else:
                words.append(parameters[0])
                n -= 1
                nr_itterations = 0
                if(n == 0):
                    i = 0
                    next_word = ""
                    while(i != len(words)-1):
                        word = words[i]
                        next_word = words[i+1]
                        char = next_word[0]

                        for j in range(0, len(word)):
                            if(char == word[j] and word[j:] == next_word[:len(word[j:])]):
                                break
                            else:
                                nr_itterations +=1
                        i += 1
                    nr_itterations += len(next_word)
                    print(nr_itterations)
                    second_first = True


        
if __name__ == "__main__":
    main()    