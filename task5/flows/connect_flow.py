from pages.home_page import HomePage

class VPNFlow:

    def __init__(self, driver):
        self.home = HomePage(driver)

    def connect_and_handle_dialog(self):
        self.home.connect_vpn()

        result = self.home.wait_for_dialog_or_connection()

        if result == "nothing_happened":
            raise Exception("Neither dialog nor connection detected")
