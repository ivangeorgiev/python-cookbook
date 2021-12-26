from pytest_bdd import given, scenario, then, when

from ...basket import Basket


@scenario("feature/basic_basket.feature", "Create empty basket")
def test_create_empty_basket():
    pass


@scenario("feature/basic_basket.feature", "Add to empty basket")
def test_add_to_empty_basket():
    pass


@given("empty basket", target_fixture="basket")
@when("I create empty basket", target_fixture="basket")
def basket():
    return Basket()


@when("I put 3 cucumbers")
def put_3_cucumbers(basket: Basket):
    basket.put(3)


@then("basket should be empty")
def assert_empty_basket(basket: Basket):
    assert basket.count == 0


@then("basket should have 3 cucumbers")
def assert_basket_has_3_cucumbers(basket: Basket):
    assert basket.count == 3
