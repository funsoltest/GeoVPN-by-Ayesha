import pytest
from pages.launch_page import LaunchPage

@pytest.mark.usefixtures("driver")
class TestLaunch:

    def test_accept_terms(self):
        launch = LaunchPage(self.driver)
        launch.accept_terms_if_present()
