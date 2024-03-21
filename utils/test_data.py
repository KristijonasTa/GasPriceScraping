from dotenv import load_dotenv
import os


class TestData:
    load_dotenv()
    url_base = "https://gas.didnt.work/"
    url_gmail = "https://www.gmail.com/"
    expected_url_gas_vilnius = "https://gas.didnt.work/?country=lt&brand=&city=Vilnius"
    file_path_json = "../project_files/degalu_kainos.json"
    file_path_excel = "../project_files/degalu_kainos.xlsx"
    excel_row_degaline = 'Degalinė'
    excel_row_adresas = 'Adresas'

    scraped_data_dyzelis = 'Dyzelis'
    excel_sheet_value_dyzelis = "Dyzelino kainos"

    scraped_data_95 = '95'
    excel_sheet_value_95 = "95 kainos"

    scraped_data_98 = '98'
    excel_sheet_value_98 = "98 kainos"

    scraped_data_lpg = 'LPG'
    excel_sheet_value_lpg = "LPG kainos"

    gmail_sign_in_email = os.getenv('SCRAPER_EMAIL')
    gmail_sign_in_password = os.getenv('SCRAPER_PASSWORD')

    gmail_recipients = os.getenv('RECIPIENT_EMAIL')
    gmail_subject = "Cheapest fuel prices in Lithuania - Vilnius"
