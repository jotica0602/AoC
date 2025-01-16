with open('input.txt','r') as file:
    connections = file.read().splitlines()
    
graph = {}
for connection in connections:
    x,y = connection.split('-')
    
    if x not in graph: graph[x] = set()
    if y not in graph: graph[y] = set()
    
    
    graph[x].add(y)
    graph[y].add(x)

seen = set()

def find_clique(graph,clique,v,seen,size):
    for neighbor in graph[v]:
        if all(neighbor in graph[n] for n in clique) and neighbor not in clique:
            seen.add(neighbor)
            return find_clique(graph,clique | {neighbor}, neighbor, seen,size + 1)

    return size,clique

best = -1
ans = {}

for v in graph:
    size, clique = find_clique(graph,{v},v,seen,1)
    if size > best: 
        best = size
        ans = clique
            
print(str.join(',',sorted(ans)),size)        