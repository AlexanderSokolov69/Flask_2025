import sys

integers = []
args = sys.argv[1:]
if args:
    for koeff, elem in enumerate(args):
        try:
            integers.append(int(elem) * (-1) ** koeff)
        except Exception as E:
            print(E.__class__.__name__)
            sys.exit(0)
    print(sum(integers))
else:
    print('NO PARAMS')
