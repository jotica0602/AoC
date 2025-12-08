import heapq
from math import dist,prod

with open('input.txt') as file:
    coords = [tuple(map(int,line.strip().split(','))) for line in file.readlines()]

parent = {coord:coord for coord in coords}

def set_of(x):
    if parent[x] == x: return x
    parent[x] = set_of(parent[x])
    return parent[x]

def merge(x,y):
    px,py = set_of(x), set_of(y)
    if px == py: return False
    parent[py] = px
    return True

def solve(part):
    q = []
    n = len(coords)
    ans = 0

    for i in range(n-1):
        a = coords[i]
        for j in range(i+1,n):
            b = coords[j]
            heapq.heappush(q,(dist(a,b),(a,b)))

    if part == 1:
        for _ in range(1000):
            _,c = heapq.heappop(q)
            c1,c2 = c
            merge(c1,c2)
        size = {}
        for node in parent:
            p = set_of(node)
            if p not in size:
                size[p] = 0
            size[p] += 1
        ans = prod(sorted(size.values())[-3:])

    if part == 2:
        while q:
            _,c = heapq.heappop(q)
            c1,c2 = c
            if merge(c1,c2):
                ans = c1[0] * c2[0]
    return ans

print(solve(part=1))
print(solve(part=2))