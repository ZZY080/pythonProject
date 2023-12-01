from selenium import  webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import  By
from time import  sleep

s=webdriver.Chrome()
s.get('https://www.cods.org.cn/')
sleep(0.4)

s.find_element_by_id("search").send_keys('长阳县民政局')
sleep(1)
btn=WebDriverWait(s,10).until(ec.presence_of_element_located((By.CLASS_NAME,'search-submit')))
s.execute_script("arguments[0].click();",btn)