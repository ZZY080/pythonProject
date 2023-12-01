import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)  # 0代表默认的摄像头设备，如果有多个摄像头可以尝试不同的索引

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 循环读取并显示视频流
while True:
    # 读取一帧视频
    ret, frame = cap.read()

    # 如果视频读取失败，则退出循环
    if not ret:
        break

    # 在窗口中显示帧图像
    cv2.imshow("Video", frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头和窗口资源
cap.release()
cv2.destroyAllWindows()

