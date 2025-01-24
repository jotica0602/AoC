import regex

class day5:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()

        htp = r'\d+\|\d+'
        up = r'\d+\,\S+'

        heads_and_tails = regex.findall(htp,text)
        graph = {}

        for head_and_tail in heads_and_tails:
            head,tail = list(map(int,head_and_tail.split('|')))
            
            if head not in graph:
                graph[head] = [tail]
                continue
            
            graph[head].append(tail)

        updates = regex.findall(up,text)
        updates = [list(map(int, upd.split(','))) for upd in updates]

        ans = 0
        
        for update in updates:
            induced_graph = self.get_induced_graph(update,graph)
            indegs = self.get_indegs(induced_graph)
            # check if the update is a valid topological sort
            if self.is_ts(update,indegs,induced_graph):
                ans += update[len(update)//2]
        return ans

    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()

        htp = r'\d+\|\d+'
        up = r'\d+\,\S+'

        heads_and_tails = regex.findall(htp,text)
        graph = {}

        for head_and_tail in heads_and_tails:
            head,tail = list(map(int,head_and_tail.split('|')))
            if head not in graph:
                graph[head] = [tail]
                continue
            graph[head].append(tail)

        updates = regex.findall(up,text)
        updates = [list(map(int, upd.split(','))) for upd in updates]

        ans = 0
        for update in updates:
            induced_graph = self.get_induced_graph(update,graph)
            indegs = self.get_indegs(induced_graph)
            # check if the update is a valid topological sort
            if not self.is_ts(update,indegs,induced_graph):
                ts = self.get_ts(induced_graph)
                ans += ts[(len(ts)-1)//2]
        return ans
    
    def get_indegs(self,graph):
        indeg = {node:0 for node in graph}
        for node in indeg:
            for n in graph:
                if node in graph[n]:
                    indeg[node] += 1
        return indeg

    def disconnect(self,node,indegs,graph):
        for neighbor in graph[node]:
            indegs[neighbor] -= 1    
            
    def is_ts(self,ts,indegs,graph):
        for node in ts:
            if indegs[node] == 0:
                self.disconnect(node,indegs,graph)
            else:
                return False
        return True
    
    def get_ts(self, graph:dict):
        ts = []  # topo sort list
        visited = set()
        for node in graph:
            if node not in visited:
                self.dfs_visit(node, graph, visited, ts)
        ts.reverse()
        return ts
    
    def dfs_visit(self, node, graph:dict, visited:set, ts:list):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs_visit(neighbor, graph, visited, ts)
        ts.append(node)
        
    def get_induced_graph(self,update,graph):
        induced_graph = {}
        for vertex in update:
            induced_graph[vertex] = [neighbor for neighbor in graph[vertex] if neighbor in update]
        return induced_graph
            
solver = day5()
print(solver.solve_part1())
print(solver.solve_part2())