# import urllib.request
# from bs4 import BeautifulSoup


# class Scraper:
#     def __init__(self, site):
#         self.site = site

#     def scrape(self):
#         response = urllib.request.urlopen(self.site)
#         html = response.read()
#         soup = BeautifulSoup(html, 'html.parser')
#         with open("output.txt", "w") as f:
#             for tag in soup.find_all('div', 'keNKEd'):
#                 for atag in tag.find_all('a'):
#                     url = atag.get('href')
#                     if url and 'html' in url:
#                         print("\n" + url)
#                         f.write(url + "\n")


# Scraper('https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja').scrape()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd
import time

# GoogleNewsサイトURL
news_site = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"

# ヘッドレスモードでChromeを起動(JSで作成されたページ対応)
options = Options()
options.add_argument('--headless')
# SeleniumにgoogleDriverを指定して読み込み(インストールしたPathを指定)
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
driver.get(news_site)

time.sleep(1)

html = driver.page_source
# エラーが発生すると裏で起動したChromeがどんどん溜まっていくので、必要なくなったらすぐに終了
driver.quit()

# ページをパース
bs = BeautifulSoup(html, "html.parser")
# Domを「.」でつなげて指定可能ですが'c-wiz'という特別なタグがあるので、途中だけfind()を使用
select_div = bs.main.find('c-wiz').div
#pandas でテーブルにする
columns = ["Name", "Url"]
df1 = pd.DataFrame(columns=columns)  # 列名を指定する

# output.txtに記事を保存
with open("output.txt", "w") as f:
    #ニュースブロックを取得
    for article in select_div.find_all('div'):
        for atag in article.find_all('a'):
            #タグの中身があるものだけ処理
            inner_text = atag.get_text()
            href_string = str(atag.get('href'))
            # aタグの中身があって、リンクに'./articles'が含まれているものを選択(記事以外を排除)
            if inner_text != "" and href_string.find('./articles') != -1:
                # リンクのurlを組み立て('?hl=ja&gl=JP&ceid=JP:ja'を削除して'./'をとったURLと接続)・・・こうしないとニュースサイトに飛ばない
                href = news_site[:-24] + href_string[1:]
                atag_text = "<a href='{}'>{}</a>".format(href, inner_text)
                f.write(atag_text + "\n")
                # pandasでCSV組み立て
                se = pd.Series([inner_text, href], columns) # 行を作成
                df1 = df1.append(se, columns) # データフレームに行を追加
#pandas でCSV出力(index=False で行番号削除)
df1.to_csv("df1.csv",index=False)
