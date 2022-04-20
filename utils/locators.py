from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    lh_select = (By.XPATH,
                 '//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[2]/button[1]/div[3]')
    rh_select = (By.XPATH,
                 '//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[5]/button[1]/div[3]')
    search_language = (By.XPATH,
                       "(//input[@placeholder='Search languages'])[1]")
    search_language_rh = (By.XPATH,
                          "(//input[@placeholder='Search languages'])[2]")
    switch_button = (By.XPATH,
                          "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[3]/div[1]/span[1]/button[1]/div[3]")

    language_selector_lh = (By.XPATH,
                            "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/button[1]/div[3]")
    # search_language = (By.XPATH,
    #                    "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/input[1]")
    # language_selector_lh = (By.XPATH,
    #                         "//div[@xpath='1']")
    lang_input_lh = (By.XPATH,
                     "//div[@data-popup-corner='top-left']/following-sibling::input")
    translated_text = (By.XPATH, "(//span[@data-number-of-phrases='1']//span)[1]")

    text_area_lh = (By.XPATH,
                 "(//span[text()='Dismiss']/following::textarea)[1]")
    language_selector_rh = (By.XPATH,
                            "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[5]/button[1]/div[3]")
    language_keyboard = (By.XPATH,
                            "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[3]/c-wiz[1]/div[4]/div[3]/c-wiz[1]/span[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]")
    letter_H = (By.XPATH,
                    "//span[text()='H']")
    letter_h = (By.XPATH,
                "//span[text()='h']")
    letter_i = (By.XPATH,
                    "//span[text()='i']")
    letter_em = (By.XPATH,
                "//span[text()='!']")
    capital_switch = (By.XPATH,
                    "(//button[@id='K16']//span)[1]")


class TranslatorText(object):
    lh_text = 'Ger'
    rh_text = 'Spanish'
    original_text = "Demokratien"
    target_lang = 'es'
    translate_url = '''http://translate.google.com/#auto/{target_lang}/{original_text}'''


