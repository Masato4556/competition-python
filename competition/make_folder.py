from bs4 import BeautifulSoup
from urllib import request
import os
import shutil
import datetime
import argparse


def make_contest_folder(name):
    dir = "./{}".format(name)
    os.mkdir(dir)


def make_question_folder(contest, questions):
    contest_dir = "./{}".format(contest)
    for q in questions:
        shutil.copytree("./template", contest_dir + "/{}".format(q))


# poetry run python fetch_testcases.py


def get_testcases(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()

    # テストケースの入力と出力のテキストを取得
    h3_elems = soup.select("h3")
    h3_input_testcase_elems = [elem for elem in h3_elems if "入力例" in elem.text]
    h3_output_testcase_elems = [
        elem for elem in h3_elems if "出力例" in elem.text]

    input_cases = [elem.next_sibling.text for elem in h3_input_testcase_elems]
    output_cases = [
        elem.next_sibling.text for elem in h3_output_testcase_elems]

    return (input_cases, output_cases)


def get_task_links(contest_name):

    tasks_url = "https://atcoder.jp/contests/{}/tasks".format(
        contest_name.lower())

    response = request.urlopen(tasks_url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()

    task_link_elems = soup.select("tr td a")
    task_links = list(set([elem.get('href') for elem in task_link_elems]))
    task_links.sort()

    return task_links


def get_task_names(task_links):
    return [task_link.split("/")[-1].upper() for task_link in task_links]


parser = argparse.ArgumentParser(description='フォルダの作成')
dt_now = datetime.datetime.now()
parser.add_argument('-c', '--contest', default=dt_now.strftime('%Y%m%d%H%M%S'))
parser.add_argument('-q', '--questions', nargs='*',
                    default=["A", "B", "C", "D", "E", "F", "G", "H-Ex"])
parser.add_argument('-g', '--get-testcase', action='store_true')

args = parser.parse_args()
folder_names = args.questions

print(args.get_testcase)
if args.get_testcase:
    task_links = get_task_links(args.contest)
    task_names = get_task_names(task_links)
    folder_names = task_names

make_contest_folder(args.contest)
make_question_folder(args.contest, folder_names)

if args.get_testcase:
    for i in range(len(task_links)):
        task_link = task_links[i]
        task_name = task_names[i]
        input_cases, output_cases = get_testcases("https://atcoder.jp" + task_link)
        print(input_cases, output_cases)
        
        # テストケースのテキストファイルを作成
        testcase_num = len(input_cases)
        for i in range(testcase_num):
            with open("./{}/{}/testcases/input/{}.txt".format(args.contest, task_name, i+1), mode='w') as f:
                f.write(input_cases[i])
            with open("./{}/{}/testcases/output/{}.txt".format(args.contest, task_name, i+1), mode='w') as f:
                f.write(output_cases[i])
