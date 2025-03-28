import argparse


def print_error(message):
    print(f"ERROR: {message}!!")


if __name__ == '__main__':
    print('Welcome to my program')
    parser = argparse.ArgumentParser()
    parser.add_argument("message")
    args = parser.parse_args()
    print_error(args.message)
