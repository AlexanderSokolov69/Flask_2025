import sys

print(f"my name is {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"first arg is: '{sys.argv[1]}' and last arg is '{sys.argv[-1]}'")
else:
    print("No arguments")
