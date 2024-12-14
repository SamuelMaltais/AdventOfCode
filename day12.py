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

    act = [False, False, False, False]
    act[0] = activations[(i,j-1)][0] or activations[(i,j-1)][0]
    act[1] = activations[(i,j-1)][1] or activations[(i,j+1)][1]
    act[2] = activations[(i+1,j)][2] or activations[(i-1,j)][2]
    act[3] = activations[(i+1,j)][3] or activations[(i-1,j)][3]
    gauche = act[0]
    droite = act[1]
    top = act[2]
    down = act[3]

    if in_(i - 1, j, matrix):
        if matrix[i-1][j] == region:
            val = calculate_per(i-1, j, region, seen, matrix, activations)
            per += val[0]
            area += val[1]
        else:
            if not gauche:
                per += 1
                act[0] = True
    else:
        if not gauche:
            per += 1
            act[0] = True

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
        if not droite:
            per += 1
            act[1] = True

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
        matrix.append(line)


seen = set()
prices = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        rows = set()
        columns = set()
        val = calculate_per(i, j, matrix[i][j], seen, matrix, rows, columns)
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