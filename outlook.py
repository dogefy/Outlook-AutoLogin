from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = EdgeOptions()
s = Service(executable_path=r'')  # webdriver path
browser = webdriver.Edge(service=s, options=options)


def login():
    browser.get('https://outlook.live.com/owa/logoff.owa')
    browser.get('https://login.live.com/login.srf')

    # username
    username = browser.find_element(By.XPATH, "//input[@id='i0116']")
    username.clear()
    username.send_keys(r'')  # *****@outlook.com

    next_button = browser.find_element(By.ID, 'idSIButton9')
    next_button.click()
    time.sleep(3)

    # password
    browser.execute_script("document.getElementById('i0118').setAttribute('class', 'form-control')")
    password = browser.find_element(By.XPATH, "//input[@id='i0118']")
    password.clear()
    password.send_keys(r'')  # password

    browser.execute_script("document.getElementById('idSIButton9').disabled=false")
    signin_button = browser.find_element(By.ID, 'idSIButton9')
    signin_button.click()

    refuse_button = browser.find_element(By.ID, 'idBtn_Back')
    refuse_button.click()

    browser.get(r'https://outlook.live.com/mail/0/')


if __name__ == '__main__':
    login()
