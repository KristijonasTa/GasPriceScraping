from dotenv import load_dotenv
import os


class TestData:
    load_dotenv()
    url_base = "https://gas.didnt.work/"
    url_gmail = "https://www.gmail.com/"
    file_path_json = "C:/Users/krtarut/Desktop/Testing/GasPrice/GasPriceTest/project_files/degalu_kainos.json"
    file_path_excel = "C:/Users/krtarut/Desktop/Testing/GasPrice/GasPriceTest/project_files/degalu_kainos.xlsx"
    excel_row_degaline = 'Degalinė'
    excel_row_adresas = 'Adresas'

    value_dyzelis = 'Dyzelis'
    sheet_value_dyzelis = "Dyzelino kainos"

    value_95 = '95'
    sheet_value_95 = "95 kainos"

    value_98 = '98'
    sheet_value_98 = "98 kainos"

    value_lpg = 'LPG'
    sheet_value_lpg = "LPG kainos"

    gmail_sign_in_email = os.getenv('SCRAPER_EMAIL')
    gmail_sign_in_password = os.getenv('SCRAPER_PASSWORD')

    gmail_recipients = os.getenv('RECIPIENT_EMAIL')
    gmail_subject = "Cheapest fuel prices in Lithuania - Vilnius"
