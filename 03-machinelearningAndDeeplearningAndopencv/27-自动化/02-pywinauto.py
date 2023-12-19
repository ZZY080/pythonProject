import time

from pywinauto import Application

# 启动 Google Chrome 浏览器
chrome = Application(backend='uia').start(r'chrome.exe')

# 等待浏览器打开
chrome.wait_cpu_usage_lower(threshold=5)

# 获取浏览器窗口
browser = chrome.window(title_re='.*Google Chrome.*')
#
# # 最大化浏览器窗口
browser.maximize()
time.sleep(2)

# 输入搜索内容到 Google 搜索框

browser.input.type_keys("Your search query")

# 模拟回车键搜索
browser.type_keys('{ENTER}')
