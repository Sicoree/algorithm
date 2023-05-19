import sys, math
input = sys.stdin.readline

def CCW(p1, p2, p3):
    return (p2[0] * p3[1] + p3[0] * p1[1] + p1[0] * p2[1] - (p2[1] * p3[0] + p3[1] * p1[0] + p1[1] * p2[0]))

def solve(points):
    points = sorted(set(points))
    # points.sort(key = lambda x : x[1])

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

hull = solve(arr)

max_l = 0
s = 0
e = len(hull) - 1
while s < e:

    for i in range(e - s):
        tmp = math.sqrt((hull[e - i][0] - hull[s][0]) ** 2 + (hull[e - i][1] - hull[s][1]) ** 2)

        if max_l < tmp:
            max_l = tmp
    
    s += 1     

print(max_l)