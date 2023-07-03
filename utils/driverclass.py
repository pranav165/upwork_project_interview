from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from constants.browser import SupportedBrowsers
from settings import IMPLICIT_WAIT


# INITIALIZING WEB DRIVER INSTANCE

class DriverClass:
    @staticmethod
    def register_driver(browser=None):
        """
        Returns driver object for a browser type
        """
        return DriverClass._get_web_driver(browser=browser)

    def _get_web_driver(browser=None):
        """
        Sets capabilities and return browser object
        """
        if browser == SupportedBrowsers.chrome:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # Using webdriver manager utitlity to auto detect and select correct web driver exe
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        elif browser == SupportedBrowsers.firefox:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Browser {} Not yet supported".format(browser))
        driver.implicitly_wait(IMPLICIT_WAIT)
        return driver
