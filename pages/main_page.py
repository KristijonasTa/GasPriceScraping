import pandas
from bs4 import BeautifulSoup

from pages.base_page import BasePage
from utils.base_class import BaseClass
from utils.locators import *
from utils.test_data import *


class MainPage(BasePage, BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        BaseClass.__init__(self)

    def scrap_data(self, gas, number):
        try:
            self.logger.info(f"Data scraping started for {gas}")
            page_content = self.driver.page_source
            soup = BeautifulSoup(page_content, 'html.parser')
            gas_station_table = (soup.find('table', class_='table is-narrow is-striped sortable')
                                 .find('tbody').find_all('tr'))

            gas_list = []

            for row in gas_station_table:
                content = {}
                whole_information_gas_station = row.find_all('td')[0]
                name_of_gas_station = whole_information_gas_station.find(string=True, recursive=False).strip()
                content[TestData.excel_row_degaline] = name_of_gas_station.replace('⛽', '')
                address = whole_information_gas_station.find('small').text
                content[TestData.excel_row_adresas] = address
                content[gas] = row.find_all('td')[number].text

                gas_list.append(content)

            return pandas.DataFrame(gas_list)
        except Exception as e:
            self.logger.error(f"Error occurred scraping failed for: {str(e)}")

    @staticmethod
    def insert_data_to_excel(df, gas, name_of_sheet, logger):
        try:
            logger.info(f"Inserting data to excel {gas}")
            df = df.replace({'-': 'x'})
            sorted_df = df.sort_values(by=gas)
            try:
                existing_excel = pandas.read_excel(TestData.file_path_excel, sheet_name=None)
            except FileNotFoundError:
                existing_excel = {}

            with pandas.ExcelWriter(TestData.file_path_excel, engine='openpyxl') as writer:
                for sheet_name, data in existing_excel.items():
                    data.to_excel(writer, sheet_name=sheet_name, index=False)
                sheet_name = name_of_sheet if name_of_sheet else existing_excel
                sorted_df.to_excel(writer, sheet_name=sheet_name, index=False)

        except Exception as e:
            logger.error(f"Error occurred while inserting data to Excel for {gas}: {str(e)}")
            raise

    def change_language(self):
        try:
            self.logger.info(f"Test started")
            self.wait_element(TITLE_OF_THE_GAS_PAGE)
            language_change = BUTTON_CHANGE_LANGUAGE_LT
            self.wait_element(language_change)
            self.click(language_change)
        except Exception as e:
            self.logger.error(f"Change language to Lithuanian error: {str(e)}")
            raise

    def select_city(self):
        try:
            self.logger.info(f"Language changed to Lithuanian Assertion passed")
            dropdown_menu = DROPDOWN_CITY_LIST
            self.click(DROPDOWN_CITY_LIST)
            self.wait_element(DROPDOWN_CITY_LIST)
            self.click(OPTION_SELECT_VILNIUS)
            self.wait_element(dropdown_menu)
            self.logger.info(f"Vilnius element selected in drop down")
        except Exception as e:
            self.logger.error(f"Vilnius element in dropdown menu not found: {str(e)}")
            raise

    def get_diesel_prices(self):
        self.logger.info(f"Vilnius element selected in drop down Assertion passed")
        data_diesel = self.scrap_data(TestData.value_dyzelis, 1)
        self.insert_data_to_excel(data_diesel, TestData.value_dyzelis, TestData.sheet_value_dyzelis, self.logger)
        self.logger.info(f"Excel sheet for {TestData.value_dyzelis} gas added")

    def get_95_prices(self):
        data_95 = self.scrap_data(TestData.value_95, 2)
        self.insert_data_to_excel(data_95, TestData.value_95, TestData.sheet_value_95, self.logger)
        self.logger.info(f"Excel sheet for {TestData.value_95} gas added")

    def get_98_prices(self):
        data_98 = self.scrap_data(TestData.value_98, 3)
        self.insert_data_to_excel(data_98, TestData.value_98, TestData.sheet_value_98, self.logger)
        self.logger.info(f"Excel sheet for {TestData.value_98} gas added")

    def get_lpg_prices(self):
        data_lpg = self.scrap_data(TestData.value_lpg, 4)
        self.insert_data_to_excel(data_lpg, TestData.value_lpg, TestData.sheet_value_lpg, self.logger)
        self.logger.info(f"Excel sheet for {TestData.value_lpg} gas added")
