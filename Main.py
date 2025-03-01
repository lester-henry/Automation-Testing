from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Scenario 1
#Step 1: Open https://www.saucedemo.com/ using Google Chrome
driver.get("https://www.saucedemo.com/")

#Step 2: As a standard_user, log in to the system successfully
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()

#Step 3: Add Sauce Labs Bolt T-Shirt and Sauce Labs Fleece Jacket to your cart.
bolt_tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
bolt_tshirt.click()
fleece_jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
fleece_jacket.click()
time.sleep(3)

#Step 4: Click your cart.
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

#Step 5: Check that the 2 items were correctly added to the cart.
assert driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")
assert driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")

#Step 6: Click checkout
checkout = driver.find_element(By.ID, "checkout")
time.sleep(3)
checkout.click()

#Step 7: Fill up the order form with any First Name, Last Name, Zip/Postal Code values.
driver.find_element(By.ID, "first-name").send_keys("Lester Henry")
driver.find_element(By.ID, "last-name").send_keys("Parco")
driver.find_element(By.ID, "postal-code").send_keys("1362")
time.sleep(3)

#Step 8: Click Continue.Check if the Price Total is correct.
confirm = driver.find_element(By.ID, "continue")
confirm.click()
expected_total_price = 71.27  
total_price_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
total_price = float(total_price_text.replace("Total: $", "").strip())
assert abs(total_price - expected_total_price) < 0.01, f"Price mismatch! Expected: {expected_total_price}, but got: {total_price}"
print("Total price is correct:", total_price)
time.sleep(3)

#Step 9: Click Finish.Check if the “Thank you for your order!” page is displayed
finish = driver.find_element(By.ID, "finish")
finish.click()
time.sleep(5)

#Logout of account
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)  
driver.find_element(By.ID, "logout_sidebar_link").click()


#Scenario 2
#Step 2: As a locked_out_user, log in to the system.
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()
time.sleep(3)

#Step 3: Check if the validation message: “Epic sadface: Sorry, this user has been locked out” is displayed.
error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
assert "Epic sadface: Sorry, this user has been locked out" in error_message


driver.quit()