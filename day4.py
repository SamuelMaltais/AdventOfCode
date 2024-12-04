s=0
s2 = 0

def search(i,j, word, m, di, dj):
    c = 0
    
    while i < len(m) and j < len(m[i]) and i >=0 and j >=0 and word[c] == m[i][j]:
        i = i + di
        j = j + dj
        c += 1
        if c == len(word):
            break

    if c == len(word):
        return 1
    else:
        return 0

with open('in.txt', 'r') as file:
    matrix = []
    for line in file:
        line = line.strip()
        matrix.append(line)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s += search(i, j, 'XMAS', matrix, 0, 1)
            s += search(i, j, 'XMAS', matrix, 0, -1)


            s += search(i, j, 'XMAS', matrix, 1, 0)
            s += search(i, j, 'XMAS', matrix, -1, 0)


            s += search(i, j, 'XMAS', matrix, 1, 1)

            s += search(i, j, 'XMAS', matrix, -1, 1)
            s += search(i, j, 'XMAS', matrix, 1, -1)
            s += search(i, j, 'XMAS', matrix, -1, -1)

            cond1   = False
            cond2 = False
            if search(i, j, 'AS', matrix, -1, -1) == 1:
                if search(i, j, 'AM', matrix, 1, 1) == 1:
                    cond1 = True
            if search(i, j, 'AM', matrix, -1, -1) == 1:
                if search(i, j, 'AS', matrix, 1, 1) == 1:
                    cond1 = True
            if search(i, j, 'AS', matrix, 1, -1) == 1:
                if search(i, j, 'AM', matrix, -1, 1) == 1:
                    cond2 = True
            if search(i, j, 'AM', matrix, 1, -1) == 1:
                if search(i, j, 'AS', matrix, -1, 1) == 1:
                    cond2 = True
            if cond1 and cond2:
                s2 += 1
            



print(s)
print(s2)
