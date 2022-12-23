from collections import defaultdict

data = [x.strip().split(' ') for x in open('day9.txt', 'r').readlines()]

grid = defaultdict(int)

head_position = (0,0)
tail_position = (0,0)

grid[tail_position] = 1

def check_tail_position():
    relative_grid = [
                    (-1, 1), (0, 1), (1, 1), 
                    (-1, 0), (0, 0), (1, 0), 
                    (-1, -1),(0, -1),(1, -1)
                    ]

    for offset_x, offset_y in relative_grid:
        if tail_position == (head_position[0] + offset_x, head_position[1] + offset_y):
            return True

    else:
        return False

for direction, distance in data:
    distance = int(distance)
    directions_grid = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    for hop in range(1, distance + 1, 1):
        head_position = (head_position[0] + directions_grid[direction][0], head_position[1] + directions_grid[direction][1])

        if check_tail_position():
            continue

        else:
            tail_position = (head_position[0] + (directions_grid[direction][0] * -1), head_position[1] + (directions_grid[direction][1] * -1))
            grid[tail_position] = 1

print(sum(grid.values()))