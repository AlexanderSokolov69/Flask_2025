import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from wikipedia import wikipedia

vk_session = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

wikipedia.set_lang('ru')


def wiki_response(request_text):
    return str(wikipedia.page(request_text).content[:1000])


def help():
    return f"What do you want to ask Wikipedia?"


def main():
    flag_wiki, flag_help = False, True
    for event in longpoll.listen():
        if event.to_me:
            if event.type == VkEventType.MESSAGE_NEW and flag_help:
                flag_wiki = not flag_wiki
                flag_help = not flag_help
                vk.messages.send(chat_id=event.chat_id,
                                 message=help(),
                                 random_id=random.randint(0, 2 ** 64))

            elif event.type == VkEventType.MESSAGE_NEW and flag_wiki:
                vk.messages.send(chat_id=event.chat_id,
                                 message=f"{wiki_response(event.text)}\n\n{help()}",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
