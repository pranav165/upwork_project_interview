from pages.common_page import CommonPage
from settings import APP_URL, USERNAME, PASSWORD
from utils.general_utils import time_it


class LoginPage(CommonPage):

    def __init__(self, selenium_driver=None, url=APP_URL):
        super().__init__(selenium_driver=selenium_driver, url=url)

    email = "email"
    password = "password"
    signin = "xpath@@//button[text()='Sign In']"
    alerts = "xpath@@//a[@href='/customer/alerts']"

    # Menu items

    @time_it
    def login_to_app(self):
        self.send_keys(self.email, USERNAME)
        self.send_keys(self.password, PASSWORD)
        self.click(self.signin)
        self.wait_till_element_is_present(self.alerts)
        return self

    @time_it
    def navigate_to_alerts(self):
        self.click(self.alerts)
        self.wait_till_element_is_present(self.alerts)
        return self
