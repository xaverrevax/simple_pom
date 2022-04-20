from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from utils.locators import *
import time


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        self.text_data = TranslatorText
        self.translate_url_set = None
        self.config = None
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        self.driver.get("https://translate.google.com/")
        return True if self.find_element(*self.locator.lh_select) else False

    def set_url_parameters(self, scenario_num):
        self.config = self.yaml_content.get('data')[scenario_num].get('scenario')
        target_lang = self.config.get('target_lang')
        translate_url = self.config.get('translate_url')
        original_text = self.config.get('original_text')
        self.translate_url_set = translate_url.format(
            target_lang=target_lang,
            original_text=original_text
        )

    def navigate_to_parametrized_url(self, scenario_num):
        self.set_url_parameters(scenario_num)
        self.driver.get(self.translate_url_set)
        flag = True
        while flag:
            try:
                el = self.find_element(*self.locator.translated_text)
            except NoSuchElementException as err:
                print("exception: {}".format(err))
            else:
                print("from the translator: {}".format(el))
                flag = False
        self.create_screenshot(image_text='translated_text_ready')
        return True if self.find_element(*self.locator.translated_text) else False

    def check_translated_text(self, scenario_num):
        self.set_url_parameters(scenario_num)
        translated_text = self.config.get('translated_text')
        return True if self.find_element(*self.locator.translated_text).text == translated_text else False

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

    def click_on_lang_switch_selector(self):
        self.click(*self.locator.switch_button)
        flag = True
        while flag:
            state = self.driver.execute_script("return document.readyState")
            if state == 'complete':
                flag = False
        self.create_screenshot(image_text='switch_selector_clicked')
        return True if self.find_element(*self.locator.switch_button) else False

    def clear_input_text_field(self):
        self.clear_input_field(*self.locator.text_area_lh)
        self.create_screenshot(image_text='clear_input_fields')
        return True

    def open_keyboard(self):
        self.click(*self.locator.language_keyboard)
        return True if self.find_element(*self.locator.letter_h) else False

    def type_word(self, scenario_num):
        self.set_url_parameters(scenario_num)
        self.click(*self.locator.capital_switch)
        # time.sleep(0.5)
        self.click(*self.locator.letter_H)
        self.click(*self.locator.capital_switch)
        self.click(*self.locator.capital_switch)
        # time.sleep(0.5)
        self.click(*self.locator.letter_i)
        self.click(*self.locator.capital_switch)
        # time.sleep(0.3)
        self.click(*self.locator.letter_em)
        verify_typed_text = self.config.get('verify_typed_text')
        return True if self.find_element(*self.locator.translated_text).text == verify_typed_text else False

    def click_on_rh_selector(self):
        self.click(*self.locator.language_selector_rh)
        self.create_screenshot(image_text='rh_selector_clicked')
        return True if self.find_element(*self.locator.search_language_rh) else False

    def set_language_in_rh_selector(self):
        el = self.find_element(*self.locator.search_language_rh)
        el.send_keys(self.text_data.rh_text)
        self.create_screenshot(image_text='rh_selector_set_lang')
        return True


