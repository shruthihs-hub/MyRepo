import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, "name").send_keys("Shruthi H S")
driver.find_element(By.CLASS_NAME, "ng-pristine").send_keys("demo113@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
drop.select_by_visible_text("Male")
drop.select_by_index(1)
driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
content = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(content)
assert "Success" in content
print(content)


