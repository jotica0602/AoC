class day_2:
    def solve_part1(self):
        with open('input.txt', 'r') as file:
            reports = [list(map(int, line.split())) for line in file]

        ans = 0

        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.

        for report in reports:
            if self.is_valid(report):
                ans += 1

        return ans
    
    def solve_part2(self):
        with open('input.txt', 'r') as file:
            reports = [list(map(int, line.split())) for line in file]

        ans = 0

        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.

        for report in reports:
            # check if it is an increasing or decreasing report
            if self.is_valid(report):
                ans += 1
            else:
                for i in range(len(report)):
                    new_report = report[:i] + report[i+1:]
                    if self.is_valid(new_report):
                        ans += 1
                        break
        
        return ans
    
    def is_valid(self, report):
        incr_or_decr = report == sorted(report) or report == sorted(report, reverse = True)

        # if not increasing nor decreasing proceed
        if not (incr_or_decr): 
            return 0

        flag = False
        for i in range(0,len(report)-1):
            if(not ((abs(report[i]-report[i+1]) >= 1) and (abs(report[i] - report[i+1]) <= 3))):
                return 0
        return 1
    
solver = day_2()
print(solver.solve_part1())
print(solver.solve_part2())