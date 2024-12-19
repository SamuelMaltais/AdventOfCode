m = []
with open ('in_cap.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace(' ', '')
        m.append(line)

availiable = m[0].split(',')

a = {}

def find_pattern_dp(pattern):
    dp = [0 for i in range(len(pattern) + 1)]
    dp[0] = 1
    for i in range(1, len(dp)):
        for pat in availiable:
            if i >= len(pat):
                if pattern[i-len(pat):i] == pat:
                    dp[i] += dp[i-len(pat)]

    return dp[-1]
def find_pattern(pattern, path, original):
    s = 0
    if pattern == '':
        if original in a:
            initial = len(a[original])
            a[original].add(tuple(path))
            return len(a[original]) - initial
        else:
            a[original] = set()
            a[original].add(tuple(path))
            return 1

    for pat in availiable:
        if len(pat) <= len(pattern):
            if pattern[:len(pat)] == pat:
                p = path[:]
                p.append(pat)
                s += find_pattern(pattern[len(pat):], p, original)    
    return s

s=0
i=0
for pat in m[1:]:
    s += find_pattern_dp(pat)
    i += 1
    print(i)

print(s)