data = [x.strip() for x in open('day41.txt', 'r').readlines()]

total = 0 

# for line in data:
#     elf1, elf2 = line.split(',')
#     elf1_start, elf1_end = elf1.split('-')
#     elf2_start, elf2_end = elf2.split('-')

#     if (int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(elf2_end)) or (int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(elf1_end)):

#         total += 1

for line in data:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')   
    if set.intersection(set(range(int(elf1_start), int(elf1_end) + 1, 1)), set(range(int(elf2_start), int(elf2_end) + 1, 1))):
        total += 1
        print(elf1, elf2)
    # else:
    #     print(elf1, elf2)


print(total)