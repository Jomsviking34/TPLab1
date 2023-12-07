import argparse
import sys
from CalcRating import CalcRating
from DataReader import DataReader
from TextDataReader import TextDataReader
from JSONDataReader import JSONDataReader
from QuartileGetter import QuartileGetter


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def select_reader(path) -> DataReader:
    if path.endswith('.txt'):
        reader = TextDataReader()
    elif path.endswith('.json'):
        reader = JSONDataReader()
    else:
        reader = None
    return reader


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = select_reader(path)
    if isinstance(reader, DataReader):
        students = reader.read(path)
        print("Students: ", students)
        rating = CalcRating(students).calc()
        print("\nRating: ", rating)
        students_list = []
        for student in rating:
            students_list.append((student, rating[student]))
        quartilegetter = QuartileGetter()
        high_quartile = quartilegetter.getHighQuartile(students_list,
                                                       False, lambda x: x[1])
        print('\nHigh quartile: ', high_quartile)
    else:
        print('Wrong file extension')


if __name__ == "__main__":
    main()
