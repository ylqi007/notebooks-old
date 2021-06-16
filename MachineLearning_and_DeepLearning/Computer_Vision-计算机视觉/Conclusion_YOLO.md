[toc]



## You Only Look Once: Unified, Real-Time Object Detection (YOLO)

### Abstract 

> Prior work on object detection repurposes classifiers to perform detection. Instead, we frame object detection as a regression problem to spatially separated bounding boxes and associated class probabilities.

* Prior work: 用 classifier 去完成 detection 的工作
* YOLO: 将 detection 模拟成 regression problem



### 1. Introduction

> Current detection systems repurpose classifiers to perform detection. To detect an object, these systems take a classifier for that object and evaluate it at various locations and scales in a test image. Systems like deformable parts (DPM) use a sliding window approach where the classifier is run at evenly spaced locations over the entire image.

* 也就是特定 object 都有一个 classifier, 这个 classifier 会在 image 的不同地方, 不同 scale 进行 evaluate.



> More recent approaches like R-CNN use region proposal methods to first generate potential bounding boxes in an image and then run a classifier on these proposed boxes. After classification, post-processing is used to refine the bounding boxes, eliminate duplicate detections, and rescore the boxes based on other objects in the scene. These complex pipelines are slow and hard to optimize because each individual component musts be trained separately.

* 更 current 的方法, 比如 R-CNN 通过生成 region proposal 来进行 detection. 这种大致分成三个步骤:
* First, generate potential bounding boxes in an image; 
* Then, run a classifier on these proposed boxes; 
* After classification, post-processing is  used to refine the bounding boxes, eliminate duplicate detections, and rescore the boxes based on other objects in the scene.



> We reframe object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities.
>
> This unified model has several benefits over traditional methods of object detection.
>
> First, YOLO is extremely fast.
>
> Second, YOLO reasons globally about the image when making predictions.
>
> Third, YOLO learns generalizable representations of objects.

* 直接从 image pixels ==> bbox coordinates + class probabilities



### 2. Unified Detection

> Our system divides the input image into an $S \times S$ **grid**. If the center of an object falls into a grid cell, that grid cell is responsible for detecting that object.
>
> Each grid cell predicts $B$ bounding boxes and confidence scores for those boxes. These confidence scores reflect how confident the model is that the box contains an object and also how accurate it thinks the box is that it predicts. Formally we define confidence as $Pr(Object) * IOU^{truth}_{pred}$. If no object exists in that cell, the confidence scores should be zero.
>
> Each bounding box consists of 5 predictions: $x, y, w, h$ and confidence. The $(x, y)$ coordinates represents the center of the box relative to the bounds of the grid cell. The width and height are predicted relative to the whole image. Finally, the confidence prediction represents the IOU between the predicted box and any ground truth box.
>
> Each grid cell also predicts $C$ conditional class probabilities, $Pr(Class_{i}|Object)$. These probabilities are conditioned on the grid cell containing an object. We only predict one set of class probabilities per grid cell, regardless of the number of boxes $B$.

* 一个 grid cell 对应 $B$ 个 boxes,
* 每个 bounding boxes 包含 5 个预测的信息: $x, y, w, h$ and confidence,
  * $(x, y)$ 是相对于 the grounds of the grid cell
  * $(w, h)$ 是相对于 the whole image
  * confidence 是 predicted box 与 gt box 的 IOU



> Our final layer predicts both class probabilities and bounding box coordinates. We normalize the bounding box width coordinates. We normalize the bounding box width and height by the image width and height so that they fall between 0 and 1. We parametrize the bounding box $x$ and $y$ coordinates to the offsets of a particular grid cell location so they are also bounded between 0 and 1.

* 将 bounding box 的 width 和 height 与整张 image 的 width 和 height 进行归一化, 这样可以保证 bounding box 的 width 和 height 在 0 到 1 之间. (如果是与 anchor box 进行归一化, 则当 bounding box 比 anchor box 大的时候, 归一化的结果就会超出 0 到 1 的范围.)
* 将 bounding box 的 $(x, y)$ 坐标设定为与对应 grid cell 的 offset.



> We use a linear activation function for the final layer and all other layers use the following leaky rectified linear activation:
> $$
> \phi(x) = 
> \begin{cases} 
> x, & \text{if }x > 0 \\
> 0.1x, & otherwise
> \end{cases}
> $$
> We optimize for sum-squared error in the output of our model. We use sum-squared error because it is easy to optimize, however it does not perfectly align with out goal of maximizing average precision. It weights localization error equally with classification error which may not be ideal. Also, in every image many grid cells do not contain any object.

* 在此版本的 YOLO 中, 采用的是 linear activation function. the final layer and all other layers use the same leaky rectified linear activation.
* 将 localization loss 和 classification loss 同等对待, 这可能是不正确的.
* 在此版本的 YOLO 中, 通过引入 $\lambda_{coord}=5$ 和 $\lambda_{noobj}=0.5$ 进行了人为的平衡.



> ![](../images/YOLO_loss.png)
>
> Note that the loss function only penalizes classification error if an object is present in that grid cell (hence the conditional class probability discussed earlier). It also only penalizes bounding box coordinate error if that predictor is "responsible" for the ground truth box (i.e. has the highest IOU of any predictor in that grid cell).

* Increase the loss from bounding box coordinate predictions and decrease the loss from confidence predictions for the boxes that don't contain objects. Use two parameters, $\lambda_{coord}=5$ and $\lambda_{noobj}=0.5$ to accomplish this.



## YOLO: Better, Faster, Stronger





## YOLOv3: An Incremental Improvement





## YOLOv4: Optimal Speed and Accuracy of Object Detection

