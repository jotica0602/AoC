import re
        
with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

pattern = r'\w+'
graph = {}

for i in range(2,len(lines)):
    node_values = re.findall(pattern,lines[i])
    u,v,w = node_values
    graph[u] = [v,w]

directions = lines[0]
n = len(directions)
index = 0
current_node = 'AAA'
steps = 0

while current_node != 'ZZZ':
    current_node = graph[current_node][0] if directions[index] == 'L' else graph[current_node][1]    
    steps += 1
    index = (index + 1) % n
    
print(steps)