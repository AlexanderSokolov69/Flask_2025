from requests import post, get

print(post('http://172.16.1.33:5050/api/jobs',
           json={'team_leader': 2, 'job': 'Прогулка по территории',
                 'work_size': 2, 'collaborators': '2, 3',
                 'is_finished': False}).json())

print(post('http://172.16.1.33:5050/api/jobs',
           json={'job': 'Прогулка по территории',
                 'work_size': 2, 'collaborators': '2, 3',
                 'is_finished': False}).json())

print(post('http://172.16.1.33:5050/api/jobs',
           json={}).json())

print(post('http://172.16.1.33:5050/api/jobs',
           json={'team_leader': 1}).json())


print(post('http://172.16.1.33:5050/api/jobs',
           json={'team_leader': 'rr', 'job': 'Прогулка по территории',
                 'work_size': 2, 'collaborators': '2, 3',
                 'is_finished': 'AAAA'}).json())

resp = get('http://172.16.1.33:5050/api/jobs')
print(resp.json())
