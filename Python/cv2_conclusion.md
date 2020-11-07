[TOC]
# cv2

* []()

## cv2 coordinates
[OpenCV Point(x,y) represent (column,row) or (row,column)](https://stackoverflow.com/questions/25642532/opencv-pointx-y-represent-column-row-or-row-column)

`image = image[:, ::-1, :]`

![](.images/flip_image.png)

## cv2, image display
* [CV01-OpenCV窗口手动关闭后堵塞程序运行的问题](https://jameslei.com/cv01-opencv-cjxbqdb52000b9ys1kjj31yn0)


## [CV2: Geometric Transformations of Images](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)
* `cv2.warpAffine` and `cv2.warpPerspective`
* **Scaling** Scaling is just resizing of the image. OpecCV comes with a function `cv2.resize()` for this purpose.
    * Scaling factor
    * Interpolation methods: `cv2.INTER_AREA` for shrinking, `cv2.INTER_CUBIC` and `cv2.INTER_LINEAR` for zooming.
* **Translation** Translation is the shifting of object's location. Let the shift in (x, y) direction be (tx, ty),
you can create the transformation matrix **M**.
    * `cv2.warpAfine()` 
* **Rotation** Transformation matrix. OpenCV provides scaled rotation with adjustable center of rotation so that
you can rotate at any location you perfer.
    * `cv2.getRorationMatrix2D`
* **Affine Transformation** In affine transformation, all parallel lines in the original image will still be
parallel in the output image.
    * `cv2.getAffineTransform`
    * `cv2.warpAffine`
* **Perspective Transformation**
    * `cv2.getPerspectiveTransform`
    * `cv2.warpPerspective`
* **Additional Resources:** [“Computer Vision: Algorithms and Applications”, Richard Szeliski]()


## Reading and saving image files with Python, OpenCV (`imread`, `imwrite`)
[cv2_read_write_image.py](cv2_read_write_image.py)

### Read and write images in color (BGR)
* Read an image file with `cv2.imread()`
    * Color image files are read as a **3D** ndarray of `row(height) x column(width) x color(3)`.
    * `img = cv2.imread('images/Lenna.png')    # BGR`
* Write ndarray as an image file with `cv2.imwrite()`
    * `cv2.imwrite("images/blue_lenna.jpg", blue)`

### Read and write images in grayscale
* Read an image file with `cv2.imread()`
    * `img_gray = cv2.imread('images/Lenna.jpg', cv2.IMREAD_GRAYSCALE)`
* Write ndarray as an image file with `cv2.imwrite()`
    * If 2D ndarray of `row(height) x column(width)` is specified as the argument of `cv2.imwrite()`, it is saved as a grayscale image file.
    * If you save 2D ndarray to a file and read it again with `cv2.imread()`, it will be read as 3D ndarray in which each color is the same value.

### Notes on cv2.imread()
* `cv2.imread()` does not raise an exception. `cv2.imread()` 并不会报异常。
    * 当文件路径不存在，只会 return `None`；当文件存在却不是图片的时候，也返回 `None`，because `None` is regarded as `False`.
* JPEG library

### If images cannot be read with cv2.imread()
* Check the current directory
* Supported formats for `cv2.imread()`

References:
* [Reading and saving image files with Python, OpenCV (imread, imwrite)](https://note.nkmk.me/en/python-opencv-imread-imwrite/)


---
## Convert BGR and RGB with Python, OpenCV (cvtColor)
### OpenCV is BGR, Pillow is RGB
* When reading a color image file, OpenCV `imread()` reads as a NumPy array ndarray of row `(height) x column (width) x color (3)`. 
The order of color is BGR `(blue, green, red)`. `cv2.imread()` 读入图片的时候，返回的是 3D 的 `ndarray`。
* When performing image processing with Pillow, you can convert `ndarray` to a `PIL.Image` object with `Image.fromarray()`, 
but in Pillow the color order assumes `RGB (red, green, blue)`.
* If you want to convert ndarray and PIL.Image objects to use both Pillow and OpenCV functions, you need to convert BGR and RGB.
如果想通过 convert ndarray 和 PIL.Image，并用 Pillow 和 OpenCV 函数处理，要先将 BGR 转换成 RGB。

### Convert BGR and RGB with OpenCV function cvtColor()
* 当用 `cv2.imwrite(img)` 的时候，`img` 应该是 `BGR` 模式，否则保存的时候，生成的图片会有颜色失真。

### Convert BGR and RGB without using cvtColor()
* Converting BGR and RGB can be realized without using `cvtColor()`.
```python
im_bgr = cv2.imread('data/src/lena.jpg')

im_rgb = im_bgr[:, :, [2, 1, 0]]
Image.fromarray(im_rgb).save('data/dst/lena_swap.jpg')

im_rgb = im_bgr[:, :, ::-1]
Image.fromarray(im_rgb).save('data/dst/lena_swap_2.jpg')
```

References:
* [Convert BGR and RGB with Python, OpenCV (cvtColor)](https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/)
* [ColorConversionCodes](https://docs.opencv.org/3.4.0/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0)


---
## Image processing with Python, NumPy
* By reading the image as a NumPy array ndarray, various image processing can be performed using NumPy functions.
读入 image 之后，保存为 ndarray 的时候，可以用 `NumPy` function 处理图片。
* Even when using OpenCV, OpenCV for Python treats image data as ndarray, so it is useful to know how to use NumPy (ndarray). 
In addition to OpenCV, there are many libraries such as scikit-image that treat images as ndarray.
在很多 package 处理 image 的时候，image 的保存形式是 `ndarray`

### Read and write images
* Passing the image data ready by `PIL.Image.open()` to `np.array()` returns 3D `ndarray`, whose shape is `(row (height), column (width), color (channel))`.
    ```python
    import numpy as np
    from PIL import Image
    img = np.array(Image.open("images/Lenna.png"))
    ```
    * The order of colors (channels) is RGB (red, green, blue). Note that it is different from the case of reading with `cv2.imread()` of OpenCV.
* If you convert the image to grayscale with `convert('L')` and then pass it to `np.array()`, it returns 2D ndarray whose shape is `(row (height), column (width))`.
    * The order of colors (channels) is `RGB (red, green, blue)`. Note that it is different from the case of reading with `cv2.imread()` of OpenCV.
    ```python
    import numpy as np
    from PIL import Image
    
    im_gray = np.array(Image.open('data/src/lena.jpg').convert('L'))
    print(im_gray.shape)    # (225, 400)
    ```
* You can also get `ndarray` from `PIL.Image` with n`p.asarray()`. `np.array()` returns a **rewritable** ndarray, while `np.asarray()` returns a non-rewritablendarray.
* The data type dtype of the read ndarray is `uint8` (8-bit unsigned integer).
* If you want to process it as a floating point number float, you can convert it with `astype()` or specify the data type in the second argument of `np.array()` and `np.asarray()`.

### How to save NumPy array ndarray as image file
* Passing ndarray to `Image.fromarray()` returns PIL.Image. It can be saved as an image file with `save()` method.
* A grayscale image (2D array) can also be passed to `Image.fromarray()`. mode automatically becomes 'L' (grayscale). It can be saved with save().
* **If the data type dtype of ndarray is float etc., an error will occur**, so it is necessary to convert to uint8.
* Note that if the pixel value is represented by `0.0` to `1.0`, it is necessary to multiply by 255 and convert to uint8 and save.

### Examples of image processing with NumPy (`ndarray`)
#### Generation of single color image and concatenation

#### Color reduction
* Cut off the remainder of the division using `//` and multiply again, the pixel values become discrete and the number of colors can be reduced.

#### Binarization
#### Trimming with slice
#### Split with slice or function
* `numpy.vsplit()`
* `numpy.hsplit()`
* `numpy.array_split()`
#### Rotate and flip

References:
* [Image processing with Python, NumPy](https://note.nkmk.me/en/python-numpy-image-processing/)
* [How to use Pillow (PIL: Python Imaging Library)](https://note.nkmk.me/en/python-pillow-basic/)
* [Image file formats](https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html)
* [NumPy: Slicing ndarray](https://note.nkmk.me/en/python-numpy-ndarray-slice/)

---
### cvtColor
* [Convert BGR and RGB with Python, OpenCV (cvtColor)](https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/)
    * When the image file is read with the OpenCV function `imread()`, the order of colors is BGR (blue, green, red). 
    On the other hand, in Pillow, the order of colors is assumed to be RGB (red, green, blue).
    * Therefore, if you want to use both the Pillow function and the OpenCV function, you need to convert BGR and RGB.
    * When reading a color image file, OpenCV imread() reads as a NumPy array ndarray of row (height) x column (width) x color (3). The order of color is BGR (blue, green, red).
        
        
References:
* [Reading and saving image files with Python, OpenCV (imread, imwrite)](https://note.nkmk.me/en/python-opencv-imread-imwrite/)
* [Convert BGR and RGB with Python, OpenCV (cvtColor)](https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/)
* [Image processing with Python, NumPy](https://note.nkmk.me/en/python-numpy-image-processing/)

## Reference
* [How can I rename a conda environment?](https://stackoverflow.com/questions/42231764/how-can-i-rename-a-conda-environment)
* [Basic python file-io variables with enumerate](https://stackoverflow.com/questions/6473283/basic-python-file-io-variables-with-enumerate)