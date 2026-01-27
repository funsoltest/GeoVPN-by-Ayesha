from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return None

    def is_present(self, locator, timeout=5):
        return self.wait_for(locator, timeout) is not None

    def click(self, locator):
        self.wait_for(locator).click()

    def press_back(self):
        self.driver.execute_script("mobile: pressKey", {"keycode": 4})

    def wait_and_click(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
            ).click()
            return True
        except:
            return False

    
