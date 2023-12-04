# 示例数据
totaldata=[]
# 假设你有一些图片链接的列表 image_urls
# 以下为示例 image_urls，你需要替换为实际的图片链接列表
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
    "https://example.com/image4.jpg",
    "https://example.com/image5.jpg",
    "https://example.com/image6.jpg",
    "https://example.com/image7.jpg",
    "https://example.com/image8.jpg",
    "https://example.com/image9.jpg",
    "https://example.com/image10.jpg",
    "https://example.com/image11.jpg",
    "https://example.com/image5.jpg",
    "https://example.com/image12.jpg",
    "https://example.com/image13.jpg",
    "https://example.com/image14.jpg",
    "https://example.com/image15.jpg",
    "https://example.com/image16.jpg",
    "https://example.com/image17.jpg",
    # 更多图片链接...
]

# 将数据每五条一组插入 soil_pic
chunk_size = 5
for i in range(0, len(image_urls), chunk_size):
    soil = {
        "soil_pic": [],
        "soil_area": "123",
        "soil_location": "南京市鼓楼区滨江半岛",
        "soil_price": "123",
        "user_id": "65659e7b90ea0c427cff346b"
    }
    soil["soil_pic"].append(image_urls[i:i + chunk_size])
    totaldata.append(soil)

# 打印更新后的 soil 字典
print(totaldata)
