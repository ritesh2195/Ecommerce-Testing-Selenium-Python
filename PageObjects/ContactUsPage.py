from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.BasePage import BasePage


class ContactUsPage(BasePage):
    __SubjectHeading = (By.CSS_SELECTOR, "#id_contact")

    __Email = (By.CSS_SELECTOR, "#email")

    __OrderReference = (By.CSS_SELECTOR, "#id_order")

    __Message = (By.CSS_SELECTOR, "#message")

    __Submit = (By.CSS_SELECTOR, "#submitMessage")

    __ValidationMessage = (By.CSS_SELECTOR, '.alert.alert-success')

    def __init__(self, driver):
        super().__init__(driver)

    def chooseSubjectHeading(self, heading):

        element = self.driver.find_element(*ContactUsPage.__SubjectHeading)

        select = Select(element)

        select.select_by_visible_text(heading)

    def enterEmailAddress(self, email):

        self.driver.find_element(*ContactUsPage.__Email).send_keys(email)

    def enterOrderReference(self, orderReference):

        self.driver.find_element(*ContactUsPage.__OrderReference).send_keys(orderReference)

    def enterMessage(self, message):

        self.driver.find_element(*ContactUsPage.__Message).send_keys(message)

    def clickSubmit(self):

        self.driver.find_element(*ContactUsPage.__Submit).click()

    def validateMessage(self):

        return self.driver.find_element(*ContactUsPage.__ValidationMessage).text
