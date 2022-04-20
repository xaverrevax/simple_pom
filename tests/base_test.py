import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')
        options.add_argument('headless')
        options.add_argument('--disable-impl-side-painting')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

