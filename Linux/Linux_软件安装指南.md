[TOC]

## 1. 最常见的安装方法 - APT

```bash
sudo apt-get install <software>
```
前提是你的软件列表里有这个软件，这就要求你的源要配好，并且经常 `sudo apt-get update` 保证你的列表最新。
这种方法会自动下载软件包到

---
## 2. deb 安装包

```bash 
sudo dkpg -i package.deb
sudo apt install package.deb
```
* If you want to install deb packages in the command line, you can use either the `apt` command 
or the `dkpg` command. The `apt` command actually uses the `dpkg` command underneath it, but apt 
is more popular and easier to use.

`dpkg` 的详细使用方法：
```bash
   dpkg -r package 删除包 
   dpkg -P package 删除包（包括配置文件）
   dpkg -L package 列出与该包关联的文件 
   dpkg -l packag 显示该包的版本e
   dpkg –unpack package.de 解开 deb 包的内容 
   dpkg -S keyword 搜索所属的包内容 
   dpkg -l 列出当前已安装的包
   dpkg -c package.deb 列出 deb 包的内容 
   dpkg –configure package 配置包
```

* 如果没有 deb 安装包，可以编译安装。

---
## 3. 二进制安装包

bin或run或sh文件或没有扩展名的文件安装（需要安装的二进制包installer） 

---
## 4. PPA 安装

1. **什么是软件仓库?** 软件仓库是一组文件，其中包含各种软件及其版本的信息，以及校验等其的详细信息。
每个版本的 Ubuntu 都有自己的四个官方软件库：

   * Main - Canonical 支持的自由开源软件。
   * Universe - 社区维护的自由开源软件。
   * Restricted - 设备的专有驱动程序。
   * Multiverse - 受版权或法律问题限制的软件。

2. **What is PPA**?  PPA 表示**个人软件包存档 (Personal Package Archive)**。根据软件仓库的概念而言，
PPA 基本上就是一个包含软件信息的网址。

3. 本机系统如何知道这些仓库的位置？仓库信息存储在 `/etc/apt/sources.list` 文件中。

