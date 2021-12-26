import dataclasses
import json

import pytest


@dataclasses.dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    city: str
    address: str
    phone_number: str

    def asdict(self):
        return dataclasses.asdict(self)

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.asdict(), f)


@pytest.fixture
def user(faker):
    result = User(
        faker.first_name(),
        faker.last_name(),
        faker.city(),
        faker.address(),
        faker.phone_number(),
    )
    return result


@pytest.fixture
def user_filepath(tmpdir):
    return tmpdir / "user.json"


def test_save_user(user, user_filepath):
    user.save(user_filepath)
    with open(user_filepath) as f:
        actual = json.load(f)
    print(actual)
    assert actual == user.asdict()
