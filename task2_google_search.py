#!/usr/bin/env python3

import os
from utils.driverclass import DriverClass
from constants.search_engine import SearchEngines
from utils.general_utils import user_input, get_search_engine_url, compare_results
from pages.google import GoogleSearch
from pages.bing import BingSearch


if __name__ == '__main__':

    print("Starting Search Engine Task")
    user_input()
    print("Opening Browser - {}".format(os.getenv("BROWSER")))
    driver = DriverClass.register_driver(browser=os.getenv("BROWSER"))
    print("Clearing Browser Cookies")
    driver.delete_all_cookies()
    print("Navigating to search engine url {}".format(get_search_engine_url(search_engine=SearchEngines.google)))
    home_page = GoogleSearch(driver)
    print("Searching for Keyword {}".format(os.getenv("KEYWORD")))
    home_page.enter_search(keyword=os.getenv("KEYWORD")).parse_search_results()
    #driver.quit()
