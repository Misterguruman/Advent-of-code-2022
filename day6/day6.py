data = [x.strip() for x in open('day6.txt').readlines()][0]

for chunk in range(len(data) - 13):
    print(set(data[chunk:chunk+14]))
    if len(set(data[chunk:chunk+14])) == 14:
        print(chunk+14)
        break