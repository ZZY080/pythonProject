import cv2

# 远程视频流的URL
video_url = "http://example.com/your_remote_video_stream_url"

# 打开视频流
cap = cv2.VideoCapture(video_url)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # 读取视频帧
    ret, frame = cap.read()

    # 检查视频是否结束
    if not ret:
        print("Video stream ended.")
        break

    # 在这里进行处理，例如显示、保存或其他操作
    cv2.imshow("Remote Video", frame)

    # 检测键盘输入，如果按下 'q' 键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频流对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