4. 当你运行 `sudo apt update` 命令时，你的系统将使用 [APT 工具](https://link.zhihu.com/?target=https%3A//wiki.debian.org/Apt) 
来检查软件仓库并将软件及其版本信息存储在缓存中。当你使用 `sudo apt install package_name` 命令时，
它通过该信息从实际存储软件的网址获取该软件包。

5. 如果软件仓库中没有关于某个包的信息，你将看到如下错误：`E: Unable to locate package`

6. **为什么要用 PPA？** 当一些软件处于测试阶段或是官方软件库还未来得及加入的时候，终端用户可以通过 PPA 安装。

7. **如何使用 PPA？PPA 是怎么工作的？** 
[PPA](https://link.zhihu.com/?target=https%3A//launchpad.net/ubuntu/%2Bppas) 代表 *个人软件包存档
(Personal Package Archive)*。在这里注意 “个人” 这个词，它暗示了这是开发人员独有的东西，并没有得到分发的
正式许可。Ubuntu 提供了一个名为 Launchpad 的平台，使软件开发人员能够创建自己的软件仓库。终端用户，也就是你，
可以将 PPA 仓库添加到 `sources.list` 文件中，当你更新系统时，你的系统会知道这个新软件的可用性，然后你可以使
用标准的 `sudo apt install` 命令安装它。例如：

   ```bash
   sudo add-apt-repository ppa:dr-akulavich/lighttable
   sudo apt-get update
   sudo apt-get install lighttable-installer
   ```

   概括下上面命令的内容

   ```bash
   sudo add-apt-repository <PPA_info>       <- 此命令将 PPA 仓库添加到列表中。
   sudo apt-get update                      <- 此命令更新可以在当前系统上安装的软件包列表。
   sudo apt-get install <package_in_PPA>    <- 此命令安装软件包。
   ```

8. **为什么使用 PPA？为何不使用 deb 包？** 
答案在于更新的过程。如果使用 DEB 包安装软件，将无法保证在运行 `sudo apt update` 和 `sudo apt upgrade` 
命令时，已安装的软件会被更新为较新的版本。这是因为 `apt` 的升级过程依赖于 `sources.list` 文件。如果文件中没
有相应的软件条目，则不会通过标准软件更新程序获得更新。

9. **官方 PPA vs 非官方 PPA** 

10. **确保 Linux 发行版本可以使用 PPA** 
如果不验证是否适用当前的版本就添加 PPA，当尝试安装不适用于你的系统版本的软件时，可能会看到类似下面的错误: 
`E: Unable to locate package`

11. **如果 PPA 不适用于你的系统版本，该如何安装应用程序？** 尽管 PPA 不适用于你的 Ubuntu 版本，
你仍然可以下载 DEB 文件并安装应用程序。

* 建议使用 Gdebi 安装 deb 文件 [Use GDebi for Quickly Installing DEB Packages in Ubuntu](https://itsfoss.com/gdebi-default-ubuntu-software-center/)

12. **要不要删除 PPA ？如何删除 PPA？** 
* Ubuntu 软件中心无法移除 PPA 安装的软件包，你必须使用具有更多高级功能的 Synaptic 包管理器。 
    * `sudo apt install synaptic`

---
## 5. [Difference Between apt and apt-get Explained](https://itsfoss.com/apt-vs-apt-get-difference/)
### 1. Why apt was introduced in the first place? 为啥那么引入 `apt`?

Debian uses a set of tools called **Advanced Packaging Tool (APT)** to manage this packaging system. 
Don’t confuse it with the command apt, it’s not the same.      
Debian 是 Ubuntu，Linux Mint 等系统的母本系统。Debian 使用一组高级打包工具(APT)管理包系统。这里的 APT 和
命令 apt 是不一样，不要搞混。
          
The `apt` commands have been introduced to solve this problem. apt consists some of the most widely 
used features from `apt-get` and `apt-cache` leaving aside obscure and seldom used features.            
`apt-get` and `apt-cache` 这种命令涉及的内容太底层，Linux 的普通用户并不会涉及，为了简化不必要的复杂性，
`apt` 对这些底层的命令做了整合，对用户更加友好。

**Bottom line: apt=most common used command options from apt-get and apt-cache.**

### 2. Difference between apt and apt-get
While apt does have some similar command options as `apt-get`, it’s not backward compatible with `apt-get`. 
That means it won’t always work if you just replace the `apt-get` part of an `apt-get` command with apt.            
`apt` 是不向后兼容的，也就是说，简单地用 `apt` 替换 `apt-get` 可能会导致命令不工作。          

![](images/apt_commands_1.png)
![](images/apt_commands_2.png)

### 3. Conclusion
* `apt` is a subset of `apt-get` and `apt-cache` commands providing necessary commands for 
package management
* while `apt-get` won’t be deprecated, as a regular user, you should start using `apt `more often. 
作为普通用户，尽量使用 `apt` 就好。

### 4. [Using apt Commands in Linux [Complete Guide]](https://itsfoss.com/apt-command-guide/) 
1. `sudo apt update`: 
Using apt commands to manage packages in Debian and Ubuntu based Linux distributions `apt` actually 
works on a database of available packages. If the database is not updated, the system won’t know 
if there are any newer packages available. This is why updating the repository should be the first 
thing to do in in any Linux system after a fresh install. 
仅仅更新信息，而不更新软件。
2. `sudo apt upgrade`: 
Once you have updated the package database, you can now upgrade the installed packages. The most 
convenient way is to upgrade all the packages that have available updates. 
当用 `sudo apt update` 更新过信息之后，可以直接使用 `sudo apt upgrade` 更新软件。            
The fastest and the most convenient way to update Ubuntu system is by this command: `sudo apt update && sudo apt upgrade -y`
3. `sudo apt install <package1> <package2> <package3>`
4. `sudo apt search <package>`
5. `sudo apt remove <package>`
6. `sudo apt autoremove`
This command removes libs and packages that were installed automatically to satisfy the 
dependencies of an installed package. If the package is removed, these automatically installed 
packages, though useless, remains in the system.
7. `apt show <package>`
8. `sudo apt remove <package>` vs `sudo apt purge <package>`
    * `apt remove` just removes the binaries of a package. It leaves residue configuration files.
    * `apt purge` removes everything related to a package including the configuration files.
    * If you used `apt remove` to a get rid of a particular software and then install it again, your software will have the same configuration files.
    * `Purge` is useful when you have messed up with the configuration of a program. You want to completely erase its traces from the system and perhaps start afresh. And yes, you can use apt purge on an already removed package.
9. `apt list --upgradeable`: Using this command, you can see all the packages that have a newer version ready to be upgraded.
    * `apt list --installed`
    * `apt list --all-versions`

## Reference:
* [软件安装指南](https://wiki.ubuntu.org.cn/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97)
* [How To Install And Remove Software In Ubuntu [Complete Guide]](https://itsfoss.com/remove-install-software-ubuntu/)
* [Ubuntu PPA 使用指南](https://zhuanlan.zhihu.com/p/55250294)
* [Use GDebi for Quickly Installing DEB Packages in Ubuntu](https://itsfoss.com/gdebi-default-ubuntu-software-center/)
* [Ubuntu中PPA源是什么](https://www.cnblogs.com/EasonJim/p/7119331.html)
* [如何在Ubuntu中添加Apt仓库](https://www.myfreax.com/how-to-add-apt-repository-in-ubuntu/)
* [详解Ubuntu软件源](https://www.jianshu.com/p/57a91bc0c594)
* [【linux清障】add-apt-repository是什么意思？](https://blog.csdn.net/qq_25863199/article/details/102799070)
* [全面介绍Ubuntu系统中的PPA，包括使用PPA及删除的方法](https://ywnz.com/linuxjc/4804.html)
* [教你在Ubuntu/Debian系统中添加Apt存储库的两种方法](https://ywnz.com/linux/5844.html)
* [3 Ways to Install Deb Files on Ubuntu [& How to Remove Them Later]](https://itsfoss.com/install-deb-files-ubuntu/)
* [Using apt Commands in Linux [Complete Guide]](https://itsfoss.com/apt-command-guide/) 
* [Difference Between apt and apt-get Explained](https://itsfoss.com/apt-vs-apt-get-difference/)