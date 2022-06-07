# Set the link to the channel to be followed
channel = 'http://www.twitch.tv/brawlhalla365'










# # # Code Below # # #
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import random
import string
from selenium.webdriver.support.ui import Select
from easygui import msgbox

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..')

def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    print(PROXY_PORT + ':' + PROXY_HOST)
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",PROXY_HOST)
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("general.useragent.override","whater_useragent")
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp, executable_path='./dep/geckodriver.exe')

class get_proxy:
    def lines(self):
        with open('__proxys.txt', 'r') as f:
            return f.readlines().__len__()
    
    def host(self):
        with open('__proxys.txt', 'r') as f:
            lines = f.readlines()
            host = lines[self].strip()
        return host.split(':')[0]
    
    def port(self):
        with open('__proxys.txt', 'r') as f:
            lines = f.readlines()
            host = lines[self].strip()
        return host.split(':')[1]

amount = int(input('How many views do you want to create? '))

def main(thread_number):
    try:
        p_num = random.randint(1, get_proxy.lines(0))
        driver = my_proxy(get_proxy.host(p_num),get_proxy.port(p_num))
        driver.install_addon("./dep/adblock.xpi")

        # Loads webpage
        driver.get(channel)
    except:
        print('Error in running thread ' + str(thread_number))
        try: driver.quit()
        except: pass

for i in range(amount):
    Thread(target=main, args=(i,), daemon=True).start()

while True:
    sleep(3)
