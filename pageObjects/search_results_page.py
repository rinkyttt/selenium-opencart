from selenium.webdriver.common.by import By
from base.base_page import BasePage

class SearchResultsPage(BasePage):
    # Locators
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-layout")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-thumb h4 a")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_search_results_count(self):
        """Get the number of products found"""
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return len(products)
    
    def get_product_names(self):
        """Get list of product names from search results"""
        return [element.text for element in self.driver.find_elements(*self.PRODUCT_NAMES)]
    
    def sort_results(self, sort_option):
        """Sort the search results"""
        self.click(self.SORT_DROPDOWN)
        sort_option_locator = (By.XPATH, f"//option[contains(text(), '{sort_option}')]")
        self.click(sort_option_locator) 