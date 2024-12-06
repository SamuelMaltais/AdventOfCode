import sys
turn = {
    (-1, 0): (0, 1),
    (0,1): (1,0),
    (1,0): (0, -1),
    (0,-1): (-1,0)
}
sys.setrecursionlimit(9999999)

def move(matrix ,curr_direction, i, j, s, m):
  

    next_i = i + curr_direction[0]
    next_j = j + curr_direction[1]

    if (i,j, next_i, next_j) in m:
        return -1

    if not (0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0])):
        return s
    else:
        if matrix[next_i][next_j] == '#':
            return move(matrix, turn[curr_direction], i, j, s, m)
        else:
            if (i, j) in m:
                return move(matrix, curr_direction, next_i, next_j, s, m)
            else:
                m.add((i,j, next_i, next_j))
                return move(matrix, curr_direction, next_i, next_j, s+1, m)

with open('in.txt', 'r') as file:
    matrix = []
    for line in file:
        line = line.strip()
        matrix.append(list(line))

    ini_i = 0
    ini_j = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                m = set()
                m.add((i,j,-1,0))
                s = move(matrix, (-1,0), i, j, 1, set())
                ini_i = i
                ini_j = j

    s2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                matrix[i][j] = '#'

                m = set()
                m.add((i,j,-1,0))
                mmh = move(matrix, (-1,0), ini_i, ini_j, 1, set())
                if mmh == -1:
                    s2 +=1 
                    print(s2)
                matrix[i][j] = '.'

print(s)
print(s2)


