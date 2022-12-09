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

passed = 0
header = "Kalkulator Faktorial"
if header in driver.page_source:
    passed += 1

input_form = "Masukkan Angka"
if input_form in driver.page_source:
    passed += 1

button = "Hitung Faktorial"
if driver.find_elements(By.CSS_SELECTOR, '#hitung'):
    passed += 1
    
footer = "Terms Of Service"
if footer in driver.page_source:
    passed += 1

if passed == 4:
    print("TC-001 passed")
else :
    print("TC-001 failed")

driver.close()
