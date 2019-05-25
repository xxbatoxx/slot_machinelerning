# coding: UTF-8
from selenium import webdriver
import pandas as pd
import datetime

##レイトギャップ平和島店のHPにアクセスする!
browser = webdriver.Chrome()
today = datetime.date.today()
#browser.get('https://reitoweb.com/b_moba/')
#browser.find_element_by_id('lSearch').click()
#browser.get('https://reitoweb.com/b_moba/doc/news.php?h=2')
#スロットの機種一覧のページ
#browser.get('https://reitoweb.com/b_moba/doc/data.php?h=2&t=29')

#データを格納するリストを作成
keys = ['日付','BB数','最終ゲーム','ART回数','回転数','差枚']

for n in range(1002,1009):
    #まどマギのスロットのページ
    url = 'https://reitoweb.com/b_moba/doc/machine.php?h=2&t=29&m=99119322&n={}'.format(n)
    browser.get(url)
    #１台ずつ情報を取り出してCSVに取り込む(for文で全台分取得したい)
    elem_BB = browser.find_element_by_id('m_BB').text
    #BB回数取得
    elem_last_game = browser.find_element_by_id('m_start').text
    #前日最終ゲーム数取得
    elem_ART = browser.find_element_by_id('m_ART').text
    #ART回数取得
    elem_count = browser.find_element_by_id('m_totalStart').text
    #回転数取得
    elem_put_out = browser.find_element_by_id('m_MY').text
    #差枚の取得

    #取得した値を格納する
    values = []
    _values = []
    _values.append(today)
    _values.append(elem_BB)
    _values.append(elem_last_game)
    _values.append(elem_ART)
    _values.append(elem_count)
    _values.append(elem_put_out)
    values.append(_values)

    if(n==1002):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1002.csv',mode='a',header=False,index=False)

    elif(n==1003):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1003.csv',mode='a',header=False,index=False)

    elif(n==1004):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1004.csv',mode='a',header=False,index=False)

    elif(n==1005):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1005.csv',mode='a',header=False,index=False)

    elif(n==1006):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1006.csv',mode='a',header=False,index=False)

    elif(n==1007):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1007.csv',mode='a',header=False,index=False)

    elif(n==1008):
        #データセットの作成
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSVファイルに書き込み
        df.to_csv('台情報_1008.csv',mode='a',header=False,index=False)

#ブラウザを閉じる
browser.close()
