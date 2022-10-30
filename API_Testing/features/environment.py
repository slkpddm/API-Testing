import requests

from payLoad import profile_retrieve
from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "API" in scenario.tags:
        url = getConfig()['API']['endpoint'] + ApiResources.retrive
        response_get = requests.get(url, params=profile_retrieve("'Rohit'"))
        res = response_get.json()
        print(res[0])
        assert res[0][0] == "Rohit"

