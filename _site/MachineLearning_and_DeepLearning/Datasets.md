[TOC]

---
## Pascal VOC
1. Tasks:
    * Object Classification
    * Object Detection
    * Object Segmentation
    * Human Layout
    * Action Classification
2. Dataset:
    * [Pascal VOC Dataset Mirror](https://pjreddie.com/projects/pascal-voc-dataset-mirror/)


---
## [COCO](https://cocodataset.org/#home)
1. Tasks: 
    * [Object Detection Task](https://cocodataset.org/#detection-2020)
        * Full details of object detection can be found in the [detection evaluation page](https://cocodataset.org/#detection-eval).
    * [Keypoint Detection Task](https://cocodataset.org/#keypoints-2020)
        * The keypoint task involves simultaneously detecting people and localizing their keypoints. 
        * [keypoint evaluation page](https://cocodataset.org/#keypoints-eval)
    * [Panoptic Segmentation Task](https://cocodataset.org/#panoptic-2020)
        * Panoptic segmentation addresses both stuff and thing classes, unifying the typically distinct semantic and instance segmentation tasks.
        * [Panoptic evaluation page](https://cocodataset.org/#panoptic-2020) 
    * [DensePose Task](https://cocodataset.org/#densepose-2020)
        * [DensePose evaluation page](https://cocodataset.org/#densepose-2020)
2. Dataset:
    * [Download Page](https://cocodataset.org/#download)
    * Images & Annotations
    * [COCOAPI](https://github.com/cocodataset/cocoapi)
3. [Data Format](https://cocodataset.org/#format-data)
    * COCO has several annotation types: for object detection, keypoint detection, stuff segmentation, panoptic, panoptic segmentation densepose, and image captioning.
    * The annotations are stored using **JSON**.

---
## Evaluation
错误率 & 精度, 召回率 & 准确率, P-R曲线, 平衡点（Break-Even Point, BEP）
### mAP


---
## References
### COCO References
* [【学习笔记】MS COCO dataset](https://zhuanlan.zhihu.com/p/32566503)
* [COCO 数据集的使用](https://www.cnblogs.com/q735613050/p/8969452.html)
* [從COCO Dataset取出特定的物件標記](https://chtseng.wordpress.com/2019/12/01/%E5%BE%9Ecoco-dataset%E5%8F%96%E5%87%BA%E7%89%B9%E5%AE%9A%E7%9A%84%E7%89%A9%E4%BB%B6%E6%A8%99%E8%A8%98/)
* [MS COCO数据标注详解](https://www.cnblogs.com/leebxo/p/10607955.html)
* [COCO数据集的标注格式](https://zhuanlan.zhihu.com/p/29393415)

### Pascal VOC References
* [Pascal Voc数据集详解 以Voc2012为例](https://blog.csdn.net/qq_39938666/article/details/89511383)
* [Pascal Voc数据集详细分析](https://phgao.blog.csdn.net/article/details/80060327?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)
* [PASCAL VOC 2012 数据集详解](https://blog.csdn.net/wenxueliu/article/details/80327316)
* [PASCAL VOC数据集的标注格式](https://zhuanlan.zhihu.com/p/33405410)

### Evaluation References
* [性能指标（模型评估）之mAP](https://blog.csdn.net/u014203453/article/details/77598997)
* [Average precision](https://sanchom.wordpress.com/tag/average-precision/)

### Other References
* [PASCAL VOC 数据集详解与MS COCO组合方式](https://www.geek-share.com/detail/2796046067.html)
* [YOLOV5在樹莓派上的測試](https://chtseng.wordpress.com/2020/07/03/yolov5%e5%9c%a8%e6%a8%b9%e8%8e%93%e6%b4%be%e4%b8%8a%e7%9a%84%e6%b8%ac%e8%a9%a6/)
* [【SSD算法】史上最全代码解析-数据篇](https://zhuanlan.zhihu.com/p/79933177)
* [【SSD算法】史上最全代码解析-核心篇](https://zhuanlan.zhihu.com/p/79854543)
* [YOLO V4的模型训练](https://my.oschina.net/u/4277473/blog/4315291)
* []()
* []()


