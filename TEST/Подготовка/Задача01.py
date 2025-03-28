import json
import sys


result = dict()
glas = 'aeyuio'
data = map(str.split, sys.stdin.readlines())

# print(list(data))
for i, spisok in enumerate(data):
    for word in spisok:
        if len(word) % 2 == len([letter for letter in word if letter.lower() in glas]) % 2:
            result.setdefault(i + 1, []).append(word)

with open('broom.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
