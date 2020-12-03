from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Driver methods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#
from selenium.webdriver.common.by import By

COMMAND_LINDES_TO_REMOVE = [
    '--disable-background-networking',
    '--disable-client-side-phishing-detection',
    '--disable-default-apps',
    '--disable-hang-monitor',
    '--disable-popup-blocking',
    '--disable-prompt-on-repost',
    '--disable-sync',
    '--enable-automation',
    '--enable-blink-features=ShadowDOMV0',
    '--enable-logging',
    '--log-level=0',
    '--no-first-run',
    '--password-store=basic',
    '--remote-debugging-port=0',
    '--test-type=webdriver',
    '--use-mock-keychain',
    'data:,'
]
COMMAND_LINDES_TO_ADD = [
    # '--user-data-dir="%s"',
    '--flag-switches-begin',
    '--flag-switches-end',
    '--start-maximized'
]

class Webdriver(webdriver.Chrome):
    def __init__(self):
        # self.options = Options()
        pass

    def __new__(self, profile:str = "", *args, **kwargs):
        options = Options()
        for arg in COMMAND_LINDES_TO_ADD:
            options.add_argument("{}".format(arg))
        if profile:
            options.add_argument("--user-data-dir={}".format(profile))
        options.add_experimental_option("excludeSwitches", COMMAND_LINDES_TO_REMOVE)
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = 'none'

        #Replace default customdriver options and caps
        final_options = kwargs.get("options", options)
        final_caps = kwargs.get("desired_capabilities", caps)
        
        if ("options" and "desired_capabilities") in kwargs:
            return webdriver.Chrome(*args, **kwargs)
        else:
            if "options" not in kwargs:
                return webdriver.Chrome(options=final_options, *args, **kwargs)
            elif "desired_capabilities" not in kwargs:
                return webdriver.Chrome(desired_capabilities=final_caps, *args, **kwargs)
            else:
                return webdriver.Chrome(options=final_options, desired_capabilities=final_caps, *args, **kwargs)


class WebdriverMethods:

    def __init__(self, driver):
        self._driver = driver


    def wait(self, time=30):
        return WebDriverWait(self._driver, time)


    def wait_until_clickable(self, param: tuple, waiting_time: int=15, *args, **kwargs):
        ''''''
        # if not wait:
        wait = self.wait(waiting_time)
        try:
            element = wait.until(
                        EC.element_to_be_clickable(param),
                        *args, **kwargs
                    )
        except TimeoutException:
            element = False
        return element


    def wait_until_presence(self, param: tuple, waiting_time: int=15, *args, **kwargs):

        # if not wait:
        wait = self.wait(waiting_time)
        try:
            element = wait.until(
                        EC.element_to_be_clickable(param),
                        *args, **kwargs
                    )   
        except TimeoutException:
            element = False
        return element


    def find_element(self, param: tuple, *args, **kwargs):
        try:
            return self._driver.find_element(param[0], param[1], *args, **kwargs)
        except NoSuchElementException as err:
            return False


    def find_elements(self, param: tuple, *args, **kwargs):
        elements = self._driver.find_elements(param[0], param[1] *args, **kwargs)
        if len(elements) == 0:
            return False
        return elements

    def get_captcha_key(self):
        return self._driver.find_element_by_xpath("//div[@id='recaptcha']").get_attribute("data-sitekey")