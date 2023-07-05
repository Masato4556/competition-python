import os
import shutil
import datetime
import argparse

def make_contest_folder(name):
    dir  = "./{}".format(name)
    os.mkdir(dir)

def make_question_folder(contest, questions):
    contest_dir  = "./{}".format(contest)
    for q in questions:
        shutil.copytree("./template", contest_dir + "/{}".format(q))


parser = argparse.ArgumentParser(description='フォルダの作成')
dt_now = datetime.datetime.now()
parser.add_argument('-c', '--contest', default=dt_now.strftime('%Y%m%d%H%M%S'))
parser.add_argument('-q', '--questions', nargs='*', default=["A", "B", "C", "D", "E", "F", "G", "H-Ex"])

args = parser.parse_args()
make_contest_folder(args.contest)
make_question_folder(args.contest, args.questions)
