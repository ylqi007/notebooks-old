# [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)

```bash
docker run -it --rm --runtime=nvidia tensorflow/tensorflow:2.1.1-gpu-jupyter python
```

> As of TensorFlow 2, eager execution is turned on by default. This enables a more interactive frontend to TensorFlow.


## 1. Tensors
> A Tensor is a multi-dimensional array. Similar to NumPy ndarray objects, tf.Tensor objects have a data type and a shape. 
> Additionally, tf.Tensors can reside in accelerator memory (like a GPU). TensorFlow offers a rich library of operations (tf.add, tf.matmul, tf.linalg.inv etc.) that consume and produce tf.Tensors. 
> These operations automatically convert native Python types.

> The most obvious differences between NumPy arrays and tf.Tensors are:
> 1. Tensors can be backed by accelerator memory (like GPU, TPU).[张量可以由加速器内存（如GPU，TPU）支持。]       
> 2. Tensors are immutable.[张量是不变的。]         

### 1.1 Numpy Compatibility
> Converting between a TensorFlow `tf.Tensors` and a NumPy `ndarray` is easy:
> 1. TensorFlow operations automatically convert NumPy ndarrays to Tensors.
> 2. NumPy operations automatically convert Tensors to NumPy ndarrays.

> `Tensors` are explicitly converted to `NumPy ndarrays` using their `.numpy()` method. These conversions are typically cheap since the array and tf.Tensor share the underlying memory representation, if possible. 
> However, sharing the underlying representation isn't always possible since the `tf.Tensor` may be hosted in GPU memory while `NumPy arrays` are always backed by host memory, and the conversion involves a copy from GPU to host memory.
> * `Tensors` 可以通过 `.numpy()` 显式的转换为 `NumPy ndarrays`。
> * `Sharing the underlying representation isn't always possible.`：因为有些 `tf.Tensor` 可能在 GPU Memory 上，`NumPy arrays` 总在 host memory 中。


## 2. GPU Acceleration
> Many TensorFlow operations are accelerated using the GPU for computation. Without any annotations, TensorFlow automatically decides whether to use the GPU or CPU for an operation—copying the tensor between CPU and GPU memory, if necessary. 
> Tensors produced by an operation are typically backed by the memory of the device on which the operation executed.            
> [大部分 `TF Operations` 使用 GPU 加速，TF 可以自动决定使用 GPU 或是 CPU。通常情况下，产生 `Tensor` 的 `Operation` 在哪个设备上，`Tensor` 就会在那个相应的设备上。]

### 2.1 Device Names
> The `Tensor.device` **property** provides a fully qualified string name of the device hosting the contents of the tensor. This name encodes many details, such as an identifier of the network address of the host on which this program is executing and the device within that host. 
> This is required for distributed execution of a TensorFlow program. The string ends with `GPU:<N> `if the tensor is placed on the N-th GPU on the host.           
> * `Tensor.device` 是 Tensor 的一个 property。

### 2.2 Explicit Device Placement
> In TensorFlow, *placement* refers to how individual operations are assigned (placed on) a device for execution. As mentioned, when there is no explicit guidance provided, TensorFlow automatically decides which device to execute an operation and copies tensors to that device, if needed. 
> However, TensorFlow operations can be explicitly placed on specific devices using the `tf.device` context manager.
```python
import time
import tensorflow as tf     # 2.1.1

def time_matmul(x):
  start = time.time()
  for loop in range(10):
    tf.matmul(x, x)

  result = time.time()-start

  print("10 loops: {:0.2f}ms".format(1000*result))

# Force execution on CPU
print("On CPU:")
with tf.device("CPU:0"):
  x = tf.random.uniform([1000, 1000])
  assert x.device.endswith("CPU:0")
  time_matmul(x)

# Force execution on GPU #0 if available
if tf.config.experimental.list_physical_devices("GPU"):
  print("On GPU:")
  with tf.device("GPU:0"): # Or GPU:1 for the 2nd GPU, GPU:2 for the 3rd etc.
    x = tf.random.uniform([1000, 1000])
    assert x.device.endswith("GPU:0")
    time_matmul(x)
```


## 3. Datasets [TensorFlow Dataset Guide](https://www.tensorflow.org/guide/datasets#reading_input_data)
### 3.1 Create a Source Dataset
> Create a source dataset using one of the factory functions like `Dataset.from_tensors`, `Dataset.from_tensor_slices`, or using objects that read from files like `TextLineDataset` or `TFRecordDataset`.

### 3.2 Apply transformations
> Use the transformations functions like `map`, `batch`, and `shuffle` to apply transformations to dataset records.

### 3.3 Iterate
> `tf.data.Dataset` objects support iteration to loop over records.




