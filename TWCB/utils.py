# -*- coding: utf-8 -*-
from collections import OrderedDict
from . import fetch
import pandas as pd

class RetriveNode():
    def __init__(self):
        self.text_path = []
        self.result = OrderedDict()

    def search_end_node(self,tree):
        if isinstance(tree,(list,tuple)): # this is a tree
            for i,subItem in enumerate(tree): # search each "node" for our item
                self.search_end_node(subItem)
                if i == len(tree)-1:
                    self.text_path = self.text_path[:-1]

        elif isinstance(tree,dict): # this is really a node
            try:
                code = tree['pxfilename']
                self.text_path.append(tree['text'].split('(')[0])
                data_title ='_'.join(self.text_path)
                self.result.update({data_title:code})
                self.text_path = self.text_path[:-1]
            
            except:
                NodeName = tree['text']
                self.text_path.append(NodeName)
                subTree = tree['nodes']
                self.search_end_node(subTree)


def get_reference():
    try:
        return pd.read_csv('./reference.csv')
    except:
        return fetch.fetch_reference_table()
        