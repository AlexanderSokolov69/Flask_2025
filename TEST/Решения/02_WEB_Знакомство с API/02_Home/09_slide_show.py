import pygame
import requests
import sys
import os

API_KEY_STATIC = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

map_requests = [
    f"https://static-maps.yandex.ru/v1?apikey={API_KEY_STATIC}&ll=2.294458,48.858302&spn=0.001,0.002",
    # Эйфелева башня:
    f"https://static-maps.yandex.ru/v1?apikey={API_KEY_STATIC}&ll=158.833772,53.256991&spn=0.05,0.05",
    # Авачинский вулкан:
    f"https://static-maps.yandex.ru/v1?apikey={API_KEY_STATIC}&ll=63.334573,45.920851&spn=0.005,0.005"
    # Площадка Байконура "Гагаринсий старт"
]


class MyError(Exception):
    pass


def load_next_slide(counter):
    # Запрашиваем изображение.
    request = map_requests[counter % len(map_requests)]
    response = requests.get(request)
    if not response:
        print("Ошибка выполнения запроса:", file=sys.stderr)
        print(request, file=sys.stderr)
        print("Http статус:", response.status_code, "(", response.reason, ")", file=sys.stderr)
        raise MyError()

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        raise MyError()

    surface = pygame.image.load(map_file)

    os.remove(map_file)
    return surface


def draw_next_slide(screen, counter):
    # Загружаем слайд.
    slide = load_next_slide(counter)
    # Рисуем слайд.
    screen.blit(slide, (0, 0))
    # Переключаем экран.
    pygame.display.flip()
    return counter + 1


def run_slide_show(screen):
    slide_counter = draw_next_slide(screen, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYUP:
                slide_counter = draw_next_slide(screen, slide_counter)


def main():
    # Инициализируем pygame
    pygame.init()
    try:
        run_slide_show(pygame.display.set_mode((600, 450)))
    except MyError as ex:
        pass
    pygame.quit()


if __name__ == "__main__":
    main()
