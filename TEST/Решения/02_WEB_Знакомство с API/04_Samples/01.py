import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'
geocode = 'Якутск'
# Готовим запрос.
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Запрос успешно выполнен, печатаем полученные данные.
    print(response.content)
else:
    # Произошла ошибка выполнения запроса. Обрабатываем http-статус.
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
