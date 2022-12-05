import sys

def main():
    get_n = True
    get_m = False
    collect_m = False
    collect_n = False
    sums=[]
    numbers=[]
    count=1
    for arg in sys.stdin:
        parameters = arg.split()
        number=int(parameters[0])
        if(get_n):
            print(f"Case {count}:")
            count+=1
            n=number
            get_n=False
            collect_n=True
            numbers=[]
            sums=[]
        elif(collect_n):
            if(n == 0):
                collect_n = False
                get_m = True
            else:
                numbers.insert(0, number)
                n-=1
        if(get_m):
            m=number
            get_m=False
            collect_m=True
        elif(collect_m):
            if(m==1):
                distance = abs(numbers[0] + numbers[1] - number)
                result = numbers[0] + numbers[1]
                for i in range(0, len(numbers)):
                    for j in range (i+1, len(numbers)):
                        num = numbers[j] + numbers[i]
                        dist = abs(num-number)
                        if(abs(num-number) < distance):
                            result = num
                            distance = dist
                print(f"Closest sum to {number} is {result}.")
                get_n = True
                collect_m = False
            else:
                m-=1
                distance = abs(numbers[0] + numbers[1] - number)
                result = numbers[0] + numbers[1]
                for i in range(0, len(numbers)):
                    for j in range (i+1, len(numbers)):
                        num = numbers[j] + numbers[i]
                        dist = abs(num-number)
                        if(abs(num-number) < distance):
                            result = num
                            distance = dist
                print(f"Closest sum to {number} is {result}.")


    
        
if __name__ == "__main__":
    main()