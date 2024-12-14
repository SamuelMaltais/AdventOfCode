from copy import deepcopy
import time
s=0

def printm(matrix):
    for row in matrix:
        print(row)

matrix = []

w=101
h=103
# w=11
# h=7

for i in range(h):
    matrix.append([0 for i in range(w)])


robots = []

with open('in.txt', 'r') as file:
    for line in file:
        line = line.strip()
        robots.append(list(map(int, line.split())))


def final_pos(pos1,pos2, vel1, vel2, s):
    return ((pos2 + vel2*s) % h, (pos1 + vel1*s) % w)

ori = deepcopy(matrix)
for k in range(0,15500):
    matrix = deepcopy(ori)
    for robot in robots:
        pos = final_pos(robot[0], robot[1], robot[2], robot[3], k)
        matrix[pos[0]][pos[1]] += 1

    
    q1=0
    q2=0
    q3=0
    q4=0
    for i in range(h//2):
        q1 += sum(matrix[i][:w//2])

    for i in range(h//2):
        q3 += sum(matrix[i][w//2 + 1:])

    for i in range(h//2 + 1,h):
        q2 += sum(matrix[i][:w//2])

    for i in range(h//2 + 1,h):
        q4 += sum(matrix[i][w//2 + 1: ]) 

    if q1*q2*q3*q4 > 232589280:
        pass

    b = 200
    if q1 > b or q2 >  b or q3 >  b or q4> b:
        with open('trees/tree'+str(k)+'.txt', 'w') as file:
            for row in matrix:
                file.write(' '.join(list(map(lambda x: '.' if x == 0 else '0',row))) + '\n')

