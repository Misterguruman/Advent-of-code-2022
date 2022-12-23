with open('day10.txt') as f:
    data = f.read().splitlines()

# PART 1 & 2
register = 1 
cycle = 1 
i = 0 
signal_strength = 0 
screen = "" 
first = True 
while i < len(data): 
    if (cycle - 20) % 40 == 0: 
        signal_strength += cycle * register

    if register <= cycle % 40 <= register + 2:
        screen += "#"
    else:
        screen += "."

    if data[i][:4] == "addx":
        if not first:
            register += int(data[i][4:])
            i += 1
        first = not first
    else:
        i += 1
    cycle += 1

print(signal_strength)
for pos, pixel in enumerate(screen, 1): 
    if pos % 40 > 0: 
        print(pixel, end="") 
    else: 
        print(pixel)