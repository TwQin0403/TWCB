# -*- coding: utf-8 -*-
'''
The interface of TWCB api.
'''
from . import fetch
from . import search
from . import utils
import time
import json

def get(code):
    '''
    Input:

    code:str or the list of str, the codes of corresponding tables 

    Output:

    pandas.DataFrame or the list of pandas.DataFrame
    '''
    if isinstance(code,(list,tuple)):
        results = []
        for single_code in code:
            print("Start to process the {}".format(single_code))

            if not isinstance(single_code,(str)):
                raise TypeError("Input Not String")

            if not 'px' in single_code:
                raise TypeError("px not in the string") 

            time.sleep(1)
            try:
                result = fetch.fetch_single_sheet(single_code)
                results.append(result)
            
            except TypeError:
                print("Invalid Code {}".format(code))
        
        return results

    elif isinstance(code,(str)):
        print("Start to process the {}".format(code))

        if not 'px' in code:
            raise TypeError("px not in the string") 

        try:
            return fetch.fetch_single_sheet(code)
        
        except TypeError:
            print("Invalid Code {}".format(code))
    
    else:
        print('Input type exception: Not support type(other than list,tuple or str)')

def get_by_search(keyword):
    code_list = search.search_by_keyword(keyword)
    return get(code_list)

def get_all(filename='download_TWCB.json'):
    result_dict={}
    info = get_info()
    for tb_name,tb_code in zip(info['tb_name'],info['code']):
        time.sleep(1)
        try:
            table = get(tb_code)
            result_dict.update({tb_name:table.to_json()})
        
        except:
            print("Error happens with tb_name:{} with the code:{}".format(tb_name,tb_code))
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result_dict,f)
    

def get_info():
    return utils.get_reference()

def get_reload_reference():
    return fetch.fetch_reference_table()
