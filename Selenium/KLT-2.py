from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()

driver.get("https://qa.putraprima.id/")

input = driver.find_element(by=By.XPATH, value='//*[@id="input"]')
result = driver.find_element(by=By.XPATH, value='//*[@id="result"]')

# TC-001 Positive case
# menampilkan hasil benar


def input_less_than_170():
    input.click()
    input.send_keys(17)
    input.send_keys(Keys.ENTER)

    expect = "Faktorial dari "
    if result.text[15:] == expect[15:]:
        print("TC-001 passed")
    else:
        print("TC-001 failed")

    time.sleep(2)
    input.clear()

# TC-001 negative case
# tidak menampilkan hasil apa apa karena nge-bug


def input_more_than_170():
    input.click()
    input.send_keys(433)
    input.send_keys(Keys.ENTER)

    expect = "Faktorial dari "
    if result.text[15:] == expect[15:]:
        print("TC-001 passed")
    else:
        print("TC-001 failed")

    time.sleep(2)
    input.clear()

# TC-002
# error karena inputan desimal atau float


def input_is_a_float():
    input.click()
    input.send_keys(1.9)
    input.send_keys(Keys.ENTER)

    expect = "Please enter an integer"
    if result.text == expect:
        print("TC-002 passed")
    else:
        print("TC-002 failed")

    time.sleep(2)
    input.clear()

# TC-003
# error karena inputan string


def input_is_a_font():
    input.click()
    input.send_keys("atmayanti")
    input.send_keys(Keys.ENTER)

    expect = "Please enter an integer"
    if result.text == expect:
        print("TC-003 passed")
    else:
        print("TC-003 failed")

    time.sleep(2)
    input.clear()

# TC-004
# error karena inputan string


def input_is_a_special_character():
    input.click()
    input.send_keys("*&/.")
    input.send_keys(Keys.ENTER)

    expect = "Please enter an integer"
    if result.text == expect:
        print("TC-004 passed")
    else:
        print("TC-004 failed")

    time.sleep(2)
    input.clear()

# TC-005
# error karena inputan kosong


def input_is_empty():
    input.click()
    input.send_keys("")
    input.send_keys(Keys.ENTER)

    expect = "Please enter an integer"
    if result.text == expect:
        print("TC-005 passed")
    else:
        print("TC-005 failed")

    time.sleep(2)
    input.clear()


input_less_than_170()
input_more_than_170()
input_is_a_float()
input_is_a_font()
input_is_a_special_character()
input_is_empty()

driver.close()
