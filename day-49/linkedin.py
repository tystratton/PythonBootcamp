from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Optional: Run in headless mode (uncomment if needed)
# chrome_options.add_argument("--headless")

service = Service("path/to/chromedriver")  # Replace with your WebDriver's path
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Wait for the page to load
    time.sleep(2)

    # Locate the username field
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("your_email@example.com")  # Replace with your LinkedIn email

    # Locate the password field
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("your_password")  # Replace with your LinkedIn password

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the home page to load
    time.sleep(5)

    print("Login successful!")
finally:
    # Close the browser
    driver.quit()