
## Dimension Cluster [YOLO 9000]
YOLOv2 中原文给出的解释是：
> Instead of choosing priors by hand, we run k-means clustering on the training set bounding boxes to 
> automatically find good priors. If we use standard k-means with Euclidean distance, larger boxes generate
> more error than smaller boxes. However, what we really want are priors that leads to good IOU scores,
> which is independent of the size of box. Thus for our distance metrix we use:
> $d(box, centroid) = 1 - IOU(box, centroid)$
> * 通过 k-means 算法选择 prior bounding boxes, i.e. prior anchors;
> * 为了避免 box size 大小引入的偏差，定义 distance 为 $d(box, centroid) = 1 - IOU(box, centroid)$;
 


## Reference
[YunYang's Notes](https://yunyang1994.github.io/2018/12/28/YOLOv3/)