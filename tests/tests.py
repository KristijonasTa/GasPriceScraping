import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.send_email_page import SendEmailPage
from utils.locators import *
from pages.main_page import MainPage
from utils.test_data import TestData


@pytest.mark.usefixtures("initialize_driver")
class TestMain:
    driver: WebDriver

    def test_filter_fuel_price_get_data_to_excel_convert_to_json_and_send_email(self, email):
        main_page = MainPage(self.driver)
        send_email_page = SendEmailPage(self.driver)
        main_page.change_language()

        title_text = self.driver.find_element(*ASSERTION_LT_LANGUAGE)
        actual_value = title_text.text

        expected_substring = "kuro kainos"
        assert expected_substring.lower() in actual_value.lower()

        main_page.select_city()

        expected_url = TestData.expected_url_gas_vilnius
        assert self.driver.current_url == expected_url

        main_page.get_diesel_prices()
        main_page.get_95_prices()
        main_page.get_98_prices()
        main_page.get_lpg_prices()

        send_email_page.extract_data_to_json()
        send_email_page.open_gmail()
        send_email_page.login_to_gmail()
        send_email_page.create_new_mail_insert_recipient(email)
        send_email_page.insert_subject_and_body()
        # send_email_page.send_email()
        send_email_page.logo()
