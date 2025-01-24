
class day23:
    def solve_part1(self):
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
                    
        return len(threesets)
    
    def solve_part2(self):
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
                    
        return str.join(',',sorted(ans))
    
solver = day23()
print(solver.solve_part1())
print(solver.solve_part2())        