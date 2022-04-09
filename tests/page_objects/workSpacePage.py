from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.page_objects.base_page_object import BasePageObject
from tests.page_objects.locators import WorkSpacePageLocators as locators


class WorkSpacePage(BasePageObject):

    def __init__(self, driver):
        self.driver = driver

    def mark_card_done(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(locators.MOVE))
        self.driver.find_element(*locators.MOVE).click()
        sel = Select(self.driver.find_element(*locators.LIST_STATUS))
        sel.select_by_index(3)
        self.driver.find_element(*locators.CLOSE_WINDOW).click()

    def add_comment(self):
        board = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(locators.BOARD))
        board.click()
        WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located(locators.COMMENT))
        cards = self.driver.find_elements(*locators.CARD)
        assert len(cards) == 2
        assert self.driver.find_element(*locators.COMMENT).is_displayed()
        cards = self.driver.find_elements(*locators.CARD)
        cards[0].click()
        self.driver.find_element(*locators.ADD_COMMENT).send_keys('test')
        self.driver.find_element(*locators.SAVE_COMMENT).click()
