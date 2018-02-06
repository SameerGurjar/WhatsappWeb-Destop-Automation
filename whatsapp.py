import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\SAMEER\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(25)


element = None

k=50
while k!=0:
    for i in driver.find_elements_by_css_selector('.chat-title'):
        words = i.text
        if 'Prince' in words:
            element = i
            break

    element.click()
    time.sleep(2)
    input_element = driver.find_element_by_css_selector('.pluggable-input-body.copyable-text.selectable-text')
    input_element.send_keys("chutiya")
    input_element.send_keys(Keys.ENTER)
   # time.sleep(3)
    k = k - 1
time.sleep(100)
driver.quit()