Coding Style
===============


Pre-commit
------------

To get started with ``pre-commit``, follow these steps:

1. **Install pre-commit.** To do so, follow `the pre-commit installation instructions <https://pre-commit.com/#install>`_.

    .. code-block:: console

        $ pip install pre-commit

    Create a ``.pre-commit-config.yaml`` configuration file. To get started use sample config:

    .. code-block:: console

        $ pre-commit sample-config > .pre-commit-config.yaml

    Here is another ``.pre-commit-config.yaml`` to start with. Based on Django ``.pre-commit-conifg.yaml``.

    .. code-block:: yaml

        # See https://pre-commit.com for more information
        # See https://pre-commit.com/hooks.html for more hooks
        repos:
        - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
            - id: trailing-whitespace
            - id: end-of-file-fixer
            - id: check-yaml
            - id: check-added-large-files
        - repo: https://github.com/PyCQA/isort
        rev: 5.9.3
        hooks:
            - id: isort
        - repo: https://github.com/PyCQA/flake8
        rev: 4.0.1
        hooks:
            - id: flake8
        - repo: https://github.com/pre-commit/mirrors-eslint
        rev: v7.32.0
        hooks:
            - id: eslint


2. Install the git hook scripts

    * run ``pre-commit install`` to setup the git hook script:

      .. code-block:: console

          $ pre-commit install
            pre-commit installed at .git\hooks\pre-commit

      Now ``pre-commit`` will run automatically on ``git commit``.

3. (Optional) Run pre-commit against all files:

   .. code-block:: console

       $ pre-commit run --all-files
       Trim Trailing Whitespace.......................................Passed
       Fix End of Files...............................................Passed
       Check Yaml.....................................................Passed
       Check for added large files....................................Passed
       Trim Trailing Whitespace.......................................Passed
       Fix End of Files...............................................Passed
       Check Yaml.....................................................Passed
       Check for added large files....................................Passed

   If you do not specify the ``--all-files`` option, ``pre-commit`` will run only against staged files.

Editorconfig
-------------

`EditorConfig <https://editorconfig.org/>`_ project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems.

Here is sample ``.editorconfig`` file, based on Django's ``.editorconfig``, to start with.

.. code-block:: ini

    # https://editorconfig.org/

    root = true

    [*]
    indent_style = space
    indent_size = 4
    insert_final_newline = true
    trim_trailing_whitespace = true
    end_of_line = lf
    charset = utf-8

    # Docstrings and comments use max_line_length = 79
    [*.py]
    max_line_length = 119

    # Use 2 spaces for the HTML files
    [*.html]
    indent_size = 2

    # The JSON files contain newlines inconsistently
    [*.json]
    indent_size = 2
    insert_final_newline = ignore

    [**/admin/js/vendor/**]
    indent_style = ignore
    indent_size = ignore

    # Minified JavaScript files shouldn't be changed
    [**.min.js]
    indent_style = ignore
    insert_final_newline = ignore

    # Makefiles always use tabs for indentation
    [Makefile]
    indent_style = tab

    # Batch files use tabs for indentation
    [*.bat]
    indent_style = tab

    [docs/**.txt]
    max_line_length = 79

    [*.yml]
    indent_size = 2


Plugins (see `EditorConfig plugins download <https://editorconfig.org/#download>`_ for full list):

- `EditorConfig for VS Code <https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig>`_


Flake8
-----------

`In-line ignoring errors <https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors>`_:

.. code-block:: python

    example = lambda: 'example'  # noqa: E731,E123

Further Flake8_ reading:

- `Flake8 documentation`_
- `Flake8 rules`_


.. _Flake8: https://flake8.pycqa.org/en/latest/index.html
.. _Flake8 documentation: Flake8_
.. _Flake8 rules: https://www.flake8rules.com/

Further reading
------------------

- `Django coding style <https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/>`_
- `Executable book Coding Style <https://executablebooks.org/en/latest/contributing.html#coding-style>`_
