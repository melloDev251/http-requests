import requests

payload = {'username':'mello', 'password':'test33'}
res = requests.post('https://httpbin.org/post', data=payload)

res_dict = res.json()

print(res_dict['form'])
