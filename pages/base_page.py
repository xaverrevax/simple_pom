from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import yaml
import os
import logging


class BasePage():
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
        self.yaml_content = None
        self.current_path = os.path.dirname(
            os.path.realpath(__file__))
        self.parent_directory = os.path.abspath(
            os.path.join(self.current_path, os.pardir))
        self.configs_directory = os.path.abspath(
            os.path.join(self.parent_directory, 'utils', 'config.yaml'))
        self.load_configuration()

    def short_ts(self):
        return datetime.datetime.utcfromtimestamp(time.time()).strftime('%H%M%S.%f')[:-3]

    def load_configuration(self):

        with open(self.configs_directory, 'r') as stream:
            try:
                self.yaml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)

    def create_screenshot(self, image_text=None):
        if not image_text:
            self.driver.save_screenshot('images/{}_at_the_target.png'.format(self.short_ts()))
        else:
            self.driver.save_screenshot('images/{}_{}.png'.format(self.short_ts(), image_text))

    def find_element(self, *locator):
        self.create_screenshot()
        return self.driver.find_element(*locator)

    def click(self, *locator):
        """ Performs click on web element whose locator is passed to it"""
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator)).click()
        el = self.driver.find_element(by=By.XPATH, value=locator[1])
        self.driver.execute_script("arguments[0].click();", el)
        self.create_screenshot(image_text='click')
        time.sleep(0.5)

    def clear_input_field(self, *locator):
        el = self.driver.find_element(*locator)
        el.clear()

    def find_and_set_text(self, text_content, *locator):
        text_area_el = self.driver.find_element(*locator)
        text_area_el.send_keys(text_content)
        text_area_el.send_keys(Keys.ENTER)
        time.sleep(1)
        self.create_screenshot(image_text='text_set_at_source')

    def click_and_set(self, text_set, **data):
        """ Performs click on web element whose locator is passed to it"""
        click_locator = data.get('click')
        set_locator = data.get('set')
        lh_language = data.get('lh_language')
        lang_input_lh = data.get('lang_input_lh')
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator)).click()
        el = self.driver.find_element(*click_locator)
        self.driver.execute_script("arguments[0].click();", el)
        self.create_screenshot(image_text='after_control_click')
        set_el = self.driver.find_element(*set_locator)
        self.driver.execute_script("arguments[0].value='{}'".format(text_set), set_el)
        self.create_screenshot(image_text='after_set_text')
        lang_input_el = self.driver.find_element(*lang_input_lh)
        lang_input_el.send_keys(Keys.ENTER)
        time.sleep(4)
        self.create_screenshot(image_text='after_set_text')


        # lh_select_el = self.driver.find_element(*lh_language)
        # self.driver.execute_script("arguments[0].click();", lh_select_el)
        # self.create_screenshot(image_text='after_lan_select')
        time.sleep(0.5)

    def get_text_from_element(self, *locator):
        self.create_screenshot(image_text='before_lh_set')


    def get_element(self, *locator):
        self.create_screenshot(image_text='before_lh_set')
        # locator = "(//input[@placeholder='Search languages'])[1]"
        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].value='testuser'", el)
        # self.driver.find_element(by=By.XPATH, value=locator)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator[1])).send_keys(text)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located("(//input[@placeholder='Search languages'])[1]")).send_keys('test')
        return self.driver.find_element(by=By.XPATH, value=locator[1])

