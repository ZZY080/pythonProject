import datetime
from selenium import webdriver
import time
import json
import requests
import random

nowdate = datetime.datetime.now()
destTime =(nowdate+datetime.timedelta(seconds=45)).strftime("%Y-%m-%d %H:%M:%S")
now=nowdate.strftime("%Y-%m-%d %H:%M:%S")
word = input("请输入关键词:")
url = f'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsMiw2LDQsNSw3LDgsOQ%3D%3D&word={word}'

# 使用 Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# 等待当前页面加载完毕
time.sleep(2)

# 模拟滚动到页面底部
last_height = driver.execute_script("return document.body.scrollHeight")


while now<=destTime:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 模拟滚动
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待页面加载

# 找到所有图片元素
elems = driver.find_elements_by_css_selector('img.main_img')
# 提取所有图片的 URL
image_urls = [elem.get_attribute('src') for elem in elems if not elem.get_attribute('src').startswith('data:image')]
# 示例数据
totaldata=[]
arealist=["123","11","12","234","121","145","124","132"]
locationlist =["南京市鼓楼区滨江半岛","南京市鼓楼区热河路","南京市玄武区南京火车站","南京市玄武区玄武湖","南京市江宁区建邺万达","南京市江宁区将军路","南京市建邺区万达广场","南京市建邺区泰山路"]
pricelist = ["1233","1345","567","123","4567","678","890","678"]
# 将数据每五条一组插入 soil_pic
chunk_size = 5
for i in range(0, len(image_urls), chunk_size):
    number=random.randint(0,7)
    soil = {
        "soil_pic": [],
        "soil_area": arealist[number],
        "soil_location": locationlist[number],
        "soil_price": pricelist[number],
        "soil_active":[
            {"title":"套餐一","price":f"{random.randint(9000,100000)}","time":"年","imgsrc":"http://192.168.1.140:8080/assets/images/arg_blue.png"},
            {"title":"套餐二","price":f"{random.randint(9000,100000)}","time":"2年","imgsrc":"http://192.168.1.140:8080/assets/images/arg_yellow.png"},
            {"title":"套餐三","price":f"{random.randint(9000,100000)}","time":"3年","imgsrc":"http://192.168.1.140:8080/assets/images/arg_green.png"}],
        "user_id": "656d7514c98ed7146c5b45d9",

    }
    soil["soil_pic"].extend(image_urls[i:i + chunk_size])
    totaldata.append(soil)

# 打印更新后的  字典
for (index,item) in enumerate(totaldata):
    response = requests.post("http://192.168.1.140:8080/api/soil/addsoil",data=json.dumps(item),headers={"Content-Type":"application/json"})
    time.sleep(0.2)
# 关闭浏览器窗口
driver.quit()
