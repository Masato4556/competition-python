import os
import shutil
import datetime
import argparse

ROOT_PATH = "./competition"


def make_contest_folder(name):
    dir = f"{ROOT_PATH}/{name}"
    os.mkdir(dir)


def make_question_folder(contest, questions):
    contest_dir = f"{ROOT_PATH}/{contest}"
    for q in questions:
        shutil.copytree(f"{ROOT_PATH}/template", contest_dir + "/{}".format(q))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='フォルダの作成')
    dt_now = datetime.datetime.now()
    parser.add_argument('-c', '--contest', default=dt_now.strftime('%Y%m%d%H%M%S'))
    parser.add_argument('-q', '--questions', nargs='*',
                        default=["A", "B", "C", "D", "E", "F", "G", "H-Ex"])
    parser.add_argument('-g', '--get-testcase', action='store_true')

    args = parser.parse_args()
    folder_names = args.questions

    make_contest_folder(args.contest)
    make_question_folder(args.contest, folder_names)
