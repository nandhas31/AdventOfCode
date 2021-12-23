with open ('./Day3/data.txt') as data:
    lines = data.readlines()

for i in range(0,len(lines[0])-1):
    count = 0
    for j in range(0,len(lines)):
        count +=  int(lines[j][i])
    if (count >= len(lines)/2):
        k=0
        while k < len(lines):
            if int(lines[k][i]) == 0:
                lines.remove(lines[k])
            else: k+=1
    else:
        k=0
        while k < len(lines):
            if int(lines[k][i]) == 1:
                lines.remove(lines[k])
            else: k+=1
print(lines)

with open ('./Day3/data.txt') as data:
    lines = data.readlines()

for i in range(0,len(lines[0])-1):
    if len(lines) == 1: break
    count = 0
    for j in range(0,len(lines)):
        count +=  int(lines[j][i])
    if (count < len(lines)/2):
        k=0
        while k < len(lines):
            if int(lines[k][i]) == 0:
                lines.remove(lines[k])
            else: k+=1
    else:
        k=0
        while k < len(lines):
            if int(lines[k][i]) == 1:
                lines.remove(lines[k])
            else: k+=1
print(lines)
