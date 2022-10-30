import requests
import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *


# POST method
url = getConfig()['API']['endpoint']+ApiResources.insert

response_post = requests.post(url,json=profile_data("SKY",0,15,35))
print(response_post.json())
assert response_post.json() == "Successfully Inserted"
#Get Method
url = getConfig()['API']['endpoint']+ApiResources.retrive
response_get = requests.get(url,params=profile_retrieve("'Rohit'"))
res = response_get.json()
print(res[0])
assert res[0][0] == "Rohit"


