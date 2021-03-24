from selenium.webdriver.support import expected_conditions

from PageObjects.Page import Page


class BasePage(Page):

    def __init__(self, driver):

        super().__init__(driver)

    def getPageTitle(self):
        return self.driver.title

    def WaitForElementToClickable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def WaitForPresenceOfElement(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))
