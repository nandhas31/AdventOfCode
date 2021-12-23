with open ('./data.txt') as data:
    lines = data.readlines()

l = []
for i in range(0, len(lines[0])-1):
    count = 0
    for j in range(0,len(lines)):
        count +=  int(lines[j][i])
    if (count >= len(lines)/2):
        l.append(len(lines[0]) - i-2)
print(l)
count = 0
for i in l:
    count += 2**i

count2 = 2**(len(lines[0])-1) - count

print(count*(count2-1))
