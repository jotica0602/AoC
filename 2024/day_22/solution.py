def mix(n,m): return n^m
def prune(n): return n & ((2 << 23) - 1)
    
def calculate_secret_number(n,times):
    for i in range(times):
        m = n << 6
        n = mix(n,m)
        n = prune(n)
        m = n >> 5
        n = mix(n,m)
        n = prune(n)
        m = n << 11
        n = mix(n,m)
        n = prune(n)
    return n

def get_best_price(prices):
    prev = 0
    for price in prices:
        act = price
        change = act - prev
        print(f'{price}',change) 
        prev = act   
        
        

class day22:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
        secret_numbers = list((map(int,text.split('\n'))))

        ans = 0
        for n in secret_numbers:
            ans += calculate_secret_number(n,2000)        
        return ans

    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
        secret_numbers = list((map(int,text.split('\n'))))

        ans = 0
        for n in secret_numbers:
            buyersseqs = [n % 10]
            buyersseqs.append(calculate_secret_number(n,2000) % 10)


        return ans
    
solver = day22()
print(solver.solve_part1())
# print(solver.solve_part2())