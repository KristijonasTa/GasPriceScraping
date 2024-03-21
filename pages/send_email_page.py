import json
import pandas
from pages.base_page import BasePage
from utils.logs_class import LogsClass
from utils.locators import *
from utils.test_data import *


class SendEmailPage(BasePage, LogsClass):
    def __init__(self, driver):
        super().__init__(driver)
        LogsClass.__init__(self)
        self.default_recipient = TestData.gmail_recipients

    @staticmethod
    def extract_data_from_excel_to_json(excel_file_path, json_file_path, logger):
        try:
            logger.info("Extract started in excel file to create JSON file")
            excel_data = pandas.read_excel(excel_file_path, sheet_name=None)
            all_sheet_data = []
            for sheet_name, df in excel_data.items():
                sheet_data = df.head()
                sheet_data_dict = sheet_data.to_dict(orient='records')
                all_sheet_data.append({sheet_name: sheet_data_dict})
            with open(json_file_path, 'w', encoding='utf-8') as file:
                json.dump(all_sheet_data, file, indent=4, ensure_ascii=False)
            logger.info("Extract ended new JSON file created with 5 lowest gast prices")
        except Exception as e:
            logger.error(f"Error occurred extracting data to json for: {str(e)}")

    @staticmethod
    def create_email_content(json_file_path, logger):
        try:
            logger.info("Taking information from JSON to create email content")
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            gas_stations_list = [pandas.DataFrame(gas_stations).iloc[0] for value in data for _, gas_stations in
                                 value.items()]

            combined_df = pandas.concat(gas_stations_list, axis=1).T
            combined_df.rename(columns={'Degaline': 'Degalinė'}, inplace=True)
            combined_df.iloc[:, 2:] = combined_df.iloc[:, 2:].apply(pandas.to_numeric, errors='coerce')
            grouped_df = combined_df.groupby([TestData.excel_row_degaline, TestData.excel_row_adresas]).first()

            email_content = ''
            for (gas_station_name, gas_station_address), row in grouped_df.iterrows():
                email_content += f"Gas station: {gas_station_name} "
                email_content += f" Address: {gas_station_address}\n"
                for gas_type, price in row.items():
                    if pandas.notna(price):
                        email_content += f"{gas_type} price: {price} EUR\n"
                email_content += "\n"
            return email_content
        except Exception as e:
            logger.error(f"Error occurred creating email content: {str(e)}")

    def extract_data_to_json(self):
        self.extract_data_from_excel_to_json(TestData.file_path_excel, TestData.file_path_json, self.logger)

    def open_gmail(self):
        try:
            self.logger.info("Initializing new window")
            self.open_new_window()
            self.switch_to_new_window()
            self.get_url(TestData.url_gmail)
            self.logger.info("New window opened GMAIL main page loaded")
        except Exception as e:
            self.logger.error(f"Open GMAIL in new window failed: {str(e)}")

    def login_to_gmail(self):
        try:
            self.logger.info("Start to login to GMAIL")
            self.send_keys(GMAIL_EMAIL_INPUT, TestData.gmail_sign_in_email)
            self.click(GMAIL_NEXT_BUTTON)
            self.wait_element(GMAIL_PASSWORD_INPUT)
            self.send_keys(GMAIL_PASSWORD_INPUT, TestData.gmail_sign_in_password)
            self.click(GMAIL_NEXT_BUTTON)
            self.logger.info("Logged in to GMAIL")
        except Exception as e:
            self.logger.error(f"Login to gmail failed: {str(e)}")

    def create_new_mail_insert_recipient(self, email=None):
        try:
            self.logger.info("Start to create new EMAIL")
            self.wait_element(GMAIL_NEW_MAIL)
            self.click(GMAIL_NEW_MAIL)
            self.wait_element(GMAIL_NEW_MAIL_TO)
            recipient_email = email or self.default_recipient
            self.send_keys(GMAIL_NEW_MAIL_TO, recipient_email)
            self.logger.info("EMAIL created, recipient added")
        except Exception as e:
            self.logger.error(f"Create new email failed: {str(e)}")

    def insert_subject_and_body(self):
        try:
            self.wait_element(GMAIL_NEW_MAIL_SUBJECT)
            self.send_keys(GMAIL_NEW_MAIL_SUBJECT, TestData.gmail_subject)
            self.wait_element(GMAIL_NEW_MAIL_INPUT)
            email_content = self.create_email_content(TestData.file_path_json, self.logger)
            self.send_keys(GMAIL_NEW_MAIL_INPUT, email_content)
            self.logger.info("Subject added, email, content added")
        except Exception as e:
            self.logger.error(f"Create new email failed: {str(e)}")

    def send_email(self):
        try:
            self.wait_element(GMAIL_SEND_MAIL)
            self.click(GMAIL_SEND_MAIL)
            self.wait_element(GMAIL_MESSAGE_SENT)
            self.logger.info("Email sent")
        except Exception as e:
            self.logger.error(f"Failed to send email: {str(e)}")

    def logo(self):
        try:
            self.wait_element(GMAIL_LOGO)
            self.logger.info("TEST PASSED")
        except Exception as e:
            self.logger.error(f"Failed to find GMAIL logo: {str(e)}")
