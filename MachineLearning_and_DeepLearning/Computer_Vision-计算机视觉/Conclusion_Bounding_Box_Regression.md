[toc]

### Cascade R-CNN: Bounding Box Regression

> A bounding box $\mathbf{b}=(b_{x}, b_{y}, b_{w}, b_{h})$ contains the four coordinates of an image patch $x$. The task of bounding box regression is to regress a candidate bounding box **b** into a target bounding box **g**, using a regressor $f(x, \mathbf{b})$. This is learned from a training sample $({\mathbf{g}_{i}, \mathbf{b}_{i}})$, so as to minimize the bounding box risk
> $$
> R_{loc}[f] = \sum^{N}_{i=1}L_{loc}(f(x_{i}, \mathbf{b}_{i}), \mathbf{g}_{i})
> $$
> Where $L{loc}$ was a $L_{2}$ loss function in R-CNN, but updated to a smoothed $L_{1}$ loss function in Fast-RCNN.
>
> To encourage a regression invariant to scale and location, $L_{loc}$ operates on the distance vector $\Delta=(\delta_{x},\delta_{y},\delta_{w},\delta_{h})$ defined by 
> $$
> \begin{align}
> \delta_{x} &= (g_{x} - b_{x}) / b_{w}	\\
> \delta_{y} &= (g_{y} - b_{y}) / b_{h}	\\
> \delta_{w} &= log(g_{w} / b_{w})	\\
> \delta_{h} &= log(g_{h} / b_{h})	\\
> \end{align}
> $$
>
> Since bounding box regression usually performs minor adjustments on *b*, the numerical values of  $\Delta$ can be very small. Hence, the risk of $R_{loc}[f]$ is usually much smaller than the classification risk. To improve the effectiveness of multi-task learning, $\Delta$ is usually normalized by its mean and variance, i.e. $\delta_{x}$ is replaced by $\delta'_{x} = (\delta_{x} - \mu_{x}) / \sigma_{x}$
>
> 

