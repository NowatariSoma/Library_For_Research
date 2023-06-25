import pandas as pd
import pyautogui
import time
import pyperclip
from functools import cache

class FUDE:
    def __init__(self):
        self.input_name()
        self.input_place()
        self.data_edit()
        # time.sleep(10)

    @cache
    def input_name(self):
        df = pd.read_csv('u8.csv')
        self.n = len(df)
        self.year = df['year'].values.tolist()
        self.degree = df['degree'].values.tolist()
        self.name = df['name'].values.tolist()
        self.now = df['now'].values.tolist()
        self.home = df['home'].values.tolist()
        self.mail = df['mail'].values.tolist()
        self.phone = df['phone'].values.tolist()
        self.work = df['work'].values.tolist()
        self.kana = df['kana'].values.tolist()
    
    @cache
    def input_place(self):
        df = pd.read_csv("tmpp.txt", sep = ",", header=None)
        place_list = ['name1', 'name2', 'now1', 'now2', 'now3', 'home', 'mail', 'phone', 'work']
        place_value = df.values.tolist()
        self.dict = dict(zip(place_list, place_value))

    @cache
    def data_edit(self):
        for i in range(self.n):
            if str(self.now[i]) == "nan" and str(self.home[i]) != "nan":
                self.now[i], self.home[i] = self.home[i], self.now[i]
    
    def w_kana(self, person):
        if str(self.kana[person]) != "nan":
            self.click_write_word([475.0, 172.0], str(self.kana[person]))
            time.sleep(0.5)

    def w_memo(self, person):
        self.click_write_word([868.0, 182.0], str(self.year[person]))
        if str(self.degree[person]) != "nan":
            self.paste_word("_"+str(self.degree[person]))
            time.sleep(0.5)

    def w_work(self, person):
        if str(self.work[person]) != "nan":
            print(self.work[person])
            self.click_write_word([472.0, 953.0], str(self.work[person]))
            time.sleep(0.5)

    def w_mail(self, person):
        if str(self.mail[person]) != "nan":
            print(self.mail[person])
            self.click_write_word([447.0, 577.0], str(self.mail[person]))
            time.sleep(0.5)

    def w_phone(self, person):
        if str(self.phone[person]) != "nan":
            print(self.phone[person])
            self.click_write_word([445.0, 631.0], str(self.phone[person]))
            time.sleep(0.5)

    def w_name(self, person):
        time.sleep(1)
        self.click_write_word(self.dict['name1'], self.name[person].split()[0])
        self.click_write_word(self.dict['name2'], self.name[person].split()[1])
        time.sleep(0.5)

    def w_address(self, person):
        if str(self.now[person]) != "nan":
            self.click_write_word([441.0, 471.0], str(self.now[person]).split()[0][0:7])
            self.click_write_word([449.0, 489.0], str(self.now[person]).split()[0][8:])
            if len(self.now[person].split()) > 1: 
                self.click_write_word([453.0, 506.0], str(self.now[person]).split()[1])
            if len(self.now[person].split()) > 2: 
                self.click_write_word([448.0, 531.0], str(self.now[person]).split()[2])
            time.sleep(0.5)

    def w_address_2(self, person):
        # print(self.home[person].split())
        if str(self.home[person]) != "nan":
            pyautogui.moveTo(772.0, 185.0)
            pyautogui.dragTo(774.0, 1018.0, button='left')
            pyautogui.click(609.0, 709.0)
            time.sleep(1)
            self.paste_word("実家住所")
            pyautogui.hotkey('tab')
            time.sleep(0.5)
            self.paste_word(self.home[person].split()[0][0:7])
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            time.sleep(0.5)
            self.paste_word(self.home[person].split()[0][8:])
            pyautogui.hotkey('tab')
            time.sleep(0.5)
            self.paste_word(self.home[person].split()[1])
            pyautogui.hotkey('tab')
            time.sleep(0.5)
            if len(self.home[person].split()) > 2:    
                self.paste_word(self.home[person].split()[2])
            pyautogui.click(x = 1529.0, y = 501.0)
            pyautogui.moveTo(772.0, 1018.0)
            pyautogui.dragTo(774.0, 185.0, button='left')
            time.sleep(0.5)
        
    def paste_word(self, word):
        pyperclip.copy(word)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

    def click_write_word(self, locate, word):
        pyautogui.moveTo(locate[0],locate[1])
        pyautogui.click()
        time.sleep(0.5)
        self.paste_word(word)

    def new_person(self):
        pyautogui.click(x = 134.0, y = 318.0)