from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from tests.page_objects.base_page_object import BasePageObject
from tests.page_objects.locators import HomePageLocators as locators
from tests.page_objects.locators import WorkSpacePageLocators


class HomePage(BasePageObject):

    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element(*locators.USER_TEXT)
        self.loginButton = driver.find_element(*locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.username.send_keys(username)
        self.loginButton.click()
        passwordText = WebDriverWait(self.driver, 15).until(
            ec.invisibility_of_element_located(locators.USER_TEXT))
        self.driver.find_element(*locators.PASSWORD_TEXT).send_keys(password)
        self.driver.find_element(*locators.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located(WorkSpacePageLocators.BOARD))
    