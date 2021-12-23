with open ('./Day4/data.txt') as data:
    lines = data.readlines()
    instructions = lines[0].split(",")

boards = []
board = []



for i in range(2, len(lines)):
    if (lines[i] == '\n'):
        boards.append(board.copy())
        board = []
    else: board.append(lines[i].replace("  "," ").replace("\n","").lstrip().split(" "))
boards.append(board)

map = []

for board in boards:
    map.append([[0 for x in range(5)] for x in range(5)])

for num in instructions:
    b = 0
    while b < len(boards):
        removed = False
        for i in range(0,5):
            if removed: break
            for j in range(0,5):
                if removed: break
                if boards[b][i][j] == num:
                    map[b][i][j] = 1

                    count1 = 0
                    count = 0
                    for c in range(0,5):
                        count += int(map[b][i][c])
                        if (count == 5): 
                            for i1 in range(0,5):
                                for j1 in range(0,5):
                                    if map[b][i1][j1] == 0: count1 += int(boards[b][i1][j1])
                            if len(boards) == 1: 
                                print(int(num)*count1)
                            else: 
                                boards.remove(boards[b])
                                map.remove(map[b])
                                removed = True
                    if not removed: 
                        count1 = 0
                        count = 0
                        for c in range(0,5):
                            count += int(map[b][c][j])
                            if (count == 5): 
                                for i1 in range(0,5):
                                    for j1 in range(0,5):
                                        if map[b][i1][j1] == 0: count1 += int(boards[b][i1][j1])
                                if len(boards) == 1: 
                                    print(int(num)*count1)
                                else: 
                                    boards.remove(boards[b])
                                    map.remove(map[b])
                                    removed = True


        if not removed: b+=1
                    
