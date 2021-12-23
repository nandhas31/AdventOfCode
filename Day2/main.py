with open ('./data.txt') as data:
    lines = data.readlines()


x = 0
y = 0

for i in range(0, len(lines)):
    l = lines[i].split(' ')
    if (l[0] == "forward"):
        x+=int(l[1])
    elif(l[0] == "down"):
        y+=int(l[1])
    elif(l[0] == "up"):
        y-=int(l[1])

print(x*y)