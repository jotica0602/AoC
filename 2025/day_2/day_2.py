with open('input.txt') as file:
    ranges = file.read().split(',')

def solve(ranges:list[str],part):
    ans = 0
    for r in ranges:
        s,f = map(int,r.split('-'))
        for id in range(s,f+1):
            id_ = str(id)
            n = len(id_)
            if part == 1:
                if n % 2 == 0 and 2 * id_[:n//2] == id_:
                    ans += int(id) 
            else:
                for i in range(1,n):
                    if n % i == 0 and (n // i) * id_[:i] == id_:
                        ans += int(id)
                        break
    return ans

print(solve(ranges,part=1))
print(solve(ranges,part=2))