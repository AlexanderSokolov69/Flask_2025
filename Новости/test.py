from requests import get, post, delete

resp = get('http://172.16.1.33:5050/api/jobs')
print(resp.json())

resp = get('http://172.16.1.33:5050/api/jobs/1')
print(resp.json())

resp = get('http://172.16.1.33:5050/api/jobs/19999999999')
print(resp.json())

resp = get('http://172.16.1.33:5050/api/jobs/string')
print(resp.json())


print(post('http://172.16.1.33:5050/api/jobs', json={}).json())

print(post('http://172.16.1.33:5050/api/jobs',
           json={'job': 'Test'}).json())

print(post('http://172.16.1.33:5050/api/jobs',
           json={'team_leader': 1, 'job': 'Прогулка по территории',
                 'work_size': 2, 'collaborators': '2, 3',
                 'is_finished': False}).json())
#
# print(delete('http://172.16.1.33:5050/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://172.16.1.33:5050/api/news/11').json())
