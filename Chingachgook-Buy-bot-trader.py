import requests
import time
from bs4 import BeautifulSoup as BS
import os
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
clear = lambda: os.system('cls') #on Windows System
colorA = lambda: os.system('color a')
color4 = lambda: os.system('color 4')
mouse = mouseController()
keyboard = keyboardController()


clear()
print('Chingachgook - Bot')
print(".....")
GlobalBuyPrice = 0
GlobalMount = 0
GlobalAccountValue = input("Write your balance: ")
print(".....")

iYB = True

if GlobalBuyPrice == "N" or GlobalBuyPrice == "n":
    iYB = False

#region update
def update(mount):
    #update
    mouse.position = (1300,780)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(2)

    #1.
    mouse.position = (750,325)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(1)

    #mount
    mouse.position = (650,425)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    
    with keyboard.pressed(Key.ctrl_l):
        time.sleep(0.1)
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        time.sleep(0.5)
    
    word2 = str(mount)
    mountList = split(word2)
    for i in range (len(mountList)):
        keyboard.press(str(mountList[i]))
        time.sleep(0.5)
        keyboard.release(str(mountList[i]))
        time.sleep(0.5)
    
    #ok
    mouse.position = (550,625)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (775,485)
    time.sleep(7)
    mouse.click(Button.left, 1)
    time.sleep(0.5)

#endregion

#region mainCode
def mainCode(buyPrice, mount, accountValue):
    global GlobalAccountValue
    global GlobalMount
    global GlobalBuyPrice 

    r = requests.get('https://crossoutdb.com/item/864')
    html = BS(r.content, 'html.parser')

    print('Chingachgook - Bot')
    print(".....")
    for el in html.select('div.card.d-inline-flex.flex-column.p-1.px-2.m-2'):
        title = el.select('span')
        if iYB == True:
            if title[0].text == "Buy":
                mainText = title[1].text
                mainText = mainText.replace('\r', '').replace('\n', '')
                mainText = mainText.replace(' ','') 
                print("Current buy is: " + mainText)

                if float(GlobalBuyPrice) < float(mainText):
                    color4()

                    buyPrice = str(float(mainText)+0.01)
                    #mount = int(float(accountValue)/float(buyPrice))
                    mount = 4
                    price_up(buyPrice,mount)

                elif float(GlobalBuyPrice) >= float(mainText):
                    colorA()
                    mount = 4
                    update(mount)
                print('Your Price is: ' + str(buyPrice))
                print('Your Mount is: ' + str(mount))
                print('Global Price is: ' + str(mainText))
                GlobalBuyPrice = buyPrice
                GlobalMount = mount
                GlobalAccountValue = accountValue
#endregion

#region Price up
def price_up(buyPrice,mount):
    mouse = mouseController()
    keyboard = keyboardController()

    #1.
    mouse.position = (750,325)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(1)

    #write a price value
    word1 = str(buyPrice)
    buyPriceList = split(word1)
    i = 0
    for i in range (len(buyPriceList)):
        keyboard.press(str(buyPriceList[i]))
        time.sleep(0.1)
        keyboard.release(str(buyPriceList[i]))
        time.sleep(0.1)

    #mount
    time.sleep(0.5)
    mouse.position = (650,425)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    
    with keyboard.pressed(Key.ctrl_l):
        time.sleep(0.1)
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        time.sleep(0.5)
    
    word2 = str(mount)
    mountList = split(word2)
    for i in range (len(mountList)):
        keyboard.press(str(mountList[i]))
        time.sleep(0.5)
        keyboard.release(str(mountList[i]))
        time.sleep(0.5)

    #ok
    mouse.position = (550,625)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (775,485)
    time.sleep(7)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
#endregion

def split(word): 
    return list(word) 

while True:
    clear()
    mainCode(GlobalBuyPrice, GlobalMount, GlobalAccountValue)
    print(".....")
    time.sleep(60)      