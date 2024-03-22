from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.find_elements(*locator)

    def send_keys(self, locator, value):
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(value)

    def click(self, locator):
        self.find_element(*locator).click()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
        except TimeoutException:
            print("Element not found")
            self.driver.quit()

    def open_new_window(self):
        self.driver.execute_script("window.open('');")

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self, url):
        self.driver.get(url)
