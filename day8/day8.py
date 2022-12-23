import numpy as np
import itertools

data = open('day8.txt', 'r').readlines()
data = [list(d.strip()) for d in data]

forest = np.array(data, dtype=int)
rows, cols = forest.shape

visible = 0
for r,c in itertools.product(range(rows),range(rows)):
    tree = forest[r,c]
    if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
        visible += 1
        continue

    if np.all(forest[r, :c] < tree):
        visible += 1
        continue

    if np.all(forest[r, c + 1:] < tree):
        visible += 1
        continue

    if np.all(forest[:r, c] < tree):
        visible += 1
        continue

    if np.all(forest[r + 1: , c] < tree):
        visible += 1
        continue
    
print(f'part 1: {visible}')

# part 2

forest = np.array(data, dtype=int)
scores = []
for r,c in itertools.product(range(rows),range(rows)):
    tree = forest[r,c]
    if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
        scores.append(0)
        continue

    leftView = 0
    for col in range(c-1, -1, -1):
        leftView += 1
        if forest[r,col] >= tree:
            break

    rightView = 0
    for col in range(c + 1, cols):
        rightView += 1
        if forest[r,col] >= tree:
            break

    upperView = 0
    for row in range(r-1, -1, -1):
        upperView += 1
        if forest[row, c] >= tree:
            break

    lowerView = 0
    for row in range(r + 1, rows):
        lowerView += 1
        if forest[row, c] >= tree:
            break

    view = leftView * rightView * upperView * lowerView
    scores.append(view)

print(f'part 2: {max(scores)}')
