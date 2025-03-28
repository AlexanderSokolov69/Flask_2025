import argparse


def count_lines(file_name):
    try:
        with open(file_name, 'rt') as f:
            lines = f.readlines()
    except Exception:
        lines = []
    return len(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="", type=str)
    args = parser.parse_args()

    print(count_lines(args.file))
