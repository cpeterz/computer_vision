# 1.导入库
import cv2
import time

# 2.方法：绘制图片中检测到的人脸
def draw_face(img, faces):
    for (x, y, w, h) in faces:
        # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


# 3.主函数：
if __name__ == "__main__":

    # 4.读取摄像头
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()

        # 5.通过opencv加载haar级联分类器
        face_alt2 = cv2.CascadeClassifier('../pre_module/haarcascade_frontalface_alt2.xml')

        last_time = time.time()
        # 6.对图像中的人脸进行检测
        face_alt2_detect_faces = face_alt2.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

        now_time = time.time()

        print(f' Processing Time = {(now_time - last_time)*1000:.2f} ms')
        # 7.绘制图片中检测到的人脸
        draw_face(frame, face_alt2_detect_faces)

        # 8.实时展示效果画面
        cv2.imshow('face', frame)
        # 每5毫秒监听一次键盘动作
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    # 8.关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()