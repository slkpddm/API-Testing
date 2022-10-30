from pytest_bdd import scenario, given, when, then


@given("I have github auth credentials")
def step_impl():
    raise NotImplementedError(u'STEP: Given I have github auth credentials')


@when("I hit getRepo API of github")
def step_impl():
    raise NotImplementedError(u'STEP: When I hit getRepo API of github')


@then("status code of response should be 200")
def step_impl():
    raise NotImplementedError(u'STEP: Then status code of response should be 200')