T = True
F = False
counterForDebug = 0
negativeOne = -1
length = []
width = []
outputNum = 0

def graphOuter(u, output, edge3, R, L, g):
    global negativeOne
    global counterForDebug
    for v in range(R):
        if g[u][v] == 1:
            if not(edge3[v]):
                edge3[v] = T
                if output[v] == negativeOne:
                    output[v] = u
                    counterForDebug += 1
                    return T
                elif graphOuter(output[v], output, edge3, R, L, g):
                    output[v] = u
                    counterForDebug += 1
                    return T
    return F

def switch(u, v):
    u, v = v, u

def checker(a):
    global length
    global width
    global counterForDebug
    if a[0] == a[2]: 
        if a[3] < a[1]:
            u = a[1]
            a[1] = a[3]
            a[3] = u
            counterForDebug += 1
            length.append(a)
        else: length.append(a)
    elif a[1] == a[3]:
        if a[2] < a[0]:
            u = a[0]
            a[0] = a[2]
            a[2] = u
            counterForDebug += 1
            width.append(a)
        else:
            width.append(a)

n = input()
m = int(n)
for i in range(m):
    a = list(map(int, input().split()))
    checker(a)
graph = [[0 for i in range(len(length))] for j in range(len(width))]
y1 = len(length)
y2 = len(width)
for firstY in range(y1):
    for secondY in range(y2):
        if length[firstY][0] >= width[secondY][0]:
            if length[firstY][0] <= width[secondY][2]:
                if width[secondY][1] >= length[firstY][1]:
                    if width[secondY][1] <= length[firstY][3]:
                        counterForDebug += 1
                        graph[secondY][firstY] = 1

right = len(graph[0])
counterForDebug += 1
output = [-1]*right
lenght2 = len(graph)
for i in range(lenght2):
    edge3 = [F]*right
    counterForDebug += 1
    if graphOuter(i, output, edge3, right, lenght2, graph):
        counterForDebug = counterForDebug + 4
        outputNum += 1
outie = m - outputNum
print(outie)