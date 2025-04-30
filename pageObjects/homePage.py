from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from utilities.baseClass import BaseClass
from config.config import TestConfig


class HomePage(BasePage):
    # Locators
    SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "body > nav:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > form:nth-child(1) > div:nth-child(1) > a:nth-child(1) > i:nth-child(3)")
    MY_ACCOUNT = (By.CSS_SELECTOR, "div[class='nav float-end'] div[class='dropdown'] span[class='d-none d-md-inline']")
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right.show")
    SHOPPING_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    WISH_LIST = (By.ID, "a[id='wishlist-total'] span[class='d-none d-md-inline']")
    CHECKOUT = (By.CSS_SELECTOR, "a[title='Checkout'] span[class='d-none d-md-inline']")
    LOGO = (By.ID, "logo")
    MACBOOK_PRICE = (By.CSS_SELECTOR,'.price-new')
    NAVIGATION_TO_CATEGORY_HEADER = (By.LINK_TEXT, "div[id='content'] h2")
    SHOPPING_CART_COUNT = (By.CSS_SELECTOR, ".text-center.p-4")
    
    # Authorization checkbox
    AUTH_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, driver):
        super().__init__(driver)
        self.base = BaseClass()
        self.base_url = TestConfig.get_base_url()
        
    def navigate_to_home_page(self):
        self.driver.get(self.base.get_website_url())
    
    def check_logo(self):
        self.is_element_visible(self.LOGO)

    def search_product(self, product_name):
        self.text_input(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
        
    def is_search_heading_visible(self, product_name):
        heading = self.driver.find_element(By.XPATH, f"//h1[contains(text(), 'Search - {product_name.lower()}')]")
        return heading.is_displayed()
    
    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART)

    def click_wish_list(self):
        self.click(self.WISH_LIST)

    def click_my_account(self):
        self.click(self.MY_ACCOUNT)

    def click_checkout(self):
        self.click(self.CHECKOUT)

    def select_currency(self):
        self.click(self.CURRENCY_DROPDOWN)

    def navigate_to_category(self, category_name):
        """
        Generic method to navigate to any category
        :param category_name: Name of the category to navigate to
        """
        category_locator = (By.LINK_TEXT, category_name)
        self.click(category_locator)

    def navigation_to_category_header(self):
        """
        Check if navigation to a specific category is successful
        :param category_name: Name of the category to check
        """
        return self.get_element_text(self.NAVIGATION_TO_CATEGORY_HEADER)

    def change_currency(self, currency_name):
        """
        Change the currency of the website
        :param currency_name: Name of the currency to change to (e.g., '€ Euro', '£ Pound Sterling', '$ US Dollar')
        """
        self.click(self.CURRENCY_DROPDOWN)
        currency_option = (By.XPATH, f"//a[@class='dropdown-item' and contains(text(), '{currency_name}')]")
        self.click(currency_option)

    def get_macbook_price(self):
        return self.get_element_text(self.MACBOOK_PRICE)
    
    def get_shopping_cart_count(self):
        return self.get_element_text(self.SHOPPING_CART_COUNT)
    
    def is_my_account_dropdown_visible(self):
        return self.is_element_visible(self.MY_ACCOUNT_DROPDOWN)

    def handle_authorization(self):
        """Handle the authorization popup if it appears"""
        try:
            # Find and click the checkbox
            checkbox = self.wait.until(EC.element_to_be_clickable(self.AUTH_CHECKBOX))
            checkbox.click()
            return True
        except TimeoutException:
            return False



    
