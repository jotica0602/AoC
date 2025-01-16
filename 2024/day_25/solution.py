with open('input.txt') as file:
    input = file.read().splitlines()
    
def parse_lock(index,input,height,width,locks):
    h = [-1] * width
    for i in range(index,index + height):
        for j in range(width):
            if input[i][j] == '#':
                h[j] += 1
    locks.append(h)
    
def parse_key(index,input,height,width,keys):
    h = [-1] * width
    for i in range(index+height-1,index-1,-1):
        for j in range(width):
            if input[i][j] == '#':
                h[j] += 1
    keys.append(h)
    
height = -1
for i in range(len(input)):
    height += 1
    if input[i] == '':
        break
    
locks = []
keys = []
width = len(input[0])

for i in range(0,len(input),height+1):
    if input[i] == '#' * width:
        parse_lock(i,input,height,width,locks)
    if input[i+height-1] == '#' * width:
        parse_key(i,input,height,width,keys)

ans = 0
for i in range(len(locks)):
    for j in range(len(keys)):
        flag = True
        for k in range(width):
            if not locks[i][k] + keys[j][k] < height - 1:
                flag = False
                break
        ans += flag

print(ans)