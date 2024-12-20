import sys
from copy import deepcopy

sys.setrecursionlimit(999999999)

def in_(i,j,m):
    if 0 <= i < len(m) and 0 <= j < len(m[0]):
        return m[i][j]
    else:
        return '#'

def dfs(i,j,m, moves, mem):

    if (i,j) in mem:
        if moves < mem[(i,j)]:
            mem[(i,j)] = moves
        else:
            return
    else:
        mem[(i,j)] = moves

    if in_(i+1, j, m) != '#':
        dfs(i+1, j, m, moves + 1, mem)
    if in_(i-1, j, m) != '#':
        dfs(i-1, j, m, moves + 1, mem)
    if in_(i, j+1, m) != '#':
        dfs(i, j+1, m, moves + 1, mem)
    if in_(i, j-1, m) != '#':
        dfs(i, j-1, m, moves + 1, mem)
        

m = []
with open ('in_real.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace(' ', '')
        m.append(line)

start = (0,0)
end = (0,0)

for j in range(len(m)):
    for i in range(len(m[0])):
        if m[i][j] == 'S':
            start = (i,j)
        elif m[i][j] == 'E':
            end = (i,j)

mem = {}
dfs(start[0],start[1],m, 0, mem)
initial = mem[end]

mem_end_based = {}
dfs(end[0], end[1],m, 0, mem_end_based)

s = 0
for pos in mem:
    cheats = []
    for x in range(-20,21):
        for y in range(-20,21):
            if abs(x) + abs(y) <= 20:
                cheats.append((x,y))
    for cheat in cheats:
        i = pos[0] + cheat[0]
        j = pos[1] + cheat[1]
        if in_(i,j,m) != '#':
            if (i,j) in mem:
                moves = mem[pos] + mem_end_based[(i,j)] + abs(cheat[0]) + abs(cheat[1])
                if moves + 100 <= initial:
                    s += 1
print(s)
  
