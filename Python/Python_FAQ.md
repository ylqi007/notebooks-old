[TOC]

## [PEP 8 — the Style Guide for Python Code](https://pep8.org/#descriptive-naming-styles)



## Python - Notes

### [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/)

Use `args` and `kwargs` in Python to add more flexibility to functions.

* **`*args`** and **`**kwargs`** allow you to pass multiple **arguments** and **keyword arguments** to a function.

* Passing a varying number of arguments to a function: collections (list list or tuple) or `*arg`

  * Simply pass a list of a set of all the arguments to functions. Create a list of a set of arguments to pass to functions is inconvenient.

  * **`*args`** allows you to pass a varying number of positional arguments.

    ```python
    # sum_integers_args.py
    def my_sum(*args):
        result = 0
        # Iterating over the Python args tuple
        for x in args:
            result += x
        return result
    
    print(my_sum(1, 2, 3))
    ```

  * `args` is just a name. You are not required to use the name `args`. You can choose any name that you prefer, such as `def my_num(*integer)`

  * The above function still works, even if you pass **the iterable object** as inters instead of `args`. All that matters here is that you use the **unpacking operator(*)**.

  * The iterable object you will get using the unpacking operator (`*`) is **not a list but a tuple**. A `tuple` is similar to a `list` that they both support slicing and iteration. However, lists are mutable while tuples are not.

* Using the Python `kwargs` variable in Function definitions

  * `**kwargs` works just like `*arg`, but instead of accepting positional arguments it accepts **keyword (or named) arguments**.

  * Like `args`, `kwargs` is just a name that can be changed to whatever you want. What is important here is the use of **unpacking operator(**)**.

  * Iterate through the Python `kwargs` dictionary:

    ```python
    # concatenate.py
    def concatenate(**kwargs):
        result = ""
        # Iterating over the Python kwargs dictionary
        for arg in kwargs.values():
            result += arg
        return result
    
    print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))  
    # RealPythonIsGreat!
    
    # concatenate_keys.py
    def concatenate(**kwargs):
        result = ""
        # Iterating over the keys of the Python kwargs dictionary
        for arg in kwargs:
            result += arg
        return result
    
    print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
    # abcde
    ```

* Ordering Arguments in a Function

  * What if you want to create a function that takes a changeable number of both **positional** and **named** arguments? **The order counts.**

  * Non-default arguments have to precede default arguments; `*args` must come before `**kwargs`.

  * To recap, the correct order for parameters is:

    1. Standard arguments
    2. `*args` arguments
    3. `**kwargs` arguments

  * For example, like the following function:

    ```python
    # correct_function_definition.py
    def my_function(a, b, *args, **kwargs):
        pass
    ```

* Unpacking with the asterisk operators: **`*`** & **`**`**

  * The unpacking operators are operators that unpack the values from iterable objects in Python. The single asterisk operator (`*`) can be used to on any iterable that Python provides, while the double asterisks(`**`) can only be used on dictionaries.


### [Python_lambda](python_lambda.md)


### [Python_Input_and_Output](python_input_and_output.md)
### [How are arguments passed by value or by reference in Python?](Pass_by_Reference_in_Python-Background_and_Best_Practices.md)

### python 下划线 [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)

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

* None in slice, [Python for Machine Learning: Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/)

* 



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

