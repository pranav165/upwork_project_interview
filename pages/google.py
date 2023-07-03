from pages.common_search import BaseSearchPage
from utils.general_utils import get_search_engine_url
from constants.search_engine import SearchEngines


class GoogleSearch(BaseSearchPage):
    url = get_search_engine_url(search_engine=SearchEngines.google)

    def __init__(self, selenium_driver=None, url=url):
        super().__init__(selenium_driver=selenium_driver, url=url)

    search_result = "xpath@@//*[@class='g Ww4FFb vt6azd tF2Cxc asEBEc']//*[@class='yuRUbf']"
    loc_title = ".//h3"
    loc_url = "./a"
    loc_description = "./../..//div[@class='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf']"  # this long class name surprisingly seems to be static

    def parse_search_results(self):
        return self._parse_search_results(locator_results=self.search_result, locator_title=self.loc_title,
                                          locator_url=self.loc_url,
                                          locator_description=self.loc_description)
