import os
import heapq
from z3 import *

with open(f'{os.path.dirname(__file__)}/input.txt') as file:
    lines = [line.strip().split() for line in file.readlines()]

def toggle(button,lights):
    l = list(lights)
    for i in range(len(button)):
        l[button[i]] = '.' if l[button[i]] == '#' else '#'
    return ''.join(l)

def dijkstra(target,buttons):
    start = '.' * len(target)
    dist = {}
    dist = {start:0}
    q = []
    heapq.heappush(q,(dist[start],start))
    while q:
        actual_dist,last_lights = heapq.heappop(q)
        # get neighbors
        for button in buttons:
            next_lights = toggle(button,last_lights)
            if next_lights not in dist: dist[next_lights] = float('inf')
            # relax
            if dist[next_lights] > actual_dist + 1:
                dist[next_lights] = actual_dist + 1
                heapq.heappush(q,(actual_dist+1,next_lights))
    return dist[target]

def decompress(buttons,n):
    vectors = []
    for button in buttons:
        vec = [0] * n
        for i in range(len(button)):
            vec[button[i]] = 1
        vectors.append(tuple(vec))
    return vectors

def solve_integer_combination_z3(vectors, target):
    k = len(vectors)
    n = len(target)

    opt = Optimize()

    # defining variables
    x = [Int(f"x{i}") for i in range(k)]

    # adding constraints
    # xi >= 0 for all i
    for xi in x:
        opt.add(xi >= 0)

    for dim in range(n):
        opt.add(Sum(x[i] * vectors[i][dim] for i in range(k)) == target[dim])

    opt.minimize(Sum(x))

    if opt.check() != sat:
        return None

    model = opt.model()

    return tuple(model[xi].as_long() for xi in x)


def solve(part): 
    ans = 0
    if part == 1:
        for line in lines:
            target_lights = line[0].replace('[','').replace(']','')
            buttons = [tuple(map(int,button.replace('(','').replace(')','').split(','))) for button in line[1:-1]]
            ans += dijkstra(target_lights,buttons)

    if part == 2:
        for line in lines:
            target_req = tuple(map(int,line[-1].replace('{','').replace('}','').split(',')))
            n = len(target_req)
            buttons = [tuple(map(int,button.replace('(','').replace(')','').split(','))) for button in line[1:-1]]
            vectors = decompress(buttons,n)
            ans += sum(solve_integer_combination_z3(vectors, target_req))
    return ans
        
print(solve(part=1))
print(solve(part=2))