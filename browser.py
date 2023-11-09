# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:39:35 2023

@author: USER
"""
import json
class Browser:
    def __init__(self):
        self.Opened_Tabs={}
        self.error=0
    def jsonReader(self,url):
        output={}
        try:
            with open(url,'r') as file:
                output=json.load(file)
        except :
            try:
                with open('./web/Errors.json','r') as file:
                    output=json.load(file)
            except:
                output={"Error":"Invalid link"}
        return output
    def displayTab(self,tab):
        tab=self.Opened_Tabs[tab]
        for x in tab:
            print(tab[x])
    #O(n) 
    def openTab(self,title,url):
        New_Tab=self.jsonReader(url)
        if title.lower() == New_Tab['title'].lower():
            New_Tab['Tabs']=[]
            self.Opened_Tabs[New_Tab['title']]=New_Tab
            self.displayTab(New_Tab['title'])
        else:
            self.error+=1
            self.Opened_Tabs[f'Error{self.error}']=New_Tab
            self.displayTab(f'Error{self.error}')
