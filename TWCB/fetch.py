# -*- coding: utf-8 -*-
import pandas as pd
import requests
import json
from . import  utils
from bs4 import BeautifulSoup as bs4
import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

#fetch the reference table
def fetch_reference_soup():
    url = 'https://cpx.cbc.gov.tw/Tree/TreeSelect'

    res = requests.session()
    page = res.get(url,verify=False)
    result = res.post('https://cpx.cbc.gov.tw/Tree/GetJsonTreeData')
    soup = bs4(result.text,'lxml')
    return soup

def fetch_reference_table():
    soup = fetch_reference_soup()  
    #making the reference table
    reference_json = eval(json.loads(soup.p.text))[0]
    RetriveNode = utils.RetriveNode()
    RetriveNode.search_end_node(reference_json)
    reference_table = pd.DataFrame({'tb_name':[],'code':[]})
    for end_node in RetriveNode.result.keys():
        tmp_df = pd.DataFrame({'tb_name':[end_node],'code':[RetriveNode.result[end_node]]})
        reference_table = reference_table.append(tmp_df)
    
    #replace the current reference table
    reference_table = reference_table[~(reference_table['code']=='EG3WM01.px')]
    reference_table.to_csv('reference.csv',index=None)
    return reference_table

#fetch the single sheet
def fetch_single_sheet_page(code):
    url = 'https://cpx.cbc.gov.tw/Data/GetJsonFromArray?pxfilename={}'.format(code)
    #get the data json
    data_json = eval(json.loads(requests.get(url,verify=False).text))
    return data_json

def fetch_single_sheet(code):
    data_json = fetch_single_sheet_page(code)

    def fetch_title(data_json):
        num_of_layers = len(data_json['headerSet'])
        title_list = []
        for i in range(num_of_layers):
            tb_list = data_json['headerSet']['Table{}'.format(i+1)]

            if (not title_list):
                title_list = [tb['data'] for tb in tb_list]
            else:
                new_list = []
                for title in title_list:
                    for tb in tb_list:
                        new_title = title + '_' + tb['data']
                        new_list.append(new_title)
                title_list = new_list
        title_list = ['date'] + title_list
        return title_list

    title_list = fetch_title(data_json)
    data = pd.DataFrame(data_json['data'],columns=title_list)
    return data
