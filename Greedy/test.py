points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
dist = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        p1 = points[i]
        p2 = points[j]
        d = abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
        dist.append((d,[i,j]))
dist.sort()

print(dist)

