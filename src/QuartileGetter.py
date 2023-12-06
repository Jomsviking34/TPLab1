# -*- coding: utf-8 -*-
from math import ceil, floor


class QuartileGetter:
    def __init__(self) -> None:
        self.quartile = []

    def getHighQuartile(self, sorted_list: list) -> list:
        c = ceil(3 * len(sorted_list) / 4)
        f = floor(3 * len(sorted_list) / 4)
        high = ceil((c+f)/2)
        self.quartile = sorted_list[high:len(sorted_list)]
        return self.quartile
