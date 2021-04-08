from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.LoginPage import LoginPage
from Utilities.ConfigReader import configReader


class HomePage(BasePage):

    __LoginButton = (By.CSS_SELECTOR, ".login")

    __ContactUs = (By.XPATH, "//a[text()='Contact us']")

    def __init__(self, driver):

        super().__init__(driver)

    def goToURL(self):

        self.driver.get(configReader.getURL())

    def goToLoginPage(self):

        self.WaitForElementToClickable(self.__LoginButton)

        self.driver.find_element(*HomePage.__LoginButton).click()

        return LoginPage(self.driver)

    def goToContactUsPage(self):

        self.driver.find_element(*HomePage.__ContactUs).click()

        return ContactUsPage(self.driver)
