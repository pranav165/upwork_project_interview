import os
from constants.browser import SupportedBrowsers
from constants.search_engine import SearchEngines


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


def compare_results(result_1: [dict], result_2: [dict]) -> None:
    """
    Compares the two search engine results and prints the common search results
    """
    url_1 = [item['url'] for item in result_1]
    url_2 = [item['url'] for item in result_2]
    print("\n SEARCH RESULTS 1 ARE {} ->".format(url_1))
    print("\n SEARCH RESULTS 2 ARE {} ->".format(url_2))
    if len(result_1) > len(result_2):
        for item1 in result_1:
            for item2 in result_2:
                if item1["url"] == item2["url"]:
                    print("\n\n ***********")
                    print("Common search result found - {}".format(item1["url"]))
                    break
    else:
        for item2 in result_2:
            for item1 in result_1:
                if item1["url"] == item2["url"]:
                    print("\n\n ***********")
                    print("Common search result found - {}".format(item1["url"]))
                    break
