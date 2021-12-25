import os

import pytest


class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age


def test_monkeypatch_can_set_module_attr(monkeypatch):
    e = {}
    monkeypatch.setattr(os, "environ", e)
    assert os.environ is e


def test_monkeypatch_can_set_env_var(monkeypatch):
    monkeypatch.setenv("PYTHON_REFS_MONKEY_PATCH", "REALLY")
    assert os.environ.get("PYTHON_REFS_MONKEY_PATCH") == "REALLY"


def test_monkeypatch_deletes_item_from_mapping(monkeypatch):
    mapping = {"name": "John", "age": 32}
    monkeypatch.delitem(mapping, "age")
    assert "age" not in mapping


def test_monkeypatch_cannot_delete_item_from_object(monkeypatch):
    obj = Person("John")
    with pytest.raises(TypeError):
        monkeypatch.delitem(obj, "name")
        assert not hasattr(obj, "name")


def test_monkeypatch_can_delete_attribte_from_object(request, monkeypatch):
    obj = Person("John")
    monkeypatch.delattr(obj, "name", raising=False)
    assert not hasattr(obj, "name")
