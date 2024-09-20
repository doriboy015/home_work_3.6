import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_should_be_button(browser):
    browser.get(link)
    button1 = 0
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").text
    assert button1 != 0, button1

