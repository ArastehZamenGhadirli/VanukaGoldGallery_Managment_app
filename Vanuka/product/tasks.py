import requests
headers = {'Authorization': 'Bearer YOUR_API_TOKEN'}
res = requests.get('https://api.alanchand.com?type=currency&symbols=usd', headers=headers)
print(res.json())
      