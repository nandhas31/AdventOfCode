with open ('./Day6/data.txt') as data:
    fish_list = data.readline().split(",")

days = 256
fish_map = {}

for fish in fish_list:
    fish_map[int(fish)] = fish_map.get(int(fish), 0) + 1

for i in range(0,days):
    num = fish_map.get(0, 0)
    for j in range(1,9):
        fish_map[j-1] = fish_map.get(j, 0)
    fish_map[6] = fish_map.get(6, 0) + num
    fish_map[8] = num

count = 0
for i in range(0,9):
    count += fish_map.get(i, 0)

print(count)