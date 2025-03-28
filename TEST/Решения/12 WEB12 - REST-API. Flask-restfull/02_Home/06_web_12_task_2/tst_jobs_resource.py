from pprint import pprint

from requests import get, post, delete

pprint(get('http://localhost:5000/api/v2/jobs').json())
pprint(get('http://localhost:5000/api/v2/jobs/5').json())
pprint(get('http://localhost:5000/api/v2/jobs/52').json())  # нет работы с таким id
# print(get('http://localhost:5000/api/v2/jobs/q').json())  # не число

pprint(post('http://localhost:5000/api/v2/jobs', json={}).json())  # нет словаря
pprint(post('http://localhost:5000/api/v2/jobs', json={'job': 'creating application for DB'}).json())  # не все поля
pprint(post('http://localhost:5000/api/v2/jobs', json={'job': 'creating application for DB', 'work_size': 12,
                                                       'team_leader': 9, 'collaborators': '6, 7',
                                                       'is_finished': True, 'category': 3}).json())

pprint(delete('http://localhost:5000/api/v2/jobs/999').json())  # id = 999 нет в базе
# print(delete('http://localhost:5000/api/v2/jobs/10').json())
