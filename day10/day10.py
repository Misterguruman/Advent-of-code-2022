data = [x.strip() for x in open('day10.txt', 'r').readlines()]

clock = 1
register = 1
current_line = ""

def write_pixel():
    global clock
    global register
    global current_line
    if clock in [register - 1, register, register + 1]:
        current_line += "#"

    else:
        current_line += "."

    if len(current_line) == 40:
        print(current_line)
        current_line = ""

def tick():
    global clock
    global current_line
    if clock == 40:
        clock = 0

    clock += 1 

for instruction in data:
    if instruction == 'noop':
        tick()
        write_pixel()

    else:
        _, value = instruction.split(' ')
        write_pixel()
        write_pixel()
        tick()
        tick()
        register += int(value)


