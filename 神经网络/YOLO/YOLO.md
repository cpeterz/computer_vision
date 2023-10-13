# YOLO

[参考链接]([写给小白的YOLO介绍 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/94986199))

## 1.基本信息

YOLO只需要看一次，不需要找到可能存在的Region,在Region-base中，需要先对图像进行分析，找出可能存在物体的区域，将他们裁剪下来后放入一个分类器中进行分类，这个过程分为两阶段，而YOLO是单阶段的。

YOLO首先使用grid将图像切分成大小相同的许多小模块， 不同于滑窗法之类的要求识别物体在窗口内，YOLO只要求识别物体的中心在grid窗口内，即：他会在grid小窗口中生成若干 bounding box，这些bounding box的中心在grid内，而大小没有要求。bounding box中具有 x,y(中心点坐标)，w,h (bounding box的高宽).

YOLO所学习的就是bounding box的这四个参数，使得每个grid生成的有限的bounding box能将物体框选。

## 2. 知识点

### 2.1 归一化

为了防止不同图片大小对bounding box的参数造成影响，会将bounding box的四个参数进行归一化，让x和y除以grid的高宽，而由于bounding box的大小往往大于grid的长宽，所以用bounding box 的高宽来除以整个图像的高宽来进行归一化。

### 2.2 置信度 confidence

condidence的计算公式：
$$
C = P_r(obj)*IOU^{pred}_{truth}
$$
其中IOU为交并比，也就是两个框框的相似程度，也就是重合部分/总体部分。 而$IOU^{pred}_{truth}\color{black}$指预测的bounding box和真实物体位置的交并比。

$Pr(obj)$是指一个grid中有物体的概率，有物体时为1，无物体时为0，也可在其中波动。

### 2.3 非极大抑制（NMS）

每个grid的中都有不少bounding box找到了物体，但我们最终只会选择其中一个，这里就是只保留confidence最大的框，而其他的均删除。

这里不使用 $Pr(obj)$ 而用confidence的原因是 想排除掉不那么合适的bounding box，而 $Pr(obj)$作用是检测物体是否存在，而很难在bounding box中做出选择。

### 2.4 如何判断识别的是同一个物体

首先判断bounding box的类别是否相同，（比如是否都是狗），然后找到这些类别中 confidence 最大的那一个作为极大bounding box，然后将与这个极大bounding box的交并比（IOU）大于一定阈值的bounding box都删掉。



## 3.运用

