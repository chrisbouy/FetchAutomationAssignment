from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.helper import helper
from pages.base_page import base_page

class ScalePage(base_page):
    def __init__(self, driver):
        super().__init__(driver)

    def bowls(self):
        return helper.find_elements_with_wait(self._driver, By.CLASS_NAME, "game-board", 10)
    
    def get_first_bowl(self):
        bowls = self.bowls()
        if bowls:
            return bowls[0]
        else:
            raise Exception("First bowl element not found.")

    def get_second_bowl(self):
        bowls = self.bowls()
        if bowls:
            return bowls[1]
        else:
            raise Exception("Second bowl element not found.")
    
    def goto_assignment_page(self):
        self.goto("")

    def find_cell(self, bowl, index):
            # Bowl is either the "left" or "right" game-board
            side = bowl.find_element(By.CLASS_NAME, "status").text.lower().split()[0]  
            cell_id = f"{side}_{index}"
            return helper.find_element_with_wait_clickable(self._driver, By.ID, cell_id, 10)
         
    def add_bars_to_bowl(self, bowl, bars):
        for i, bar in enumerate(bars):
            cell = self.find_cell(bowl, i)
            cell.clear()  # Clear any existing value
            cell.send_keys(str(bar))

    def click_weigh(self):
        # XPath for the ordered list
        ol_xpath = "//div[contains(@class, 'game-info')]//ol"

        # Find the ordered list (ol) element
        ol_element = self._driver.find_element(By.XPATH, ol_xpath)

        # Check if the ol element is empty by inspecting its inner HTML
        is_first_weigh = ol_element.get_attribute("innerHTML").strip() == ""

        # Click the weigh button
        weigh_button = helper.find_element_with_wait_clickable(self._driver, By.ID, "weigh", 10)
        weigh_button.click()

        if is_first_weigh:
            # This is the first weigh, so we need to wait until the first 'Wieghings' entry exists
            WebDriverWait(self._driver, 10).until(lambda driver: len(driver.find_elements(By.XPATH, f"{ol_xpath}/li")) > 0)
        else:
            # If it's not the first weigh, wait for the list to update with a new entry
            initial_count = len(ol_element.find_elements(By.TAG_NAME, "li"))
            WebDriverWait(self._driver, 10).until(lambda driver: len(driver.find_elements(By.XPATH, f"{ol_xpath}/li")) > initial_count)
        
    def get_result(self):
        #ID is not unique, so using xpath
        comparison_operator_xpath = "//div[@class='result']//button[@id='reset']"
        comparison_operator = helper.find_element_with_wait_viewable(self._driver, By.XPATH, comparison_operator_xpath, 10)   
        match comparison_operator.text:
            case '=':
                return "Equal"
            case '>':
                return "Right"
            case '<':
                return "Left"
    
    def click_reset(self):
        #ID is not unique, so using xpath
        reset_button_xpath = "//button[@id='reset' and text()='Reset']"
        reset_button = helper.find_element_with_wait_clickable(self._driver, By.XPATH,reset_button_xpath, 10)
        reset_button.click()
        
    def select_fake_bar_from_main_group(self, bar):
        bars_group = helper.find_element_with_wait_viewable(self._driver, By.CLASS_NAME, "coins", 10)        
        bar_id = f"coin_{bar}"
        fake = helper.find_element_with_wait_clickable(self._driver,By.ID, bar_id, 10)
        helper.highlight_element(self._driver, fake)
        fake.click()