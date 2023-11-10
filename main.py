# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:05:04 2023

@author: USER
"""
from browser import Browser
browser=Browser()
def main():
    text="1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit"
    option=int(input(f"{text}:"))
    if option==1:
        title=input("Enter the title:")
        url=input("Enter the URL:")
        browser.openTab(title, url)
        main()
    elif option==2:
        index=input("Enter the tab index you want to close:")
        index= int(index) if len(index)>0 else None
        browser.closeTab(index)
        main()
    elif option==3:
        index=input("Enter the tab index you want to close:")
        index= int(index) if len(index)>0 else None
        browser.swichTab(index)
        main()
    elif option==4:
        ######
        main()
    elif option==5:
        ######
        main()
    elif option==6:
        ######
        main()
    elif option==7:
        ######
        main()
    elif option==8:
        ######
        main()
    elif option==9:
        return
    else:
        print("Unvalid operation please make sure you input a digit in range 0 to 9")
        main()
    
main()