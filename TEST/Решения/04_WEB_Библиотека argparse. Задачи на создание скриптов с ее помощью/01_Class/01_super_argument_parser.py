import argparse

params = argparse.ArgumentParser()
params.add_argument("a", nargs='*', default=['no args'])
args = params.parse_args()
for a in args.a:
    print(a)
