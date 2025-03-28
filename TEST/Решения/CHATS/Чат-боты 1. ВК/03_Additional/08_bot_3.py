import random

import vk_api
from vk_api.longpoll import VkLongPoll


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    response = vk.photos.get(album_id=272048436, group_id=GROUP_ID)
    photo_to_send = ''
    if response['items']:
        photo_to_send = random.choice(
            [f"photo{item['owner_id']}_{item['id']}" for item in response['items']]
        )

    vk_session = vk_api.VkApi(
        token=TOKEN)
    longpoll = VkLongPoll(vk_session, GROUP_ID)

    for event in longpoll.listen():
        print(event)
        vk = vk_session.get_api()
        if event.to_me:
            if event.text:
                name = vk.users.get(user_id=event.user_id)[0]['first_name']

                city = None
                try:
                    city = vk.users.get(user_id=event.user_id, fields='city')[0]['city']['title']
                except Exception:
                    pass
                if city:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f'Привет, {name}! Как поживает {city}?\nА это котик',
                                     attachment=photo_to_send,
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f'Привет, {name}!',
                                     attachment=photo_to_send,
                                     random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
