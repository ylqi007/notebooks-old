[TOC]

# [7. Input and Output](https://docs.python.org/3.6/tutorial/inputoutput.html)

## 7.1 Fancier Output Formatting
Ways of writing values:
1. *expression* statements, 比如赋值操作等等;
2. `print()` function;
3. Using the `write()` method of file objects, the standard output file can be referenced as `sys.stdout`.

There are two ways to format your output:
1. The first way is to do all the string handling yourself, using string slicing and concatenation 
operations you can create any layout you can imagine.
2. The second way is to use **formatted string literals**, or the `str.format()` method.
3. The `string` module contains a `Template` class what offers yet another way to substitute values into 
strings.

How do you convert values to strings?
1. Python has ways to convert any value to a string: pass it to the `repr()` or `str()` functions.
2. The `str()` function is meant to return representations of values which are fairly human-readable,
while `repr()` is meant to generate representations which can be read by the interpreter. 
3. For objects which don’t have a particular representation for human consumption, `str()` will return 
the same value as `repr()`.
4. Many values, such as numbers or structures like `lists` and `dictionaries`, have the same representation using either function. 
`Strings`, in particular, have two distinct representations.

### 7.1.1 Old string formatting
* [printf-style String Formatting](https://docs.python.org/3.6/library/stdtypes.html#old-string-formatting)


## 7.2 Reading and Writing Files
`open()` returns a **file object**, and is most commonly used with two arguments: `open(filename, mode)`.
* The first argument is a string containing the filename. The second argument is another string containing
a few characters describing the way in which the file will be used.
* Normally, files are opened in **test mode**, that means, you read and write strings from and to the file,
which are encoded in a specific encoding.
* In text mode, the default when reading is to convert platform-specific line endings (`\n` on Unix, 
`\r\n` on Windows) to just `\n`. When writing in text mode, the default is to convert occurrences of `\n` 
back to platform-specific line endings.
* It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the 
file is properly closed after its suite finishes, even if an exception is raised at some point. 
Using with is also much shorter than writing equivalent try-finally blocks. (1) `with` 语句会自动关闭文件；
(2) 避免了 try-finally 常常的语句结构。

### 7.2.1 Methods of File Objects
1. To read a file's contents, call `f.read(size)`, which reads some quantity of data and returns it as 
a `string` (in text mode) or `bytes` object (in binary mode). 
    * *size* is an optional numeric argument. When size is omitted or negative, the **entire contents** 
    of the file will be read and returned; it’s your problem if the file is twice as large as your 
    machine’s memory.
    * If the end of the file has been reached, `f.read()` will return an empty string(' ').
2. `f.readline()` reads **a single line** from the file; a newline character (`\n`) is left at the 
end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
从单个行读取文件的时候，每个行文件的结尾都是 `\n`，除了最后一行可能不是以 `\n` 结尾。这也将使 `f.readline()` 的
return value 变得不确定。
    * For reading lines from a file, you can loop over the **file object**. This is memory efficient, 
    fast, and leads to simple code.
3. If you want to read all the lines of a file in a list you can also use `list(f)` or `f.readlines()`.
4. `f.write(string)` writes the contents of string to the file, returning the number of characters written.
    * Other types of objects need to be converted – either to a `string` (in text mode) or a `bytes` object (in binary mode) – before writing them:
5. `f.tell()` returns an integer giving the file object’s current position in the file represented as 
number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
6. To change the file object’s position, use `f.seek(offset, from_what)`. 

### 7.2.2 Saving structured data with `json`
* [19.2. json — JSON encoder and decoder](https://docs.python.org/3.6/library/json.html#module-json)
