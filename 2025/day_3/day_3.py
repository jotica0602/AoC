with open('input.txt') as f:
    lines = f.read().split()

def solve(lines,part):
    ans = 0
    for line in lines:
        n = len(line)
        start = 0
        num = ''
        size = 2 if part == 1 else 12
        length = size
        while length > 0:
            m = '0'
            for i in range(start,n-length+1):
                if line[i] > m and length - 1 <= n - i:
                    m = line[i]
                    start = i + 1
            num += m
            length -= 1
        ans += int(num)
    return ans

print(solve(lines,part=1))
print(solve(lines,part=2))