import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="class")
def driver(request):
    """Setup Appium driver for Android."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.fast.secure.proxyvpn.unlimitedproxy.security"
    options.app_activity = "com.example.safevpn.ui.activity.MainActivity"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    request.cls.driver = driver
    yield driver  # Test runs here
    driver.quit()  # Clean teardown
