data_rows = [[int(char) for char in x.strip()] for x in open('day8.txt', 'r').readlines()]

total = 0

counted = []
for row in data_rows:

    current_row_highest = -1
    counted_row = []
    for tree in row:
        if tree > current_row_highest:
            current_row_highest = tree
            total += 1
            counted_row.append(1)
        else:
            counted_row.append(0)

    current_row_highest = -1
    for index, tree in enumerate(reversed(row)):
        if tree > current_row_highest:
            current_row_highest = tree
            if counted_row[(index + 1) * -1] == 1:
                continue
            else:
                counted_row[(index + 1) * -1] = 1
                total += 1

    counted.append(counted_row)

for x, row in enumerate(data_cols):
    current_row_highest = -1
    for y, tree in enumerate(row):
        if tree > current_row_highest:
            current_row_highest = tree
            if counted[y][x] == 1:
                continue
            else:
                counted[y][x] = 1
                total += 1

    current_row_highest = -1
    for y, tree in enumerate(reversed(row)):
        if tree > current_row_highest:
            current_row_highest = tree
            if counted[y][(x + 1) * -1] == 1:
               continue
            else:
                counted[y][(x + 1) * -1] = 1
                total += 1

print(total)
