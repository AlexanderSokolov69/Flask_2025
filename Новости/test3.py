#!/usr/bin/env python3
# coding:utf-8
from requests import get, post, delete

resp = get('http://localhost:5050/api/v2/news')
print(resp.json())

# resp = get('http://localhost:5050/api/v2/news/3')
# print(resp.json())
#
resp = delete('http://localhost:5050/api/v2/news/16')
print(resp.json())

req = post('http://localhost:5050/api/v2/news',
           json={'title': 'Новость v2', 'content': 'Прогулка по территории v2',
                 'is_private': True, 'is_published': True,
                 'user_id': 1})
print(req.json())

