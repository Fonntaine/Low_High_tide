from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import datetime
from twilio.rest import Client

driver = webdriver.Chrome('/Users/judeslater/Downloads/chromedriver')

driver.get('https://magicseaweed.com/Nosara-Surf-Report/445/Tide/')

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="msw-js-tide-list"]')))

all_days = driver.find_elements_by_xpath('//*[@id="msw-js-tide-list"]/div')

ocean_data = all_days[1].text # there is one hidden `div` which I have to skip to get today's data


driver.quit()

driver.get('https://ahoy.twilio.com/')

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="msw-js-tide-list"]')))

all_days = driver.find_elements_by_xpath('//*[@id="msw-js-tide-list"]/div')

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele      
    return str1  
        

textmessage = listToString(ocean_data)

account_sid = 'Your account sid'
auth_token = 'Your auth token'
client = Client(account_sid, auth_token)



from_whatsapp_number='whatsapp:+(Your twilio number)'

to_whatsapp_number='whatsapp:+(Your number)'

client.messages.create(body=(textmessage), from_=from_whatsapp_number, 
                        to=to_whatsapp_number)