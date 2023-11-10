# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:39:35 2023

@author: USER
"""
import json
import requests
"""response=requests.get('https://www.sefactory.io/')
if response.status_code==200:
    print(response.text[:response.text.find('</title>')])"""
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
    def urlReader(self,url):
        res=requests.get(url)
        if res.status_code==200:
            return res.text
        else:
            return '<h1>Page not found</h1>'
        
    def displayTab(self,tab):
        tab=self.Opened_Tabs[tab]
        for x in tab:
            print(tab[x])
    #O(n) 
    def openTab(self,title,url):
        New_Tab=self.urlReader(url)
        self.Opened_Tabs[title]={'title':title,'content':New_Tab,'Tabs':[]}
        print(self.Opened_Tabs[title]['content'])
    #O(1)
    def closeTab(self,index=None):
        if len(self.Opened_Tabs) <1:
            return
        elif index==None :
            tabs=list(self.Opened_Tabs.keys())
            Removed_item=self.Opened_Tabs.pop(tabs[len(tabs)-1])
            if Removed_item['title'].find('/')!=-1:
               Is_Nested=Removed_item['title'].find('/')
               self.Opened_Tabs[Removed_item['title'][:Is_Nested]]['Tabs'].remove(Removed_item['title'])
        else:
            tab=list(self.Opened_Tabs.keys())[index]
            Removed_item=self.Opened_Tabs[tab]['title']
            self.Opened_Tabs.pop(self.Opened_Tabs[tab])
            for x in self.Opened_Tabs:
                if tab in x:
                    self.Opened_Tabs.pop(x)
                if Removed_item['title'].find('/')!=-1:   
                   Is_Nested=Removed_item['title'].find('/')
                   self.Opened_Tabs[Removed_item['title'][:Is_Nested]]['Tabs'].remove(Removed_item['title'])
    #O(n)
    def swichTab(self,index):
        if len(self.Opened_Tabs) <1 or index>len(self.Opened_Tabs)-1:
            return
        elif index==None or len(self.Opened_Tabs)>1:
            tabs=list(self.Opened_Tabs.keys())
            self.displayTab(tabs[len(tabs)-1])
        else:
            tabs=list(self.Opened_Tabs.keys())
            self.displayTab("--",tabs[index])
    #O(1)
    def displayAll(self):
        for x in self.Opened_Tabs:
            print(self.Opened_Tabs[x]['title'])
            Nested_Tabs=self.Opened_Tabs[x]['Tabs']
            for Y in Nested_Tabs:
                print("--",Y['title'])
    #O(n^2)
    def openNestedTab(self,index):
        if len(self.Opened_Tabs) <1:
            print('No Tabe to nest')
            return
        Parent_Tab=list(self.Opened_Tabs.keys())[index]
        tab=Tab={'title':f'{Parent_Tab}/{input("Enter the title:")}','content':input("Enter content:"),"Tabs":[]}
        print(Parent_Tab)
        self.Opened_Tabs[Parent_Tab]['Tabs'].append(tab['title'])
        self.Opened_Tabs[tab['title']]=tab
    #O(1)
    def clareAllTabs(self):
        self.Opened_Tabs={}
    #O(1)
    