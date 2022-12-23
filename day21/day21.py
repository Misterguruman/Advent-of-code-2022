data = [x.strip() for x in open('day21.txt', 'r').readlines()]

# number_monkeys_ = [x.split(': ')[0] for x in data if line.split(': ')[1].isnumeric()]
monkeys = {}
waiting = {}
yelled = []

def find_children(name):
    if name == 'humn':
        return 'X' 
    if 'operator' in monkeys[name]:
        rstring =  "(" + find_children(monkeys[name]['monkey1']) + monkeys[name]['operator'] + find_children(monkeys[name]['monkey2']) + ")"
        if 'X' in rstring:
            return rstring
        
        return str(eval(rstring))
    else:
        return str(monkeys[name]['value'])

def solve_p2():
    target1, target2 = find_children(monkeys['root']['monkey1']), find_children(monkeys['root']['monkey2'])
    print("Problem 1 " + target1)

    print("Problem 2 " + target2)
    # if 'X' in target1:
    #     match = eval(target2)
    #     target = target1
    # else:
    #     match = eval(target1)
    #     target = target2
        
    # guess = 0
    # while True:
    #     if match == eval(target.replace('X', str(guess))):
    #         print("SOLUTION: " + str(guess))
    #         break

    #     # else:
    #     #     print("Trying " + target1.replace('X', str(guess)))

    #     guess += 1

def update_monkey_value(name):
    if monkeys[name]['operator'] == '+':
        monkeys[name]['value'] = monkeys[monkeys[name]['monkey1']]['value'] + monkeys[monkeys[name]['monkey2']]['value']
    elif monkeys[name]['operator'] == '-':
        monkeys[name]['value'] = monkeys[monkeys[name]['monkey1']]['value'] - monkeys[monkeys[name]['monkey2']]['value']
    elif monkeys[name]['operator'] == '*':
        monkeys[name]['value'] = monkeys[monkeys[name]['monkey1']]['value'] * monkeys[monkeys[name]['monkey2']]['value']
    elif monkeys[name]['operator'] == '/':
        monkeys[name]['value'] = monkeys[monkeys[name]['monkey1']]['value'] // monkeys[monkeys[name]['monkey2']]['value']

def update_monkeys():
    for key, value in monkeys.items():
        if value['waiting']:
            if value['monkey1'] in yelled and value['monkey2'] in yelled:
                if key == 'root':
                    update_monkey_value(key)
                    solve_p2()
                monkeys[key]['yelled'] = True
                yelled.append(key)
                monkeys[key]['waiting'] = False

                update_monkey_value(key)
                update_monkeys()

for line in data:
    name, operation = line.split(': ')

    if operation.isnumeric():
        yelled.append(name)
        monkeys[name] = {'waiting': False, 'yelled': True, 'value': int(operation)}

    else:
        monkey1, operator, monkey2 = operation.split(' ')
        monkeys[name] = {'waiting': True, 'yelled': False, 'value': 0, 'monkey1': monkey1, 'operator': operator, 'monkey2': monkey2}

    update_monkeys()