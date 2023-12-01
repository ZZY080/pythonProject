import time

from selenium import  webdriver

driver = webdriver.Chrome()
driver.get("https://authserver.nuaa.edu.cn/authserver/login")
driver.maximize_window()
# driver.quit()
time.sleep(8)
