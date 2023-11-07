# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JSONDataReader import JSONDataReader
from QuartileGetter import QuartileGetter


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if path.endswith('.txt'):
        reader = TextDataReader()
    if path.endswith('.json'):
        reader = JSONDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    students_list = []
    for student in rating:
        students_list.append((student, rating[student]))

    def takeSecond(elem):
        return elem[1]

    students_list.sort(key=takeSecond)
    quartilegetter = QuartileGetter()
    high_quartile = quartilegetter.getHighQuartile(students_list)
    print('High quartile:')
    print("Rating: ", high_quartile)


if __name__ == "__main__":
    main()
