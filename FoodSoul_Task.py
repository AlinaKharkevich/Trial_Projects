from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# chrome_options = Options()  
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)  # headless browser option

driver = webdriver.Chrome() 
driver.get("https://shop.foodsoul.pro")
time.sleep(5)

delivery = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/ul/li[2]")
delivery.click()
time.sleep(5)

place = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]")
place.click()
time.sleep(5)

# Your Profile
profile_button = driver.find_element(By.XPATH, "//button[@aria-label='profile']")
profile_button.click()
time.sleep(5)

phone_number = input("Please enter the phone number: ")
phone_input = driver.find_element(By.XPATH, "//input[@data-inputmask-mask='+7 (999) 999-99-99']")
phone_input.clear()
phone_input.send_keys(phone_number)
time.sleep(5)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(5)

if "CAPTCHA" in driver.page_source:
    # Prompt the user to manually solve the CAPTCHA
    input("Please solve the CAPTCHA manually, then press Enter to continue...")
    time.sleep(5)
    submit_button.click()
    time.sleep(5)

try:
    # Registration Process if you are a new user
    close_button = driver.find_element(By.XPATH, "//button[@aria-label='close-modal']")
    close_button.click()
    time.sleep(5)

    name = input("Please enter your Name: ")
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Имя']")
    name_input.clear()
    name_input.send_keys(name)
    time.sleep(5)

    date = driver.find_element(By.XPATH, "//input[@placeholder='Дата рождения']")
    date.click()
    time.sleep(5)

    year = driver.find_element(By.XPATH, "//div[@class='date-navigation__value' and text()='2023']")
    year.click()
    time.sleep(5)
    year_choice = driver.find_element(By.XPATH, "//div[@class='select-popover__item' and text()='2000']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", year_choice)
    year_choice.click()
    time.sleep(5)

    month = driver.find_element(By.XPATH, "//div[@class='date-navigation__value date-navigation__month' and text()='август']")
    month.click()
    time.sleep(5)
    month_choice = driver.find_element(By.XPATH, "//div[@class='select-popover__item' and text()='сентябрь']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", month_choice)
    month_choice.click()
    time.sleep(5)

    day = driver.find_element(By.XPATH, "//li[@class='date-days__item' and text()='18']")
    day.click()
    time.sleep(5)

    gender = driver.find_element(By.XPATH, "//button[@aria-label='toggle']")
    gender.click()
    time.sleep(5)
    gender_choice = driver.find_element(By.XPATH, "//span[contains(text(), 'Женщина')]")
    gender_choice.click()
    time.sleep(5)

    register_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    register_button.click()
    time.sleep(5)

    input("Please call the phone number manually, then press Enter to continue...")
    time.sleep(5)

except NoSuchElementException:
    # Log in if you are a NOT new user
    input("Please call the phone number manually, then press Enter to continue...")
    time.sleep(5)

# Order and Cart
food = driver.find_element(By.XPATH, "//label[@for='Асума-productParams']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", food)
time.sleep(5)

food_num = driver.find_element(By.XPATH, "//*[@id='recommendrecommend']/div/div[3]/div[2]/div[3]/div[2]")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", food_num)
food_num.click()
time.sleep(5)

cart_button = driver.find_element(By.XPATH, "//button[@aria-label='cart']") 
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_button)
cart_button.click()
time.sleep(15)

driver.save_screenshot('cart_screenshot.png') # Cart Screenshot

order_food = driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div[2]/div/button") 
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_food)
order_food.click()
time.sleep(5)

# Payment and Confirmation
payment_method = driver.find_element(By.XPATH, "//input[@placeholder='Оплата*']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_method)
payment_method.click()
time.sleep(5)

payment_choice = driver.find_element(By.XPATH, "//span[contains(text(), 'Наличными')]")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_choice)
payment_choice.click()
time.sleep(5)

confirm_order = driver.find_element(By.XPATH, "//*[@id='app']/main/div[2]/form/div/div/div[1]/button/div") 
confirm_order.click()
time.sleep(5)

exit_order = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/button") 
exit_order.click()
time.sleep(5)

driver.quit()