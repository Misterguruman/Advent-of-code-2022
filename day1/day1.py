if __name__ == '__main__':
    data = [x.strip() for x in open('day1.txt', 'r').readlines()]

    totals = []
    current_elf = 0

    for line in data:
        if line == '':
            totals.append(current_elf)
            current_elf = 0 
            continue

        current_elf += int(line)

    # print(max(totals))
    totals.sort()
    print(sum(totals[-3:]))
