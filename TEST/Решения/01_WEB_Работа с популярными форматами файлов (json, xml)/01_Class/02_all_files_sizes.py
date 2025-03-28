import os


def human_read_format(size):
    values = ['Б', 'КБ', 'МБ', 'ГБ']
    num = 0
    while size >= 1024:
        size /= 1024
        num += 1
    return f"{round(size)}{values[num]}"


def get_files_sizes():
    files = [f'{c} {human_read_format(os.path.getsize(c))}'
             for c in os.listdir('.') if os.path.isfile(c)]
    return '\n'.join(files)