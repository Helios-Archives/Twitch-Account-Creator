from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from easygui import msgbox


def generate_username():
    with open('usernames.txt', 'r') as f:
        lines = f.readlines()
        username = random.choice(lines).strip()
    with open('used.txt', 'r') as f:
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


# Options
options = Options()
options.headless = False


# Start firefox and install extensions
driver = webdriver.Firefox(options=options)
driver.install_addon("adblock.xpi")

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

# Now the hard part begins.

msgbox("Click ok after you have completed the capcha.")

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]/button').click()
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div[2]/button').click()

with open("infolist.txt", "a") as f:
    f.write(username + ":" + password + "\n")
with open("used.txt", "a") as f:
    f.write(username + "\n")


