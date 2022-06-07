from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import Select
from easygui import msgbox


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..')

def generate_username():
    with open('__usernames.txt', 'r') as f:
        lines = f.readlines()
        username = random.choice(lines).strip()
    with open('_usernames_used.txt', 'r') as f:
        if username in f.read():
            return generate_username()
    return username

def generate_password():
    return "".join(random.choice(string.ascii_letters) for i in range(random.randint(12, 20)))

def generate_month():
    return random.randint(1, 12)

def generate_day():
    return random.randint(1, 28)

def generate_year():
    return random.randint(1970, 2001)

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


while True:
    # Start firefox and install extensions
    p_num = random.randint(1, get_proxy.lines(0))
    driver = my_proxy(get_proxy.host(p_num),get_proxy.port(p_num))
    driver.install_addon("./dep/adblock.xpi")

    # Loads webpage
    driver.get("http://www.twitch.tv/")

    # Click sign up
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button').click()

    username = generate_username()
    password = generate_password()
    email = username + "@gmail.com"

    print(username + ":" + password)

    month = generate_month()
    day = generate_day()
    year = generate_year()

    sleep(1)

    # Does username and password.
    driver.find_element(By.ID, 'signup-username').send_keys(username)
    driver.find_element(By.ID, 'password-input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="password-input-confirmation"]').send_keys(password)

    # Does month of birth.
    select = Select(driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select'))
    select.select_by_value(str(month))

    # Does day and year of birth.
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input').send_keys(str(day))
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input').send_keys(str(year))

    # Switches to email
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/button/div').click()

    sleep(0.5)

    # Does email.
    driver.find_element(By.ID, 'email-input').send_keys(email)

    sleep(0.5)

    # Submits form.
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button/div/div').click()

    # Put Somthing Cool Here if you want.
    # Currently the program waits for the user to complete the captcha.

    while True:
        do_quit = False
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
            break
        except:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/strong')
                driver.quit()
                print("Error in sign up")
                do_quit = True
                break
            except:
                sleep(0.1)
    if do_quit:
        break


    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div[2]/button').click()

    with open("___infolist.txt", "a") as f:
        f.write(username + ":" + password + "\n")
    with open("_usernames_used.txt", "a") as f:
        f.write(username + "\n")

    sleep(2)
    driver.quit()

try:
    sleep(10)
except:
    print("Error")