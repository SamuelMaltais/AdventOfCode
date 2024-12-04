s=0
with open('in.txt', 'r') as file:
    do=True
    d='do()'
    dt="don't()"
    for line in file:
        line = line.strip()
        ok = 'mul('
        end = ')'
        n1=''
        n2=''
        i=0
        seq=0

        for si in range(len(line)):
            char = line[si]
            if si + len(d) < len(line):
                if line[si:si+len(d)] == 'do()':
                    do = True
            if si + len(dt) < len(line):
                if line[si:si+len(dt)] == "don't()":
                    do = False
            if seq == 0:
                if char == ok[i]:
                    i+=1
                else:
                    i=0
                    n1=''
                    n2=''
                if i == 4:
                    seq += 1
            elif seq == 1:
                j=0
                if char == ',' and n1 != '':
                    seq += 1
                elif char in ['0','1','2','3','4','5','6','7','8','9']:
                    n1 += char
                else:
                    seq = 0
                    i = 0
                    n1=''
                    n2=''
            else:
                j=0
                if char == ')' and n2 != '':
                    if do:
                        s += (int(n1)*int(n2))
                    n1=''
                    n2=''
                    seq = 0
                    i =0

                elif char in ['0','1','2','3','4','5','6','7','8','9']:
                    n2 += char
                else:
                    seq = 0
                    i = 0
                    n1=''
                    n2=''

print(s)