
file = open("Dz_5_1.txt", 'a', encoding='utf-8')

while True:
    string = input("Print text: ")
    if not string:
        file.close()
        print("Close")
        break
    file.write(f'{string}\n')
