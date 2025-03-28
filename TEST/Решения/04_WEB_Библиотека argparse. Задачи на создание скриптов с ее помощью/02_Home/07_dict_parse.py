import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dictionary', nargs='*')
parser.add_argument('--sort', action='store_true')

parsed_args = parser.parse_args()

args = parsed_args.dictionary
out_dict = {}
sort_flag = parsed_args.sort

for pair in args:
    key, value = pair.split('=')
    out_dict[key] = value

if sort_flag:
    for key in sorted(out_dict):
        print(f'Key: {key}\tValue: {out_dict[key]}')
else:
    for key, value in out_dict.items():
        print(f'Key: {key}\tValue: {value}')
