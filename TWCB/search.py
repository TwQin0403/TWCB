# -*- coding: utf-8 -*-
import pandas as pd
from . import utils
from . import fetch

try:
    reference = pd.read_csv('reference.csv')

except:
    reference = fetch.fetch_reference_table()


def search_by_keyword(keyword):
    reference = utils.get_reference()
    reference_dict = {tb_name:code for tb_name,code in zip(reference['tb_name'],reference['code'])}
    tb_name_list = []
    for key,value in reference_dict.items():
        if keyword in key:
            print('In the table name {} with code {}'.format(key,value))
            tb_name_list.append(value)
    return tb_name_list