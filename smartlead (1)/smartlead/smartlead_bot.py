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
import getpass

# pwd = getpass.getpass("Enter password: ")

# if pwd == "run homedepot materials bot":
#     pass
# else:
#     while(True):
#         print("Incorrect password")
#         sleep(10)

# firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/bcgxfdql.default-release'
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

# driver = webdriver.Firefox(options=firefox_options)
# driver.maximize_window()
# driver.get("https://app.smartlead.ai/")
quickstart.main()
column_count = quickstart.getColumnCount()
email_list = quickstart.getEmailList()
password_list = quickstart.getPasswordList()
print(email_list)
print(password_list)

LOGIN_EMAIL = "carson@spitzsolutions.com"
LOGIN_PWD = "n^Qm3fctOiZcbD3c"

MESSAGE_PER_DAY = 30
MINIMUM_TIME_GAP = 5
# REPLY_TO_ADDRESS = "i dont even need one"

index = 0

while(index < column_count):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app.smartlead.ai/")

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")))

        login_elements = driver.find_elements(By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")
        login_elements[0].send_keys(LOGIN_EMAIL)
        login_elements[1].send_keys(LOGIN_PWD)

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase full-width\"]"))).click()
        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable flex items-center no-wrap app-project-route\"]")))

        email_accounts_element = driver.find_elements(By.CSS_SELECTOR, "a[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable flex items-center no-wrap app-project-route\"]")[1]
        email_accounts_element.click()

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase q-ml-md\"]"))).click()

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable email-connect-card\"]")))

        select_email_provider = driver.find_elements(By.CSS_SELECTOR, "div[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable email-connect-card\"]")[2]
        select_email_provider.click()

        email_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-report-event=\"Signin_Email_Phone_Skype\"]")))
        email_input.send_keys(email_list[index])

        next_button = driver.find_element(By.CSS_SELECTOR, "input[data-report-event=\"Signin_Submit\"]")
        next_button.click()

        password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
        password_input.send_keys(password_list[index])

        next_button = driver.find_element(By.CSS_SELECTOR, "input[data-report-event=\"Signin_Submit\"]")
        next_button.click()

        # new_pwd = random_password_generator.getRandomPassword()

        # current_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"currentPassword\"]")))
        # new_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"newPassword\"]")))
        # confirm_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"confirmNewPassword\"]")))

        # current_password_input.send_keys(password_list[index])
        # new_password_input.send_keys(new_pwd)
        # confirm_password_input.send_keys(new_pwd)

        # next_button = driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]")
        # next_button.click()
        sleep(5)
        try:
            accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"idSIButton9\"]")))
            accept_button.click()
        except:
            later_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"btnAskLater\"]")))
            later_button.click()
            # sleep(3)
            accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"idSIButton9\"]")))
            accept_button.click()

        sleep(5)

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle text-primary q-btn--actionable q-focusable q-hoverable\"]"))).click()
        
        sleep(10)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"number\"]")))

        username = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4[class=\"email-account-text\"]"))).text
        # print(username)
        correct_username = username.split("(")[0].strip()
        print(correct_username)
        

        input_count = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"number\"]")))

        input_day_elements = driver.find_elements(By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")
        
        # driver.execute_script(f'document.querySelectorAll("input.q-field__native.q-placeholder]")[0].value = "{MESSAGE_PER_DAY}";')
        # for _ in range(14):
        #     keyboard.press('tab')
        #     keyboard.release('tab')
        # keyboard.write(MESSAGE_PER_DAY)
        # for _ in range(3):
        #     keyboard.press('tab')
        #     keyboard.release('tab')
        #     keyboard.write(correct_username)
        # keyboard.press('tab')
        # keyboard.release('tab')
        # input_day_elements[0].clear()
        length = len(input_day_elements[0].get_attribute('value'))
        for i in range(length):
            input_count.send_keys(Keys.BACKSPACE)

        input_day_elements[0].send_keys(MESSAGE_PER_DAY)
        input_day_elements[1].clear()
        input_day_elements[1].send_keys(MINIMUM_TIME_GAP)

        text_area = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"fr-element fr-view\"]")))
        driver.execute_script("arguments[0].innerHTML = arguments[1];", text_area, correct_username)
        text_area.send_keys(Keys.RETURN)
        text_area.send_keys(Keys.BACKSPACE)

        sleep(2)

        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-checkbox__bg absolute\"]")))
        checkbox_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"q-checkbox__bg absolute\"]")
        checkbox_elements[0].click()

        
        # reply_to_address_element = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"q-field__input q-placeholder col\"]")))
        # reply_to_address_element.send_keys(REPLY_TO_ADDRESS)

        # ind = False
        # while(ind == False):
        #     replyInput = (By.CSS_SELECTOR, "input[class=\"q-field__input q-placeholder col\"]")
        #     reply_to_address_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(replyInput))
        #     try:
        #         reply_to_address_element.click()
        #         reply_to_address_element.clear()
        #         reply_to_address_element.send_keys(REPLY_TO_ADDRESS)
        #         reply_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item__section column q-item__section--main justify-center\"]")))
        #         reply_dropdown.click()
        #         ind = True
        #     except:
        #         # If the element becomes stale, re-locate it and try again
        #         try:
        #             reply_to_address_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(replyInput))
        #             reply_to_address_element.click()
        #             reply_to_address_element.clear()
        #             reply_to_address_element.send_keys(REPLY_TO_ADDRESS)
        #             reply_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item__section column q-item__section--main justify-center\"]")))
        #             reply_dropdown.click()
        #             ind = True
        #         except: pass

        
        sleep(2)
        # signature_field_parent = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"fr-element fr-view\"]")))
        # signature_field = signature_field_parent.find_element(By.CSS_SELECTOR, ":first-child")
        
        # driver.execute_script("arguments[0].innerText = arguments[1];", signature_field, correct_username)
        # sleep(3)
        save_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase"]')))
        # save_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase\"]")
        save_button.click()
        sleep(3)
        # sleep(1000)
        current_url = driver.current_url
        driver.quit()
        sleep(3)
        # test.firefox_run(current_url, correct_username)

    except:
        pass
    index += 1