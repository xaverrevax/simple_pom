import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestTranslateGerman2Spanish(BaseTest):

    def test_1_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_2_navigate_to_parametrized_url(self):
        scenario_num = 1
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        self.assertTrue(page.navigate_to_parametrized_url(scenario_num))

    def test_3_check_translated_text(self):
        scenario_num = 1
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_translated_text(scenario_num))

    def test_4_lang_switch(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        self.assertTrue(page.click_on_lang_switch_selector())

    def test_5_check_translated_text(self):
        scenario_num = 2
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_translated_text(scenario_num))

    def test_6_clear_input_fields(self):
        print("\n" + str(test_cases(5)))
        page = MainPage(self.driver)
        self.assertTrue(page.clear_input_text_field())

    def test_7_select_input_tool(self):
        print("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        self.assertTrue(page.open_keyboard())

    def test_8_type_word(self):
        scenario_num = 3
        print("\n" + str(test_cases(7)))
        page = MainPage(self.driver)
        self.assertTrue(page.type_word(scenario_num))

    # def test_2_set_source_language(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.set_source_text())
    #
    # def test_3_click_on_target_language_selector(self):
    #     print("\n" + str(test_cases(2)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.click_on_rh_selector())
    #
    # def test_4_set_target_language(self):
    #     print("\n" + str(test_cases(3)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.set_language_in_rh_selector())

    # def test_click_and_set_lh_selector(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.check_click_and_set_lh_selector())

    # def test_click_on_lh_selector(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.check_click_on_lh_selector())
    #
    # def test_set_lh_selector(self):
    #     print("\n" + str(test_cases(2)))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.set_language_in_lh_selector())

    # def test_search_item(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     search_result = page.search_item("iPhone")
    #     self.assertIn("iPhone", search_result)
    #
    # def test_sign_up_button(self):
    #     print("\n" + str(test_cases(2)))
    #     page = MainPage(self.driver)
    #     sign_up_page = page.click_sign_up_button()
    #     self.assertIn("ap/register", sign_up_page.get_url())
    #
    # def test_sign_in_button(self):
    #     print("\n" + str(test_cases(3)))
    #     page = MainPage(self.driver)
    #     login_page = page.click_sign_in_button()
    #     self.assertIn("ap/signin", login_page.get_url())
    #
    # def test_sign_in_with_valid_user(self):
    #     print("\n" + str(test_cases(4)))
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_valid_user("valid_user")
    #     self.assertIn("yourstore/home", result.get_url())
    #
    # def test_sign_in_with_in_valid_user(self):
    #     print("\n" + str(test_cases(5)))
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_in_valid_user("invalid_user")
    #     self.assertIn("There was a problem with your request", result)