import sys
first=True
people=[]
Q=0
N=0
restart = [0,0]
i = 0
for arg in sys.stdin:
    parameters = arg.split()
    if(first):
        N=int(parameters[0])
        Q=int(parameters[1])
        first=False
        people=[[0,0]]*(N+1)
    else:
        Q-=1
        if(Q == 0):
            first=True
        event = parameters[0]
        if(event == "RESTART"):
            r = int(parameters[1])
            restart=[i, r]
        elif(event == "SET"):
            person = int(parameters[1])
            money = int(parameters[2])
            people[person] =  [i, money]
        elif(event == "PRINT"):
            person = int(parameters[1])
            if(people[person][0] >= restart[0]):
                print(people[person][1])
            else:
                print(restart[1])
    i+=1

