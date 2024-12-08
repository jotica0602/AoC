import heapq
from sortedcontainers import SortedList

class day1:
    def solve_part1():
        with open('input.txt','r') as file:
            text = file.read()
            data = text.split()

        l1 = [int(data[i]) for i in range(0,len(data),2)]
        l2 = [int(data[i]) for i in range(1,len(data),2)]
        l1.sort()
        l2.sort()

        ans = 0
        for i in range(len(l1)):
            ans += abs(l1[i] - l2[i])

        return ans
    
    def solve_part2():
        with open('input.txt','r') as file:
            text = file.read()
            data = text.split()

        l1 = [int(data[i]) for i in range(0,len(data),2)]
        l2 = [int(data[i]) for i in range(1,len(data),2)]

        ms = SortedList()

        for num in l1: 
            if ms.__contains__(num):
                continue
            ms.add(num)

        for num in l2:
            if ms.__contains__(num):
                ms.add(num)

        ans = 0
        for element in l1:
            ans += element * (ms.count(element)-1)
        
        return ans

print(day1.solve_part1())
print(day1.solve_part2())