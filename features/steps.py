from lettuce import step
from lettuce import world
from echo_client import run_client


@step('the string (\w+)')
def the_string(step, msg):
    world.cla = msg


@step('when I call echo_client')
def call_echo_client(step):
    world.client = run_client(world.cla)


@step('I see the output (\w+)')
def compare(step, expected):
    assert world.client == expected, "Got %s" % expected
