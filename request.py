import requests

url ='https://crudcrud.com/api/92e80444a04f4061b04191956495ea4b/cars'

car = {'manufacturer': 'Ferrari', 'model': 'Italia'}

# response = requests.post(url, json=car)

# response = requests.get(url)

# response = requests.put(url, json=car)

response = requests.delete(url)

print(response)