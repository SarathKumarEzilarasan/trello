import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.action_chains import ActionChains


class BasePageObject:

    CLICK_ELEMENT_SCRIPT = "arguments[0].click()"
    GRAPHITE_GREY_WHEELS = (By.XPATH, "//div[@aria-label='18\" 5-spoke Y-design, graphite grey wheels']")
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)

    def __click_element__(self, clickable_element):
        """
        Executes click event over an element, no matters if it's displayed on the screen or not
        :param clickable_element: element that will be clicked
        :return:
        """
        self.browser.execute_script(self.CLICK_ELEMENT_SCRIPT, clickable_element)

    def __wait_until_visible__(self, seconds, by_tuple):
        """
        Makes browser to wait the number of seconds received by parameter for the element represented by the by_tuple
        :param seconds: seconds to wait
        :param by_tuple: tuple that represents the element we are waiting for. I.e: (By.XPATH, '//div[@id='id']')
        :return:
        """
        return WebDriverWait(self.browser, seconds).until(
            ec.visibility_of_element_located(by_tuple))

    def __wait_until_in_visible__(self, seconds, by_tuple):
        """
        Makes browser to wait the number of seconds received by parameter for the element represented by the by_tuple
        :param seconds: seconds to wait
        :param by_tuple: tuple that represents the element we are waiting for. I.e: (By.XPATH, '//div[@id='id']')
        :return:
        """
        return WebDriverWait(self.browser, seconds).until(
            ec.invisibility_of_element_located(by_tuple))

    def __scroll_to_element_center__(self, element, extra_space=0):
        """
        Try to center the element received by parameter in the middle of the screen
        :param element:
        :param extra_space:
        :return:
        """
        # desired_y = (element.size['height'] / 1) + element.location['y']
        # current_y = (browser.execute_script('return window.innerHeight') / 2) + browser.execute_script(
        #     'return window.pageYOffset')
        # scroll_y_by = desired_y - current_y
        # browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by + extra_space)
        #self.browser.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(2)
        self.actions.move_to_element(element)

