[toc]

### NMS

对NMS进行分类，大致可分为以下六种，这里是依据它们在各自论文中的核心论点进行分类，这些算法可以同时属于多种类别。

1. 分类优先：传统NMS，Soft-NMS (ICCV 2017)
2. 定位优先：IoU-Guided NMS (ECCV 2018)
3. 加权平均：Weighted NMS (ICME Workshop 2017)
4. 方差加权平均：Softer-NMS (CVPR 2019)
5. 自适应阈值：Adaptive NMS (CVPR 2019)
6. +中心点距离：DIoU-NMS (AAAI 2020)



#### Efficient non-maximum suppression



#### Learning Non-Maximum Suppresion (NMS-Net) (#分类优先)



#### Soft-NMS - Improving Object Detection with One Line of Code (#分类优先)

是Traditional NMS的推广。

显然，对于IoU≥NMS阈值的相邻框，Traditional NMS的做法是将其得分暴力置0。这对于有遮挡的案例较不友好。因此Soft-NMS的做法是采取得分惩罚机制，使用一个与IoU正相关的惩罚函数对得分 ![[公式]](https://www.zhihu.com/equation?tex=s) 进行惩罚。



#### Acquisition of Localization Confidence for Accurate Object Detection (#定位优先)

提出 IoU-Net

IoU-Guided NMS出现于IoU-Net一文中，研究者认为框的定位与分类得分可能出现不一致的情况，特别是框的边界有模棱两可的情形时。因而该文提出了IoU预测分支，来学习定位置信度，进而使用定位置信度来引导NMS。

具体来说，就是使用定位置信度作为NMS的筛选依据，每次迭代挑选出最大定位置信度的框 ![[公式]](https://www.zhihu.com/equation?tex=M) ，然后将IoU≥NMS阈值的相邻框剔除，但把冗余框及其自身的最大分类得分直接赋予 ![[公式]](https://www.zhihu.com/equation?tex=M) ，这样一来，**最终输出的框必定是同时具有最大分类得分与最大定位置信度的框。**



#### Inception Single Shot MultiBox Detector for object detection (#加权平均)???

weighted-NMS

论文认为Traditional NMS每次迭代所选出的最大得分框未必是精确定位的，冗余框也有可能是定位良好的。那么与直接剔除机制不同，Weighted NMS顾名思义是对坐标加权平均，加权平均的对象包括 ![[公式]](https://www.zhihu.com/equation?tex=M) 自身以及IoU≥NMS阈值的相邻框。



#### Softer-NMS: Rethinking Bounding Box Regression for Accurate Object Detection (#方差加权平均)

Softer-NMS同样是坐标加权平均的思想，不同在于权重 ![[公式]](https://www.zhihu.com/equation?tex=w_i) 发生变化，以及引入了box边界的不确定度。



#### Adaptive NMS: Refining pedestrian detection in a crowd (#自适应阈值)

**Adaptive NMS**的研究者认为这在物体之间有严重遮挡时可能带来不好的结果。我们期望当物体分布稀疏时，NMS大可选用小阈值以剔除更多冗余框；而在物体分布密集时，NMS选用大阈值，以获得更高的召回。既然如此，该文提出了密度预测模块，来学习一个框的密度。

一个GT框 ![[公式]](https://www.zhihu.com/equation?tex=B_i) 的密度标签定义如下，

![[公式]](https://www.zhihu.com/equation?tex=d_i%3A%3D%5Cmax%5Climits_%7BB_i%2CB_j%5Cin+GT%7DIoU%28B_i%2CB_j%29%2C+%5Cquad+i%5Cneq+j) 

模型的输出将变为 ![[公式]](https://www.zhihu.com/equation?tex=%28x%2Cy%2Cw%2Ch%2Cs%2Cd%29) ，分别代表box坐标，宽高，分类得分，密度，其中密度 ![[公式]](https://www.zhihu.com/equation?tex=d) 越大，代表该框所处的位置的物体分布越密集，越有可能是遮挡严重的地方；反之密度 ![[公式]](https://www.zhihu.com/equation?tex=d) 越小，代表该框所处的位置的物体分布越稀疏，不太可能有遮挡。

论文以Traditionnal NMS和Soft-NMS的线性惩罚为基础，将每次迭代的NMS阈值更改如下：

![[公式]](https://www.zhihu.com/equation?tex=N_t%3D%5Cmax%5C%7Bthresh%2C+d_M%5C%7D) 

其中 ![[公式]](https://www.zhihu.com/equation?tex=thresh) 代表最小的NMS阈值。



#### Distance-IoU loss: Faster and better learning for bounding box regression (#+中心点距离)

* IoU loss and Generalized IoU (GIoU) loss still suffer from the problems of slow convergence and inaccurate regression.
* Propose a Distance-IoU (DIoU) loss by incorporating the normalized distance between the predicted box and the target box, which converges mush faster in training than IoU and GIoU losses.
* Summarizes three geometric factors in bounding box regression:
  * Overlap area
  * Central point distance
  * Aspect ratio
  * Based on the above three geometric factors, a Complete IoU (CIoU) loss is proposed, thereby leading to faster convergence and better performance.
* By incorporating DIoU and CIoU losses into state-of-the-art object detection algorithms, i.e. YOLO v3, SSD and Faster-R-CNN, they will achieve notable performance gain over IoU and GIoU.
* DIoU can be easily adopted into non-maximum suppresion (NMS) to act as the criterion, further boosting performance improvement.



* IoU loss 只适用与有 overlap 存在的情况，对于没有 overlap 的情况，则不能贡献 gradient，也就是对训练没有贡献。因此出现了 GIoU，引入 the smallest box covering B and Bgt，这会使 predicted box 向 the target box 靠近。



![](/home/ylqi007/work/notebooks/MachineLearning_and_DeepLearning/images/DIoU_0.jpeg)

* 三种情况下计算IoU和GIoU的时候，都是相同的；但是计算DIoU的时候是不一样的，因为distance between central points is different.



#### Reference

[Reflections on Non Maximum Suppression (NMS)](https://whatdhack.medium.com/reflections-on-non-maximum-suppression-nms-d2fce148ef0a)

[一文打尽目标检测NMS——精度提升篇](https://zhuanlan.zhihu.com/p/151914931)

[一文打尽目标检测 NMS——效率提升篇](https://bbs.cvmart.net/topics/2950)

[一、faster-rcnn源码阅读：nms的CUDA编程](https://zhuanlan.zhihu.com/p/80902998)

