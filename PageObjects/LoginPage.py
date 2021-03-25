from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    __Email = (By.CSS_SELECTOR, "#email")

    __Password = (By.CSS_SELECTOR, "#passwd")

    __Submit = (By.CSS_SELECTOR, "#SubmitLogin")

    __Message = (By.CSS_SELECTOR, ".info-account")

    __UserInfo = (By.CSS_SELECTOR, ".header_user_info a span")

    PersonalInfo = (By.XPATH, "//span[text()='My personal information']")

    LoginEmail = (By.CSS_SELECTOR, "#email")

    def __init__(self, driver):
        super().__init__(driver)

    def doLogin(self, email, password):
        self.driver.find_element(*LoginPage.__Email).send_keys(email)

        self.driver.find_element(*LoginPage.__Password).send_keys(password)

        self.driver.find_element(*LoginPage.__Submit).click()

    def verifyLoginTest(self):
        loginInfo = {}

        self.WaitForPresenceOfElement(self.__Message)

        msg = self.driver.find_element(*LoginPage.__Message).text

        loginInfo['login_message'] = msg

        name = self.driver.find_element(*LoginPage.__UserInfo).text

        loginInfo['UserName'] = name

        self.driver.find_element(*LoginPage.PersonalInfo).click()

        self.WaitForPresenceOfElement(self.LoginEmail)

        mail = self.driver.find_element(*LoginPage.LoginEmail).get_attribute('value')

        loginInfo['email'] = mail

        return loginInfo
