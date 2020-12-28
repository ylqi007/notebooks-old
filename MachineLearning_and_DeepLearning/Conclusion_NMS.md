[toc]

### NMS

#### Efficient non-maximum suppression



#### Learning Non-Maximum Suppresion (NMS-Net)



#### Soft-NMS - Improving Object Detection with One Line of Code

是Traditional NMS的推广。

显然，对于IoU≥NMS阈值的相邻框，Traditional NMS的做法是将其得分暴力置0。这对于有遮挡的案例较不友好。因此Soft-NMS的做法是采取得分惩罚机制，使用一个与IoU正相关的惩罚函数对得分 ![[公式]](https://www.zhihu.com/equation?tex=s) 进行惩罚。

#### Acquisition of Localization Confidence for Accurate Object Detection (定位优先)

IoU-Guided NMS出现于IoU-Net一文中，研究者认为框的定位与分类得分可能出现不一致的情况，特别是框的边界有模棱两可的情形时。因而该文提出了IoU预测分支，来学习定位置信度，进而使用定位置信度来引导NMS。

具体来说，就是使用定位置信度作为NMS的筛选依据，每次迭代挑选出最大定位置信度的框 ![[公式]](https://www.zhihu.com/equation?tex=M) ，然后将IoU≥NMS阈值的相邻框剔除，但把冗余框及其自身的最大分类得分直接赋予 ![[公式]](https://www.zhihu.com/equation?tex=M) ，这样一来，最终输出的框必定是同时具有最大分类得分与最大定位置信度的框。

#### Inception Single Shot MultiBox Detector for object detection (加权平均)???



#### 方差加权平均 (Softer-NMS)???



#### Adaptive NMS: Refining pedestrian detection in a crowd

**Adaptive NMS**的研究者认为这在物体之间有严重遮挡时可能带来不好的结果。我们期望当物体分布稀疏时，NMS大可选用小阈值以剔除更多冗余框；而在物体分布密集时，NMS选用大阈值，以获得更高的召回。既然如此，该文提出了密度预测模块，来学习一个框的密度。

#### Distance-IoU loss: Faster and better learning for bounding box regression

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