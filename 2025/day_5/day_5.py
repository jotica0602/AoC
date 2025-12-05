def solve(part):
    with open('input.txt') as file:
        lines = file.read().split()

    ranges = []
    nums = []

    for line in lines:
        if '-' in line:
            s,f = list(map(int,line.split('-')))
            ranges.append((s,f))
        else:
            nums.append(int(line))

    ranges.sort(key=lambda x:x[0])
    intervals = [ranges.pop(0)]
    ans = 0

    # an interval (s,f) is extandable by another interval (i,j) if: s <= i <= f and f < j
    while ranges:
        i,j = ranges.pop(0)
        s,f = intervals[-1]
        if s <= i <= f and f < j:
            intervals[-1] = (s,j)
        if i > f:
            intervals.append((i,j))
    if part == 1:
        for n in nums:
            for s,f in intervals:
                if s <= n <= f:
                    ans += 1
    if part == 2:
        for s,f in intervals:
            ans += f-s + 1
    return ans

print(solve(part=1))
print(solve(part=2))