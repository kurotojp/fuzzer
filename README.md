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
```
$ pip3 intsall pwntools
$ git clone https://github.com/kurotojp/fuzzer.git
```

