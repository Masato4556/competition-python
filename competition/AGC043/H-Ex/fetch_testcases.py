

# poetry run python fetch_testcases.py
from urllib import request
from bs4 import BeautifulSoup

url = f'https://atcoder.jp/contests/abc294/tasks/abc294_e'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

# TODO: テストケースを取得してテキストファイルとして配置する

response.close()