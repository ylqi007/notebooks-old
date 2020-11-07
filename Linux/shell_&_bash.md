
## shell
> shell 是用户和 Linux (或者更准确的说，是用户和 Linux 内核)之间的接口程序。你在提示符后输入的每个命令都是先由 shell 解释，然后传给 Linux 内核。

shell 是一个命令语言解释器(command-language interpreter)。拥有自己内建的 shell 命令集。
此外，shell 也能被系统中其他有效的 Linux 实用程序和应用程序(utilities and application programs)所调用。
不论何时你键入一个命令，它都被 Linux shell所解释，比如 `pwd`, `cp` and `rm`等。

> shell 首先检查命令是否是内部命令，不是的话再检查是否是一个应用程序，这里的应用程序可以是 Linux 本身的实用程序，比如 `ls`, `rm`.
> 然后 shell 试着在搜索路径($PATH)里寻找这些应用程序。搜索路径是一个能找到可执行程序的目录列表。
> 如果你键入的命令不是一个内部命令并且在路径里没有找到这个可执行文件，将会显示一条错误信息。
> 而如果命令被成功的找到的话，shell 的内部命令或应用程序将被分解为系统调用并传给 Linux 内核。


## Bash (The Bourne Again Shell)
* WHY? 为什么要用 bash 来代替 sh 呢？         
Bourne shell 最大的缺点在于它处理用户的输入方面。在 Bourne shell 里键入命令会很麻烦，尤其当你键入很多相似的命令时。而 bash 准备了几种特性使命令的输入变得更容易。 

## shell 变量
* 在 Bash shell 中，每一个变量的值都是字符串，无论你给变量赋值时有没有使用引号，值都会以字符串的形式存储。这意味着，Bash shell 在默认情况下不会区分变量类型，即使你将整数和小数赋值给变量，它们也会被视为字符串，这一点和大部分的编程语言不同。 
* Shell 支持以下三种定义变量的形式：
    * `variable=value`
    * `variable='value'`
    * `variable="value"`
    * 如果 value 不包含任何空白符(例如空格、Tab缩进等)，那么可以不使用引号；如果 value 包含了空白符，那么就必须使用引号包围起来。
    * 注意，赋值号的周围不能有空格。
* 变量使用：
* 使用一个定义过的变量，只要在变量名前面加美元符号 $ 即可。
* 变量名外面的花括号 `{}` 是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界。
* 推荐给所有变量加上花括号 `{}`，这是个良好的编程习惯。
* 以单引号' '包围变量的值时，单引号里面是什么就输出什么，即使内容中有变量和命令（命令需要反引起来）也会把它们原样输出。这种方式比较适合定义显示纯字符串的情况，即不希望解析变量、命令等的场景。
* 以双引号" "包围变量的值时，输出时会先解析里面的变量和命令，而不是把双引号中的变量名和命令原样输出。这种方式比较适合字符串中附带有变量和命令并且想将其解析后再输出的变量定义。
* 严长生的建议：如果变量的内容是数字，那么可以不加引号；如果真的需要原样输出就加单引号；其他没有特别要求的字符串等最好都加上双引号，定义变量时加双引号是最常见的使用场景。
* 将命令的结果赋值给变量
    * variable=`command`
    * variable=$(command)
    * 第一种方式把命令用反引号包围起来，反引号和单引号非常相似，容易产生混淆，所以不推荐使用这种方式；第二种方式把命令用 `$()` 包围起来，区分更加明显，所以推荐使用这种方式。
* 只读变量: readonly
* 删除变量: unset
* 变量类型
    * 1) 局部变量
    * 2) 环境变量
    * 3) shell变量


## Reference:
1. [Shell 风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-shell-styleguide/contents/)
2. [什么是Bash、什么是shell？](https://blog.csdn.net/lizhidefengzi/article/details/74066590)
3. [linux超级基础系列——什么是shell? bash和shell有什么关系？（转）](https://blog.csdn.net/wenlifu71022/article/details/4069929)
4. [Linux Bash Shell学习（七）：shell编程基础——运行Shell脚本、function](https://blog.csdn.net/flowingflying/article/details/5014914?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase)



