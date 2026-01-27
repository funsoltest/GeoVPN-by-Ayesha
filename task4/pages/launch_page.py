from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

class LaunchPage(BasePage):

    ACCEPT_BTN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Accept & Continue")'
    )

    HOME_INDICATOR = (
        AppiumBy.ID,
        "com.fast.secure.proxyvpn.unlimitedproxy.security:id/vpn_on_off_icon"
    )

    def handle_launch(self):
        if self.is_present(self.ACCEPT_BTN, 10):
            self.click(self.ACCEPT_BTN)

        if not self.wait_for(self.HOME_INDICATOR, 20):
            raise Exception("Home screen did not load")
