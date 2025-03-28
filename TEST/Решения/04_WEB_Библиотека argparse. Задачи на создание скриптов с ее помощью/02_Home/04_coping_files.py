def file_copy():
    import argparse
    from itertools import islice

    parser = argparse.ArgumentParser()
    parser.add_argument("--upper", action="store_true")
    parser.add_argument("--lines", type=int, default=None)
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    with open(args.source, 'rt', encoding="utf8") as input_data:
        data_in = map(lambda x: x.upper() if args.upper else x,
                      islice(input_data, args.lines))
        data_out = "".join(data_in)

        with open(args.destination, 'wt', encoding="utf8") as output_data:
            print(data_out, file=output_data, end='')


if __name__ == "__main__":
    file_copy()
