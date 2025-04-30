import pytest
import time
from pageObjects.homePage import HomePage

class TestHomePage:
    def test_home_page_functionality(self, setup):
        """Test all homepage functionalities"""
        home_page = HomePage(setup)
        
        # Add initial delay to let the browser fully initialize
        time.sleep(2)

        # Test logo visibility
        home_page.navigate_to_home_page()
        home_page.handle_authorization()
        time.sleep(1)  # Add small delay between actions
        assert home_page.check_logo() is True, "Logo should be visible"
        
        # Test search functionality
        home_page.search_product("iPhone")
        time.sleep(1)
        assert home_page.is_search_heading_visible("iPhone"), "Search results page should be visible"
        
        # Test currency dropdown
        home_page.navigate_to_home_page()
        time.sleep(1)
        home_page.change_currency("€ Euro")
        time.sleep(1)
        assert "€" in home_page.get_macbook_price(), "Price should contain € symbol"
        
        # Test category navigation
        home_page.navigate_to_home_page()
        time.sleep(1)
        home_page.navigate_to_category("Desktops")
        time.sleep(1)
        assert "Desktops" in home_page.navigation_to_category_header(), "Should be on Desktops page"
        
        # Test shopping cart
        home_page.navigate_to_home_page()
        time.sleep(1)
        home_page.click_shopping_cart()
        time.sleep(1)
        assert "Your shopping cart is empty!" in home_page.get_shopping_cart_count(), "Empty cart message should be visible"
        
        # Test my account
        home_page.navigate_to_home_page()
        time.sleep(1)
        home_page.click_my_account()
        time.sleep(1)
        assert home_page.is_my_account_dropdown_visible(), "My account dropdown should be visible"
