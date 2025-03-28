import argparse

p = argparse.ArgumentParser()
p.add_argument("--per-day", type=float, default=0)
p.add_argument("--per-week", type=float, default=0)
p.add_argument("--per-month", type=float, default=0)
p.add_argument("--per-year", type=float, default=0)
p.add_argument("--get-by", choices=["day", "month", "year"], default="day")
args = p.parse_args()

profit = args.per_day
profit += args.per_week / 7.0
profit += args.per_month / 30.0
profit += args.per_year / 360.0

if args.get_by == 'day':
    print(int(profit))
elif args.get_by == 'month':
    print(int(profit * 30))
elif args.get_by == 'year':
    print(int(profit * 360))
