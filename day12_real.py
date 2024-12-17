from copy import deepcopy


s=0

def in_(i,j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) 


def place_wall(direction, i, j, matrix):
    if not in_(i,j, matrix):
        return
    if direction == 'horizontal':
        if matrix[i][j] == '_':
            matrix[i][j] = '+'
        else:
            matrix[i][j] = '|'
    else:
        if matrix[i][j] == '|':
            matrix[i][j] = '+'
        else:
            matrix[i][j] = '_'

def traverse(matrix, region):
    tot = 0
    
    for i in range(0, len(matrix), 2):
        curr = False
        direction = None
        for j in range(1, len(matrix), 2):
            if matrix[i][j] == " " or matrix[i][j] == '|':
                if curr:
                    tot += 1
                    matrix[i][j] = "O"
                curr = False
            elif matrix[i][j] == '_' or matrix[i][j] == '+':
                curr = True
                
            else:
                curr=True

        if curr:
            tot += 1

    for j in range(0, len(matrix), 2):
        curr = False
        for i in range(1, len(matrix), 2):

            if matrix[i][j] == " " or matrix[i][j] == '_':
                if curr:
                    tot += 1
                curr = False
            elif matrix[i][j] == '|' or matrix[i][j] == '+':
                curr = True
            else:
                curr=True
        if curr:
            tot += 1

    # for row in matrix:
    #     print(row)
        
    return tot
                
def calculate_per(i, j, region, seen, matrix ):
    per = 0
    area = 0
    
    if (i,j) in seen:
        return (0,0)
    else:
        seen.add((i,j))

    if in_(i - 2, j, matrix):
        if matrix[i-2][j] == region:
            val = calculate_per(i-2, j, region, seen, matrix )
            per += val[0]
            area += val[1]
        else:
            place_wall('vertical', i-1, j, matrix)
    else:
        place_wall('vertical', i-1, j, matrix)

    if in_(i + 2, j, matrix):
        if matrix[i+2][j] == region:
            val = calculate_per(i+2, j, region, seen, matrix )
            per += val[0]
            area += val[1]
        else:
            place_wall('vertical', i+1, j, matrix)
    else:
        place_wall('vertical', i+1, j, matrix)

    if in_(i, j+2, matrix):
        if matrix[i][j+2] == region:
            val = calculate_per(i, j+2, region, seen, matrix )
            per += val[0]
            area += val[1]
        else:
            place_wall('horizontal', i, j+1, matrix)
    else:
        place_wall('horizontal', i, j+1, matrix)


    if in_(i, j - 2, matrix):
        if matrix[i][j-2] == region:
            val = calculate_per(i, j - 2, region, seen, matrix )
            per += val[0]
            area += val[1]
        else:
            place_wall('horizontal', i, j-1, matrix)

    else:
        place_wall('horizontal', i, j-1, matrix)

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
        matrix.append([' ' for x in range(len(matrix[0]))])

    matrix.insert(0, [' ' for x in range(len(matrix[0]))])

seen = set()
prices = {}


for i in range(1,len(matrix), 2):
    for j in range(1,len(matrix[0]),2):

        m = deepcopy(matrix)
        val = calculate_per(i, j, matrix[i][j], seen, m)
        perms = traverse(m)
        
        curr = dict.get(prices, matrix[i][j],(0,0))
        if perms != 0:
            print(perms, val[1],m[i][j])
            for row in m:
                print(row)
        s += perms*val[1]
        #prices[matrix[i][j]] = (curr[0] + val[0], curr[1] + val[1])
    #print(str(i) + '/' + str(len(matrix)))
    

# for k in prices:
#     s += prices[k][0] * prices[k][1]

print(s)