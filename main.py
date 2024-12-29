#!/usr/bin/env python3

import os
from utils.driverclass import DriverClass
from utils.general_utils import user_input, log_to_console
from pages.vxg_alerts import AppPage
from settings import APP_URL, PERFORMANCE

"""
Sample Test Scenario

1) Navigate to - http://cloudtwo.cloud-vms.com/customer/alerts
2) Login with Valid Credentials
3) Navigate to Alerts
4) Filter table by site name - Toronto
5) Click on Review
6) Validate GPT response status is True
"""

if __name__ == '__main__':

    log_to_console("Starting Test Automation for VXG Web Client")
    user_input()
    if PERFORMANCE:
        log_to_console("Will be logging Performance metrics".format(APP_URL))
    log_to_console("Opening Browser - {}".format(os.getenv("BROWSER")))
    driver = DriverClass.register_driver(browser=os.getenv("BROWSER"))
    log_to_console("Clearing Browser Cookies")
    driver.delete_all_cookies()
    log_to_console("Navigating to Application URL -{}".format(APP_URL))
    app_page = AppPage(driver)
    app_page.login_to_app()
    log_to_console("Running Test Scenario")
    log_to_console("Filtering by site 'Toronto' and checking if alert is present. ")
    app_page.filter_by_site(site_name='Toronto')
    app_page.sleep_in_seconds(2)
    app_page.review_alert()
    log_to_console("Successfully verified Alert has review status as True")
    app_page.sleep_in_seconds(10)
