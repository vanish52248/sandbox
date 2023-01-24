from bs4 import BeautifulSoup
import requests

# pythonのウェブサイトをスクレイピング
html = requests.get('https://www.python.org')

soup = BeautifulSoup(html.text)

# titleタグの中身をすべてリストで取得
titles = soup.find_all("title")
print(titles[0].text)


# イントロダクション内の文字列をすべて取得
intro = soup.find_all("div", {"class": "introduction"})
print(intro[0].text)
