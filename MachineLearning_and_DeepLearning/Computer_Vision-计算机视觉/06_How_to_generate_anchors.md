[toc]



## How to generate anchor boxes?

> Object detection algorithms usually sample a large number regions in the input image or feature maps, determine whether these regions contain objects of interest, and adjust the edges of the regions so as to predict the ground-truth bounding box of the target more accurately. Different models use different region sampling method.
>
> 物体识别算法通常会在 image or feature map 上采样一些 regions，判断这些 regions 是否包含我们感兴趣的目标，然后调整 regions‘ edges，让预测 bounding box 更加准确。
>
> Assume that the input image has a height of *h* and width of *w*. We generate anchor boxes with different shapes and ratios centered on each pixel of the image.
>
> * height of *h* and width of *d*, then there will be *hw* pixels, i.e. *hw* centers.
>
> Assume that the size is $s \in (0,1]$, the aspect ratio is $r > 0$, and the width and height of the anchor box are $ws\sqrt(r)$ and $hs/\sqrt(r)$ , respectively, then the area of an anchor will be $whs^{2}$. 
>
> Assume that we have a set of sizes $\{s_{1},..., s_{n}\}$ and a set of aspect of ratios $\{r_{1},..., r_{m}\}$. 
>
> * If we use a combination of all sizes and aspect ratios with each pixel as the center, then the input image will have $whnm$ anchors.
> * Although the above all combinations may cover all gt_boxes, the computational complexity is often excessive. Therefore, we are usually only interested in a combination containing $s_{1}$ or $r_{1}$ sizes and aspect ratios, then there will be $n + m - 1$ anchors for this image. This time, the number of anchors for this image centered on each pixel will be $wh(n+m-1)$. 
>
> ```python
> # https://d2l.ai/chapter_computer-vision/anchor.html    
> #@save
> def multibox_prior(data, sizes, ratios):
>     """ Generate prior anchor boxes.    
>     """
>     in_height, in_width = data.shape[-2:]	# Get the height and width of this image
>     device, num_sizes, num_ratios = data.device, len(sizes), len(ratios)
>     boxes_per_pixel = (num_sizes + num_ratios - 1)
>     size_tensor = torch.tensor(sizes, device=device)	# sizes, like [0.75, 0.5, 0.25]
>     ratio_tensor = torch.tensor(ratios, device=device)	# ratios, like [1, 2, 0.5]
>     # Offsets are required to move the anchor to center of a pixel
>     # Since pixel (height=1, width=1), we choose to offset our centers by 0.5
>     offset_h, offset_w = 0.5, 0.5
>     steps_h = 1.0 / in_height  	# Scaled steps in y axis, i.e. 1.0 / 224
>     steps_w = 1.0 / in_width  	# Scaled steps in x axis, i.e. 1.0 / 224
> 
>     # Generate all center points for the anchor boxes
>     center_h = (torch.arange(in_height, device=device) + offset_h) * steps_h
>     center_w = (torch.arange(in_width, device=device) + offset_w) * steps_w
>     shift_y, shift_x = torch.meshgrid(center_h, center_w)
>     shift_y, shift_x = shift_y.reshape(-1), shift_x.reshape(-1)
> 
>     # Generate boxes_per_pixel number of heights and widths which are later
>     # used to create anchor box corner coordinates (xmin, xmax, ymin, ymax)
>     # size_tensor = [s0, s1, ..., s(n-1)], ratio_tensor[1:]=[r1, r2, ..., r(m-1)]
>     # w = [s0, s1, ..., s(n-1), s[0]*r1, s[0]*r2, ..., s[0]*r(m-1)], len=n+m-1
>     # h = [s0, s1, ..., s(n-1), s[0]/r1, s[0]/r2, ..., s[0]/r(m-1)], len=n+m-1
>     w = torch.cat((size_tensor, sizes[0] * torch.sqrt(ratio_tensor[1:])))\
>                 * in_height / in_width / 2
>     h = torch.cat((size_tensor, sizes[0] / torch.sqrt(ratio_tensor[1:]))) / 2
>     # torch.stack((-w, -h, w, h)) is of shape (4, len), where len=(n+m-1)
>     # anchor_manipulattion.shape = (in_height * in_width * len, 4)
>     anchor_manipulations = torch.stack((-w, -h, w, h)).T.repeat(
>                                         in_height * in_width, 1)
> 
>     # Each center point will have boxes_per_pixel number of anchor boxes, so
>     # generate grid of all anchor box centers with boxes_per_pixel repeats
>     out_grid = torch.stack([shift_x, shift_y, shift_x, shift_y],
>                 dim=1).repeat_interleave(boxes_per_pixel, dim=0)
> 
>     output = out_grid + anchor_manipulations
>     # the returned tensor is (batch_size, number of anchor boxes, 4)
>     return output.unsqueeze(0)	# Returns a new tensor with a dimension of size one inserted at the specified position.
> 
> ```
>
> * 在上面代码中生成 `center_h` and `center_w` 的代码，比较难懂，可以参考下面的写法
>
> ```
>     # now the centers will be 0.5 offset from top left corner
> 	center_h = (torch.arange(in_height, device=device) + offset_h) / in_height
>     center_w = (torch.arange(in_width, device=device) + offset_w) / in_width
> ```
>
> * [`stack` vs `cat`](https://stackoverflow.com/questions/54307225/whats-the-difference-between-torch-stack-and-torch-cat-functions/54307331)
>   * Assume `A` and `B` are of shape (3, 4)
>   * `stack`, concatenates sequence of tensors along a **new dimension**, `torch.cat([A, B], dim=0)` will be of shape (6, 4).
>   * `cat`, concatenates the given sequence of sequence tensors in the **given dimension**, `torch.stack([A, B], dim=0)` will be of shape (2, 3, 4).
> * [PyTorch -- repeat() & expand()](https://zhuanlan.zhihu.com/p/58109107)
> * After changing the shape of the anchor box variable to `(img_height, img_width, anchors_per_pixel, 4)`, we can obtain all the anchor boxes centered on a specified pixel position.



> The appropriate bounding box is selected as the bounding box with the highest IOU between the gt_box and anchor_box. Note that this trick of assignment ensures that an anchor box predicts ground truth for an object centered at its own grid center, and not a grid cell far away.
>
> Note that the anchor box that is responsible to predict a ground truth label is chosen as the box that gives maximum IOU when placed at the center of the ground truth box, i.e. only size is consider while assigning ground truth boxes.



> In fact, if anchor boxes are not tuned correctly, your neural network will never even know that certain small, large or irregular objects exist and will never have a chance to detect them.



## Faster R-CNN 中关于 Anchor 的内容

> At each sliding-window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as $k$. So the *reg* layer has $4k$ outputs encoding the coordinates of $k$ boxes, and the *cls* layer outputs $2k$ scores that estimate probability of object or not object for each proposal. The $k$ proposals are parameterized *relative* to $k$ reference boxes, which we call **anchor**. An anchor is centered as the sliding window in question, and is associated with a scale and aspect ration.

* At each sliding-window location, the model 同时 predict $k$ region proposals; 
* **每个 proposal** 对应4个 *loc* 坐标，所以 reg layer 输出 $4k$ outputs for this location, 后续计算 loc regression loss 的时候会用到这里的输出;
* **每个 proposal** 对应2个 scores，分别对应 of object 和 not object，所以 *cls* layer 输出 $2k$ outputs, 后续计算 cls loss 的时候会用到这里的输出; 
* 输出的 $k$ 个 proposals 的参数都是相对于 $k$ 个参考坐标，也就是 `k` anchors.



> **Translation-Invariant Anchors？**



> **Multi-Scale Anchors as Regression References**
>
> There have been two popular ways for multi-scale predictions. The first way is based on image/feature pyramids. The images are resized at multiple scales, and feature maps are computed for each scale. The second way is to use sliding windows of multiple scales (and/or aspect ratios) on the feature maps. The second way is usually adopted jointly with the first way.
>
> ![](../images/Handle_rescales.png)
>
> As a comparison, our anchor-based method is built on ***a pyramid of anchors***, which is more cost-efficient. ==Our method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios.==

* Method 1. Rescale image，然后在 rescaled image 上计算 feature map; 
* Method 2. 用不同 scales 的 sliding window.
* 对 bounding boxes 的分类和回归是以不同 scales 和 ratios 的 anchors。



> **Encode anchor with gt_box**
>
> We assign a positive label to two kinds of anchors: (i) the anchor/anchors with the highest Intersection-over-Union (IoU) overlap with a ground-truth box, or (ii) an anchor that has an IoU overlap higher than 0.7 with any ground-truth box. ==Note that a single ground-truth box may assign positive labels to multiple anchors.== Usually the second condition is sufficient to determine the positive samples; but we still adopt the first condition for the reason that in some rare cases the second condition may find no positive sample. We assign a negative label to a non-positive anchor if its IoU ratio is lower than 0.3 for all ground-truth boxes. Anchors that neither positive nor negative do not contribute to the training objective.

* Anchors assigned positive labels:
  * Have the highest IoU with a ground-truth box.
  * Have an IoU overlap higher than 0.7 with any ground-truth box.
  * A single ground-truth box may assign positive labels to multiple anchors.
* Anchors assigned negative labels:
  * If its IoU is lower than 0.3 for all ground-truth boxes, i.e. the max IoU is lower than 0.3.
* Anchors that neither positive nor negative do not contribute to the training objective. 也就是 ignored anchors 对训练目标没有贡献。



> **Loss Function**
>
> Our loss function for an image is defined as:
>
> $$L({p_{i}},{t_{i}})=\frac{1}{N_{cls}} \sum_{i}L(p_{i}, p^{*}_{i})+\lambda \frac{1}{N_{reg}} \sum_i p^{*}_{i} L_{reg}(t_{i}, t^{*}_{i})$$
>
> Here, $i$ is the index of an anchor in a mini-batch and $p_{i}$ is the predicted probability of anchor $i$ being an object. The ground-truth label $p^{*}_{i}$ is 1 if the anchor is positive, and is 0 is the anchor is negative. $t_{i}$ is a vector representing the 4 parameterized coordinates of the predicted bounding box, and $t^{*}_{i}$ is that of the ground-truth box associated with a positive anchor. 
>
> The classification loss $L_{cls}$ is log loss over two classes (object vs. not object). For the regression loss, we use $L_{reg}(t_{i}, t^{*}_{i}) = R(t_{i} - t^{*}_{i})$ where $R$ is the robust loss function (smooth $L_{i}$)  defined in *Fast R-CNN*.
>
> The two terms are normalized by $N_{cls}$ and $N_{reg}$ and weighted by a balancing parameter $\lambda$. By default we set $\lambda = 10$, and thus both $cls$ and $reg$ terms are roughly equally weighted. We also note that the normalization as above is not required and could be simplified.
>
> For bounding box regression, we adopt the parameterizations of the 4 coordinates following R-CNN:
>
> $t_{x} = (x - x_{a}) / w_{a}, t_{y} = (y - y_{a}) / h_{a}$
>
> $t_{w}=log(w/w_{a}), t_{h}=log(h/h_{a})$
>
> $t^{*}_{x} = (x^{*} - x_{x}) / w_{a}, t^{*}_{y} = (y^{*} - y_{a}) / h_{a}$
>
> $t^{*}_{w}=log(w^{*}/w_{a}), t^{*}_{h}=log(h^{*}/h_{a})$
>
> where $x, y, w$ and $h$ denote the box's center coordinates and its width and height. Variable $x, x_{a}$ and $x^{*}$ are for the predicted box, anchor box, and ground-truth box respectively (likewise for $y, w, h$).

* $L_{cls}$ is log loss; $L_{reg}$ uses the robust loss function (like smooth $L_{1}$).
* 在计算 box regression loss 的时候，$t_{x}$ and $t^{*}_{x}$ 都是经过与 anchor box 编码过的，其中中心点坐标 $(x, y)$ 是经过平移、伸缩变换的，大小 $(w, y)$ 是经过 $log$ 处理的。==[原因？为什么这么做？]==



### Reference

1. [Implementing Anchor generator](https://keras.io/examples/vision/retinanet/#implementing-anchor-generator)
2. [13.4. Anchor Boxes](https://d2l.ai/chapter_computer-vision/anchor.html#anchor-boxes)
3. [(Part 1) Generating Anchor boxes for Yolo-like network for vehicle detection using KITTI dataset.](https://medium.com/@vivek.yadav/part-1-generating-anchor-boxes-for-yolo-like-network-for-vehicle-detection-using-kitti-dataset-b2fe033e5807), 不清晰，没有 generate anchors 的代码
4. [Anchor Boxes — The key to quality object detection](https://towardsdatascience.com/anchor-boxes-the-key-to-quality-object-detection-ddf9d612d4f9), 一些 anchor box 的要点
5. [kuangliu](https://github.com/kuangliu)/**[pytorch-retinanet](https://github.com/kuangliu/pytorch-retinanet)**, `encoder.py` 中有 generate anchor box 的代码
6. [The End of Anchors — Improving Object Detection Models and Annotations](https://towardsdatascience.com/the-end-of-anchors-improving-object-detection-models-and-annotations-73828c7b39f6)
7. [Face detection - An overview and comparison of different solutions](https://www.liip.ch/en/blog/face-detection-an-overview-and-comparison-of-different-solutions-part1)
8. [Stephenfang51](https://github.com/Stephenfang51)/**[faster_RCNN_anchor_box](https://github.com/Stephenfang51/faster_RCNN_anchor_box)**  , Faster R-CNN 生成 anchor box 的思路
9. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks
10. [Bounding Box Encoding and Decoding in Object Detection](https://leimao.github.io/blog/Bounding-Box-Encoding-Decoding/)
11. [Object Detections中Anchors的那些事](https://zhuanlan.zhihu.com/p/42314266)
12. [RetinaNet的Anchor生成策略](https://yinguobing.com/anchor-boxes-of-retinanet/)
13. [一文读懂Faster RCNN](https://zhuanlan.zhihu.com/p/31426458)
14. [K-means聚类生成Anchor box](https://zhuanlan.zhihu.com/p/109968578)
15. 

