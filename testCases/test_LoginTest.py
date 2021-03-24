from PageObjects.HomePage import HomePage
from testCases.BaseTest import BaseTest


class Test_01_Login(BaseTest):

    def test_Login(self):

        self.homePage = HomePage(self.driver)

        self.homePage.goToURL()

        self.loginPage = self.homePage.goToLoginPage()

        self.loginPage.doLogin('rrm@gmail.com', 'qwerty')

        li = self.loginPage.verifyLoginTest()

        msg = li.get('login_message')

        name = li.get('UserName')

        assert 'Welcome to your account' in msg

        assert name == 'vinit kumar'

        assert li.get('email') == 'rrm@gmail.com'
