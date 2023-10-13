# 1.导入库
import cv2
import time

# 2.方法：绘制图片中检测到的人脸
def draw_face(img, faces):
    for (x, y, w, h) in faces:
        # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 10)


# 3.主函数：
if __name__ == "__main__":
    # 4.读取一张照片
    img = cv2.imread('../face_picture/face_picture3.jpg')
    cv2.imshow('face', img)

    # 5.转换成灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 6.通过opencv加载haar级联分类器
    face_alt2 = cv2.CascadeClassifier('../pre_module/haarcascade_frontalface_alt2.xml')
    # face_alt2 = cv2.CascadeClassifier('../pre_module/haarcascade_eye.xml')
    last = time.time()
    # 7.对图像中的人脸进行检测
    face_alt2_detect_faces = face_alt2.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
    now = time.time()
    print(((now - last)*1000) )
    # 8.绘制图片中检测到的人脸
    draw_face(img, face_alt2_detect_faces)

    # 保存带有人脸框的图像
    output_filename = 'output_image.jpg'
    cv2.imwrite(output_filename, img)

    # 9.显示照片
    cv2.imshow('face', img)

    # 10.关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()