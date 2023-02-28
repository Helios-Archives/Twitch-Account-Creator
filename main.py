from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from random_username.generate import generate_username
import requests
import random
from time import sleep
from selenium.webdriver.support.ui import Select
import string
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
import os

# Makes sure the program is running in the correct directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def start():
    global driver
    # Start firefox and install extensions
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=GeckoDriverManager().install())
    # driver.get("http://www.whatsmyua.info/")
    driver.install_addon("adblock.xpi")

    # Loads webpage
    driver.get("http://www.twitch.tv/")


def check_name(username):
    r = requests.head("https://passport.twitch.tv/usernames/" + username,
                      headers={'Connection':'close'})
    
    if r.status_code == 403:
        success = False
        while success == False:
            r = requests.head("https://passport.twitch.tv/usernames/" + username,
                              headers={'Connection':'close'})
            if r.status_code != 403:
                success = True
    
    if r.status_code == 200:
        return {'username': username, 'taken': True, 'status_code': r.status_code}
    else:
        return {'username': username, 'taken': False, 'status_code': r.status_code}


def get_username():
    while True:
        username = generate_username(1)[0] + str(random.randint(0, 99))
        if check_name(username)['taken'] == False:
            return username
        else:
            print(f"Username {username} taken, trying again...")
            continue


def get_password():
    # generate a password containing a random 12 characters
    return "".join(random.choice(string.ascii_letters) for i in range(random.randint(12, 20)))


def Sign_up_s1():
    global username, password
    # find the text on the page that says "Sign up"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Sign Up')]]"))).click()

    # find the username field and enter a username
    username = get_username()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "signup-username"))).send_keys(username)

    # find the password field and enter a password
    password = get_password()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password-input"))).send_keys(password)

    # click next
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Next Step')]]"))).click()

    while True:
        try: WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Use email instead')]]"))); return
        except: WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Next Step')]]"))).click()


def Sign_up_s2():
    # find the text on the screen that says "Use email instead"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Use email instead')]]"))).click()

    # find the email field and enter an email
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email-input"))).send_keys(username + "@gmail.com")

    # click next
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Next Step')]]"))).click()

    while True:
        try: WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Date of Birth')]]"))); return
        except: WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Next Step')]]"))).click()


def Sign_up_s3():
    global day, month, year
    # click the month dropdown
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Month')]]"))).click()

    # select a random month and click it
    month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'" + month + "')]]"))).click()

    # click the day dropdown
    day = random.randint(1, 28)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(day).perform()


    # click the year dropdown
    year = random.randint(1990, 2005)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(year).perform()
    

    # get the coordinates of the button with text "Sign Up"
    button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Sign Up')]]")))
    x = button.location['x']
    y = button.location['y']

    # click coordinates of the button
    ActionChains(driver).move_by_offset(x, y).click().perform()
    

def Store_info():
    with open("z_infolist.txt", "a") as f:
        f.write(f"{username}:{password}:{month}/{day}/{year}")


start()
Sign_up_s1()
Sign_up_s2()
Sign_up_s3()
Store_info()

