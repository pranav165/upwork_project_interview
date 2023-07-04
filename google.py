#!/usr/bin/env python3

import os
from utils.driverclass import DriverClass
from constants.search_engine import SearchEngines
from utils.general_utils import user_input, get_search_engine_url, log_to_console
from pages.google import GoogleSearch


if __name__ == '__main__':

    log_to_console("Starting Search Engine Task")
    user_input()
    log_to_console("Opening Browser - {}".format(os.getenv("BROWSER")))
    driver = DriverClass.register_driver(browser=os.getenv("BROWSER"))
    log_to_console("Clearing Browser Cookies")
    driver.delete_all_cookies()
    log_to_console("Navigating to search engine url {}".format(get_search_engine_url(search_engine=SearchEngines.google)))
    home_page = GoogleSearch(driver)
    log_to_console("Searching for Keyword {}".format(os.getenv("KEYWORD")))
    home_page.enter_search(keyword=os.getenv("KEYWORD")).parse_search_results()
    driver.quit()
