from collections import defaultdict

data = [x.strip().split(' ') for x in open('day9.txt', 'r').readlines()]

grid = defaultdict(int)

head_position = (0,0)
k1_position = (0,0)

knots = [
    (0,0), # Knot 1 (follows old rules)
    (0,0), # Remainder follow based on the direction of the last
    (0,0),
    (0,0),
    (0,0),
    (0,0),
    (0,0),
    (0,0),
    (0,0),
    (0,0)  # Tail, we update the grid with this tail
    ]

directions_grid = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def find_leader_direction(leader, follower):
    U_match = [(-1, 2), (0, 2), (1,  2)] #Move it one Y Down relative to the leader (Goes Below)
    D_match = [(1, -2), (0,-2), (-1, -2)] #Move it to one Y above the Leader (Goes Above)
    L_match = [(-2, 1), (-2,0), (-2,-1)] # Move it one X above the Leader (Goes to it's right)
    R_match = [(2,  1), (2, 0), (2, -1)]  # Move it one X below the leader ( Goes to the left )

    relative_location = (leader[0] - follower[0], leader[1] - follower[1])

    if relative_location in U_match:
        return "U"

    elif relative_location in D_match:
        return "D"
    
    elif relative_location in L_match:
        return "L"

    elif relative_location in R_match:
        return "R"

    else:
        return 'F'

def update_knots(head_direction):
    for index in range(len(knots)):
        if index == 0:
            if check_connection(knots[index], head_position):
                break

            direction = head_direction

        else:
            if check_connection(knots[index], knots[index - 1]):
                break
    
            direction = find_leader_direction(knots[index-1], knots[index])
        
        knots[index] = (knots[index - 1][0] + (directions_grid[direction][0] * -1), knots[index - 1][1] + (directions_grid[direction][1] * -1))

def check_connection(leader, follower):
    relative_grid = [
                    (-1, 1), (0, 1), (1, 1), 
                    (-1, 0), (0, 0), (1, 0), 
                    (-1, -1),(0, -1),(1, -1)
                    ]

    for offset_x, offset_y in relative_grid:
        if follower == (leader[0] + offset_x, leader[1] + offset_y):
            return True

    else:
        return False

for direction, distance in data:
    distance = int(distance)

    for _ in range(distance):
        head_position = (head_position[0] + directions_grid[direction][0], head_position[1] + directions_grid[direction][1])

        if check_connection(head_position, k1_position):
            continue

        else:
            k1_position = (head_position[0] + (directions_grid[direction][0] * -1), head_position[1] + (directions_grid[direction][1] * -1))
            grid[knots[-1]] = 1

        update_knots(direction)

print(sum(grid.values()))

"""
.BBB.  B for goes below
R...L  L for goes to it's Left
R.1.L  R for goes to it's Right
R...L  A for goes Above it
.AAA.
"""