import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.form_locators import FormPageLocators as Locators

class FormPage(BasePage):
    def fill_fields_and_submit(self):
        first_name = 'Hello'
        last_name = 'World'
        email = 'hello@world.com'
 #       self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        time.sleep(1)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        time.sleep(1)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        time.sleep(1)
        self.element_is_visible(Locators.MOBILE).send_keys('1234567890')
        time.sleep(1)
        subject = (self.element_is_visible(Locators.SUBJECT))
        time.sleep(1)
        subject.send_keys('English')
        time.sleep(1)
        subject.send_keys((Keys.RETURN))
        time.sleep(1)
        self.element_is_visible(Locators.HOBBIES).click()
        time.sleep(3)
        self.element_is_visible(Locators.GENDER).click()
        time.sleep(1)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('City, 1234, USA')
        time.sleep(5)
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(5)
#        self.element_is_visible(Locators.RESULT_TABLE)
        return first_name, last_name, email


    def form_resut(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text