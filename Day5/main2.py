def split(line):
    l = line.replace("\n","").split(" ")
    return [l[0].split(","), l[2].split(",")]

def convert(line):
    return [[int(line[0][0]), int(line[0][1])],[int(line[1][0]), int(line[1][1])]]

with open ('./Day5/data.txt') as data:
    lines = data.readlines()
    arrs = list(map(split, lines))
    arrs = list(map(convert, arrs))

map = [[0 for i in range(1000)] for i in range(1000)]

for arr in arrs:
    dY = abs(arr[0][1] - arr[1][1]) 
    dX = abs(arr[0][0] - arr[1][0])

    if arr[0][1] == arr[1][1]:
        if (arr[0][0] < arr[1][0]):
            for i in range(arr[0][0], arr[1][0]+1):
                map[arr[1][1]][i] += 1
        else:
            for i in range(arr[1][0], arr[0][0]+1):
                map[arr[1][1]][i] += 1
    elif arr[0][0] == arr[1][0]:
        if (arr[0][1]) < int(arr[1][1]): 
            for i in range(arr[0][1], arr[1][1]+1):
                map[i][arr[1][0]] += 1
        else:
            for i in range(arr[1][1], arr[0][1]+1):
                map[i][arr[1][0]] += 1
    elif dY == dX:
        if (arr[0][0] < arr[1][0] and arr[0][1] < arr[1][1]):
            for i in range(0,dY+1):
                map[arr[0][1] + i][arr[0][0] + i] += 1
        elif (arr[0][0] > arr[1][0] and arr[0][1] > arr[1][1]):
            for i in range(0,dY+1):
                map[arr[0][1] - i][arr[0][0] - i] += 1
        elif (arr[0][0] > arr[1][0] and arr[0][1] < arr[1][1]):
            for i in range(0,dY + 1):
                map[arr[0][1] + i][arr[0][0] - i] += 1
        elif (arr[0][0] < arr[1][0] and arr[0][1] > arr[1][1]):
            for i in range(0,dY + 1):
                map[arr[0][1] - i][arr[0][0] + i] += 1
        
count = 0
for i in range(1000):
    for j in range(1000):
        if (int(map[i][j]) > 1): count+=1

print(count)
