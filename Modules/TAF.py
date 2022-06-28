# Set the link to the channel to be followed
channel = 'https://www.twitch.tv/rusty_o7'









# # # Code Below # # #

import os, sys
from time import sleep
from easygui import msgbox
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..')

# Creates file for alroady followed accounts
if not os.path.exists(f'./users/{channel.split("/")[-1]}.txt'):
    with open(f'./users/{channel.split("/")[-1]}.txt', 'w') as f:
        f.write('')
        followed = []
else:
    with open(f'./users/{channel.split("/")[-1]}.txt', 'r') as f:
        followed_t = f.readlines()
        followed = []
        for x in followed_t:
            followed.append(x.replace("\n", ""))

from selenium import webdriver
from selenium.webdriver.common.by import By

# function to get the amount of lines in the file
def get_line_count():
    with open('___infolist.txt', 'r') as f:
        lines = f.readlines()
        return len(lines)

def read_name(line):
    with open('___infolist.txt', 'r') as f:
        lines = f.readlines()
        return lines[line]

def follow(amt):
    try: 
        info = read_name(amt)
        if info.split(':')[0] in followed:
            print('Already followed')
            return None
    except: 
        print('No name on that line')
        return None

    driver = webdriver.Firefox(executable_path='./dep/geckodriver.exe')
    driver.install_addon("./dep/adblock.xpi")
    driver.get(channel)

    # Clicks login button
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[2]/div/div[1]/div[1]/button')
            login_xpath = '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[2]/div/div[1]/div[1]/button'
            break
        except:
            try:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button')
                login_xpath = '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button'
                break
            except:
                sleep(1)
    
    driver.find_element(By.XPATH, login_xpath).click()

    # Sleeps
    sleep(2)

    # Does username and password.
    driver.find_element(By.ID, 'login-username').send_keys(info.split(':')[0])
    driver.find_element(By.ID, 'password-input').send_keys(info.split(':')[1])

    # Clicks login button
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button').click()

    # Sleeps
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
            break
        except:
            sleep(1)

    # Clicks remind later
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div/div[3]/div[2]/button').click()

    # Clicks Follow
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button').click()
    except:
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button').click()
        except:
            print('Already following')
            sleep(1)
            driver.quit()
            return None
    # Sleeps
    sleep(1)

    with open(f'./users/{channel.split("/")[-1]}.txt', 'a') as f:
        f.write(info.split(':')[0] + '\n')

    # Exits
    driver.quit()

for i in range(0, get_line_count()):
    follow(i)
