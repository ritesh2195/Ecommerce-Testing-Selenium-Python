from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    Email = (By.CSS_SELECTOR, "#email")

    Password = (By.CSS_SELECTOR, "#passwd")

    Submit = (By.CSS_SELECTOR, "#SubmitLogin")

    Message = (By.CSS_SELECTOR, ".info-account")

    UserInfo = (By.CSS_SELECTOR, ".header_user_info a span")

    PersonalInfo = (By.XPATH, "//span[text()='My personal information']")

    LoginEmail = (By.CSS_SELECTOR, "#email")

    def __init__(self, driver):
        super().__init__(driver)

    def doLogin(self, email, password):
        self.driver.find_element(*LoginPage.Email).send_keys(email)

        self.driver.find_element(*LoginPage.Password).send_keys(password)

        self.driver.find_element(*LoginPage.Submit).click()

    def verifyLoginTest(self):
        loginInfo = {}

        self.WaitForPresenceOfElement(self.Message)

        msg = self.driver.find_element(*LoginPage.Message).text

        loginInfo['login_message'] = msg

        name = self.driver.find_element(*LoginPage.UserInfo).text

        loginInfo['UserName'] = name

        self.driver.find_element(*LoginPage.PersonalInfo).click()

        self.WaitForPresenceOfElement(self.LoginEmail)

        mail = self.driver.find_element(*LoginPage.LoginEmail).get_attribute('value')

        loginInfo['email'] = mail

        return loginInfo
