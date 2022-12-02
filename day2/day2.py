# Show row/column options
rows = ['X', 'Y', 'Z']
columns = ['A', 'B', 'C']

# Represent that data in a multidimensional array using rows/columns above
# -1 draw, 1 win, 2 loss
results = [
    [-1, 1, 2],
    [2, -1, 1],
    [1, 2, -1]
]
all_possibilities = {}

def get_score_p1(column, row):
    match results[columns.index(column)][rows.index(row)]:
        case -1:
            win_offset = 3
        case 1:
            win_offset = 6
        case 2:
            win_offset = 0

    return win_offset + rows.index(row) + 1

def get_move(column, row):
    match row:
        case "X": # loss
            return rows[results[columns.index(column)].index(2)]
        case "Y": # draw
            return rows[results[columns.index(column)].index(-1)]
        case "Z": # win
            return rows[results[columns.index(column)].index(1)]

def get_score_p2(line):
    our_move = get_move(line[0], line[-1])
    return all_possibilities[f"{line[0]} {our_move}"]

if __name__ == '__main__':
    total_score_p1 = 0
    total_score_p2 = 0
    for option1 in columns:
        for option2 in rows:
            all_possibilities[f"{option1} {option2}"] = get_score_p1(option1, option2)
        
    for line in [x.strip() for x in open('day2.txt', 'r').readlines()]:
        total_score_p1 += all_possibilities[line]
        total_score_p2 += get_score_p2(line)

    print(f"Part 1 Solution: {total_score_p1}")
    print(f"Part 2 Solution: {total_score_p2}")


