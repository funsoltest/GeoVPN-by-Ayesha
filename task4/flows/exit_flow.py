from pages.home_page import HomePage
from pages.exit_page import ExitPage

class ExitFlow:

    def __init__(self, driver):
        self.home = HomePage(driver)
        self.exit = ExitPage(driver)

    def exit_from_home(self):
        if not self.home.is_home_screen():
            raise Exception("Not on Home screen")

        self.home.press_back()
        self.exit.exit_app()
