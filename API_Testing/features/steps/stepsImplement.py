import requests

from payLoad import profile_data
from utilities.configurations import getConfig, getPassword
from utilities.resources import ApiResources


@given(u'The player details which needs to be added to database')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.insert
    context.payLoad = profile_data("SKY", 0, 15, 35)


@when(u'We execute the Insert PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad)


@then(u'Profile is successfully inserted')
def step_impl(context):
    print(context.response.json())
    assert context.response.json() == "Successfully Inserted"


@given(u'The player details {player} and {test} and {odi} and {t20} which needs to be added to database')
def step_impl(context, player, test, odi, t20):
    context.url = getConfig()['API']['endpoint'] + ApiResources.insert
    context.payLoad = profile_data(player, test, odi, t20)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ('slkpddm@gmail.com', getPassword())


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
