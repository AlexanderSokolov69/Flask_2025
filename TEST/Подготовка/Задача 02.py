import json
import requests
import csv


with open('property.json', encoding='utf-8') as f:
    prop = json.load(f)

data = requests.get(f"http://{prop['host']}:{prop['port']}")
spisok = json.loads(data.content)

result = [['no', 'sum', 'div', 'product', 'len']]
for i, numbers in enumerate(spisok):
    numbers = [num for num in numbers if num % 7 == prop['mod7'] and len(str(num)) <= prop['length']]
    if numbers:
        _no = i + 1
        _sum = sum(numbers)
        _div = sum([n // 7 for n in numbers]) // 7
        if len(numbers) == 1:
            _product = numbers[0] ** 2
        else:
            _product = min(numbers) * max(numbers)
        _len = len(''.join([str(n) for n in numbers]))
        result.append([_no, _sum, _div, _product, _len])

with open('chalk.csv', 'w', newline='', encoding='utf-8') as f:
    csv_file = csv.writer(f)
    csv_file.writerows(result)
