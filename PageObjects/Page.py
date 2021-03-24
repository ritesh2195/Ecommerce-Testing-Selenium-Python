from abc import ABC, abstractmethod

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page(ABC):

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    @abstractmethod
    def getPageTitle(self):
        pass

    @abstractmethod
    def WaitForElementToClickable(self, locator):
        pass

    @abstractmethod
    def WaitForPresenceOfElement(self, locator):
        pass
