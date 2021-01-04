[TOC]

## [PEP 8 — the Style Guide for Python Code](https://pep8.org/#descriptive-naming-styles)



## Python - Notes

* [Python_lambda](python_lambda.md)
* [Python_Input_and_Output](python_input_and_output.md)
* [How are arguments passed by value or by reference in Python?](Pass_by_Reference_in_Python-Background_and_Best_Practices.md)

* python 下划线 [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)

  * Single and double underscores have a meaning in Python variable and method names. 单下划线和双下划线在 Python 的变量和方法中都有意义。
  * Single Leading Underscore: `_var`. A hint that a variable or method starting with a single underscore is intended for internal use. [Defined in PEP 8](http://pep8.org/#descriptive-naming-styles)
  * Single Trailing Underscore: `var_`. A single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords. [Explained in PEP 8](http://pep8.org/#descriptive-naming-styles)
  * Double Leading Underscore: `__var`. 
    * A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.
    * Double underscore name mangling is fully transparent to the programmer.
    * Name mangling affects **all names** (including variables and methods) that start with two underscore characters in class context.
  * Double Leading and Trailing Underscore: `__var__`
    * Name mangling is **not** applied if a name **starts and ends** with double underscores.
    * Names that have both leading and trailing double underscores reserved for special use in the language. 
  * Single Underscore: `_`
    * Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary of insignificant.

  | Pattern                                    | Example   | Meaning                                                      |
  | ------------------------------------------ | --------- | ------------------------------------------------------------ |
  | **Single Leading Underscore**              | `_var`    | Naming convention indicating a name is meant for internal use.  Generally not enforced by the Python interpreter (except in wildcard  imports) and meant as a hint to the programmer only. |
  | **Single Trailing Underscore**             | `var_`    | Used by convention to avoid naming conflicts with Python keywords. |
  | **Double Leading Underscore**              | `__var`   | Triggers name mangling when used in a class context. Enforced by the Python interpreter. |
  | **Double Leading and Trailing Underscore** | `__var__` | Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes. |
  | **Single Underscore**                      | `_`       | Sometimes used as a name for temporary or insignificant variables  (“don’t care”). Also: The result of the last expression in a Python  REPL. |

  

* Ellipsis -- [What does the Ellipsis object do?](https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do)

  * Ellipsis is used here to indicate a placeholder for the rest of the array dimensions not specified.



## References

* [Using List Comprehensions Effectively](https://realpython.com/courses/using-list-comprehensions-effectively/)
* [Python Type Checking (Guide)](https://realpython.com/python-type-checking/#hello-types)
* [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)
* [Python's map(): Processing Iterables Without a Loop](https://realpython.com/python-map-function/#understanding-map)
* [第112天：Python 到底是值传递还是引用传递](http://www.ityouknow.com/python/2020/01/07/python-function_parameter-112.html)
* [Python函数值传递和引用传递（包括形式参数和实际参数的区别）](http://c.biancheng.net/view/4471.html)
* [Unpack a tuple / list in Python](https://note.nkmk.me/en/python-tuple-list-unpack/)


## PyCharm
* [PyCharm设置每行最大长度限制](https://blog.csdn.net/weixin_42122355/article/details/83373889?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

