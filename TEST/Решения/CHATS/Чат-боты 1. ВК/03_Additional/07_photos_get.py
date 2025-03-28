import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    response = vk.photos.get(album_id=ALBUM_ID, group_id=GROUP_ID)
    if response['items']:
        for item in response['items']:
            # print(item)
            print(item['sizes'][0]['url'],
                  f"{item['sizes'][0]['width']}x{item['sizes'][0]['height']}")


if __name__ == '__main__':
    main()
