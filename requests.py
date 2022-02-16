import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':5,'KM':13000,'HP':320,'Cylinders':4,'Gears':5,'Weight':1200})

print(r.json())
