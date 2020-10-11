import requests
import time
from bs4 import BeautifulSoup as BS
import os
clear = lambda: os.system('cls') #on Windows System
colorA = lambda: os.system('color a')
color4 = lambda: os.system('color 4')



clear()
print('Container DIY')
print(".....")
yourBuyPrice = input("Write your buying price: ")
yourSellPrice = input("Write your selling price: ")
print(".....")

iYS = True
iYB = True

if yourBuyPrice == "N" or yourBuyPrice == "n":
    iYB = False
if yourSellPrice == "N" or yourSellPrice == "n":
    iYS = False


def mainCode():
    r = requests.get('https://crossoutdb.com/item/81')
    html = BS(r.content, 'html.parser')

    print('Container DIY')
    print(".....")
    for el in html.select('div.card.d-inline-flex.flex-column.p-1.px-2.m-2'):
        title = el.select('span')
        if iYB == True:
            if title[0].text == "Buy":
                mainText = title[1].text
                mainText = mainText.replace('\r', '').replace('\n', '')
                mainText = mainText.replace(' ','')
                print("Current buy is: " + mainText)

                answer = float(yourBuyPrice) - float(mainText)
                print("Your position is: " + str(answer))
                if float(yourBuyPrice) < float(mainText):
                    print("!!RUN CHANGE!!RUN CHANGE!!")
                    color4()
                elif float(yourBuyPrice) >= float(mainText):
                    print("GOOD")
                    colorA()
            
        if iYS == True:
            if title[0].text == "Sell":
                mainText = title[1].text
                mainText = mainText.replace('\r', '').replace('\n', '')
                mainText = mainText.replace(' ','')
                print("Current sell is: " + mainText)

                answer = float(mainText) - float(yourSellPrice)
                print("Your position is: " + str(answer))
                if float(yourSellPrice) > float(mainText):
                    print("!!RUN CHANGE!!RUN CHANGE!!")
                    color4()

                elif float(yourSellPrice) <= float(mainText):
                    print("GOOD")
                    colorA()

while True:
    clear()
    mainCode()
    print(".....")
    time.sleep(30)      