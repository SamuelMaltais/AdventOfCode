import sys
s=0



def test_equation(val, nums, curr, i):
    if i >= len(nums):
        if val == int(curr):
            return True
        else:
            return False
    
    b1 = test_equation(val, nums, curr*int(nums[i]), i+1)
    b2 = test_equation(val, nums, curr+int(nums[i]), i+1)
    b3 = test_equation(val, nums, int(str(curr)+nums[i]),i+1)
    

    return b1 or b2 or b3

with open('in.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split()

        if test_equation(int(line[0]), line[2:], int(line[1]), 0):
            s += int(line[0])

print(s)