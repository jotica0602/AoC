def operate_block(block,operation):
    result = 0 if operation == '+' else 1
    for n in block:
        result = result + int(n) if operation == '+' else result * int(n)
    return result

def get_num(block:tuple[str]):
    n = len(block)
    num = ''
    for i in range(n):
        if block[i].isnumeric():
            num += block[i]
    return num

def solve(part):
    ans = 0
    if part == 1:
        with open('input.txt') as file:
            lines = [line.split() for line in file.readlines()]
        blocks = list(zip(*lines))
        for block in blocks:
            ans += operate_block(block[:-1],block[-1])

    if part == 2:
        with open('input.txt') as file:
            lines = [list(line) for line in file.readlines()]
            blocks = list(zip(*lines))

        operator = ''
        nums = []
        for block in blocks:
            if block[-1] == '+': operator = '+'
            if block[-1] == '*': operator = '*'
            n = get_num(block)
            if n == '':
                ans += operate_block(nums,operator)
                nums.clear()
            else: 
                nums.append(n)

    return ans

print(solve(part=1))
print(solve(part=2))