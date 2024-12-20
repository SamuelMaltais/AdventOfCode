arr=[]
with open('in_buttons.txt', 'r') as file:
    for line in file:
        line = line.strip()
        arr.append(line)

s=0
for i in range(0, len(arr), 4):
    a = list(map(int, arr[i].split()))
    b = list(map(int, arr[i + 1].split()))
    
    a[0] += 10000000000000
    a[1] += 10000000000000
    b[0] += 10000000000000
    b[1] += 10000000000000

    z = list(map(int, arr[i + 2].split()))
    
    max_a = min(z[0] // a[0], z[1] // a[1],100)
    max_b = min(z[0] // b[0], z[1] //b[1],100)

    curr = 3*max_a * max_b

    for i in range(max_a + 1):
        for j in range(max_b + 1):
            if i*a[0] + j*b[0] == z[0] and i*a[1] + j*b[1] == z[1]:
                curr = min(curr, 3*i + j)

    if curr != 3*max_a * max_b:
        s += curr
print(s)
