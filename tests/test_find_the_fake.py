import pytest
from logic.fake_gold_bar_finder import FakeGoldBarFinder

@pytest.mark.usefixtures("setup")
class TestFindFakeBar:
    def test_find_the_fake(self):
        fake_finder = FakeGoldBarFinder(self.driver)
        
        bars = list(range(9)) 

        
        fake_bar = fake_finder.find_fake_bar(bars)
        
        weighings = fake_finder.scale_page.get_weighings()
        print("Weighings:")
        for weighing in weighings:
            print(weighing)
            
        result_message = fake_finder.verify_fake_bar(fake_bar)

        print(f"Fake bar found: {fake_bar}")
        print(f"Result message: {result_message}")
