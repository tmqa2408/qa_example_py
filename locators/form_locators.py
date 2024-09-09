from selenium.webdriver.common.by import By
from random import randint


class FormPageLocators:
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    RESULT_TABLE = (By.XPATH, '//*[@class="table-responsive"]//td[2]')
