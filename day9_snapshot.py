mem = []
tot = ''
s=0
id=0
blocks = []

def place_block(right, num, mem):
    size_block = 0

    while mem[right] == num and right >= 0:
        size_block += 1
        right -= 1
        
    for i in range(len(blocks)):
        block = blocks[i]
        size = block[1] - block[0]
        indx = block[0]
        if block[0] > right:
            return size_block
        if size >= size_block:
            for i in range(size_block):
                mem[indx + i] = num
                mem[right + i] = -1
            if num == 8:
                print(block)
            blocks[i] = (block[0] + size_block, block[1])
            return size_block

    


with open('in2.txt', 'r') as file: 
    for line in file:
        tot += line.strip()

curr_index = 0  
for i in range(len(tot)):
    if i % 2 == 0:
        for _ in range(int(tot[i])):
            mem.append(id)
            curr_index += 1
        id += 1
    else:
        blocks.append((curr_index, curr_index + int(tot[i])))
        for _ in range(int(tot[i])):
            mem.append(-1)
            curr_index += 1

    

r = len(mem) - 1
l = 0

while r > l and l < len(mem) and r >= 0:
    if mem[r] == -1:
        r -= 1
        continue
    r -= place_block(r, mem[r], mem)
    print(mem)
    

for i in range(len(mem)):
    if mem[i] != -1:
        s += int(mem[i]) * i

print(s)