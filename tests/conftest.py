import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, or edge"
    )

@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(get_browser):
    browser = get_browser.lower()
    driver = None
    
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Browser {browser} is not supported")
    
    driver.maximize_window()
    yield driver
    driver.quit() 