from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ExitPage(BasePage):

    EXIT_BUTTON = (
        AppiumBy.ID,
        "com.fast.secure.proxyvpn.unlimitedproxy.security:id/exit_tv_card"
    )

    def exit_app(self):
        if self.is_present(self.EXIT_BUTTON):
            self.click(self.EXIT_BUTTON)
