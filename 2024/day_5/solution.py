import regex

class day5:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()

        htp = r'\d+\|\d+'
        hp=r'(\d+)\|'
        tp = r'\|(\d+)'
        up = r'\d+\,\S+'

        heads_and_tails = regex.findall(htp,text)
        graph = {}

        for head_and_tail in heads_and_tails:
            head = int(regex.findall(hp,head_and_tail)[0])
            
            if head not in graph:
                graph[head] = [int(regex.findall(tp,head_and_tail)[0])]
                continue
            
            graph[head].append(int(regex.findall(tp,head_and_tail)[0]))

        updates = regex.findall(up,text)
        updates = [list(map(int, upd.split(','))) for upd in updates]

        for head_and_tail in heads_and_tails:
            tail = int(regex.findall(tp,head_and_tail)[0])
            if tail not in graph:
                graph[tail] = []
        
        ans = 0
        
        for update in updates:
            indegs = self.get_indegs(graph)
            
            nodes = set(graph.keys())
            dif = set(nodes).difference(update)
            
            # disconnect diff nodes from graph
            for node in dif:
                self.disconnect(node,indegs,graph)
                
            # check if the update is a valid topological sort
            if self.is_ts(update,indegs,graph):
                ans += update[len(update)//2]
                
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
        is_top_sort = True
        for node in ts:
            if indegs[node] == 0:
                self.disconnect(node,indegs,graph)
            else:
                is_top_sort = False
        
        return is_top_sort
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()

        htp = r'\d+\|\d+'
        hp=r'(\d+)\|'
        tp = r'\|(\d+)'
        up = r'\d+\,\S+'

        heads_and_tails = regex.findall(htp,text)
        graph = {}

        for head_and_tail in heads_and_tails:
            head = int(regex.findall(hp,head_and_tail)[0])
            
            if head not in graph:
                graph[head] = [int(regex.findall(tp,head_and_tail)[0])]
                continue
            
            graph[head].append(int(regex.findall(tp,head_and_tail)[0]))

        updates = regex.findall(up,text)
        updates = [list(map(int, upd.split(','))) for upd in updates]

        for head_and_tail in heads_and_tails:
            tail = int(regex.findall(tp,head_and_tail)[0])
            if tail not in graph:
                graph[tail] = []
        
        ans = 0
        
        ts = self.get_ts(graph)
        print(ts)
        
        for update in updates:
            indegs = self.get_indegs(graph)
            
            nodes = set(graph.keys())
            dif = set(nodes).difference(update)
            
            # disconnect diff nodes from graph
            for node in dif:
                self.disconnect(node,indegs,graph)
                
            # check if the update is invalid
            if not self.is_ts(update,indegs,graph):
                induced_graph = self.get_induced_graph(update,graph)
                ts = self.get_ts(induced_graph)
                ts.reverse()
                dif = [v for v in ts if v in update]
                ans += dif[len(dif)//2]
                   
        return ans
    
    def get_ts(self, graph:dict):
        ts = []  # Lista para almacenar el orden topológico
        visited = set()  # Conjunto para mantener los nodos visitados
        for node in graph:
            if node not in visited:
                self.dfs_visit(node, graph, visited, ts)
        return ts
    
    def dfs_visit(self, node, graph:dict, visited:set, ts:list):
        visited.add(node)
        for neighbor in graph[node]:  # Obtener vecinos del nodo actual
            if neighbor not in visited:
                self.dfs_visit(neighbor, graph, visited, ts)
        ts.append(node)  # Agregar nodo al orden topológico al finalizar
        
    def get_induced_graph(self,update,graph):
        induced_graph = {}
        for vertex in update:
            induced_graph[vertex] = [neighbor for neighbor in graph[vertex] if neighbor in update]
        return induced_graph
            
solver = day5()
print(solver.solve_part1())
print(solver.solve_part2())