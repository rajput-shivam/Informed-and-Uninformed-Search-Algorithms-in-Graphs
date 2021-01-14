from heapq import heapify,heappush,heappop

def BestFirstSearch(Graph, EucledianDistance, source, destination, priorityQueue, traversalPath):
        print(priorityQueue, end="--->")
        parent = heappop(priorityQueue)
        print(parent)
        priorityQueue = []
        traversalPath += parent[1]
        if parent[1] == destination:
                return "\nReached Goal State: " + traversalPath
        for child in Graph[parent[1]]:
                heappush( priorityQueue, [ EucledianDistance[child], child ] )
        return BestFirstSearch(Graph, EucledianDistance, source, destination, priorityQueue, traversalPath)
        
        
        
Graph = {
          'A' : ['B','C','D'],
          'B' : ['A','E'],
          'C' : ['A','E','F'],
          'D' : ['A','F'],
          'E' : ['B','C','H'],
          'F' : ['D','C','G'],
          'G' : ['H','F'],
          'H' : ['E','G']
        }
EucledianDistance = {'A':40,'B':32,'C':25,'D':35,'E':19,'F':17,'G':0,'H':10}   # Output depends completely on Eucledian Distance(Heuristic)
source, destination = 'A', 'G'
priorityQueue, traversalPath = [[EucledianDistance[source],source]], ''
print(BestFirstSearch(Graph, EucledianDistance, source, destination, priorityQueue, traversalPath))
