import sys
import math

def find_closest_sum(target, sums):
    left = 0
    right = len(sums)-1
    while(left < right):
        middle = math.floor((left+right)/2)
        if(sums[middle] <= target):
            left = middle + 1
        else:
           right = middle - 1
    options=[]
    if(sums[middle+1] != None):
        options.insert(0, sums[middle+1])
    if(sums[middle] != None):
        options.insert(0, sums[middle])
    if(sums[middle-1] != None):
        options.insert(0, sums[middle-1])

    distance = abs(options[0]-target)
    result = options[0]
    for i in range(1, len(options)):
        if(abs(options[i]-target) < distance):
            result=options[i]
            distance=abs(options[i]-target)
    print(f"Closest sum to {target} is {result}.")





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
                for i in range(0, len(numbers)):
                    for j in range (i+1, len(numbers)):
                        sums.insert(0, numbers[j] + numbers[i])
                sums.sort()
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
                find_closest_sum(number, sums)
                get_n = True
                collect_m = False
            else:
                m-=1
                find_closest_sum(number, sums)



    
        
if __name__ == "__main__":
    main()