from pages.scale_page import ScalePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FakeGoldBarFinder:
    def __init__(self, driver):
        self.driver = driver
        self.scale_page = ScalePage(driver)

    def find_fake_bar(self, bars):
        while len(bars) > 1:
            #split bars into 2 groups
            mid_point = len(bars) // 2
            
            # This takes the first half of the list bars, from the start up to (but not including) mid_point
            left_group = bars[:mid_point]
            
            # Takes the next mid_point number of elements starting from mid_point
            right_group = bars[mid_point:mid_point * 2]
            
             # The odd bar out if len(bars) is odd
            odd_out = bars[mid_point * 2:] 
            
            # Ensure left_group is entered into the first grid and right_group into the second
            first_bowl = self.scale_page.get_first_bowl()
            second_bowl = self.scale_page.get_second_bowl()
            self.scale_page.add_bars_to_bowl(first_bowl, left_group)
            self.scale_page.add_bars_to_bowl(second_bowl, right_group)

            self.scale_page.click_weigh()  
            result = self.scale_page.get_result()  

            # Keep going through this loop with the lighter group until there's only 2 bars.  
            # If 'result' is 'Equal', then odd man out is the fake
            if result == "Left":
                bars = left_group
            elif result == "Right":
                bars = right_group
            else:
                bars = odd_out

            self.scale_page.click_reset() 
        # The remaining bar is the fake one
        #self.scale_page.get_weighings_list()
        return bars[0]  

    def verify_fake_bar(self, bar):
        #click on bar
        self.scale_page.select_fake_bar_from_main_group(bar)
        # Wait for the alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Get the text from the alert
        alert_text = alert.text

        # Assert that the alert text is as expected
        assert alert_text == "Yay! You find it!", f"Unexpected alert text: {alert_text}"

        # Accept the alert to close it
        alert.accept()
        #return message
        return alert_text

 