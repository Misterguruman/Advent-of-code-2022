import math
monkey_container = {}

class Monkey:
    def __init__(self, init_data):
        name, starting_items, operation, test, true_monkey, false_monkey = init_data
        self.name           = name.replace('Monkey ', '').replace(':', '')
        starting_items      = starting_items.replace('  Starting items: ', '').split(', ')
        self.starting_items = [int(worry_level) for worry_level in starting_items]
        self.operation      = operation.replace('  Operation: new = ', '')
        self.test           = int(test.replace('  Test: divisible by ', ''))
        self.true_monkey    = true_monkey.replace('    If true: throw to monkey ', '')
        self.false_monkey   = false_monkey.replace('    If false: throw to monkey ', '')
        self.inspection_count = 0

    def update(self):
        if self.starting_items:
            global monkey_container
            _starting_items = self.starting_items.copy()
            for index, item in enumerate(_starting_items):
                self.inspection_count += 1
                # item = math.floor(self.apply_operation(item) / 3)
                item = self.apply_operation(item)
                if item % self.test == 0:
                    monkey_container[self.true_monkey].starting_items.append(item)
                else:
                    monkey_container[self.false_monkey].starting_items.append(item)

            self.starting_items = []

    def apply_operation(self, old):
        return eval(self.operation)

data = open('day11.txt', 'r').read().split('\n\n')

for monkey in [x.split('\n') for x in data]:
    mon = Monkey(monkey)
    monkey_container[mon.name] = mon

for i in range(10000):
    [monkey.update() for monkey in monkey_container.values()]
    if i % 10 == 0:
        print(f"Finishing level {i}")

inspection_counts = [monkey.inspection_count for monkey in monkey_container.values()]
inspection_counts.sort()

print(inspection_counts[-1] * inspection_counts[-2])


