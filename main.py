from selenium import webdriver
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
ISP_EMAIL = os.getenv("ISP_EMAIL")

firefox_driver = os.getenv("FIREFOX_DRIVER_LOCATION")

driver = webdriver.Firefox(executable_path=firefox_driver)

driver.get("https://www.speedtest.net/")

time.sleep(3)

go_button = driver.find_element_by_css_selector(".start-button a")
go_button.click()

time.sleep(60)

download_speed = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

upload_speed = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text

print(f"Download: {download_speed}, Upload: {upload_speed}")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=ISP_EMAIL,
                        msg=f"Subject: Internet Speed test\n\n"
                            f"Download speed: {download_speed}\nUpload speed: {upload_speed}")

driver.quit()
