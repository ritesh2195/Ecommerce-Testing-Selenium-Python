import time

from PageObjects.HomePage import HomePage
from Utilities.Constants import Constants
from testCases.BaseTest import BaseTest


class Test_002_ContactUs(BaseTest):

    def test_ContactUsTest(self):

        self.homePage = HomePage(self.driver)

        self.homePage.goToURL()

        self.contactUs = self.homePage.goToContactUsPage()

        self.contactUs.chooseSubjectHeading(Constants.SubjectHeading)

        self.contactUs.enterEmailAddress(Constants.Email)

        self.contactUs.enterOrderReference(Constants.OrderReference)

        self.contactUs.enterMessage(Constants.Message)

        self.contactUs.clickSubmit()

        msg = self.contactUs.validateMessage()

        assert 'Your message has been successfully sent to our team' in msg

