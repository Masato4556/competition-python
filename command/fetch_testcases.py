from bs4 import BeautifulSoup
from urllib import request
import argparse
import os

ROOT_PATH = "./competition"


def generate_question_path(main_dir, sub_dir):
    return f'{ROOT_PATH}/{main_dir}/{sub_dir}'


def generate_input_path(main_dir, sub_dir):
    question_path = generate_question_path(main_dir, sub_dir)
    return f'{question_path}/testcases/input/'


def generate_output_path(main_dir, sub_dir):
    question_path = generate_question_path(main_dir, sub_dir)
    return f'{question_path}/testcases/output/'


def make_testcase_dir(main_dir, sub_dir) -> None:
    os.makedirs(generate_input_path(main_dir, sub_dir), exist_ok=True)
    os.makedirs(generate_output_path(main_dir, sub_dir), exist_ok=True)


def get_testcases(url) -> tuple[list[str], list[str]]:
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='テストケースの取得')
    parser.add_argument('main_dir')
    parser.add_argument('sub_dir')
    parser.add_argument('url')
    args = parser.parse_args()

    input_cases, output_cases = get_testcases(args.url)
    print(input_cases, output_cases)

    make_testcase_dir(args.main_dir, args.sub_dir)

    # テストケースのテキストファイルを作成
    testcase_num = len(input_cases)
    for i in range(testcase_num):
        with open(f"{generate_input_path(args.main_dir, args.sub_dir)}/{i+1}.txt", mode='w') as f:
            f.write(input_cases[i])
        with open(f"{generate_output_path(args.main_dir, args.sub_dir)}/{i+1}.txt", mode='w') as f:
            f.write(output_cases[i])
