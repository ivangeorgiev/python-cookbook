import pytest
from pytest_bdd import given, parsers, scenario, scenarios, then, when

from ...basket import Basket

scenarios("feature/basket.feature")


@pytest.fixture
def basket_factory():
    return Basket


@scenario("feature/basket.feature", "Get cucumbers")
def test_get_cucumbers():
    pass


# @scenario("feature/basket.feature", "Get cucumbers multiple times")
# def test_get_cucumbers_multiple_times():
# pass


@given(
    parsers.parse("there are {start:d} cucumbers"),
    target_fixture="basket",
)
@given(
    parsers.parse("there are {start:d} cucumber"),
    target_fixture="basket",
)
@given(
    parsers.parse("there are {start:d} cucumbers in the basket"),
    target_fixture="basket",
)
@given(
    parsers.parse("there are {start:d} cucumber in the basket"),
    target_fixture="basket",
)
def given_basket(start: int, basket_factory) -> Basket:
    return basket_factory(start)


@when("I create empty basket", target_fixture="basket")
def create_empty_basket() -> Basket:
    return Basket()


@when(parsers.parse("I put {num:d} cucumber"))
@when(parsers.parse("I put {num:d} cucumbers"))
@when(parsers.parse("I put {num:d} cucumber to the basket"))
@when(parsers.parse("I put {num:d} cucumbers to the basket"))
def put_cucumbers(num, basket: Basket):
    basket.put(num)


@when(parsers.parse("I get {num:d} cucumber"))
@when(parsers.parse("I get {num:d} cucumbers"))
@when(parsers.parse("I get {num:d} cucumber from the basket"))
@when(parsers.parse("I get {num:d} cucumbers from the basket"))
def get_cucumbers(num, basket: Basket):
    basket.get(num)


@then(parsers.parse("I should have {num:d} cucumber"))
@then(parsers.parse("I should have {num:d} cucumbers"))
@then(parsers.parse("I should have {num:d} cucumber in the basket"))
@then(parsers.parse("I should have {num:d} cucumbers in the basket"))
def assert_left(num, basket: Basket):
    assert basket.count == num
