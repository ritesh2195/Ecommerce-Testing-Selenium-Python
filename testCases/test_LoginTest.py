from PageObjects.HomePage import HomePage
from Utilities.DataProvider import getData
from testCases.BaseTest import BaseTest
import pytest


class Test_01_Login(BaseTest):

    @pytest.mark.parametrize("email, password", getData())
    def test_Login(self, email, password):

        self.homePage = HomePage(self.driver)

        self.homePage.goToURL()

        self.loginPage = self.homePage.goToLoginPage()

        self.loginPage.doLogin(email, password)

        li = self.loginPage.verifyLoginTest()

        msg = li.get('login_message')

        name = li.get('UserName')

        assert 'Welcome to your account' in msg

        assert name == 'vinit kumar'

        assert li.get('email') == 'rrm@gmail.com'
