from bs4 import BeautifulSoup
from urllib import request
import argparse
import os

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


parser = argparse.ArgumentParser(description='テストケースの取得')
parser.add_argument('url')
args = parser.parse_args()


input_cases, output_cases = get_testcases(args.url)
print(input_cases, output_cases)


os.makedirs("testcases/input")
os.makedirs("testcases/output")

# テストケースのテキストファイルを作成
testcase_num = len(input_cases)
for i in range(testcase_num):
    with open("./testcases/input/{}.txt".format(i+1), mode='w') as f:
        f.write(input_cases[i])
    with open("./testcases/output/{}.txt".format(i+1), mode='w') as f:
        f.write(output_cases[i])
