from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import quickstart
import random_password_generator
import requests
import keyboard
import time
from selenium.webdriver.common.keys import Keys

firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/bcgxfdql.default-release'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

def firefox_run(current_url, username):

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(current_url)

    sleep(10)

    # skill_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(skillsInput))
    aaa = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"number\"]")))
    length = len(aaa.get_attribute('value'))
    # aaa.click()
    for i in range(length):
        aaa.send_keys(Keys.BACKSPACE)

    aaa.send_keys(5)
    # sleep(5)
    text_area = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"fr-element fr-view\"]")))

    driver.execute_script("arguments[0].innerHTML = arguments[1];", text_area, username)
    text_area.send_keys(Keys.RETURN)
    text_area.send_keys(Keys.BACKSPACE)

    sleep(2)
    # print(aaa.get_attribute('value'))
    save_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase"]')))
    save_button.click()
    sleep(3)
    driver.quit()