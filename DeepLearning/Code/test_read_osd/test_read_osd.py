import cv2  
import pytesseract  
  
# 配置Tesseract OCR路径  
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # 根据你的Tesseract OCR安装路径进行修改
  
# 打开视频文件或摄像头  
video_source = "record.mp4"  # 替换为你的视频文件路径
# video_source = 0  # 用于从摄像头捕获  
  
cap = cv2.VideoCapture(video_source)

# 获取视频的宽度和高度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象，指定输出视频文件的编解码器和帧率
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 使用MP4编解码器
out = cv2.VideoWriter("output_video.mp4", fourcc, 30, (20, 45), isColor=False)

# 设置识别配置
config = r'--oem 1 --psm 6 tessedit_char_whitelist=0123456789'

while cap.isOpened():
    # 读取视频帧  
    ret, frame = cap.read()  
    if not ret:  
        break  
  
    # 将帧转换为灰度图像  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # 应用二值化处理，根据背景颜色调整阈值  
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)
  
    # 使用形态学操作消除噪声和毛刺  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  
  
    # 查找轮廓并绘制边界矩形  
    # contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #     x, y, w, h = cv2.boundingRect(contour)
    #
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #     # 提取OSD信息的子图像
    #     osd_image = gray[y:y+h, x:x+w]
    #
    #     # 使用Tesseract OCR将OSD信息转换为数字
    #     osd_text = pytesseract.image_to_string(osd_image, lang='chi_sim')
    #     print(f"OSD Text: {osd_text}, x: {x}, y:{y}, w: {w}, h: {h}")

    x = 41
    y = 136
    w = 361 - 41
    h = 181 - 136
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 提取OSD信息的子图像
    osd_image = binary[y:y+h, x:x+w]

    # 使用Tesseract OCR将OSD信息转换为数字
    osd_text = pytesseract.image_to_string(osd_image, config=config)
    print(f"OSD Text: {osd_text}, x: {x}, y:{y}, w: {w}, h: {h}")

    # 显示处理后的帧
    cv2.imshow("Frame", frame)

    # 保存灰度图像
    out.write(osd_image)

    key = cv2.waitKey(1) & 0xFF  
    if key == ord("q"):  
        break  
  
# 释放资源并关闭窗口  
cap.release()  
cv2.destroyAllWindows()