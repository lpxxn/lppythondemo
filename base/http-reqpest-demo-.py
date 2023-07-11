import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)

assert r.status_code == 200, f'Should be 200 current is {r.status_code}'

print(r.encoding)
print(r.text)
print(r.json())

print(r.json()['authenticated'])
# print(r.json()['user1'])
print(r.json().get('authenticatedvvv'))

if r.json().get('adsf') is None:
    print('adsf is None')