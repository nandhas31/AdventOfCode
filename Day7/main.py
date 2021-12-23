import statistics

with open ('./Day7/data.txt') as data:
    crab_pos_list = data.readline().replace("\n","").split(",")
    crab_pos_list = list(map(lambda l: int(l), crab_pos_list))

median = statistics.median(crab_pos_list)

count = 0
for i in crab_pos_list:
    count += int(abs(i-median))

print(count)