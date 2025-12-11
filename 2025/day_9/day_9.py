with open('input.txt') as file:
    points = [tuple(map(int,line.strip().split(','))) for line in file.readlines()]

yc = sorted({y for y,_ in points})
xc = sorted({x for _,x in points})
n = len(points)

def encode_axis(axis):
    encoded_axis = {axis[0]:0}
    gap = 1
    for i in range(1,len(axis)):
        if axis[i-1] != axis[i] - 1:
            gap += 1
        encoded_axis[axis[i]] = gap
        gap += 1
    return encoded_axis

xmap = encode_axis(xc)
ymap = encode_axis(yc)

def neighbors(x,y):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dx,dy in directions:
        yield x+dx,y+dy

def is_in_segment(xp,yp,x1,y1,x2,y2):
    if min(x1,x2) <= xp <= max(x1,x2) and min(y1,y2) <= yp <= max(y1,y2):
        return (x2-x1) * (yp-y1) == (y2-y1) * (xp-x1)

def is_inside(xp,yp,segments):
    count = 0
    for i in range(n):
        (x1,y1),(x2,y2) = segments[i],segments[(i+1) % n]
        if is_in_segment(xp,yp,x1,y1,x2,y2): return True
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1)/(y2-y1)) * (x2-x1):
            count += 1

    return count % 2 == 1

def fill_segments(grid,segments):
    for i in range(len(segments)):
        x1,y1 = segments[i]
        x2,y2 = segments[(i+1)%n]
        if x1 == x2:
            for j in range(min(y1,y2)+1,max(y1,y2)):
                grid[x1][j] = 'O'
        if y1 == y2:
            for j in range(min(x1,x2)+1,max(x1,x2)):
                grid[j][y1] = 'O'

def fill_grid(sx,sy,grid,segments):
    q = [(sx,sy)]
    valid = lambda x,y: 0<= x < len(grid) and 0 <= y < len(grid[0])
    while q:
        x,y = q.pop(0)
        for nx,ny in neighbors(x,y):
            if not valid(nx,ny): continue
            if grid[nx][ny] == '#' or grid[nx][ny] == 'O': continue
            if is_inside(nx,ny,segments):
                q.append((nx,ny))
                grid[nx][ny] = 'O'

def solve(part):
    ans = 0
    if part == 1:
        for i in range(n-1):
            x1,y1 = points[i]
            for j in range(n):
                x2,y2 = points[j]
                ans = max(ans,(abs(x1-x2)+1) * (abs(y1-y2)+1))

    if part == 2:
        H = xmap[xc[-1]] + 1
        W = ymap[yc[-1]] + 1
        new_points = [(xmap[x],ymap[y]) for (y,x) in points]
        grid = [['.'] * W for _ in range(H)]
        for (x,y) in new_points:
            grid[x][y] = '#'

        fill_segments(grid,new_points)
        (fx,fy) = new_points[0]
        fill_grid(fx,fy,grid,new_points)

        for i in range(n):
            for j in range(i+1,n):
                (y1,x1),(y2,x2) = points[i],points[j]
                a,b = abs(y1-y2) + 1, abs(x1-x2) + 1
                area = a * b
                if area > ans and is_filled(x1,y1,x2,y2,grid):
                    ans = area
    return ans

def is_filled(x1,y1,x2,y2,grid):
    filled = True
    x1 = xmap[x1]
    y1 = ymap[y1]
    x2 = xmap[x2]
    y2 = ymap[y2]

    for i in range(min(x1,x2),max(x1,x2)+1):
        for j in range(min(y1,y2),max(y1,y2)+1):
            filled = grid[i][j] == '#' or grid[i][j] == 'O'
            if not filled: return False
    return True

print(solve(part=1))
print(solve(part=2))