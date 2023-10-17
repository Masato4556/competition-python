

# poetry run python fetch_testcases.py
from urllib import request
from bs4 import BeautifulSoup


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


tasks_url = "https://atcoder.jp/contests/abc306/tasks"

response = request.urlopen(tasks_url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

task_link_elems = soup.select("tr td a")
task_links = list(set([elem.get('href') for elem in task_link_elems]))
task_links.sort()
print(task_links)

for task_link in task_links:
    url = f'https://atcoder.jp/contests/abc294/tasks/abc294_e'

    task_name = task_link.split("/")[-1]

    print(task_name[-1].upper())

    # input_cases, output_cases = get_testcases(url)

    # # テストケースのテキストファイルを作成
    # testcase_num = len(input_cases)
    # for i in range(testcase_num):
    #     with open("./testcases/input/{}.txt".format(i+1), mode='w') as f:
    #         f.write(input_cases[i])
    #     with open("./testcases/output/{}.txt".format(i+1), mode='w') as f:
    #         f.write(output_cases[i])
