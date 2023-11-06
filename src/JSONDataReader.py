# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json


class JSONDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            students = json.load(file)
        for key in students:
            self.students[key] = []
            subjects = students[key]
            for subject in subjects:
                self.students[key].append((subject, int(subjects[subject])))
        return self.students
