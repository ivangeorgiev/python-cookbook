import json
import os

import pytest

from ....contacts import Application


@pytest.fixture
def save_filepath(tmpdir):
    return tmpdir / "contacts.json"


class TestLoading:
    def test_load(self, save_filepath):
        app = Application(save_filepath=save_filepath)

        with open(save_filepath, "w+") as f:
            json.dump({"_contacts": [("NAME SURNAME", "3333")]}, f)

        app.load()

        assert app._contacts == [("NAME SURNAME", "3333")]


class TestSaving:
    def test_save(self, save_filepath):
        app = Application(save_filepath=save_filepath)
        app._contacts = [("NAME SURNAME", "3333")]

        try:
            os.unlink("./contacts.json")
        except FileNotFoundError:
            pass

        app.save()

        with open(save_filepath) as f:
            assert json.load(f) == {"_contacts": [["NAME SURNAME", "3333"]]}
