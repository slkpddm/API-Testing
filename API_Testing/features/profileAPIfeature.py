from pytest_bdd import scenario, given, when, then


@given("The player details which needs to be added to database")
def step_impl():
    raise NotImplementedError(u'STEP: Given The player details which needs to be added to database')


@when("We execute the Insert PostAPI method")
def step_impl():
    raise NotImplementedError(u'STEP: When We execute the Insert PostAPI method')


@then("Profile is successfully inserted")
def step_impl():
    raise NotImplementedError(u'STEP: Then Profile is successfully inserted')


@given("status code of response should be 201")
def step_impl():
    raise NotImplementedError(u'STEP: And  status code of response should be 201')


@given("The player details <player> and <test> and <odi> and <t20> which needs to be added to database")
def step_impl():
    raise NotImplementedError(
        u'STEP: Given The player details <player> and <test> and <odi> and <t20> which needs to be added to database')