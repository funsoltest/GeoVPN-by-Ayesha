from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

class ExitPage(BasePage):

    EXIT_BUTTON = [
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/exit_tv_card"),
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/card_exit"),
        (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Exit\")")
    ]

    def exit_app(self):
        for locator in self.EXIT_BUTTON:
            if self.is_present(locator):
                self.click(locator)
                return
        raise Exception("Exit not found")
