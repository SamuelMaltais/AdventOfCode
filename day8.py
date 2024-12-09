import heapq
import sys
import math
sys.setrecursionlimit(9999999)

s=0
antennas = {}
antinodes = set()

def in_bounds(pos, matrix):
    if 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]):
        return True
    else: 
        return False

with open('in.txt', 'r') as file:
    matrix = []
    i = 0
    for line in file:
        line = line.strip()
        matrix.append(line)
        for j in range(len(line)):
            c = line[j]
            if c != '.':
                if c in antennas:
                    antennas[c].append((i, j))
                else:
                    antennas[c] = [(i,j)]
        i += 1
    
    for key in antennas:
        for i in range(len(antennas[key])):
            for j in range(i + 1, len(antennas[key])):
                node1 = antennas[key][i]
                node2 = antennas[key][j]

                di = node1[0] - node2[0]
                dj = node1[1] - node2[1]
                
                d = math.gcd(di, dj)
                di = di 
                dj = dj 

                k = -5000
                for _ in range(10000):
                    pos1 = (node1[0] + k*di,node1[1] + k*dj)

                    if in_bounds(pos1, matrix):
                        if pos1 not in antinodes:
                            s += 1
                            antinodes.add(pos1)
                    

                    k += 1
print(len(antinodes))
print(s)