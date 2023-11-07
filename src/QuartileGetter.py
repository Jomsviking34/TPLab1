# -*- coding: utf-8 -*-
from math import ceil


class QuartileGetter:
    def __init__(self) -> None:
        self.quartile = []

    def getHighQuartile(self, sorted_list: list) -> list:
        high = int(ceil(3 * len(sorted_list) / 4))
        self.quartile = sorted_list[high:len(sorted_list)]
        return self.quartile
