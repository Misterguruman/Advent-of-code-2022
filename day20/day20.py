example_string = """1
2
-3
3
-2
0
4"""

example_data = example_string.split('\n')

data = [x.strip() for x in open('day20.txt', 'r').readlines()]
working_copy = [x for x in data]

for item in data:
    if item == 0:
        print("True")