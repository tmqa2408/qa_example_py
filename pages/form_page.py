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
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.MOBILE).send_keys('1234567890')
        self.scroll_down()
        subject = (self.element_is_visible(Locators.SUBJECT))
        subject.send_keys('English')
        subject.send_keys((Keys.RETURN))
        self.scroll_down()
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.GENDER).click()
        self.scroll_down()
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('City, 1234, USA')
        self.scroll_down()
        self.element_is_visible(Locators.SUBMIT).click()
#        self.element_is_visible(Locators.RESULT_TABLE)
        return first_name, last_name, email


    def form_resut(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text