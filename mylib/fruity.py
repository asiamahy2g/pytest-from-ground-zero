"""A simple module to randomly select a fruit."""

from random import choices


def random_fruit():
    """Return a random fruit from the list."""
    fruits = ["apple", "banana", "cherry"]
    return choices(fruits)[0]
