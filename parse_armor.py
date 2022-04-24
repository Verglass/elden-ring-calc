items = []

with open('raw/greaves_raw.txt', 'r') as f:
    for line in f:
        line = line.split(' ')
        flag = False
        result = 0
        name = ''
        for part in line:
            if part[0].isalpha() or part[0] == '(':
                name += part + ' '

        for idx, char in enumerate(name):
            if char.isupper():
                if flag:
                    result = idx
                    flag = False
                else:
                    flag = True

            elif char == ' ' or char == '-':
                flag = False

        name = name[result:]
        items.append((name, line[-1].strip()))

with open('data/greaves.txt', 'w') as f:
    for item in items:
        f.write(f'{item[0]} {item[1]}\n')
