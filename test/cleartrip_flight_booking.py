from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\testing-python-app\Reflektive\Driver\chromedriver.exe')
url="https://www.cleartrip.com/"
driver.maximize_window()
driver.get(url)

element_round_trip=driver.find_element_by_xpath("//label[@title='Round trip']")

element_round_trip.click()
time.sleep(3)

origin=driver.find_element_by_id("FromTag")
origin.send_keys("Bangalore")
destination=driver.find_element_by_id("ToTag")
destination.send_keys("New Delhi")

derapture_date=driver.find_element_by_id("DepartDate")
derapture_date.click()
dateToSelect = driver.find_element(By.XPATH, "//a[contains(text(),'18')]")
dateToSelect.click()
return_date=driver.find_element_by_id("ReturnDate")
return_date.click()
return_date_dateToSelect=driver.find_element(By.XPATH, "//a[contains(text(),'19')]")
return_date_dateToSelect.click()
element_adult = driver.find_element_by_id("Adults")
sel = Select(element_adult)
sel.select_by_value("1")

element_children= driver.find_element_by_id("Childrens")
sel = Select(element_children)
sel.select_by_value("1")

search_button=driver.find_element_by_id("SearchBtn")
search_button.click()
time.sleep(10)
try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='ResultContainer_1_1']"))
            )
except TimeoutError:
    print("element not visiable")


driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(10)
late_night_return=driver.find_element_by_xpath("//label[@for='1_1_20_24_arrivalTime']")
late_night_return.click()
driver.execute_script("window.scrollBy(0, -200);")
all_last_flight=driver.find_elements_by_xpath("//div[@class='colZero leg col12 last']/nav/ul/li")
all_last_flight[-1].click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(3)
submit_button=driver.find_element_by_xpath("//div[@id='ResultContainer_1_1']//button[contains(@type,'submit')][contains(text(),'Book')]")
submit_button.click()

try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='itineraryOpen']/div/p"))
            )
except TimeoutError:
    print("element not visiable")

insurance_acecpt_checkbox=driver.find_element_by_id("insurance_confirm")
insurance_acecpt_checkbox.click()

itenary_btn=driver.find_element_by_id("itineraryBtn")
itenary_btn.click()

email_id=driver.find_element_by_id("username")
email_id.send_keys("qatestteewe@gmail.com")
login_continu_btn=driver.find_element_by_id("LoginContinueBtn_1")
login_continu_btn.click()
time.sleep(5)
element_first_person_title = driver.find_element_by_id("AdultTitle1")
sel = Select(element_first_person_title)
sel.select_by_visible_text("Mr")

driver.find_element_by_id("AdultFname1").send_keys("Karan")
driver.find_element_by_id("AdultLname1").send_keys("malhotra")

element_children_title = driver.find_element_by_id("ChildTitle1")
sel = Select(element_children_title)
sel.select_by_visible_text("Miss")

driver.find_element_by_id("ChildFname1").send_keys("Kiran")
driver.find_element_by_id("ChildLname1").send_keys("malhotra")
# element_first_person_boddate=driver.find_element_by_id("AdultDobDay1")
# sel = Select(element_first_person_boddate)
# sel.select_by_visible_text("1")
#
# element_first_person_boddate=driver.find_element_by_id("AdultDobDay1")
# sel = Select(element_first_person_boddate)
# sel.select_by_visible_text("1")
#
# element_first_person_bodyear=driver.find_element_by_id("AdultDobYear1")
# sel = Select(element_first_person_bodyear)
# sel.select_by_value("1980")
element_child_boddate=driver.find_element_by_id("ChildDobDay1")
sel = Select(element_child_boddate)
sel.select_by_visible_text("1")
element_child_dobmon=driver.find_element_by_id("ChildDobMonth1")
sel = Select(element_child_dobmon)
sel.select_by_visible_text("Jan")

element_child_dobmon=driver.find_element_by_id("ChildDobYear1")
sel = Select(element_child_dobmon)
sel.select_by_visible_text("2009")


mobile_number=driver.find_element_by_id("mobileNumber")
mobile_number.send_keys("1234567890")
travel_continu_btn=driver.find_element_by_id("travellerBtn")
travel_continu_btn.click()
#
#
#
#

# print(len(all_last_flight))
#

