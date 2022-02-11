import shutil
import requests

url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
response = requests.get(url, stream=True)
with open('samples/img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response