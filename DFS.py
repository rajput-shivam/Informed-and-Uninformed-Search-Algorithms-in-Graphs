#DFS

def dfs(graph, source, dest):
  visited, stack = [source], [source] 
  while stack:
    s = stack.pop()
    print(s, end = " ")
    if s == dest:
      return "\nRecahed Destination"
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)

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
dest = 'Bucharest'
print(dfs(graph, source, dest))
