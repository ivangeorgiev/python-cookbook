Behavior Driven Development with `pytest-bdd`_
================================================

To install ``pytest-bdd``:

.. code-block:: console

   $ pip install pytest-bdd
   ..................

We are going to test a simple basket simulation:

.. code-block:: python
   :caption: basket.py

   class Basket:
      count: int

      def __init__(self, count=None) -> None:
         self.count = count or 0

      def get(self, count):
         if count <= 0:
               raise ValueError(f"Cannot give zero or negative number of cucumbers.")
         if self.count >= count:
               self.count -= count
         else:
               raise ValueError(
                  f"Cannot give you {count} cucumbers. There {self.count} left."
               )
         return count

      def put(self, count):
         if count <= 0:
               raise ValueError(f"Cannot put zero or negative number of cucubmers.")
         self.count += count
         return count

``pytest-bdd`` basics
-----------------------------

pytest-bdd implements a subset of the Gherkin language to enable automating project requirements testing and to facilitate behavioral driven development.

Let's start with a simple scenario - creating an empty basket:

.. code-block:: gherkin
   :caption: feature/basic_basket.feature

   Feature: Basic basket
      Scenario: Create empty basket
         When I create empty basket
         Then basket should be empty

This scenario has no ``Given`` steps, just one ``When`` step for action and one ``Then`` step for result validation. We need to implement them:

.. code-block:: python
   :caption: test_basic_basket.py

   from .basket import Basket
   from pytest_bdd import scenario, given, when, then


   @scenario("feature/basic_basket.feature", "Create empty basket")
   def test_create_empty_basket():
      pass

   @when("I create empty basket", target_fixture="basket")
   def basket():
      return Basket()

   @then("basket should be empty")
   def assert_empty_basket(basket: Basket):
      assert basket.count == 0

Although trivial scenario, our test uses one of the most important aspects of the testing - the fixtures. ``pytest`` implements fixtures as dependency injection mechanism which could be used to maintain state between steps. In our scenario the ``when`` step creates a basket and needs somehow to pass the basket to following steps. To achieve this, we use ``target_fixture="basket"`` in the ``when`` step to tell ``pytest-bdd`` to assign the result of the function to a ``basket`` ``pytest`` fixutre. Later we specify the ``basket`` argument to the ``then`` step to tell ``pytest`` to inject the ``basket`` fixture.

We can execute the tests now and observe the output:

.. code-block:: console

   $ pytest
   ============================= test session starts =============================
   ........................
   tests\basket\test_basic_basket.py .                                      [100%]

   ============================== 1 passed in 0.05s ==============================

Let's add one more test scenario to our feature definition:

.. code-block:: gherkin

   # ....
   Scenario: Add to empty basket
      Given empty basket
      When I put 3 cucumbers
      Then basket should have 3 cucumbers

We have to implement:

- ``given`` step: *"empty basket"*
  We observe that this step is identical with the ``when`` step we already created: *"I create empty basket"* so we are not going to create a new function, but mark the same function.
- ``when`` step: *"I put 3 cucumbers"*
- ``then`` step: *"basket should have 3 cucumbers"*

.. code-block:: python
   :caption: test_basic_basket.py

   # ...

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

   @then("basket should have 3 cucumbers")
   def assert_basket_has_3_cucumbers(basket: Basket):
      assert basket.count == 3


Step arguments
------------------

What if we want to perform the *"I put 3 cucumbers"* step with different number of cucumbers? Should we define a new step implementation and also a new step implementation for the ``then`` validation step? ``pytest-bdd`` provides step arguments:

.. code-block:: gherkin
   :caption: basket.feature

   Feature: Basket
      Scenario: Get cucumbers multiple times
         Given there are 5 cucumbers in the basket
         When I get 1 cucumber
         And I get 3 cucumbers
         Then I should have 1 cucumbers

We implement this as:

.. code-block:: python

   from basket import Basket

   from pytest_bdd import scenario, given, when, then, parsers

   @given(
      parsers.parse("there are {start:d} cucumbers in the basket"),
      target_fixture="basket",
   )
   def basket(start: int) -> Basket:
      return Basket(start)


   @when(parsers.parse("I get {num:d} cucumbers"))
   def get_cucumbers(num, basket: Basket):
      basket.get(num)

   @then(parsers.parse("I should have {num:d} cucumbers"))
   def assert_left(num, basket: Basket):
      assert basket.count == num

Step decorator can accept as first ``name`` argument:

- ``str`` - exact match. Passes no parameters.
- ``parse`` - Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like ``{param:Type}``. The named fields are extracted, optionally type converted and then used as step function arguments.
- ``cfparse`` - Provides an extended parser with “Cardinality Field” (CF) support.
- ``re`` - This uses full regular expressions to parse the clause text. You will need to use named groups ``“(?P<name>…)”`` to define the variables pulled from the text and passed to your step function.

We are using ``parse`` argument to parametrize our steps.


Scenario outlines
-------------------

Scenarios can be parametrized to cover few cases. In Gherkin the variable templates are written using corner braces as ``<somevalue>``. These are called `scenario outlines <https://behat.org/en/v3.0/user_guide/writing_scenarios.html#scenario-outlines>`__:

.. code-block::
   :caption: basket.feature

   # .........
   Scenario Outline: Get cucumbers
      Given there are <start> cucumbers in the basket
      When I put <num> cucumbers
      Then I should have <left> cucumbers

      Examples:
         | start | num | left |
         | 0     | 5   | 5    |
         | 3     | 7   | 10   |

We have only one step implementation missing: the *"I put <num> cucumbers"* ``when`` step:

.. code-block:: python
   :caption: basket.py

   @when(parsers.parse("I put {num:d} cucumbers"))
   def get_cucumbers(num, basket: Basket):
      basket.get(num)



For detailed information refer to the `pytest-bdd documentation`_.

.. _`pytest-bdd`: `pytest-bdd source`_
.. _`pytest-bdd documentation`: https://pytest-bdd.readthedocs.io/en/latest/
.. _`pytest-bdd source`: https://github.com/pytest-dev/pytest-bdd
