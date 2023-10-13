import cv2

# 加载已经经过训练的模型
classifier = cv2.CascadeClassifier('../pre_module/haarcascade_frontalface_alt2.xml')

# 准备数据集，包括图像和标签
dataset = [
    {'image': 'path/to/image1.jpg', 'label': 'face'},
    {'image': 'path/to/image2.jpg', 'label': 'non-face'},
    # 添加更多图像和标签
]

correct_count = 0
total_count = len(dataset)

for data in dataset:
    image_path = data['image']
    label = data['label']

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用分类器进行对象检测
    detected_faces = classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # 如果检测到人脸，假定为正确
    if len(detected_faces) > 0 and label == 'face':
        correct_count += 1
    # 如果没有检测到人脸，假定为正确
    elif len(detected_faces) == 0 and label == 'non-face':
        correct_count += 1

# 计算正确率
accuracy = (correct_count / total_count) * 100
print(f'正确率: {accuracy:.2f}%')
