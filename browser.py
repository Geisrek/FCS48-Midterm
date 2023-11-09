# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:39:35 2023

@author: USER
"""
import json
class Browser:
    def __init__(self):
        self
    def jsonReader(self,url):
        output={}
        try:
            with open(url,'r') as file:
                output=json.load(file)
        except Exception as e:
            output={'Errore':e}
        return output
    def openTab(self,title,url):
        pass
browser=Browser()
print(list(browser.jsonReader('./web/Youtube.json').keys()))