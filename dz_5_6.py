import re

file_to_read_path = open('text_6.txt', 'r', encoding='utf-8')

def calculate_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    ttl_hours = 0
    for hour in line_of_hours.split():
        ttl_hours += float(hour)
    return ttl_hours

hours_info = {}
for line in file_to_read_path.readlines():
    listed_line = line.split(': ')
    hours_info[listed_line[0]] = calculate_hours(listed_line[1])

print(f'Итого имеем:\n {hours_info}')

file_to_read_path.close()