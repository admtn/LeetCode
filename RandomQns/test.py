from collections import deque,defaultdict
import heapq
# sum 1 to N inclusive, but excluse divisble by 5 and 7
def sumton(n):
    # find all numbers divisble by 5
    # find all numbers divisble by 7
    res = 0
    for i in range(1,n+1):
        if i%7 == 0 or i%5 == 0:
            continue
        res += i
    print(res)
    return res

def find(n):

    def excludeSum(k):
        numK = n//k
        sumK = (k + numK*k) * (numK/2)
        return sumK

    res = (1+n)* n/2 - excludeSum(5) - excludeSum(7) + excludeSum(35)
    print(res)

def findPairs(arr,k):
    l,r = 0,len(arr)-1
    res = []
    while l < r:
        sum = arr[l] + arr[r]
        if sum > k:
            r -= 1
        elif sum < k:
            l += 1
        else:
            res.append((arr[l],arr[r]))
            r -= 1

    print(res)
line = "2,7,5,11,13,15,16,17,20,26,29;28"
for line in sys.stdin:
    n = int(line)
    def excludeSum(k):
        numK = n//k
        sumK = (k + numK*k) * (numK/2)
        return sumK
    res = (1+n)* n/2 - excludeSum(5) - excludeSum(7) + excludeSum(35)
    print(res)

for line in sys.stdin:
    numbers, X = line.strip().split(';')
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
    


# z  = "2,4,11,224,15"
# print(z.split(','))
# findPairs([1,2,3,4,7,9,12,16,21],10)