import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_book_availability(browser):
    browser.get(link)
    icon = browser.find_element(By.CSS_SELECTOR, "p.instock.availability>i")
    icon_class = icon.get_attribute("class")

    assert "icon-ok" in icon_class, "The book is not available"

    time.sleep(15)
