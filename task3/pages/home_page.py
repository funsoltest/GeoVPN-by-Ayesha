from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):

    VPN_TOGGLE_ELEMENTS = [
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/inner_circle_view"),
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/connectionStatus"),
        (AppiumBy.ID, "com.fast.secure.proxyvpn.unlimitedproxy.security:id/vpn_on_off_icon")
    ]

    def tap_vpn_toggle(self):
        for locator in self.VPN_TOGGLE_ELEMENTS:
            if self.is_present(locator):
                self.click(locator)
                return
        raise Exception("VPN toggle not found")
