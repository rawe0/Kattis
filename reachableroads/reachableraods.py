def graph_is_searched(graph):
    for item in graph:
        if(item[1] == 0):
            return False
    return True

def get_first_not_visited_node(array):
    for i in range(len(array)):
        if(array[i][1] == 0):
            return i

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        r = int(input())
        graph = [[[], -1] for _ in range(1000)]
        if(r < 1):
            print(m-1)
        else:
            for _ in range(r):
                parameters = input().split()
                x = int(parameters[0])
                y = int(parameters[1])
                graph[x][0].append(y)
                graph[y][0].append(x)
                graph[x][1] = 0
                graph[y][1] = 0

            count = 0
            while(not graph_is_searched(graph)):
                item = get_first_not_visited_node(graph)
                queue = []
                queue.append(item)
                while(len(queue) != 0):
                    node = queue.pop(0)
                    graph[node][1] = 1
                    for index in graph[node][0]:
                        if (graph[index][1] == 0):
                            queue.append(index)
                count +=1
            print(count-1)
                
if __name__ == "__main__":
    main()    