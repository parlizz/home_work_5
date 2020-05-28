
file = open('dz_5_2.txt', 'r', encoding='utf-8')
lines = file.readlines()

print(f'В файле {len(lines)} строк')

i = 1
for string in lines:
    print(f'В строке {i} {len(string.split())} слов(а)')
    i += 1
file.close()