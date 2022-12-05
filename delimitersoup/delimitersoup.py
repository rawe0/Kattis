import sys

def main():
    first = True
    for arg in sys.stdin:
        if(first):
            parameters = arg.split()
            first = False
            stack = []
        else:
            i = 0
            for char in arg:
                if(char in ['{', '(', '[']):
                    stack.append(char)
                    i+=1
                    continue       
                elif char  == ' ':
                    i+=1
                    continue
                elif char == ']':
                    if(len(stack) != 0 and stack.pop() == '['):
                        i+=1
                        continue
                    else:
                        print(f"{char} {i}")
                        break
                elif char == ')':
                    if(len(stack) != 0 and stack.pop() == '('):
                        i+=1
                        continue
                    else:
                        print(f"{char} {i}")
                        break
                elif char == '}':
                    if(len(stack) != 0 and stack.pop() == '{'):
                        i+=1
                        continue
                    else:
                        print(f"{char} {i}")
                        break
            if(i == len(arg)-1):
                print("ok so far")
            first = True



if __name__ == "__main__":
    main()
