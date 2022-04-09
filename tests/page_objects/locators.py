from selenium.webdriver.common.by import By


class HomePageLocators:
    USER_TEXT = (By.ID, "user")
    LOGIN_BUTTON = (By.ID, "login")
    SUBMIT_BUTTON = (By.ID, "login-submit")
    PASSWORD_TEXT = (By.ID, "password")


class WorkSpacePageLocators:
    BOARD = (By.CSS_SELECTOR, "[class='board-tile']")
    CARD = (By.CSS_SELECTOR, '[class="list-card-details js-card-details"]')
    COMMENT = (By.CSS_SELECTOR, '[title="Comments"]')
    ADD_COMMENT = (By.CSS_SELECTOR, '[aria-label="Write a comment"]')
    SAVE_COMMENT = (By.CSS_SELECTOR, '[class$="js-add-comment"]')
    MOVE = (By.CSS_SELECTOR, '[title="Move"]')
    LIST_STATUS = (By.CSS_SELECTOR, '[class="js-select-list"]') #VISIBLE TEXT - Done
    CLOSE_WINDOW = (By.CSS_SELECTOR, '[class$="js-close-window"]')




# https://trello.com/sarathkumarsworkspace8
