from pages.launch_page import LaunchPage

class LaunchFlow:

    def __init__(self, driver):
        self.launch = LaunchPage(driver)

    def complete_launch(self):
        self.launch.handle_launch()
