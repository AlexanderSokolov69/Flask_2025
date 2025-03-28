import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', nargs='*')

    args = list(map(int, parser.parse_args().integers))
    count = len(args)

    if count == 2:
        print(sum(args))
    elif count < 2:
        print('TOO FEW PARAMS')
    else:
        print('TOO MUCH PARAMS')

except Exception as E:
    print(E.__class__.__name__)
