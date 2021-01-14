from heapq import heapify,heappush,heappop

def AStarAlgo(source, destination, graph, heuristic):
        PriorityQueue = [[heuristic['S'],source]]
        while PriorityQueue:
                print(PriorityQueue, end='--->')
                parent = heappop(PriorityQueue)
                print(parent)
                if parent[1][-1] == destination:
                        return "\nReached Goal State: " + str(parent[1])
                for child in graph[parent[1][-1]]:
                        if child[1] not in parent[1]:
                                heappush( PriorityQueue, [ parent[0]-heuristic[parent[1][-1]]+child[0]+heuristic[child[1]], parent[1]+child[1] ] )
                        
                
graph = {
          'S' : [[4,'B'],[3,'C']],
          'B' : [[4,'S'],[12,'E'],[5,'F']],
          'C' : [[3,'S'],[7,'D'],[10,'E']],
          'D' : [[7,'C'],[2,'E']],
          'E' : [[12,'B'],[10,'C'],[2,'D'],[5,'G']],
          'F' : [[5,'B'],[16,'G']],
          'G' : [[16,'F'],[5,'E']]
        }
heuristic = {'S':14,'B':12,'C':11,'D':6,'E':4,'F':11,'G':3}
source = 'S'
destination = 'G'
print(AStarAlgo(source, destination, graph, heuristic))










