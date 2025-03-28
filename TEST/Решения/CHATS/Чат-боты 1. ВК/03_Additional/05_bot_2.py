import datetime
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


def main():
    vk_session = vk_api.VkApi(token=TOKEN)

    longpoll = VkLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()

    dt = datetime.datetime.now()

    day = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг',
           4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if event.text:
                    date, time, weekday = dt.strftime('%Y-%m-%d'), dt.strftime('%H:%M:%S'), dt.weekday()
                    if "время" in event.text.lower() or "число" in event.text.lower() or \
                            "дата" in event.text.lower() or "день" in event.text.lower():
                        vk.messages.send(chat_id=event.chat_id,
                                         message=f"Сегодня {date}\n{day[weekday]}\nСейчас {time}",
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        vk.messages.send(chat_id=event.chat_id,
                                         message='Я могу сообщить дату, время и день недели, если Вы напишете одно из этих слов',
                                         random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
