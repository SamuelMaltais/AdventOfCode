s=0
matrix = []

def travel(i, j, curr, visited, matrix):
    tot = 0
    visited = set()
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        pass
    else:
        return 0
    
    if curr == 9:
        return 1

    if 0 <= i+1 < len(matrix):
        if matrix[i + 1][j] == curr + 1:
            if (i+1, j) not in visited:
                visited.add((i+1, j))
                tot += travel(i + 1, j, curr + 1, visited, matrix)
    if 0 <= i-1 < len(matrix):
        if matrix[i - 1][j] == curr + 1:
            if (i-1, j) not in visited:
                visited.add((i-1, j))
                tot += travel(i - 1, j, curr + 1, visited, matrix)
        
    if 0 <= j+1 < len(matrix[0]):
        if matrix[i][j + 1] == curr + 1:
            if (i, j + 1) not in visited:
                visited.add((i, j + 1))
                tot += travel(i, j + 1, curr + 1, visited, matrix)
        
    if 0 <= j-1 < len(matrix[0]):
        if matrix[i][j - 1] == curr + 1:
            if (i, j - 1) not in visited:
                visited.add((i, j - 1))
                tot += travel(i, j - 1, curr + 1, visited, matrix)
    
    return tot

with open('in.txt', 'r') as file:
    for line in file:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        matrix.append(list(map(int,row)))



for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            visited = set()
            visited.add((i,j))
            s += travel(i, j, 0, visited, matrix)





print(s)