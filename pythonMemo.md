# Pythonメモ

- コメントは、#
- ブロックは、:とインデント
- インデントはスペース4個
- 長い文字列(改行含む)は、"""、()、{}、などでかける  
    () {} 
- forの書き方

    ```py
    for i in range(100):
        ブロック
    ```

- 型宣言は基本なし

    ```py
    - b: int = 20
    ```

    とかで明示的に指定することも可
- インクリメント(i++など)は使えない
- 代入時に -=、+= は使用可能
- 変数名に記号は使えない(_は使える)
- 14%4 は、2になり、14//4 は3になる
- 型はtype()で調べられる
- 比較演算子は他と同じ
- 論理演算子は、&&(||)とかじゃなく and (or) で記述
- if文もブロックは:とインデント、条件は()なし
- elseはelse、elseifは、elif
- elseにも:がいる
- ifとかforなどの:で終わる行を「ヘッタ」といい、その下にインデントした行をスイートと言う
- 定数はない。ただし 2 とかは値が2のオブジェクトと言えるので、生の値が定数と言えなくもない
- 定数の代わりに変数を使用して表記する。慣習的に大文字とアンダーバーで表現される様子
- 関数定義はdef。 functionとかはない。
- 関数にretuenがなければ、noneが返る。
- len() 文字列の長さを返す。
- str()、int()、float()などはその型に変換して返す。
- 型変換ができない場合、エラーになる(int("aaa")は0じゃない)
- 代入された値が文字列か判定(intか判定)

    ```py
    if type(x) != int:
        return 0
    ```

- 関数外の変数はグローバル
- 関数内でグローバル変数に書き込むときは、global で明示的に定義。
- 例外処理は、try catch ではなく、try except
- except にはどんな例外を取るか指定可能
- 関数の仕様を表すコメントなどをdocstringといい、「'''」から「'''」までをコメントとして扱える。

## コンテナ

- 文字列はオブジェクト

    ```py
    "Hello".upper()
    ```
    上記で大文字変換。
- リスト

    ```py
    fruit = list()
    または
    fruet = []
    ```

## try

上では、continue がないと if でエラーになる

try で失敗すると、何も実行されていない状態になるため

```py
a = [0, 2, 6, 7]

while True:
  i = input("Number? ( quit = q ) :")
  if i == "q":
    break
  try:
    answer = int(i)
  except ValueError:
    print("数字を入れてください!")
    continue
  if answer in a:
    print("あたり! ")
  else:
    print("はずれ!")```

```py
a = [0, 2, 6, 7]

while True:
i = input("Number? ( quit = q ) :")
if i == "q":
  break
try:
  i = int(i)
except ValueError:
  print("数字を入れてください!")
if i in a:
  print("あたり! ")
else:
  print("はずれ!")
```

## スクレイピング

通常ページなら良いが、JSで作成されたページは、JSでレンダリング後のHTMLを拾う必要があるので、下記のツールが必要です。

- BeautifulSoup
  - スクレイピングライブラリ
- ~~PhantomJS~~
  - ~~ヘッドレスブラウザ~~
- ChromeDriver
  - Chrome を操作するドライバー
- Selenium
  - ブラウザの自動操作を行うツール

PhantomJSを使ってHTMLの取得からJavascriptの実行を行い、その結果をBeautifulSoupに渡すことでスクレイピングを行います。Seleniumは、PhantomJSの制御に利用します。

### BeautifulSoupのインストール

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

### ChromeDriver

[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/) から「ChromeDriver」を選択し、ダウンロードします。

```sh
$ cd ~/Downloads/
$ cp chromedriver /usr/local/bin/
```

注意：GoogleChromeのバージョンにあったものをインストールする。(新しいものがいいわけではない)

### Selenimのインストール

Seleniumはpipからインストールすることができます。

```sh
$ pip install --upgrade selenium
```

### ~~PhantomJSのインストール~~

~~PhantomJSは以下のサイトから実行ファイルをダウンロードして、そのファイルにパスを通すことで動かせるようにします。~~

- ~~[http://phantomjs.org/](http://phantomjs.org/)~~

~~ダウンロードしてきたファイルを、例えば以下のようにすることで、パスを通すことができます。~~
