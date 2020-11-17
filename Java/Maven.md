[TOC]

## 1. Maven 

### 1.1 Maven 基础介绍

Maven 是一个 Java 项目管理和构建工具，它可以定义项目结构、项目依赖，并使用统一的方式进行自动化构建，是 Java 项目不可缺少的工具。

Java 项目需要的东西：

1. 确定引入哪些依赖包；
2. 确定项目的目录结构；
3. 配置环境，比如 JDK 的版本，编译打包流程，当前版本号等等；
4. 除了使用 IDE 之外，还可以使用命令行工具进行编译，才能够让一个项目在独立的服务器上编译、测试和部署。

Maven 就是专门为 Java 项目打造的管理和构建工具，其主要功能有：

* 提供了一套标准化的项目结构；
* 提供了一套标准化的构建流程（编译，测试，打包，发布……）；
* 提供了一套依赖管理机制。

Maven 项目结构：

```bash
a-maven-project			# 项目名称
├── pom.xml				# 项目描述文件
├── src
│   ├── main
│   │   ├── java		# Java 源代码
│   │   └── resources	# 资源文件
│   └── test
│       ├── java		# 测试源码
│       └── resources
└── target
```

`pox.xml` 描述文件结构：

```xml
<project ...>
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.itranswarp.learnjava</groupId>
	<artifactId>hello</artifactId>
	<version>1.0</version>
	<packaging>jar</packaging>
	<properties>
        ...
	</properties>
	<dependencies>
        <dependency>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
            <version>1.2</version>
        </dependency>
	</dependencies>
</project>

```

* `groupId`, 类似于 Java 的包名，通常是组织名称；
* `artifactId`, 类似于 Java 的类名，通常是项目名称；
* 一个 Maven project 就可以由 `groupId`, `artifactId` and `version` 作为唯一的标识。在引入其他第三方库的时候，也是通过这三个变量确定的。
* 使用 `<dependency>` 声明一个依赖后，Maven 会自动下载这个依赖包，并将其放到 classpath 中。



### 1.2 依赖管理

1. Maven 的第一个作用就是解决依赖管理。只需要声明项目需要的 `abs` jar 包，Maven 会在导入 `abc` jar 包的同时，再判断出 `abc` 依赖的 jar 包，并自动导入。

   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
       <version>1.4.2.RELEASE</version>
   </dependency>
   ```

2. 依赖关系

   Maven定义了几种依赖关系，分别是`compile`、`test`、`runtime`和`provided`。

   * 默认的`compile`是最常用的，Maven会把这种类型的依赖直接放入classpath；
   * `test`依赖表示仅在测试时使用，正常运行时并不需要。最常用的`test`依赖就是 JUnit；
   * `runtime`依赖表示编译时不需要，但运行时需要。最典型的`runtime`依赖是JDBC驱动，例如MySQL驱动；
   * `provided`依赖表示编译时需要，但运行时不需要。最典型的`provided`依赖是Servlet API，编译的时候需要，但是运行时，Servlet服务器内置了相关的jar，所以运行期不需要。

3. Maven如何知道从何处下载所需的依赖？也就是相关的jar包？

   答案是Maven维护了一个中央仓库（[repo1.maven.org](https://repo1.maven.org/)），所有第三方库将自身的jar以及相关信息上传至中央仓库，Maven就可以从中央仓库把所需依赖下载到本地。Maven并不会每次都从中央仓库下载jar包。一个jar包一旦被下载过，就会被Maven自动缓存在本地目录（用户主目录的`.m2`目录），所以，除了第一次编译时因为下载需要时间会比较慢，后续过程因为有本地缓存，并不会重复下载相同的jar包。

### 1.3 构建流程

Maven 不但有标准化的项目结构，而且还有一套标准化的构建流程，可以自动化实现编译，打包，发布，等等。

1. Lifecycle 和 Phase
2. Goal

### 1.4 使用插件

使用Maven构建项目就是执行lifecycle，执行到指定的phase为止。每个phase会执行自己默认的一个或多个goal。goal是最小任务单元。

### 1.5 模块管理

在软件开发中，把一个大项目分拆为多个模块是降低软件复杂度的有效方法。

中央仓库 vs 私有仓库 vs 本地仓库







## Reference

* [Maven 基础](https://www.liaoxuefeng.com/wiki/1252599548343744/1255945359327200)