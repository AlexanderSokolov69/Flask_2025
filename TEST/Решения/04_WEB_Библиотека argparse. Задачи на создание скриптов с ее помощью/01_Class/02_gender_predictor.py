import argparse

dict_movie = {"melodrama": 0, "football": 100, "other": 50}
parser = argparse.ArgumentParser()
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--movie", choices=["melodrama", "football", "other"], default='other')
args = parser.parse_args()
if args.cars not in range(101):
    args.cars = 50
if args.barbie not in range(101):
    args.barbie = 50

boy = int((100 - args.barbie + args.cars + dict_movie[args.movie]) / 3)
girl = 100 - boy

print(f"boy: {boy}\ngirl: {girl}")