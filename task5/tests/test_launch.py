import pytest
from flows.launch_flow import LaunchFlow
from flows.connect_flow import VPNFlow
from flows.exit_flow import ExitFlow

@pytest.mark.usefixtures("driver")
class TestVPNJourney:

    def test_full_vpn_journey(self):
        LaunchFlow(self.driver).complete_launch()
        VPNFlow(self.driver).connect_and_handle_dialog()
        ExitFlow(self.driver).exit_from_home()

