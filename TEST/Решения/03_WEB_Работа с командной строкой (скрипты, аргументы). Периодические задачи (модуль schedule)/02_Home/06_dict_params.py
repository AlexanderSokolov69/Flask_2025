import sys

args = sys.argv[1:]
out_dict = {}
key_order = []
sort_flag = False

while args:
    arg = args.pop(0)
    if arg == '--sort':
        sort_flag = True
        continue
    k, v = arg.split('=')
    out_dict[k] = v
    key_order.append(k)

if sort_flag:
    key_order.sort()

for k in key_order:
    print(f'Key: {k}\tValue: {out_dict[k]}')
