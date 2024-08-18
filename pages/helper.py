from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

class helper:

    @staticmethod
    def highlight_element(driver, element):
        js = driver.execute_script
        js("arguments[0].style.border='3px solid red'", element)

    @staticmethod
    def find_element_with_wait_clickable(driver, by, value, timeout):
        try:
            wait = WebDriverWait(driver, timeout)
            return wait.until(EC.element_to_be_clickable((by, value)))
        except NoSuchElementException:
            return None

    @staticmethod
    def find_element_with_wait_viewable(driver, by, value, timeout):
        try:
            wait = WebDriverWait(driver, timeout)
            return wait.until(EC.visibility_of_element_located((by, value)))
        except NoSuchElementException:
            return None

    @staticmethod
    def find_elements_with_wait(driver, by, value, timeout):
        try:
            wait = WebDriverWait(driver, timeout)
            return wait.until(EC.visibility_of_all_elements_located((by, value)))
        except:
            return None

