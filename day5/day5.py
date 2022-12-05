data = [x.strip() for x in open('day5.txt').readlines()]

'''
    [W]         [J]     [J]        
    [V]     [F] [F] [S] [S]        
    [S] [M] [R] [W] [M] [C]        
    [M] [G] [W] [S] [F] [G]     [C]
[W] [P] [S] [M] [H] [N] [F]     [L]
[R] [H] [T] [D] [L] [D] [D] [B] [W]
[T] [C] [L] [H] [Q] [J] [B] [T] [N]
[G] [G] [C] [J] [P] [P] [Z] [R] [H]
 1   2   3   4   5   6   7   8   9 
'''

stacks = {
    "1" : ['G','T','R','W'],
    "2" : ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
    "3" : ['C', 'L', 'T', 'S', 'G', 'M'],
    "4" : ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
    "5" : ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
    "6" : ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
    "7" : ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
    "8" : ['R', 'T', 'B'],
    "9" : ['H', 'N', 'W', 'L', 'C']
}

# part 1
# for line in data:
#     move, from_stack, to_stack = line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
#     move = int(move)
#     for inc in range(move):
#         stacks[to_stack].append(stacks[from_stack].pop())

# part 2
for line in data:
    move, from_stack, to_stack = line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
    move = int(move)

    stacks[to_stack] += stacks[from_stack][move * -1:]
    del stacks[from_stack][move * -1:]

# output
for key in stacks.keys():
    print(stacks[key][-1])