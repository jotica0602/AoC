with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def solve(lines:list[str],part):
    start = 50
    ans = 0
    if part == 1:
        for line in lines:
            num = int(line[1:])
            start = (start - num) % 100 if line.startswith('L') else (start + num) % 100
            if start == 0: 
                ans += 1

    if part == 2:
        for line in lines:
            num = int(line[1:])
            for _ in range(num):
                start = (start - 1) % 100 if line.startswith('L') else (start + 1) % 100
                if start == 0: 
                    ans += 1 
    return ans

print(solve(lines,part=1))
print(solve(lines,part=2))