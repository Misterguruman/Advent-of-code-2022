data = [x.strip() for x in open('day7.txt', 'r').readlines()]

directory_information = {}

current_directory = []

def folder_size(root):
    indirect = 0

    if not directory_information[root]['directories']:
        return directory_information[root]['total']

    for directory in directory_information[root]['directories']:
        if directory_information[directory].get('indirect'):
            indirect += directory_information[directory]['indirect']
            break
        indirect_size = folder_size(directory)
        indirect += indirect_size
        directory_information[directory]['indirect'] = indirect_size


    return directory_information[root]['total'] + indirect

def command(string:str):
    if string.startswith('ls'):
        return
    # if not ls, is cd
    _, parameter = string.split(' ')

    if parameter == '..':
        current_directory.pop()
        return 

    if parameter == '/':
        current_directory = ['/']
        return

    current_directory.append(parameter)

    if directory_information.get(parameter):
        return

    directory_information[parameter] = {'total': 0, 'directories': []}
    return

def file(string):
    file_size, file_name = string.split(' ')

    if directory_information[current_directory[-1]].get(file_name):
        return

    directory_information[current_directory[-1]][file_name] = int(file_size)
    directory_information[current_directory[-1]]['total'] += int(file_size)
    return

def directory(string):
    _, dir_name = string.split(' ')
    if dir_name in directory_information[current_directory[-1]]['directories']:
        return

    directory_information[current_directory[-1]]['directories'].append(dir_name)
    return

for line in data:
    if line[0] == '$':
        command(line.replace('$ ', ''))
        continue

    #if is a chad, mad-lad, or alpha individual
    if line[0].isnumeric():
        file(line)
        continue

    if line.startswith('dir'):
        directory(line)
        continue

solution_total = 0
for key, value in directory_information.items():
    if value['total'] > 100_000:
        continue

    if folder_size(key) <= 100_000:
        solution_total += value['total']

print(solution_total)


