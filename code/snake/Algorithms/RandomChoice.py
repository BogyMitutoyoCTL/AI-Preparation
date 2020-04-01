from random import random

from Algorithms.Algorithms import Algorithm
from GameData import GameData


class RandomChoice(Algorithm):
    def __init__(self):
        super().__init__()

    """
    A stupid algorithm that returns a random value.
    This can be used for comparisons with other algorithms.

    Best result: length 4 on a 10x20 field in 1000 epochs
    """

    def decide(self, info: GameData) -> str:
        r = int(random() * 4)
        return {0: "north", 1: "east", 2: "south", 3: "west"}[r]
