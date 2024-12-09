
class day8:
    def solve_part1(self):
        with open('input.txt','r') as file:
            lines = file.read().split()
            
        def is_in_bounds(antinode,grid):
            return antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid)
                
        grid = [list(line) for line in lines]


        antennas = {}

        # first i need to get all the antennas
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != '.' and grid[i][j] not in antennas:
                    antennas[grid[i][j]] = [(i,j)]
                elif grid[i][j] != '.' and grid[i][j] in antennas:
                    antennas[grid[i][j]].append((i,j))
                    
        # now i need to find where the antinodes occurs

        antinodes = set()
        for antenna in antennas:
            for i in range(len(antennas[antenna])):
                x1,y1 = antennas[antenna][i]
                for j in range(i+1,len(antennas[antenna])):
                    x2,y2 = antennas[antenna][j]
                    antinodes.add((2*x1 - x2, 2*y1 - y2))
                    antinodes.add((2*x2 - x1, 2*y2 - y1))
     
        ans = len([antinode for antinode in antinodes if is_in_bounds(antinode,grid)])
        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            lines = file.read().split()
            
        def is_in_bounds(antinode,grid):
            return antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid)
                
        grid = [list(line) for line in lines]


        antennas = {}

        # first i need to get all the antennas
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != '.' and grid[i][j] not in antennas:
                    antennas[grid[i][j]] = [(i,j)]
                elif grid[i][j] != '.' and grid[i][j] in antennas:
                    antennas[grid[i][j]].append((i,j))
                    
        # now i need to find where the antinodes occurs

        antinodes = set()
        for antenna in antennas:
            for i in range(len(antennas[antenna])):
                x1,y1 = antennas[antenna][i]
                for j in range(len(antennas[antenna])):
                    if i == j: continue
                    x2,y2 = antennas[antenna][j]
                    delta_x, delta_y = x1-x2, y1-y2
                    x,y = x1,y1
                    while is_in_bounds((x,y),grid):
                        antinodes.add((x,y))
                        x += delta_x
                        y += delta_y

        ans = len(antinodes)
        return ans
    
solver = day8()
print(solver.solve_part1())
print(solver.solve_part2())

