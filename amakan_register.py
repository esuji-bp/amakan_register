# coding: utf-8
# amazonのurlリストをamakanに投げて登録するやつ
# デザイン変更で動かなくなる可能性が高い
from time import sleep

from selenium import webdriver

import utils


amakan_top_url = 'https://amakan.net/'
amakan_login_url = 'https://amakan.net/login'
amakan_product_url = 'https://amakan.net/search?query={}'

email = 'your user_id or email'
password = 'your password'


def login_amakan():
    # ログインページヘ
    driver.get(amakan_login_url)
    # ユーザーIDを入力
    elem = driver.find_element_by_name('name_or_email')
    elem.clear()
    elem.send_keys(email)
    # パスワードを入力
    elem = driver.find_element_by_name('password')
    elem.clear()
    elem.send_keys(password)

    elem.submit()
    # トップページに遷移していたらログイン成功
    if driver.current_url == amakan_top_url:
        return True


def regist_amakan():
    amazon_url_list = utils.pickle_load('amazon_url_list.pickel')

    for url in amazon_url_list[22:]:
        try:
            # 個別ページにアクセス
            driver.get(amakan_product_url.format(url))
            print(driver.find_element_by_css_selector('.card-header').text)

            # 「読んだ」ボタンを取得
            elem = driver.find_element_by_css_selector('.wis-numbers > .waves-effect')

            # 既に「読んだ」がついていたらスキップ
            if 'active' not in elem.get_attribute('class'):
                elem.click()
        except Exception as e:
            # なんか失敗したらとりあえずエラーだけ出しておく
            print(url)
            print(e)

        # 感謝のsleep1秒
        sleep(1)


if __name__ == '__main__':
    # ヘッダーレスの方が良いと思うけど、準備のいらないFirefoxにしておく
    driver = webdriver.Firefox()

    login_flg = login_amakan()
    if login_flg:
        regist_amakan()
