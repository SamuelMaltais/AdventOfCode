s=0


def count(n, depth, max_depth, seen):

    if((n, depth) in seen):
        return seen[(n, depth)]
    
    if depth == max_depth:
        return 1
    elif n == 0:
        seen[(n, depth)] = count(n + 1, depth+1, max_depth, seen)
        return seen[(n, depth)]
    elif len(str(n)) % 2 == 0:
        o = str(n)
        k = len(o) // 2
        seen[(n, depth)] = count(int(o[:k]), depth+1, max_depth, seen) + count(int(o[k:]), depth+1, max_depth, seen)
        return seen[(n, depth)]
    else:
        seen[(n, depth)] = count(n*2024, depth+1, max_depth, seen)
        return seen[(n, depth)]

with open('in.txt', 'r') as file:
    for line in file:
        line = line.strip()
        arr = list(map(int, line.split()))
   
    seen = {}
    for elem in arr:
        s += count(elem, 0, 75, seen)
print(s)