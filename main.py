import requests as requests
import urllib.requests as url

api = requests.get('https://api.unsplash.com/search/collections?query=hello&page=1&per_page=5&client_id=')

the_data = api.json()

#print(the_data.keys())
#print(data['total'])
#print(data['results'])


for img_data in the_data['results']:
    file_name = str(img_data['id']) + ".jpg"
    img_url = img_data['cover_photo']['urls']['raw']
    suffix = '&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1920&fit=max'
    print(img_url)
    img_url = img_url + suffix
    url.urlretrieve(img_url, file_name)