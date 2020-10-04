import math
import numpy as np

img_shape = (300, 300)
feat_shape = (3, 3)
anchor_size = (207, 261)
anchor_ratio = [2, 0.5]
offset = 0.5
dtype = np.float32
step = 100


def ssd_anchor_one_layer(img_shape,
                         feat_shape,
                         anchor_size,
                         anchor_ratio,
                         offset=0.5):
    y, x = np.mgrid[0:feat_shape[0], 0:feat_shape[1]]
    print('================== Original y ==================')
    print(y)
    # Normalization
    y = (y.astype(dtype) + offset) * step / img_shape[0]
    x = (x.astype(dtype) + offset) * step / img_shape[1]
    print('================== Normalized y ==================')
    print(y)
    # Expand dims to support easy broadcasting
    y = np.expand_dims(y, -1)
    x = np.expand_dims(x, -1)
    print('================== Expanded y ==================')
    print(y)

    # Compute relative height and width
    num_anchors = len(anchor_size) + len(anchor_ratio)
    h = np.zeros((num_anchors,), dtype=dtype)
    w = np.zeros((num_anchors,), dtype=dtype)

    h[0] = anchor_size[0] / img_shape[0]
    w[0] = anchor_size[0] / img_shape[0]
    di = 1
    if len(anchor_size) > 1:
        h[1] = math.sqrt(anchor_size[0] * anchor_size[1]) / img_shape[0]
        w[1] = math.sqrt(anchor_size[0] * anchor_size[1]) / img_shape[1]
        di += 1
    for i, r in enumerate(anchor_ratio):
        h[i + di] = anchor_size[0] / img_shape[0] / math.sqrt(r)
        w[i + di] = anchor_size[0] / img_shape[1] * math.sqrt(r)
    return y, x, h, w