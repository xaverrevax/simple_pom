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

    language_selector_lh = (By.XPATH,
                            "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/button[1]/div[3]")
    # search_language = (By.XPATH,
    #                    "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/input[1]")
    # language_selector_lh = (By.XPATH,
    #                         "//div[@xpath='1']")
    lang_input_lh = (By.XPATH,
                     "//div[@data-popup-corner='top-left']/following-sibling::input")

    text_area_lh = (By.XPATH,
                 "//span[text()='Dismiss']/following::textarea")
    language_selector_rh = (By.XPATH,
                            "//body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[5]/button[1]/div[3]")


class TranslatorText(object):
    lh_text = 'Ger'
    rh_text = 'Spanish'
    original_text = "Demokratien"


