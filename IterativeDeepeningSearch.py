# Iterative Deepening Search

def DLS(graph, source, dest, level):
    print("\n\n",level)
    visited, stack1, stack2 = [source], [source], {source:0}
    while stack1:
        s = stack1.pop()
        print(s, end=" ")
        if s == dest:
            return True
        for child in graph[s]:
            if child not in visited:
                stack2[child] = stack2[s]+1
                if stack2[child]>level:
                    break
                visited.append(child)
                stack1.append(child)
    return False

def IterativeDLS(graph, source, dest, level):
    for i in range(level+1):
        if DLS(graph, source, dest, i):
            return "\n==>Destination Reached"
    return "\n==>Destination Not Reachable"

        
graph = {
    'Arad' : ['Timisoara', 'Sibia', 'Zaerind'],
    'Timisoara' : ['Arad','Lugoj'],
    'Sibia' : ['Arad','Sibui', 'Fagaras'],
    'Zaerind' : ['Arad','Orudea'],
    'Lugoj' : ['Timisoara'],
    'Sibui' : ['Sibia'],
    'Fagaras' : ['Sibia','Bucharest'],
    'Orudea' : ['Zaerind','Bucharest'],
    'Bucharest' : ['Fagaras']
}
source = 'Arad'
destination = 'Bucharest'
level=3
print(IterativeDLS(graph, source, destination, level))
