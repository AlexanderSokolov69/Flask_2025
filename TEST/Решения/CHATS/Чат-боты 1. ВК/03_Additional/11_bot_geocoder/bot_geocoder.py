import sys

import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(
    token=TOKEN)

longpoll = VkLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()


def map_type():
    return f"Choose type of map"


def help():
    return f"Type the place your want to see"


def get_coords(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        return toponym_coodrinates.split(" ")
    else:
        return None, None


def get_map(lon_lat, type, delta="0.005", point=None):
    if point is None:
        map_params = {
            "ll": lon_lat,
            "spn": ",".join([delta, delta]),
            "l": type
        }
    else:
        map_params = {
            "ll": lon_lat,
            "spn": ",".join([delta, delta]),
            "l": type,
            "pt": point
        }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=map_params).content


def save_geo(toponim, map_type, filename):
    try:
        lat, lon = get_coords(toponim)
        lon_lat = f"{lat},{lon}"
        content = get_map(lon_lat, map_type, point=lon_lat)
        try:
            with open(f'static/img/{filename}', 'wb') as file:
                file.write(content)
            return filename
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(2)
    except Exception as e:
        return 'No data' + str(e)


def upload_picture(album_id, group_id, filename):
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return ''

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        f'static/img/{filename}',
        album_id=album_id,
        group_id=group_id
    )
    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
    return vk_photo_id


def main():
    flag_data, flag_help, flag_type = False, True, False
    place = ''
    for event in longpoll.listen():
        if event.to_me:
            if event.type == VkEventType.MESSAGE_NEW and flag_help:
                flag_data = not flag_data
                flag_help = not flag_help
                vk.messages.send(chat_id=event.chat_id,
                                 message=help(),
                                 random_id=random.randint(0, 2 ** 64))

            elif event.type == VkEventType.MESSAGE_NEW and flag_data:
                flag_data = not flag_data
                flag_type = not flag_type
                place = event.text
                vk.messages.send(chat_id=event.chat_id,
                                 message=map_type(),
                                 keyboard=open("keyboard.json", "r", encoding="utf-8").read(),
                                 random_id=random.randint(0, 2 ** 64))
            elif event.type == VkEventType.MESSAGE_NEW and flag_type:
                flag_data = not flag_data
                flag_type = not flag_type
                map = event.text
                album_id = ALBUM_ID
                pic_name = upload_picture(album_id, -event.user_id, save_geo(place, map, 'map.png'))
                vk.messages.send(chat_id=event.chat_id,
                                 message=f'That`s {place}.\n{help()}',
                                 attachment=pic_name,
                                 keyboard=open("keyboard_remove.json", "r", encoding="utf-8").read(),
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
