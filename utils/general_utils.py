import os
from constants.browser import SupportedBrowsers
from constants.search_engine import SearchEngines
from datetime import datetime


def user_input():
    """
    Handles user input for browser choice and keyword
    """
    browser_choice = int(input("Enter 1 for Chrome 2 for Firefox\n"))
    if browser_choice not in [1, 2]:
        print("Invalid Selection {}. Aborting...".format(browser_choice))
    elif browser_choice == 1:
        os.environ["BROWSER"] = SupportedBrowsers.chrome
    else:
        os.environ["BROWSER"] = SupportedBrowsers.firefox
    keyword = (input("Enter Keyword to search\n"))
    os.environ["KEYWORD"] = keyword


def get_search_engine_url(search_engine=None):
    """
    Returns search engine url
    """
    url = None
    if search_engine == SearchEngines.google:
        url = SearchEngines.google.value
    elif search_engine == SearchEngines.bing:
        url = SearchEngines.bing.value
    return url


def log_to_console(msg):
    time_now = datetime.now().isoformat().replace("T", " ")
    print(f"INFO {time_now}:--------- {msg}")
