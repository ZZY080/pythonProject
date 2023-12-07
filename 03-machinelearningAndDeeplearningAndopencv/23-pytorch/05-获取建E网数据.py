import datetime
from selenium import webdriver
import time
import re
import pandas as pd
import  pymongo


url = f'https://nco.justeasy.cn/pano/panolist.php'
# 得到数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 新建数据库
mydb=myclient["justeasy"]
# 创建集合
mycol = mydb["info"]


# 查询所有文档的 id 字段
mongo_all_id = mycol.find({}, {"_id": 0,"id": 1})
mongo_list_id = [doc["id"] for doc in mongo_all_id]
# 读取 Excel 文件 从200行开始
df = pd.read_excel('./全景1.xls',header=None)
part_id_list = df.iloc[:, 0].tolist()[:181]  # 选择第一列并转换为列表
part_id_list.extend(mongo_list_id)
part_id_list=list(set(part_id_list))



# # 读取 CSV 文件并取消索引
df = pd.read_csv('all.csv', index_col=False,header=None)

# 获取第一列数据并转换为列表 从第1500行开始
all_id_list = df.iloc[:, 0].tolist()[1301:]  # 获取第一列数据并转换为列表
id_list= [item for item in all_id_list if item not in part_id_list ]

# 使用 Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# 等待当前页面加载完毕
time.sleep(10)

for id in id_list:
    # 通过类名获取input框
    element_input = driver.find_element_by_css_selector(".form-control.input-text")
    element_input.clear()
    element_input.send_keys(id)
    element_search = driver.find_element_by_css_selector(".btn.btn-primary")
    time.sleep(1)
    element_search.click()
    time.sleep(1)
    mydict = {}
    mydict["id"] = id
    # 首先获取tbody中tr的个数 如果只有两个则数据为空
    element_tr_count =len( driver.find_elements_by_css_selector(".table.table-condensed  tbody tr")[1].find_elements_by_css_selector("td"))
    if(element_tr_count==1):
        continue
    element_td = driver.find_elements_by_css_selector("tbody tr")[1].find_elements_by_css_selector("td")[2]
    # 获取<tr>元素的HTML字符串表示
    tr_str = element_td.get_attribute('outerHTML')

    # 正则提取 ID 和 随机字符串 分别定义正则表达式
    id_pattern = re.search(r'<strong>ID：</strong>(.*?)<br>', tr_str)
    href_pattern = re.search(r'<a\s+href="(.*?)"\s+target="_blank">', tr_str)
    random_string_pattern = re.search(r'<strong>随机串：</strong>(.*?)<br>', tr_str)

    # 获取匹配到的值
    # if id_pattern:
    #     id_value = id_pattern.group(1).strip()
    #     mydict["id"]=id_value
    #     print(id_value)
    if random_string_pattern:
        random_string_value = random_string_pattern.group(1).strip()
        mydict["secret"]=random_string_value
    # 获取匹配到的链接
    if href_pattern:
        href_value = href_pattern.group(1).strip()
        mydict["url"]=href_value
    mydict["isfinsh"]=False
    mydict["isclick"]=False
    mydict["iserror"]=False
    mycol.insert_one(mydict)
time.sleep(800)
# 关闭浏览器窗口
driver.quit()
