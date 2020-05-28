dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('text_4.txt', 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open('text_4_t.txt', 'w', encoding='utf-8') as file_write:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_write)
