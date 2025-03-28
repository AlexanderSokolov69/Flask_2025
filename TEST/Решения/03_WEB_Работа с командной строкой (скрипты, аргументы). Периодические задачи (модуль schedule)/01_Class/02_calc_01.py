import sys

try:
    args = sys.argv[1:]
    a, b = int(args[0]), int(args[1])
    print(a + b)
except Exception:
    print(0)
