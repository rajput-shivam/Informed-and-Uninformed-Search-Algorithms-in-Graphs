#BFS

def bfs(graph, source, dest):
  if source == dest:
    return "Already At Destination"
  visited, queue = [source], [source] 
  while queue:                  # non-empty-list = infinite-iteration / empty-list = no-iteration
    print (queue,"---->",end=" ")
    s = queue.pop(0)
    print (queue,"\t:",s)
    if s == dest:
      return "Reached Destination"
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

graph = {
    'O':['S','Z'],
    'Z':['A'],
    'A':['S','T','Z'],
    'S':['A','F','R','O'],
    'F':['B','S'],
    'R':['C','P','S',],
    'P':['B','C','R'],
    'T':['A','L'],
    'L':['T','M'],
    'M':['L','D'],
    'D':['M','C'],
    'C':['D','R','P'],
    'B':['P','F','G','U'],
    'G':['B'],
    'U':['B','H','V'],
    'H':['U','E'],
    'E':['H'],
    'V':['U','I'],
    'I':['N','V'],
    'N':['I']
}
source = 'A'
dest = 'V'
print(bfs(graph, source, dest))
