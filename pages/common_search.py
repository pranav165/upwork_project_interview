from utils.pagebase import PageBase
from utils.general_utils import log_to_console

class BaseSearchPage(PageBase):
    search_input = "name@@q"
    next_page = "xpath@@//a[@aria-label='Page 2']"

    def __init__(self, selenium_driver=None, url=None):
        super().__init__(selenium_driver, url)

    def enter_search(self, keyword: str = None):
        """
        Perform search
        """
        self.send_keys(self.search_input, keyword)
        self.hit_enter(self.search_input)
        return self

    def _parse_search_results(self, locator_results=None, locator_title=None, locator_url=None,
                              locator_description=None):
        """
        Parse for required data
        :param locator_results - Locator to fetch individual tiles of the results
        :param locator_title - Title child of the parent result element
        :param locator_title - anchor tag containing href attribute
        :param locator_description - element representing short desc of the result
        """
        results = self._parse_attributes(locator_results, locator_title, locator_url, locator_description)
        log_to_console("The third search result is  ---->")
        log_to_console(results[2].text)

    def _parse_attributes(self, locator_results=None, locator_title=None, locator_url=None, locator_description=None):
        self.wait_till_element_is_present(locator_results, timeout=10)
        matching_results = self.find_elements(locator_results)
        return matching_results
