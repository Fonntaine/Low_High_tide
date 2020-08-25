from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import datetime

driver = webdriver.Chrome('/Users/judeslater/Downloads/chromedriver')

driver.get('https://ahoy.twilio.com/')

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div/header/ul/li[2]/a')))

login_button = driver.find_element_by_xpath('/html/body/nav/div/header/ul/li[2]/a')
login_button.click()
#all_days = driver.find_elements_by_xpath('//*[@id="msw-js-tide-list"]/div')


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
email_type = driver.find_element_by_xpath('//*[@id="email"]')
email_type.send_keys('judeslater1@gmail.com')
email_click = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/form/div[2]/button')
email_click.click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
password_type = driver.find_element_by_xpath('//*[@id="password"]')
password_type.send_keys('oottiiss11886622')
password_click = driver.find_element_by_xpath('//*[@id="login"]')
password_click.click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="two-factor"]/div/ul/li[3]/button')))
auth_button = driver.find_element_by_xpath('//*[@id="two-factor"]/div/ul/li[3]/button')
auth_button.click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="two-factor"]/div/div[1]/div/div/input')))
auth_type = driver.find_element_by_xpath('//*[@id="two-factor"]/div/div[1]/div/div/input')
auth_button.send_keys('9Zg3R1HerFSlt0sby_-HFxIOVLySuiiETLietDfa')


time.sleep(20)
driver.quit()