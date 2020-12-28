[TOC]

官方提供的 60 mins 的教材。

## Tensors and Operations



## Autograd: Automatic Differentiation

The `autograd` package provides automatic differentiation for all operations on Tensors.

```python
Tensor.requires_grad
Tensor.backward()
Tensor.detach()

```



## Neural Networks

Neural networks can be constructed using the `torch.nn` package.

A typical training procedure for a neural network is as follows:

- Define the neural network that has some learnable parameters (or weights)
- Iterate over a dataset of inputs
- Process input through the network
- Compute the loss (how far is the output from being correct)
- Propagate gradients back into the network’s parameters
- Update the weights of the network, typically using a simple update rule: `weight = weight - learning_rate * gradient`



## Train a Classifier



## Reference

[1. What is PyTorch?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#what-is-pytorch)

[2. Autograd: Automatic Differentiation](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#autograd-automatic-differentiation)

[3. Neural Networks](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#neural-networks)

[4. Training a classifier](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py)

[Torch -- Tensor operations](https://pytorch.org/docs/stable/torch.html)

[*class* `torch.autograd.``Function`](https://pytorch.org/docs/stable/autograd.html#function)

[torch.nn](https://pytorch.org/docs/stable/nn.html#torch-nn)

[Serialization semantics](https://pytorch.org/docs/stable/notes/serialization.html#id1)



