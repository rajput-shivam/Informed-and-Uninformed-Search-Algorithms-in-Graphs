#DFS-BACKTRACKING

def dfs(graph, source, dest):
  visited, stack = [source], [source]
  while stack:
          s = stack[0]
          print("\n",s, end ="")
          i = -1
          for child in graph[s]:
                  if child not in visited:
                          i = i+1
                          visited.insert(i, child)
                          stack.insert(i, child)
                          break
          if i == -1:
                  if s==dest:
                          return("==>DESTINATION FOUND")
                  else:
                          print("==> DESTINATION NOT FOUND", end="")
                  visited.remove(graph[s][0])
                          
                  
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
dest = 'Arad'
print(dfs(graph, source, dest))
