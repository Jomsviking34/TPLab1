# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.JSONDataReader import JSONDataReader


class TestJSONDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "{\n" + \
               "  \"Иванов Иван Иванович\": {\n" + \
               "    \"математика\": 91,\n" + \
               "    \"химия\": 100,\n" + \
               "    \"программирование\": 91\n" + \
               "  }\n" + \
               "}"
        data = {
            "Иванов Иван Иванович": [
                ("математика", 91), ("химия", 100), ("программирование", 91)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JSONDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
