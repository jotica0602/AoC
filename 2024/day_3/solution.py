import regex


class day3:
    def solve_part1():
        with open('input.txt','r') as file:
            text = file.read()

        p1 = r'mul\(\d+\,\d+\)'
        p2 = r'\d+'

        results = regex.findall(p1,text)

        ans = 0
        for result in results:
            digits = regex.findall(p2,result)
            op_result = int(digits[0]) * int(digits[1])
            ans += op_result
        return ans
    
    def solve_part2():
        with open('input.txt','r') as file:
            text = file.read()

        pattern = r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)"
        p2 = r'\d+'

        results = regex.findall(pattern,text)
        flag = False

        ans = 0
        for result in results:
            if result == 'do()':
                flag = False
                continue

            if result == 'don\'t()':
                flag = True
                continue
            
            if not flag and result != 'do()' and result != 'don\'t()':
                digits = regex.findall(p2,result)
                op_result = int(digits[0]) * int(digits[1])
                ans += op_result

        return ans


print(day3.solve_part1())
print(day3.solve_part2())