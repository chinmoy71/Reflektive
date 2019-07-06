from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    executable_path=r'C:\Users\user\Documents\testing-python-app\Reflektive\Driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)

search_select = driver.find_element_by_id("searchDropdownBox")

sel = Select(search_select)

sel.select_by_visible_text("Books")
time.sleep(5)

serach_item = driver.find_element_by_id("twotabsearchtextbox")
serach_item.send_keys("A Brief History of Everyone Who Ever Lived")
click_go_btn = driver.find_element_by_xpath("//input[@value='Go']")
click_go_btn.click()

driver.implicitly_wait(10)

find_book_element = driver.find_element_by_xpath("//li[@id='result_0']//img[@class='s-access-image cfMarker']")
find_book_element.click()
time.sleep(5)
handels=driver.window_handles;

driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
buy_now_btn=driver.find_element_by_id("buy-now-button")
buy_now_btn.click()
login_mail=driver.find_element_by_id("ap_email")
login_mail.clear()
login_mail.send_keys("9830777150")
