names = []
weights = []

with open('raw/greatswords_raw.txt', 'r') as f:
    count = 0
    for line in f:
        line = line.strip()
        if line in ['A', 'B', 'C', 'D', 'E']:
            count = 0
        count += 1
        if count == 3:
            names.append(line)
        if line and line[0].isdigit():
            n = line.split('\t')[0]
            weights.append(n)

with open('data/greatswords.txt', 'w') as f:
    for name, weight in zip(names, weights):
        f.write(f'{name}  {weight}\n')
