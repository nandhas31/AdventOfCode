with open ('./input.txt') as data:
    lines = data.readlines()

count = 0
for i in range(3, len(lines)):
    if int(lines[i-3]) < int(lines[i]):
        count+=1
print(count)