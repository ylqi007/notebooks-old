[TOC]

# [How are arguments passed by value or by reference in Python?](https://www.tutorialspoint.com/how-are-arguments-passed-by-value-or-by-reference-in-python)
* Python uses a mechanism, which is known as **"Call-by-Object"**, sometimes also called **"Call by Object Reference"** or **"Call by Sharing"**
* If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like Call-by-value. It's different, if we pass mutable arguments.
如果传入参数的不可变变量，则是像值传递；如果传入的参数是可变变量，则是 reference 传递。
* All **parameters (arguments)** in the Python language are passed by **reference**. It means if you 
change what a parameter refers to within a function, the change also reflects back in the calling function.

## Pass by Reference in Python
* **Pass** means to provide an argument to a function, 传递意思是向一个函数输入参数;
* **By reference** means that the argument you're passing to the function is a **reference** to a variable
that already exists in memory rather than an independent copy of that variable. 引用传递是将 memory 中已有变量
的 reference 传递给函数，而不是将 memory 中的变量复制一份传递给函数。
* Since you're giving the function a reference to an existing variable, all operations performed on this 
reference will directly affect the variable to which it refers. 所有的操作都会直接作用在 reference 指向的 memory 中的变量。
* Does Python passes arguments by value rather than by reference? 
Not quite. Python passes arguments neither by reference nor by value, but **by assignment**.

### Contrasting Pass by Reference and Pass by Value
* When you pass function arguments by reference, those arguments are only references to existing values. 
* In contrast, when you pass arguments by value, those arguments become independent copies of the original values.
* 引用传递只传递引用，指向的是同一个 variable；值传递是要重新复制一份 variable, 与原有 variable 是相互独立的。
* Python's built-in `id()` returns an integer representing the memory address of the desired object.

### Using Pass by Reference Constructs
* **Avoiding Duplicate Objects**
* **Returning Multiple Values**
    * Luckily, Python already supports returning multiple values. Strictly speaking, a Python function
    that returns multiple values actually returns a `tuple` containing each value.
* Creating Conditional Multiple-Return Functions

## Passing Arguments in Python
* Python passes arguments by assignment. That is, when you call a Python function, each function
argument becomes a variable to which the passed value is assigned. function 中的 argument 都是被赋值的对象。

### Understanding Assignment in Python
* [7.2. Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
    * If the assignment target is an identifier, or variable name, then this name is bound to the object.
    For example, in `x = 2`, x is the name and 2 is the object.
    * If the name is already bound to a separate object, then it's re-bound to the new object. 
* All Python objects are implemented in a **particular structure**. One of the properties of this 
structure is a **counter** that keeps track of how many names have been bound to this object. 
This counter is called a **[reference counter](https://docs.python.org/3/extending/extending.html#reference-counts)**.

### Exploring Function Arguments
* Function arguments in Python are **local** variables. What does that mean? Local is one of Python’s scopes. 
These scopes are represented by the namespace dictionaries mentioned in the previous section. 
You can use `locals()` and `globals()` to retrieve the local and global namespace dictionaries, respectively.

## Replicating Pass by Reference With Python
### Best Practice: Return and Reassign

### Best Practice: Use Dictionaries and lists

## Conclusion
* Python works differently from languages that support passing argument by reference or by value.
* Function arguments become local variable assigned to each value that way passed to the function.