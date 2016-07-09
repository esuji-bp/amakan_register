# amakan_register

## description

本を自炊したPDFファイルのバーコード（JANコード）を読み取り、Product Advertising APIに投げることでAmazon.co.jp上でのURLを取得、selenium上でamakanに逐次「読んだ」登録します。

Python3系、ImageMagick、zbarのインストール、Amazon Product Advertising APIの用意が必要です。

このプログラムではAPIに投げた結果からAmazon上のURLのみを取得していますが、一緒に取れるタイトル、著者、出版社名を用いてpdfファイルをリネームしていくものもあります。詳しくは https://github.com/esuji5/yonkoma2data/ を参照してください。

Amazonの購入履歴からamakanに「読んだ」登録できるいかしたプロダクトはこちら https://github.com/amakan/amakankan


## require
### インストール
- install Python3 (3.5推奨) http://www.python.jp/
- install zbar(http://zbar.sourceforge.net/)
- install ImageMagick(http://www.imagemagick.org/script/index.php)
- `$ pip install -r requirement.txt`
- install Firefox(https://www.mozilla.org/ja/firefox/new/)、もしくはseleniumで立ち上げるブラウザをお好みで設定してください

### その他準備
- Amazon Product Advertising API(https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html)に登録
- key_amazon.pyに↑のID、Keyを入力
- amakan_register.pyにamakanのユーザーID/パスワードを入力
- リネームしたいpdfファイル群を入れたディレクトリ


## run
- `$ python pdf_to_amazonurl.py path/to/pdffiles_dir`
- 成功するとamazon_url_list.pickelが作成されます。
- `$ python amakan_register.py`
