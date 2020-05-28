num_list = []
while True:
    try:
        num = float(input('Введите число: '))
        num_list.append(str(num))
    except ValueError:
        print('Ввод чисел прерван!')
        break
with open('text_5_5.txt', 'w', encoding='utf-8') as file_write:
    print(f'{" ".join(num_list)}', file=file_write)

with open('text_5_5.txt', 'r', encoding='utf-8') as file_read:
    num_list = file_read.readline().split()
    num_sum = 0
    for num in num_list:
        num_sum += float(num)
print(f'Сумма чисел: {num_sum}')
