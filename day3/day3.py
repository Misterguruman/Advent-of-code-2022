import string

data = [x.strip() for x in open('day3.txt', 'r').readlines()]
reference = [""] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

def solve_p1():

    total = 0
    for line in data:
        compartment1, compartment2 = line[:len(line) // 2], line[len(line) // 2:]
        for character in compartment1:
            if character in compartment2:
                total += reference.index(character)
                break

    print(total)

def solve_p2():
    total = 0 
    for index in range(0, len(data), 3):
        elf1, elf2, elf3 = data[index:index+3]
        for character in elf1:
            if character in elf2 and character in elf3:
                total += reference.index(character)
                break

    print(total)

def solution():
    total = 0
    for line in data:
        total += list(string.ascii_letters).index(set.intersection(set(line[:len(line) // 2]), set(line[len(line) // 2:])).pop()) + 1

    print(total)



if __name__ == "__main__":
    solve_p1()
    solve_p2()
    solution()