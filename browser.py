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
    #O(1)
    def closeTab(self,index=None):
        if len(self.Opened_Tabs) <1:
            return
        elif index==None or len(self.Opened_Tabs)>1:
            tabs=list(self.Opened_Tabs.keys())
            self.Opened_Tabs.pop(tabs[len(tabs)-1])
        else:
            tab=list(self.Opened_Tabs.keys())[index]
            for x in self.Opened_Tabs:
                if tab in x:
                    self.Opened_Tabs.pop(x)
    #O(n)
    def swichTab(self,index):
        if len(self.Opened_Tabs) <1 or index>len(self.Opened_Tabs)-1:
            return
        elif index==None or len(self.Opened_Tabs)>1:
            tabs=list(self.Opened_Tabs.keys())
            self.displayTab(tabs[len(tabs)-1])
        else:
            tabs=list(self.Opened_Tabs.keys())
            self.displayTab(tabs[index])
    #O(1)
    def displayAll(self):
        for x in self.Opened_Tabs:
            print(self.Opened_Tabs[x]['title'])
            Nested_Tabs=self.Opened_Tabs[x]['Tabs']
            for Y in Nested_Tabs:
                print(Y)
    #O(n^2)
    def openNestedTab(tab,index):
        Parent_Tab=list(self.Opened_Tabs.keys())[index]
        self.Opened_Tabs[Parent_Tab]['Tabs'].append(tab)