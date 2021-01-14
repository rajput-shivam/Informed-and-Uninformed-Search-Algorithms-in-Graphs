def get_key(graph,val,visited): 
    for key, value in graph.items():
        if val in value and key in visited:
            return key 

def DLS(graph, source, dest, level):
    if source == dest:
        return "Already at Destination"
    visited, stack1, stack2 = [source], [source], {source:0}
    while stack1:
        s = stack1.pop()
        print(s, end=" ")
        if s == dest:
            return "\n==>Reached Destination"
        for child in graph[s]:
            if child not in visited:
                parent = get_key(graph,child,visited)
                stack2[child] = stack2[parent]+1
                if stack2[child]>level:
                    break
                visited.append(child)
                stack1.append(child)
    return "\n==>Cannnot Reach Destination"

graph = {
    'Arad' : ['Timisoara', 'Sibia', 'Zaerind'],
    'Timisoara' : ['Arad','Lugoj'],
    'Sibia' : ['Arad','Sibui', 'Fagaras'],
    'Zaerind' : ['Arad','Orudea'],
    'Lugoj' : ['Timisoara'],
    'Sibui' : ['Sibia'],
    'Fagaras' : ['Sibia','Bucharest'],
    'Orudea' : ['Zaerind'],
    'Bucharest' : ['Fagaras']
}
source = 'Arad'
destination = 'Bucharest'
level=2
print(DLS(graph, source, destination, level))
