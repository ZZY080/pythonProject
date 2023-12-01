import requests
from lxml import etree

url = "https://www.gaokao.cn/";

heades = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "accept-language": 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
}

response = requests.get(url=url)
content= response.text

html = etree.HTML(content)
links = html.xpath("//a")

print(links)


