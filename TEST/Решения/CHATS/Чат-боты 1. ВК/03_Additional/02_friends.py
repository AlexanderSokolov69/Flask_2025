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
    response = vk.friends.get(fields="bdate, city")
    if response['items']:
        data = [
            (item['last_name'], item['first_name'], item['bdate'])
            for item in response['items']
        ]
        print(*[' '.join(items) for items in sorted(data)], sep='\n')


if __name__ == '__main__':
    main()
