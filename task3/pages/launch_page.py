from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LaunchPage(BasePage):

    ACCEPT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Accept & Continue")'
    )

    def accept_terms_if_present(self):
        if self.is_present(self.ACCEPT_BUTTON):
            self.click(self.ACCEPT_BUTTON)
