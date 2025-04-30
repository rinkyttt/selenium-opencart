# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import logging
import time
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)
        
    def click(self, locator):
        """
        Waits for an element to be clickable and then clicks it.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except (ElementClickInterceptedException, TimeoutException) as e:
            self.logger.error(f"Error clicking on element {locator}: {str(e)}")
            self.take_screenshot("click_error")
            raise
    
    def text_input(self, locator, text):
        """
        Waits for an element to be visible and then enters text into it.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :param text: Text to enter into the element
        """
        try: 
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text into element: {locator}")
        except TimeoutException as e:
            self.logger.error(f"Error entering text into element {locator}: {str(e)}")
            self.take_screenshot("text_input_error")
            raise
        
    def take_screenshot(self, name):
        """
        Takes a screenshot of the current page and saves it to the screenshots directory.
        
        :param name: Name of the screenshot file
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots") 
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")  
        
    def get_element_text(self, locator):
        """
        Waits for an element to be visible and then returns its text.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :return: Text of the element
        """ 
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException as e:
            self.logger.error(f"Error getting text from element {locator}: {str(e)}")
            self.take_screenshot("get_element_text_error")
            raise
        
    def is_element_present(self, locator):
        """
        Checks if an element is present in the DOM.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :return: True if the element is present, False otherwise
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def is_element_visible(self, locator):
        """
        Checks if an element is visible on the page.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :return: True if the element is visible, False otherwise
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def is_element_enabled(self, locator):
        """
        Checks if an element is enabled.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :return: True if the element is enabled, False otherwise
        """
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
        
    def is_element_selected(self, locator): 
        """
        Checks if an element is selected.
        
        :param locator: Tuple (By.ID, "element_id") or (By.XPATH, "//div")
        :return: True if the element is selected, False otherwise
        """ 
        try:
            self.wait.until(EC.element_to_be_selected(locator))
            return True
        except TimeoutException:
            return False    
        

