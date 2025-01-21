import requests

#response = requests.get('https://www.walissonsilva.com')
response = requests.get('https://escoladepos.ufg.br/')

print('Status code: ', response.status_code)
print('Header')
print(response.headers)

print('\n Content')
print(response.content)
