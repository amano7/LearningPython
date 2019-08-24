# スクレイピング

BeautifulSoupを使用します

- BeautifulSoup
  - スクレイピングライブラリ

通常ページならだけで良いですが、Googleの検索結果ページやGoogleNewsなど、JSで作成されたページはレンダリング後のHTMLを拾う必要があるので、下記のツールが必要になります。

- ChromeDriver
  - Chrome を操作するドライバー
- Selenium
  - ブラウザの自動操作を行うツール

PhantomJSを使う方法もありますが、PhantomJSはすでにサポートが終了していますのでChromeDriverを使用します。

## BeautifulSoupのインストール

BeautifulSoupはpipで導入することができます。

```sh
$ pip install --upgrade beautifulsoup4
```

```sh
# ダウンロードしてきたディレクトリに移動
# 以下の場合は、Downloadフォルダにある例です
$ cd ~/Downloads/phantomjs-2.1.1-macosx/

# /usr/local/bin にコピー
$ cp bin/phantomjs /usr/local/bin/
#もしくは~/.bash_profileなどでパスを通すのでも可
```

## ChromeDriver

ChromeDriver は、Google Chromeをヘッドレス(非表示)で起動することができるものです。

余分な処理も走らないので、起動するのも早いです。

ちなみに、オプションを設定しないと、ブラウザが開きます。

指定方法は、コードサンプルを見てください。

[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/) から「ChromeDriver」を選択し、ダウンロードします。

```sh
$ cd ~/Downloads/
$ cp chromedriver /usr/local/bin/
```

**注意：** GoogleChromeのバージョンにあったものをインストールする。(新しいものがいいわけではない)

pip で入れることができそうです。
そちらのほうがかんたんで安全かもしれません。

## Selenimのインストール

Seleniumはpipからインストールすることができます。

```sh
$ pip install --upgrade selenium
```
