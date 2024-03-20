from selenium.webdriver.common.by import By

TITLE_OF_THE_GAS_PAGE = (By.XPATH, "//h1[@class='title']")
BUTTON_CHANGE_LANGUAGE_LT = (By.XPATH, "//a[@href='?country=lt']")
DROPDOWN_CITY_LIST = (By.XPATH, "//select[@id='cities']")
OPTION_SELECT_VILNIUS = (By.XPATH, "//*[@id='cities']/option[contains(.,'Vilnius')]")
ASSERTION_LT_LANGUAGE = (By.XPATH, "/html/body/div/div[2]/table/caption/p[1]")

GMAIL_EMAIL_INPUT = (By.XPATH, "//input[@id='identifierId']")
GMAIL_NEXT_BUTTON = (By.XPATH, "//span[normalize-space()='Next']")
GMAIL_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

GMAIL_NEW_MAIL = (By.XPATH, "//div[contains(text(),'Compose')]")
GMAIL_NEW_MAIL_TO = (By.XPATH, "//div[@role='presentation']//input[@type='text']")
GMAIL_NEW_MAIL_SUBJECT = (By.XPATH, "//input[@name='subjectbox']")
GMAIL_NEW_MAIL_INPUT = (By.XPATH, "//div[@role='textbox']")
GMAIL_SEND_MAIL = (By.XPATH, "//div[text()='Send']")
GMAIL_MESSAGE_SENT = (By.XPATH, "//span[contains(.,'Message sent')]")
GMAIL_LOGO = (By.XPATH, "//img[@role='presentation']")
