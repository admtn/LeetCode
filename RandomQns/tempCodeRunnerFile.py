numbers, X = line.split(';')
nums = list(map(int, numbers.split(',')))
X = int(X)

res = []
l,r = 0, len(nums)-1
while l < r:
    leftNum = nums[l]
    rightNum = nums[r]
    total = leftNum + rightNum
    if total > X:
        r -= 1
    elif total < X:
        l += 1
    else:
        res.append((leftNum,rightNum))
        l += 1

if res:
    print(";".join([f"{a},{b}" for a, b in res]))
else:
    print("NULL")