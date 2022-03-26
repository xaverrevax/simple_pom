from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        self.text_data = TranslatorText
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.lh_select) else False

    def check_click_and_set_lh_selector(self):
        locators = {'click': self.locator.lh_select,
                    'set': self.locator.search_language,
                    'lh_language': self.locator.language_selector_lh,
                    'lang_input_lh': self.locator.lang_input_lh}
        lh_text = self.text_data.lh_text
        self.click_and_set(lh_text, **locators)
        return True if self.find_element(*self.locator.search_language) else False

    def set_source_text(self):
        original_text = self.text_data.original_text
        self.find_and_set_text(original_text, *self.locator.text_area_lh)
        self.create_screenshot(image_text='set_source_text')
        return True if self.find_element(*self.locator.language_selector_rh) else False

    def click_on_rh_selector(self):
        self.click(*self.locator.language_selector_rh)
        self.create_screenshot(image_text='rh_selector_clicked')
        return True if self.find_element(*self.locator.search_language_rh) else False

    def set_language_in_rh_selector(self):
        el = self.find_element(*self.locator.search_language_rh)
        el.send_keys(self.text_data.rh_text)
        self.create_screenshot(image_text='rh_selector_set_lang')
        return True


