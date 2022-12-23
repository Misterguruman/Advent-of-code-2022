from collections import defaultdict
from itertools import accumulate

directory_sizes = defaultdict(int)

for line in open('day7.txt'):
    match line.split():
        case '$', 'cd', '/': 
            current_directory = ['']
        case '$', 'cd', '..': 
            current_directory.pop()
        case '$', 'cd', x: 
            current_directory.append(x)
        case '$', 'ls': 
            pass
        case 'dir', _: 
            pass
        case size, _:
            for item in accumulate(current_directory):
                directory_sizes[item] += int(size)

p1 = sum(size for size in directory_sizes.values() if size <= 100_000)
p2 = min(size for size in directory_sizes.values() if size >= directory_sizes[''] - 40_000_000)

print(p1, p2)