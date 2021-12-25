Testing with Pytest
====================

`Pytest`_ is arguably the most popular and widespread testing framework in the Python community. It is also compatible with Python's `unittest`_ and `doctest`_.


`Pytest`_ plugins
-------------------

- `pytest-bdd`_ - Implements a subset of the Gherkin language to enable automating project requirements testing and to facilitate behavioral driven development.
- `pytest-cov`_ - Produces coverage reports.
- `pytest-django`_ -  Provides a set of useful tools for testing Django applications and projects.
- `pytest-randomly`_ - Randomly order tests with controlled seed.
- `pytest-reverse`_ - Execute tests in reverse order.
- `pytest-splinter`_ - Provides a set of fixtures to use `splinter`_ for browser testing with `pytest`_
- `pytest-xdist`_ - Adds test execution modes, e.g. multi-CPU and distributed.

Running `doctest`_ test cases
-----------------------------

By default `pytest`_ is looking for ``test_*.txt`` files and if such a file is found, `pytest`_ executes the `doctest`_ tests defined in this file.

`Pytest`_ can also discover and execute `doctest`_ test cases from Python modules. For example if a function has docstring which contains `doctest`_ test cases, `pytest`_ can execute the tests.

.. code-block:: python
   :name: addition-doctest-py
   :caption: addition_doctest.py

   def add(*args):
      """Add one or more numbers and return the result.

      >>> add(3, 2)
      5
      >>> add(5, 4, 3, 2, 3, 4, 5)
      26
      """
      return sum(args)

To execute test cases from modules, specify the ``--doctest-modules`` option to `pytest`_.

.. code-block:: console

   $ pytest --doctest-modules
   ============================== test session starts ==============================
   platform win32 -- Python 3.8.1, pytest-6.1.0, py-1.9.0, pluggy-0.13.1
   rootdir: C:\Sandbox\PoC\python-repl-cmd\src
   plugins: cov-2.8.1, django-4.4.0, flask-0.14.0
   collected 1 item

   addition_doctest.py .                                                      [100%]

   =============================== 1 passed in 0.04s ===============================

For further information refer to the `pytest doctest`_ integration documentation.

Running `unittest`_ test cases
-------------------------------

`Pytest`_ can discover and execute `unittest`_ test cases:

.. code-block:: python
   :name: test-addition-py
   :caption: test_addition.py

   import unittest

   def add(*args):
      return sum(args)

   class TestAddition(unittest.TestCase):
      def test_result_is_sum(self):
         result = add(3, 2)
         self.assertEqual(result, 5)

      def test_add_many(self):
         result = add(5, 4, 3, 2, 3, 4, 5)
         self.assertEqual(result, 26)

Running the tests is as easy as:

.. code-block:: console

   $ pytest
   ============================== test session starts ==============================
   platform win32 -- Python 3.8.1, pytest-6.1.0, py-1.9.0, pluggy-0.13.1
   rootdir: C:\Sandbox\PoC\python-repl-cmd\src
   plugins: cov-2.8.1, django-4.4.0, flask-0.14.0
   collected 2 items

   test_addition.py ..                                                        [100%]

   =============================== 2 passed in 0.06s ===============================

This makes it very easy to migrate from `unittest`_ to `pytest_` or to combine tests that use different frameworks.

.. _doctest: https://docs.python.org/3/library/doctest.html
.. _pytest: https://docs.pytest.org/en/latest/doctest.html
.. _pytest doctest: https://docs.pytest.org/en/latest/doctest.html
.. _pytest-bdd: https://github.com/pytest-dev/pytest-bdd
.. _pytest-cov: https://github.com/pytest-dev/pytest-cov
.. _pytest_cov documentation: https://pytest-cov.readthedocs.io/en/latest/
.. _pytest-django: https://pytest-django.readthedocs.io/en/latest/
.. _pytest-randomly: https://github.com/pytest-dev/pytest-randomly
.. _pytest-reverse: https://github.com/adamchainz/pytest-reverse
.. _pytest-splinter: https://github.com/pytest-dev/pytest-splinter
.. _pytest-xdist: https://github.com/pytest-dev/pytest-xdist
.. _splinter: https://splinter.readthedocs.io/en/latest/
.. _unittest: https://docs.python.org/3/library/unittest.html

.. _speed up your django tests: https://adamchainz.gumroad.com/l/suydt
