class Basket:
    count: int

    def __init__(self, count=None) -> None:
        self.count = count or 0

    def get(self, count):
        if count <= 0:
            raise ValueError(
                "Cannot give zero or negative number of cucumbers."
            )  # noqa
        if self.count >= count:
            self.count -= count
        else:
            raise ValueError("Cannot give you more cucumbers than what's left.")  # noqa
        return count

    def put(self, count):
        if count <= 0:
            raise ValueError("Cannot put zero or negative number of cucubmers.")  # noqa
        self.count += count
        return count
