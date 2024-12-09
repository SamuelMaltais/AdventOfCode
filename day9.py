mem = []
tot = ''
s=0
id=0

def place_block(left, right, num, mem):
    size_block = 0
    while mem[right] == num and right >= 0:
        size_block += 1
        right -= 1
        
    while left <= right and right >= 0 and left < len(mem):
        size_mem = 0
        while mem[left] == -1 and left < len(mem):
            size_mem += 1
            left += 1
        
        if size_mem >= size_block:
            right += 1
            left -= size_mem

            for i in range(size_block):
                mem[left + i] = num
                mem[right + i] = -1

            break

        left += 1

    return size_block + 1
    


with open('in.txt', 'r') as file: 
    for line in file:
        tot += line.strip()
        
for i in range(len(tot)):
    if i % 2 == 0:
        for _ in range(int(tot[i])):
            mem.append(id)
        id += 1
    else:
        for _ in range(int(tot[i])):
            mem.append(-1)
    

r = len(mem) - 1
l = 0

while r > l and l < len(mem) and r >= 0:
    if mem[r] == -1:
        r -= 1
        continue

    l = 0
    r -= place_block(l, r, mem[r], mem) - 1
    

for i in range(len(mem)):
    if mem[i] != -1:
        s += int(mem[i]) * i

print(s)