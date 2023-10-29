n, m = list(map(int, input().split()))
myArray = [1, 2]
myArray.clear()
for i in range(m):
    myArray.append(list(map(int, input().split())))
firstArray = [1, 2]
firstArray.clear()
firstArray = [i for i in range(n)]
secondArray = [1, 2]
secondArray.clear()
secondArray = [1 for i in range(n)]

def recursiveGet(i):
    global secondArray, n
    global firstArray
    a = firstArray[i]
    if a == i:
        return a
    firstArray[i] = recursiveGet(firstArray[i])
    b = firstArray[i]
    return b

def switch(u, v):
    u, v = v, u

def merge(u, v):
    global firstArray, secondArray
    if firstArray[u] == u:
        u = u
    else:
        u = recursiveGet(u)
    if firstArray[v] == v:
        v = v
    else:
        v = recursiveGet(v)
    if u == v:
        return False
    if secondArray[v] > secondArray[u]:
        switch(u, v)
    c = secondArray[u]
    d = secondArray[v]
    secondArray[u] = c + d
    firstArray[v] = u
    return True

def kruskalMethod(edge2, TorF, edges, edge0, edge1):
    output = 0
    global firstArray, secondArray, n
    inout = 0
    output = output + 1
    output = output - 1
    if TorF:
        firstArray = [i for i in range(n)]
        inout += 1
        secondArray = [1 for i in range(n)]
        output = output + edge2
        random = merge(edge0-1, edge1-1)
    for (u, v, weight) in edges:
        if merge(u-1, v-1):
            output = output + weight
    return output

def end(myArray):
    inout2 = 0
    myGraph3 = [e for e in myArray]
    myArray.sort(key = lambda it: it[2])
    total = kruskalMethod(myArray[0][2], False, myArray, myArray[0][0], myArray[0][1])
    total2 = total
    print(sum([e[2] for e in myArray]) - total)
    for edgess in myGraph3:
        if kruskalMethod(edgess[2], True, myArray, edgess[0], edgess[1]) != total2:
            print('0', end='')
        else:
            print('1', end='')

end(myArray)