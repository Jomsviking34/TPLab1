# -*- coding: utf-8 -*-
from math import ceil, floor


class QuartileGetter:
    def __init__(self) -> None:
        self.quartile = []

    def getHighQuartile(self, list: list,
                        is_sorted: bool = True, func=None) -> list:
        if not is_sorted:
            list.sort(key=func)
        c = ceil(3 * len(list) / 4)
        f = floor(3 * len(list) / 4)
        high = int((c+f)/2)
        self.quartile = list[high:len(list)]
        return self.quartile
