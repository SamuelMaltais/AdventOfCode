s=0
f = []
with open('in_test.txt', 'r') as file:

    for line in file:
        line = line.strip()
        f.append(line)


A = int(f[0].split(':')[1])
B = int(f[1].split(':')[1])
C = int(f[2].split(':')[1])

program = list(map(int, f[3].split(',')))

def get_val(operand, A, B, C):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        return operand

i=0

def simulate_program(A,B,C, i, index,seen):
    if (A,B,C,i) in seen:
        return False

    if index >= len(program):
        return True
    if i >= len(program):
        return False

    op = program[i]
    operand = program[i+1]
    v = get_val(operand, A, B, C)
    
    #seen.add((A,B,C,i))

    if(op == 0):
        A = A // (2**v)
    elif(op == 1):
        B=B^operand
    elif(op == 2):
        B = v % 8
    elif(op == 3):
        if A != 0:
            i = operand
            return simulate_program(A, B, C, i, index, seen)
    elif(op == 4):
        B=B ^ C
    elif(op == 5):
        if program[index] != v % 8:
            return False
        index += 1
    elif(op == 6):
        B=A // (2**v)
    else:
        C=A // (2**v)

    i += 2
    return simulate_program(A, B, C, i, index, seen)



#16325867064000
#130606920348432
program.reverse()
#A=130606920348432
A = int(''.join(list(map(str,program))) + '0', 8)
program.reverse()

while True:
    if simulate_program(A, B, C, 0, 0, set()):
        print(A)
        break

    A +=  1
    #print(A)

#print(','.join(list(map(str, res))))