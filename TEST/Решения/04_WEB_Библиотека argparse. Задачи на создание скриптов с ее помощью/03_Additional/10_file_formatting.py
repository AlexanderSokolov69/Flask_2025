import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'rt', encoding='utf-8') as input_file:
            lines = [line.strip() for line in input_file.readlines()]

        cur_height = 0
        cur_line = 0
        line_pos = 0
        out = []
        while cur_height < frame_height and cur_line < len(lines):
            line = lines[cur_line]
            out.append(line[line_pos:line_pos + frame_width])
            cur_height += 1
            line_pos += frame_width
            if len(line) <= line_pos:
                cur_line += 1
                line_pos = 0
        return "\n".join(out)
    except Exception as E:
        return str(E)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("--frame-height", type=int, default=50, help="block height size")
    p.add_argument("--frame-width", type=int, default=50, help="block width size")
    p.add_argument("file_name", type=str, help="file name")
    args = p.parse_args()

    print(format_text_block(args.frame_height, args.frame_width, args.file_name))
