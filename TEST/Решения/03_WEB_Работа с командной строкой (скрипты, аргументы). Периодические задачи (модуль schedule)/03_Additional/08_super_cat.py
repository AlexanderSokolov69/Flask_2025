import sys

args = sys.argv[1:]

file_name = ''
count_flag = False
num_flag = False
sort_flag = False

while args:
    arg = args.pop(0)
    if arg == '--count':
        count_flag = True
    elif arg == '--num':
        num_flag = True
    elif arg == '--sort':
        sort_flag = True
    else:
        file_name = arg

if len(file_name) == 0:
    print('ERROR')
    exit()

try:
    f = open(file_name, 'rt')
    lines = [x.strip() for x in f.readlines()]
    f.close()
except FileNotFoundError:
    print('ERROR')
    exit()

if sort_flag:
    lines.sort()
for num, l in enumerate(lines):
    prefix = ''
    if num_flag:
        prefix = f'{num} '
    print(prefix, l, sep='')
if count_flag:
    print(f'rows count: {len(lines)}')
