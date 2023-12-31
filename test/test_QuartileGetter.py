# -*- coding: utf-8 -*-
from src.QuartileGetter import QuartileGetter
import pytest


class TestQuartileGetter:
    @pytest.fixture()
    def input_data(self) -> list:
        data: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return data

    def test_getHighQuartile_10(self, input_data: list) -> None:
        quartilegetter = QuartileGetter()
        high_quartile = quartilegetter.getHighQuartile(input_data)
        assert high_quartile == [8, 9, 10]

    def test_getHighQuartile_2(self, input_data: list) -> None:
        quartilegetter = QuartileGetter()
        high_quartile = quartilegetter.getHighQuartile(input_data[0:2])
        assert high_quartile == [2]

    def test_getHighQuartile_0(self) -> None:
        quartilegetter = QuartileGetter()
        high_quartile = quartilegetter.getHighQuartile([])
        assert len(high_quartile) == 0
