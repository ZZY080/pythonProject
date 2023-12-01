from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver import ActionChains # 用于滑动滑块
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from PIL import  Image  # 用于抠图
import time

driver = webdriver.Chrome()
driver.get('https://music.163.com/')
driver.maximize_window()
#元素本身的值是动态属性的无法直接定位到该元素，通过寻找’登录‘元素，在定位其父级元素
driver.find_element_by_xpath("//a[text()='登录']/..").click()
time.sleep(2)
web_input = driver.find_element_by_xpath("//a[text()='选择其他登录模式']").click()
#勾选同意条款
driver.find_element_by_xpath("//input[@id='j-official-terms']").click()
#点击手机登录
driver.find_element_by_xpath("//div[@class='tan2MIhq']").click()
time.sleep(2)
# 点击密码登录
driver.find_element_by_xpath("//div[@class='_3Mb1fXSG']/a[@href='javascript:;']").click()
#在号码输入框输入号码
driver.find_element_by_xpath("//input[@class='_2OT0mQUQ']").send_keys('19170376686')
#在密码输入框输入密码
driver.find_element_by_xpath("//input[@class='sR89MU1J']").send_keys('ZZY806@!.')
time.sleep(2)
#点击登录按钮
driver.find_element_by_xpath("//div[@class='tan2MIhq']").click()
time.sleep(0.6)
# 破解滑块验证码
slide = driver.find_element_by_xpath('//div[@class="yidun_slider"]')
# 拖动滑块
for i in range(100,320,5):
    actions_chains = ActionChains(driver)
    actions_chains.click_and_hold(slide)
    actions_chains.move_by_offset(i, 0)
    actions_chains.release()
    actions_chains.perform()
    time.sleep(1)
time.sleep(1000)
#运行结束后释放资源
driver.quit()