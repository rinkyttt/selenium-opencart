import os
import sys
import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

print("Loading conftest.py...")  # Add this line to verify loading

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture()
def setup():
    print("Setting up WebDriver with stealth mode...")
    options = uc.ChromeOptions()
    
    # Basic settings
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    
    # Stealth settings
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    
    # Additional stealth settings
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--no-first-run')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--dns-prefetch-disable')
    
    # Random user agent
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
    
    # Create undetected Chrome instance
    driver = uc.Chrome(
        options=options,
        driver_executable_path=None,
        suppress_welcome=True,
        use_subprocess=True,
        version_main=122  # Specify Chrome version
    )
    
    # Additional CDP commands for stealth
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            window.chrome = {
                runtime: {}
            };
        '''
    })
    
    yield driver
    
    print("Tearing down WebDriver...")
    driver.quit() 