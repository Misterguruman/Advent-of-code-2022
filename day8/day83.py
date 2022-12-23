
INPUT_FILE = 'day8.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        trees = tuple([tuple(map(int, list(row.strip())))
                       for row in file.read().strip().split()])

    visibles = 0

    for i, row in enumerate(trees):
        for j, col in enumerate(row):
            element = trees[i][j]

            top = tuple([element > row[j] for row in trees[:i]])
            left = tuple([element > col for col in trees[i][:j]])
            right = tuple([element > col for col in trees[i][j + 1:]])
            bottom = tuple([element > row[j] for row in trees[i + 1:]])

            if any([all(top), all(left), all(right), all(bottom)]):
                visibles += 1

    print(visibles)


if __name__ == '__main__':
    main()