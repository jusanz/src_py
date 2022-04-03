import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.by import By


def webdriver(headless=False, no_image=True, tor=False):
    service = Service(ChromeDriverManager().install())

    options = Options()
    if no_image:
        prefs = {"profile.managed_default_content_settings.images": 2} # no images
        options.add_experimental_option("prefs", prefs)
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1200x600')
    if tor:
        PROXY = "socks5://localhost:9050"
        options.add_argument('--proxy-server={}'.format(PROXY))

    return selenium.webdriver.Chrome(service=service, options=options)

def find_element(parent, xpath):
    return parent.find_element(by=By.XPATH, value=xpath)

def find_elements(parent, xpath):
    return parent.find_elements(by=By.XPATH, value=xpath)
