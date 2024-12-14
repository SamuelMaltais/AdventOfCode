s=0

def in_(i,j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) 

def calculate_per(i, j, region, seen, matrix, activations):
    per = 0
    area = 0
    
    if (i,j) in seen:
        return (0,0)
    else:
        seen.add((i,j))

    if in_(i - 1, j, matrix):
        if matrix[i-1][j] == region:
            val = calculate_per(i-1, j, region, seen, matrix, activations)
            per += val[0]
            area += val[1]
        else:
            pass
    else:
        pass

    if in_(i + 1, j, matrix):
        if matrix[i+1][j] == region:
            val = calculate_per(i+1, j, region, seen, matrix, activations)
            per += val[0]
            area += val[1]
        else:
            if not droite:
                per += 1
                act[1] = True
    else:
        matrix[i][j]

    if in_(i, j+1, matrix):
        if matrix[i][j+1] == region:
            val = calculate_per(i, j+1, region, seen, matrix, activations)
            per += val[0]
            area += val[1]

            

        else:
            if j+1 not in column:
                per += 1
                column.add(j+1)

    else:
        if j+1 not in column:
                per += 1
                column.add(j+1)

    if in_(i, j - 1, matrix):
        if matrix[i][j-1] == region:
            val = calculate_per(i, j - 1, region, seen, matrix, activations)
            per += val[0]
            area += val[1]
        else:
            if j not in column:
                per += 1
                column.add(j)
    else:
        if j not in column:
                per += 1
                column.add(j)

    return (per, area + 1)
    

matrix = []
with open('in3.txt', 'r') as file:

    for line in file:
        line = line.strip()
        row = []
        for i in range(len(line)*2 + 1):
            if i % 2 == 0:
                row.append(' ')
            else:
                row.append(line[i//2])
        matrix.append(row)

    matrix.insert(0, [' ' for x in range(len(matrix[0]))])

print(matrix)
seen = set()
prices = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        rows = set()
        columns = set()
        val = calculate_per(i, j, matrix[i][j], seen, matrix[:][:], rows, columns)
        perms = val[0]
        # for v in rows:
        #     for i in range(len(matrix[0])):
        #         if in_(v, i, matrix) and in_(v,i+1, matrix):
        #             if matrix[v][i] == matrix[v][i+1]:
        #                 perms += 1
        # for v in columns:
        #     for i in range(len(matrix)):
        #         if in_(i, v, matrix) and in_(i+1,v, matrix):
        #             if matrix[i][v] == matrix[i+1][v]:
        #                 perms += 1

        curr = dict.get(prices, matrix[i][j],(0,0))
        s += perms*val[1]
        #prices[matrix[i][j]] = (curr[0] + val[0], curr[1] + val[1])

# for k in prices:
#     s += prices[k][0] * prices[k][1]

print(s)