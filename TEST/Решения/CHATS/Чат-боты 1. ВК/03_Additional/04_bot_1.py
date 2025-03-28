import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()


def main():
    for event in longpoll.listen():
        print(event)
        if event.type == VkEventType.MESSAGE_NEW:
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
                                         message=f'Привет, {name}! Как поживает {city}?',
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        vk.messages.send(chat_id=event.chat_id,
                                         message=f'Привет, {name}!',
                                         random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
