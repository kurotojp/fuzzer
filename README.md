# fuzzer
Chrome拡張機能のXSSを検知するfuzzer

# 使い方


# 説明
1. server.pyはpythonのhttp.serverでサーバを立ち上げる
1. detect.pyは1とは別ポートでサーバを立ち上げる
1. browser.pyでchromeを立ち上げ、1のサーバにアクセスする(このときにURLにfuzzデータをつける)
1. fuzzデータは1にリクエストを送るようになっているので, detect.pyにリクエストが飛ぶとそのfuzzデータによってXSS脆弱性を検知したとする
1. 3,4を繰り返す


# インストール
* https://www.google.co.jp/chrome/canary/ よりChrome Canaryをダウンロード
```
$ sudo apt install ~/Downloads/google-chrome-stable_current_amd64.deb
```
* https://sites.google.com/a/chromium.org/chromedriver/downloads からChromeのversionにあったDriverを選択し、インストール
* 以下のコマンドでversionは確認できる
```
$ /usr/bin/google-chrome --version
```
* chromedriverはPATHにある必要があるので、適当に移動させる必要がある
* 

```
$ pip3 intsall pwntools==4.2.1
$ pip3 install Flask==1.1.2
$ pip3 install selenium==3.141.0
$ pip3 install language-selector==0.1
$ pip3 install six==1.15.0
$ git clone https://github.com/kurotojp/fuzzer.git
```

