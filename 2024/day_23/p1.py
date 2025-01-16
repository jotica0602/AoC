with open('input.txt','r') as file:
    connections = file.read().splitlines()
    
graph = {}
for connection in connections:
    x,y = connection.split('-')
    
    if x not in graph: graph[x] = set()
    if y not in graph: graph[y] = set()
    
    
    graph[x].add(y)
    graph[y].add(x)


threesets = set()
targets = [v for v in graph if v.startswith('t')]

for target in targets:
    for neighbor in graph[target]:
        for n in graph[neighbor]:
            if n == neighbor or neighbor == target or target == n: continue
            if n in graph[target]:
                threesets.add(tuple(sorted([target,neighbor,n])))
            
print(len(threesets))