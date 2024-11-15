from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    """для полей (from fields)"""

    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    """созданная форма (created form)"""

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    """чекбоксы """
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-expand-all')
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-collapse-all')
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')

class WebTablePageLocators:
    #add person
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "#age")
    SALARY_INPUT = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchBox")
    SELECT_ROWS = (By.CSS_SELECTOR, "span select")
    SELECT_VALUE_5 = (By.CSS_SELECTOR, "span select [value='5']")
    SELECT_VALUE_10 = (By.CSS_SELECTOR, "span select [value='10']")
    SELECT_VALUE_20 = (By.CSS_SELECTOR, "span select [value='20']")
    SELECT_VALUE_25 = (By.CSS_SELECTOR, "span select [value='25']")
    #table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    PARENT_ROW = ".//ancestor::div[@class='rt-tr-group']"