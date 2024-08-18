import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from configsettings import configsettings

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Implicit wait

    config = configsettings._init_configuration()
    base_url = config["BaseUrl"]
    print(f"Base URL in setUp: {base_url}")

    if not base_url.startswith("http"):
        raise ValueError(f"Invalid URL format: {base_url}")

    driver.get(base_url)
        
   # Adds the driver instance to the test class via the request object
    request.cls.driver = driver

    yield  # Pass control back to the test code.

    # Teardown code
    driver.quit()

