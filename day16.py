s=0
m=[]

e = (0,0)
s = (0,0)

rot = {
    (0,1): (-1, 0),
    (-1, 0): ()
}
rot2 = {}
for k in rot:
    rot2[rot[k]] = k


def smart(score, i,j,m, mem, di, dj):
    if not (0 <= i < len(m) or 0 <= j < len(m[0])):
        return
    
    if (i,j) in mem:
        if score < mem[(i,j)]:
            mem[(i,j)] = score
        else:
            return
        
    if m[i][j] == '#':
        return
        
    if (i,j) == e:
        mem[e] = min(dict.get(mem, e, 0), score)

    smart(score + 1, i+di,j+dj,m, mem, di,dj)
    a = rot((di,dj))
    b = rot2((di,dj))
    smart(score + 1001, i + a[0], j + a[1], m, mem, a[0], a[1])
    

    # Rotate right



with open('in.txt', 'r') as file:
    for line in file:
        line = line.strip()
        m.append(line)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 'S':
            s = (i,j)
        if m[i][j] == 'E':
            e = (i,j)






