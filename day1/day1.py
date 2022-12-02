def main():
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

def main_optimized():
    with open('day1.txt', 'r') as f:
        data = f.read().split('\n\n')

    totals = [sum([int(string) for string in elf.split('\n')]) for elf in data]
    print(f"Result 1: {max(totals)}")
    totals.sort()
    print(f"Result 2: {sum(totals[-3:])}")

if __name__ == '__main__':
    main_optimized()