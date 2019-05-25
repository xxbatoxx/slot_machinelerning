# coding: UTF-8
from selenium import webdriver
import pandas as pd
import datetime

##���C�g�M���b�v���a���X��HP�ɃA�N�Z�X����
browser = webdriver.Chrome()
today = datetime.date.today()
#browser.get('https://reitoweb.com/b_moba/')
#browser.find_element_by_id('lSearch').click()
#browser.get('https://reitoweb.com/b_moba/doc/news.php?h=2')
#�X���b�g�̋@��ꗗ�̃y�[�W
#browser.get('https://reitoweb.com/b_moba/doc/data.php?h=2&t=29')

#�f�[�^���i�[���郊�X�g���쐬

for n in range(1002,1009):
    #�܂ǃ}�M�̃X���b�g�̃y�[�W
    url = 'https://reitoweb.com/b_moba/doc/machine.php?h=2&t=29&m=99119322&n={}'.format(n)
    browser.get(url)
    #�P�䂸�������o����CSV�Ɏ�荞��(for���őS�䕪�擾������)
    elem_BB = browser.find_element_by_id('m_BB').text
    #BB�񐔎擾
    elem_last_game = browser.find_element_by_id('m_start').text
    #�O���ŏI�Q�[�����擾
    elem_ART = browser.find_element_by_id('m_ART').text
    #ART�񐔎擾
    elem_count = browser.find_element_by_id('m_totalStart').text
    #��]���擾
    elem_put_out = browser.find_element_by_id('m_MY').text
    #�����̎擾

    #�擾�����l���i�[����
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
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1002.csv',mode='a',header=False,index=False)

    elif(n==1003):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1003.csv',mode='a',header=False,index=False)

    elif(n==1004):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1004.csv',mode='a',header=False,index=False)

    elif(n==1005):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1005.csv',mode='a',header=False,index=False)

    elif(n==1006):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1006.csv',mode='a',header=False,index=False)

    elif(n==1007):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1007.csv',mode='a',header=False,index=False)

    elif(n==1008):
        #�f�[�^�Z�b�g�̍쐬
        df = pd.DataFrame(values)
        #df.columns = keys
        #CSV�t�@�C���ɏ�������
        df.to_csv('����_1008.csv',mode='a',header=False,index=False)

#�u���E�U�����
browser.close()
