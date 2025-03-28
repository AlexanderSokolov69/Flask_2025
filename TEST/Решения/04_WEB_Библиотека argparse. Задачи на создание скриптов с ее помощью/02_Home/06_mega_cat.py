import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')

try:
    args = parser.parse_args()
    file_name = args.file_name
    count_flag = args.count
    num_flag = args.num
    sort_flag = args.sort
    if len(file_name) == 0:
        raise Exception('')

    with open(file_name, 'rt') as input_data:
        lines = [x.strip() for x in input_data.readlines()]

    if sort_flag:
        lines.sort()
    for num, l in enumerate(lines):
        prefix = ''
        if num_flag:
            prefix = f'{num} '
        print(f'{prefix}{l}')
    if count_flag:
        print(f'rows count: {len(lines)}')

except Exception as E:
    print('ERROR')
