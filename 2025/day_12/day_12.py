import os 
from math import prod

with open(f'{os.path.dirname(__file__)}/input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

areas = []
matrices = []

area = 0
for i in range(len(lines)):
    if '#' in lines[i]:
        area += lines[i].count('#')
    if lines[i] == '': 
        areas.append(area)
        area = 0
    if 'x' in lines[i]:
        matrices.append((
            prod(list(
                map(
                    int,
                    lines[i][0:lines[i].index(':')].split('x'))
                    )
                ),
            list(
                map(
                    int,
                    lines[i][lines[i].index(':')+1:].split()
                    )
                )
                ))

ans = 0
for (area,shapes) in matrices:
    print(list(zip(areas,shapes)))
    print(sum(list(a * b for (a,b) in zip(areas,shapes))),area)
    if sum(list(a * b for a,b in zip(areas,shapes))) <= area:
        ans += 1

print(ans)