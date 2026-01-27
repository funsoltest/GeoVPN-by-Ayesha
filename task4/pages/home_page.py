from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):

    VPN_TOGGLE = [
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/inner_circle_view"),
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/connectionStatus"),
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/vpn_on_off_icon")
    ]

    DIALOG_CLOSE = (
        AppiumBy.ID,
        "com.fast.secure.proxyvpn.unlimitedproxy.security:id/close_btn"
    )

    CONNECTED_STATUS = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().textContains("Tap to Disconnect")'
    )

    HOME_INDICATOR = VPN_TOGGLE[1]

    def connect_vpn(self):
        for locator in self.VPN_TOGGLE:
            if self.is_present(locator):
                self.click(locator)
                return
        raise Exception("VPN toggle not found")

    def wait_for_dialog_or_connection(self, timeout=20):
        end_time = time.time() + timeout

        while time.time() < end_time:
            if self.is_present(self.DIALOG_CLOSE, 1):
                self.click(self.DIALOG_CLOSE)
                return "dialog_closed"

            if self.is_present(self.CONNECTED_STATUS, 1):
                return "connected"

        return "nothing_happened"


    def is_home_screen(self):
        return self.is_present(self.HOME_INDICATOR, 5)
