import requests
import shutil

url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-142209.jpg'
img1 = 'img1.jpg'

r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(img1, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
