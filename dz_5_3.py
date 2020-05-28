file = open('text_3.txt', 'r', encoding='utf-8')
lines = file.readlines()
count = len(lines)

sum = 0
for row in lines:
    line = row.split()
    if (float(line[1]) < 20000):
        print(f'{line[0]} Имеет оклад менее 20000руб 00коп')
    sum += float(line[1])

sum_sr = sum / count

print(sum)
print(f'Средний зароботок: {sum_sr:.2f} руб')

file.close()
