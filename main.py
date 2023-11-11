# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:05:04 2023

@author: USER
"""
from browser import Browser
import time
browser=Browser()
def platform():
    text="\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit"
    option=int(input(f"{text}:"))
    if option==1:
        title=input("Enter the title:")
        url=input("Enter the URL:")
        browser.openTab(title, url)
        platform()
    elif option==2:
        index=input("Enter the tab index you want to close:")
        index= int(index) if len(index)>0 else None
        browser.closeTab(index)
        platform()
    elif option==3:
        index=input("Enter the tab index you want to swich:")
        index= int(index) if index !='' else None
        browser.swichTab(index)
        platform()
    elif option==4:
        browser.displayAll()
        platform()
    elif option==5:
        index=int(input('Enter the tab index:'))
        browser.openNestedTab(index)
        platform()
    elif option==6:
        browser.clareAllTabs()
        platform()
    elif option==7:
        path=input('Enter the path :')
        browser.saveTabs(path)
        platform()
    elif option==8:
        path=input('Enter the path :')
        browser.importTabs(path)
        platform()
    elif option==9:
        return
    else:
        print("Unvalid operation please make sure you input a digit in range 0 to 9")
        platform()
def main():
    Reception='Hello Boss'
    Farwell="Good bye"
    for x in Reception:
        print(x,end='')
        time.sleep(0.20)
    
    platform()
    for x in Farwell:
        print(x,end='')
        time.sleep(0.20)
    
main()