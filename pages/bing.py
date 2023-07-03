from pages.common_search import BaseSearchPage
from utils.general_utils import get_search_engine_url
from constants.search_engine import SearchEngines


class BingSearch(BaseSearchPage):
    url = get_search_engine_url(search_engine=SearchEngines.bing)

    def __init__(self, selenium_driver=None, url=url):
        super().__init__(selenium_driver=selenium_driver, url=url)

    search_result = "xpath@@//li[@class='b_algo']"
    loc_title = ".//h2"
    loc_url = ".//h2/a"
    loc_description = ".//p"

    def parse_search_results(self):
        """
        Parse the scraped data into list of dict
        """
        return self._parse_search_results(locator_results=self.search_result, locator_title=self.loc_title,
                                          locator_url=self.loc_url,
                                          locator_description=self.loc_description)
