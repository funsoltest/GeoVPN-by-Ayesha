from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Appium server configuration
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"

# Launch an already-installed app
options.app_package = "com.fast.secure.proxyvpn.unlimitedproxy.security"
options.app_activity = "com.example.safevpn.ui.activity.MainActivity"
options.no_reset = True

# Connect to Appium server
print("Connecting to Appium server...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("App launched successfully!")

time.sleep(3)

# Close app
print("Test completed!")
driver.quit()

