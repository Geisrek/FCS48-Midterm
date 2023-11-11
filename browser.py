# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:39:35 2023

@author: USER
"""
import json,os,requests
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
        print(url[:11])
        if (url[:12]=='https://www.' or url[:11]=='http://www.') and '.' in url[12:]:
            New_Tab=self.urlReader(url)
            self.Opened_Tabs[title]={'title':title,'url':url,'content':New_Tab,'Tabs':[]}
            print(self.Opened_Tabs[title]['content'])
        else:
            print("Unvalid linke")
    #O(1)
    def closeTab(self,index=None):
        if len(self.Opened_Tabs) <1:
            return
        elif index==None :
            tab=list(self.Opened_Tabs.keys())
            self.Opened_Tabs.pop(tab[len(tab)-1])
        else:
            tab=list(self.Opened_Tabs.keys())[index]
            self.Opened_Tabs.pop(tab)
    #O(1)
    def swichTab(self,index):
        if index!=None and index>len(self.Opened_Tabs)-1:
            return
        elif index==None :
            tabs=list(self.Opened_Tabs.keys())
            title=tabs[len(tabs)-1]
            tab=self.Opened_Tabs[title]
            print(tab['title'],'\n',tab['content'])
            if 'Tabs' in list(self.Opened_Tabs[title].keys()):
                for x in tab['Tabs']:
                   print(x['title'],'\n',x['content']) 
        else:
            title=list(self.Opened_Tabs.keys())[index]
            tab=self.Opened_Tabs[title]
            print(tab['title'],'\n',tab['content'])
            if 'Tabs' in list(self.Opened_Tabs[title].keys()):
                for x in tab['Tabs']:
                   print(x['title'],'\n',x['content']) 
    #O(n)
    def displayAll(self):
        for x in self.Opened_Tabs:
            print(self.Opened_Tabs[x]['title'])
            if 'Tabs' in list(self.Opened_Tabs[x].keys()):
                Nested_Tabs=self.Opened_Tabs[x]['Tabs']
                for tab in Nested_Tabs:
                    print("--",tab['title'])
    #O(n^2)
    def openNestedTab(self,index):
        if len(self.Opened_Tabs) <1:
            print('No Tabe to nest')
            return
        Parent_Tab=list(self.Opened_Tabs.keys())[index]
        Nested_Tab_Name=input("wich tab you want to open:")
        childe=f'{self.Opened_Tabs[Parent_Tab]["url"]}/{Nested_Tab_Name}'
        content=self.urlReader(childe)
        tab={'title':f'{Nested_Tab_Name}','url':childe,'content':content}
        print(tab)
        self.Opened_Tabs[Parent_Tab]['Tabs'].append(tab)
    #O(1)
    def clareAllTabs(self):
        self.Opened_Tabs={}
    #O(1)
    def saveTabs(self,path):
        Path=f'web/{path}'
        if os.path.exists(Path):
            file_content=self.jsonReader(Path)
            file_content.update(self.Opened_Tabs)
            try:
                with open(Path, 'w') as json_file:
                     json.dump(file_content,json_file, indent=2)
            except:
                print("Some think went wrong :(")
        else:
            try:
                with open(Path, 'w') as json_file:
                     json.dump(self.Opened_Tabs,json_file, indent=2)
            except:
                print("Some think went wrong :(")
    def importTabs(self,path):
        Path=f'web/{path}'
        Tabs=self.jsonReader(Path)
        print(type(Tabs))
        for x in Tabs:
            print(Tabs[x]['title'],'\n',Tabs[x]['url'],'\n',Tabs[x]['content'])
            Nested_Tabs=Tabs[x]['Tabs']
            for tab in Nested_Tabs:
                    print("--",tab['title'],'\n--',tab['url'],'\n--',tab['content'])
browser=Browser()
browser.importTabs('MyTabs.json')