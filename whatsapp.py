import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\SAMEER\Downloads\chromedriver_win32\chromedriver.exe') #path to chrome webdriver file
driver.get('https://web.whatsapp.com/')
time.sleep(25)


element = None

count=50     # number of messages to send
while count!=0:
    for i in driver.find_elements_by_css_selector('.chat-title'):
        words = i.text
        if 'Prince' in words:    # name of the person
            element = i
            break

    element.click()
    time.sleep(2)
    try:
        input_element = driver.find_element_by_css_selector('.pluggable-input-body.copyable-text.selectable-text')
    except:
        continue
    input_element.send_keys("xxxxx")      # messgage to send
    input_element.send_keys(Keys.ENTER)
    time.sleep(1)
    count -= 1
time.sleep(100)
driver.quit()
