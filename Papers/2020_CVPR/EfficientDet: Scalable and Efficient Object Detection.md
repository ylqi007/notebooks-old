
## Abstract
> 1. First, we propose a weighted bi-directional feature pyramid network (BiFPN), which allows easy and fast multiscale feature fusion;
> 2. Second, we propose a compound scaling method that uniformly scales the resolution, depth, andwidth for all backbone, 
> feature network, and box/class prediction networks at the same time.
> 3.  Based on these optimizations and better backbones, we have developed a new family of object detectors, called EfficientDet

## 1. Introduction
> Based on the one-stage detector paradigm, we examine the design choices for backbone, feature fusion, and class/box network, 
> and identify two main challenges:
> Challenge 1: efficient multi-scale feature fusion.
>   * While fusing different input features, most previous works simply sum them up without distinction; however, since different 
> input features are at different resolutions, we observe they usually contribute to the fused output feature unequally. 
>   * To address this issue, we propose a simple yet highly effective weighted bi-directional feature pyramid network (BiFPN), 
> which introduces learnable weights to learn the importance of different input features, while repeatedly applying top-down 
> and bottom-up multi-scale feature fusion.
> 
> Challenge 2: model scaling:
>   * Inspired by recent works [39], we propose a compound scaling method for object detectors, which jointly scales up 
> the resolution/depth/width for all backbone, feature network, box/class prediction network.
>
> Combining EfficientNet backbones with our propose **BiFPN** and **compound scaling**, we have developed a new family of object detectors, 
> named **EfficientDet**, which consistently achieve better accuracy with much fewer parameters and FLOPs than previous object detectors.


## 2. Related Work
> * **One-Stage Detectors:** without a region-of-interest proposal step.
> 
> To develop efficient detector architectures, such as:
> * One-stage
> * Anchor-free detectors
>
> * **Multi-Scale Feature Representations:** 
>   * One of the main difficulties in object detection is to effectively represent and process multi-scale features.
> 
> * **Model Scaling:** In order to obtain better accuracy, it is common to scale up a baseline detector by employing bigger 
> backbone networks (e.g., from mobile-size models [38, 16] and ResNet [14], to ResNeXt [41] and AmoebaNet [32]), 
> or increasing input image size (e.g., from 512x512 [24] to 1536x1536 [45]). 


## 3. BiFPN
### 3.1 Problem Formulation
> Multi-scale feature fusion aims to aggregate features at different resolutions.

### 3.2 Cross-Scale Connections
> Conventional top-down FPN is inherently limited by the one-way information flow. To address this issue, PANet adds an 
> extra bottom-up path aggregation network, as shown in Figure 2(b). Cross-scale connections are further studied in [20, 18, 42]. 
>
> To improve model efficiency, this paper proposes several optimizations for cross-scale connections:
> 1. First, we remove those nodes that only have one input edge.
> 2. Second, we add an extra edge from the original input to output node if they are at the same level, in order to fuse more features without adding much cost;
> 3. Third, unlike PANet [26] that only has one top-down and one bottom-up path, we treat each bidirectional (top-down & bottom-up) path 
> as one feature network layer, and repeat the same layer multiple times to enable more high-level feature fusion.

### 3.3 Weighted Feature Fusion
> When fusing features with different resolutions, a common way is to first resize them to the same resolution and then sum them up.
> Pyramid attention network, 
> All previous methods treat all input features equally without distinction. However, we observe that since different input 
> features are at different resolutions, they usually contribute to the output feature unequally.
> To address this issue, we propose to add an additional weight for each input, and let the network to learn the importance 
> of each input feature. Based on this idea, we consider three weighted fusion approaches:
> * **Unbounded fusion:**
> * **Softmax-based fusion:**
> * **Fast normalized fusion:**


## 4. EfficientDet
### 4.1 Efficient Architecture
> We employ ImageNet-pretrained EfficientNets as the backbone network. Our proposed BiFPN serves as the feature network, 
> which takes level 3-7 features {P3 , P4, P5, P6 , P7 } from the backbone network and repeatedly applies top-down and 
> bottom-up bidirectional feature fusion. These fused features are fed to a class and box network to produce object class 
> and bounding box predictions respectively.
> 

### 4.2 Compounded Scaling
> We propose a new compound scaling method for object detection, which uses a simple compound coefficient φ to jointly 
> scale up all dimensions of backbone , BiFPN, class/box network, and resolution.
>
> Backbone network: 
> BiFPN network:
> Box/class prediction network:
> Input image resolution



