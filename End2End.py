from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
items = driver.find_elements(By.XPATH,"//app-card/div[1]")
for item in items:
    tobeadd = item.find_element(By.XPATH,"div/h4").text
    if tobeadd == "Blackberry":
        item.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver .find_element(By.CSS_SELECTOR,".btn-success").click()

driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in message
print(message)