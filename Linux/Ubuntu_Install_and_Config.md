[TOC]

## Ubuntu Installation
- [ ] UEFI + GPT v.s. BIOS + MBR
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### 1. BIOS vs UEFI
#### 1.1 什么是 BIOS？
BIOS (Basic Input Output System) 从字面意义上称为 “基本输入输出系统”，专门负责系统硬件的各种参数设定，
本质上是“程序”，也就是一组“代码”。

BIOS 程序是用汇编语言编写的。

**BIOS 是做什么的？** 作为计算机开机之后，CPU 要进行处理的第一个“可执行程序”，也就是第一个开机启动项。
它将带领 CPU 去一一识别加载于主板的重要硬件和集成元件，如硬盘、显卡、声卡以及各种接口，然后它按照预设顺序读
取存储器上的操作系统引导文件，如 DOS、Windows、Linux 等。顺利引导系统之后，BIOS 基本功成身退、隐于后台，
如果有需要还可以直接通过系统接口，在系统界面中更改相关设定，以便让整体系统运行更加高效。这就是 BIOS 的使命。
也就是说 BIOS 是用于加载电脑最基本的程序代码，负担着**初始化硬件**，**检测硬件功能**以及**引导操作系统**的任务。

**什么是 BIOS 芯片？** 通常有关电脑所说的 BIOS 芯片，是特指存储 BIOS 那那一块 ROM 芯片，这个特定的 ROM 
芯片主要是存储 BIOS 程序。
ROM 芯片是一个实体物品，是一类芯片，可以存储 BIOS 程序也可以存储其他各种程序、代码，也就是说它的本质就是一个
储存器。它的位置在主机板上一颗小小的快闪 EEPROM 内存模块板中。

**现如今的BIOS类型(两种)**
* **传统 BIOS**：开机 —> BIOS 初始化 —> BIOS 自检 —> 引导操作系统 —> 进入
* **UEFI BIOS**：开机 —> UEFI 初始化 —> 引导操作系统 —> 进入

相比较来说第二种方式节约一步，开机启动也就更快。


#### 1.2 什么是 UEFI？
**UEFI**，全称是 Unified Extensible Firmware Interface，即“统一的可扩展固件接口”，是一种详细描述全新
类型接口的标准，是适用于电脑的标准固件接口，旨在替代 BIOS。

- [ ] TODO: ADD more explaination

![BIOS vs UEFI](https://upload-images.jianshu.io/upload_images/3404443-758ebecaaa9d5f37?imageMogr2/auto-orient/strip|imageView2/2/w/500)


1. MBR 对应的是利用 BISO 选择启动器代码，GPT 对应是利用 UEFI 选择启动。


### 2. MBR vs GPT
#### 2.1 什么是 MBR？
MBR 和 GPT 是两种硬盘分区方案。

MBR 全称是 Master Boot Record，主分区引导记录。


#### 2.2 什么是 GPT？
GPT 全称是 Globally Unique Identifier Partition Table Format (GUID 分区表)，是源于 EFI (可扩展固件接口)
使用的磁盘分区构架。


#### 2.3 MBR v.s. GPT
1. MBR 磁盘最多允许存在 4 个主分区，并且支持磁盘最大容量为 2TB；而 GPT 磁盘最多可允许存在 128 个主分区
（在Windows系统中），支持磁盘的最大容量为18EB（1EB = 1024 PB = 1024 * 1024 TB）。
2. 每个GPT磁盘都存在 Protective MBR，用来防止不能识别 GPT 分区的磁盘管理工具的破坏。

相较于 MBR，GPT 具有以下优点：
1. 得益于 LBA 提升至 64 位，以及分区表中每项 128 位设定，GPT可管理的空间近乎无限大，假设一个扇区大小仍为
512 字节，可表示扇区数为，算下来，可管理的硬盘容量 = 18EB(1EB = 1024 PB = 1,048,576 TB)，2T 在它面前完
全不在话下。按目前的硬盘技术来看，确实近乎无限，不过，以后的事谁知道呢。
2. 分区数量几乎没有限制，由于可在表头中设置分区数量的大小，如果愿意，设置个分区也可以（有人愿意管理这么多分区吗），
不过，目前 windows 仅支持最大 128 个分区。
3. **自带保险**，由于**在磁盘的首尾部分**各带一个 GPT 表头，任何一个受到破坏后都可以通过另一份恢复，
极大地提高了磁盘的抗性（两个一起坏的请出门买彩票）。
4. 循环冗余检验值针对关键数据结构而计算，提高了数据崩溃的检测几率。
5. 尽管目前分区类型不超过百数（十数也没有吧。），GPT 仍提供了 16 字节的 GUID 来标识分区类型，使其更不容易产生冲突。
6. 每个分区都可以拥有一个特别的名字，最长 72 字节，足够写一首七律了。满足你的各种奇葩起名需求。
7. 完美支持 UEFI，毕竟它就是 UEFI 规范的衍生品。在将来全行业 UEFI 的情境下，GPT 必将更快淘汰 MBR。


### 3. BIOS + MBR v.s. UEFI + GPT

1. UEFI + GPT 最好用 64 位操作系统。
2. GPT 能使用大于 2.2 T 的硬盘，MBR 不行。支持最大卷为 18 EB (1EB=1048576TB)。
3. GPT 分区磁盘有备份分区表来提高分区数据结构的完整性。
4. UEFI + GPT 开机启动更快，开机时跳过外设检测，搭载固态硬盘开机时间更短。
5. UEFI + GPT 支持 Secure Boot。通过保护预启动或预引导进程，抵御 bootkit 攻击，从而提高安全性。所有在开机时
比 Windows 内核更早加载，实现内核劫持的技术，都可以称之为 Bootkit。
6. **UEFI + GPT：可用，可启动系统。最常见！未来趋势。**


### 4. 文件系统
* FAT (File Allocation Tables)，文件分配表
* UEFI 分区采用 FAT32
* 微软后期也在限制 FAT32 的使用，大于 32GB 的移动介质如U盘等都推荐采用 exFAT 了

如何选择文件系统，快速回答：如果您不确定，请使用 **Ext4**

Ext4 是大多数 Linux 发行版上的默认文件系统，因为它是旧版 Ext3 文件系统的改进版本。虽然它不是最前沿的文件系统，
但是很好：这意味着 Ext4 是岩石坚固和稳定。

在未来，Linux发行版将逐渐向 BtrFS 转移。 BtrFS 仍然是前沿的，看到很多开发，所以你会想要避免它在生产系统。
数据损坏或其他问题的风险不值得潜在的速度提高。 

“使用 Ext4”的建议只适用与 Linux 系统分区和只有 Linux 访问的磁盘分区。这是因为像 Windows，maxOS 这样的系统
无法读取 Ext4 文件系统。所以如果要格式化要与其他操作系统共享的外部设备(U 盘，移动硬盘等)，则不应该使用 Ext4，
而应该使用 exFAT 或 FAT32。

Reference
* [BIOS到底是什么](https://zhuanlan.zhihu.com/p/89058949)
* [UEFI 引导与 BIOS 引导在原理上有什么区别？](https://www.zhihu.com/question/21672895)
* [UEFI背后的历史](https://zhuanlan.zhihu.com/p/25281151)
* [UEFI是什么？与BIOS的区别在哪里？UEFI详解！](https://www.hack520.com/uefi.html)
* [MBR与GPT](https://zhuanlan.zhihu.com/p/26098509)
* [MBR 与 GPT，关于分区表你应该知道的一些知识 - 硬盘使用知识大全（8）](https://www.eassos.cn/jiao-cheng/ying-pan/mbr-vs-gpt.php)
* [UEFI启动模式下安装Ubuntu 16.04教程](https://blog.csdn.net/Jesse_Mx/article/details/61425361)
* [FAT文件系统与UEFI](https://zhuanlan.zhihu.com/p/25992179)
* [深入理解 ext4 等 Linux 文件系统](https://zhuanlan.zhihu.com/p/44267768)
* [Linux文件系统详解](http://c.biancheng.net/view/880.html)
* [Linux系统简介](http://c.biancheng.net/linux_tutorial/10/)
* [你应该使用哪个Linux文件系统？](http://www.howtoip.com/htg-explains-which-linux-file-system-should-you-choose/)
* [你的页面文件或交换分区有多大？](http://www.howtoip.com/how-big-should-your-page-file-or-swap-partition-be/)
* [http://phillw.net/isos/linux-tools/uefi-n-bios/GrowIt.pdf](https://phillw.net/isos/linux-tools/uefi-n-bios/GrowIt.pdf)
* [Installing Ubuntu with GPT partition table](https://help.ubuntu.com/community/InstallUbuntu11.10OnLenovoEFI/GPT/WLAN/Power/BIOS#Installing_Ubuntu_with_GPT_partition_table)


* [UEFI+GPT与BIOS+MBR各自有什么优缺点？](https://www.zhihu.com/question/28471913)
* [UEFI+GPT与BIOS+MBR各自有什么优缺点？ - 知乎用户的回答 - 知乎](https://www.zhihu.com/question/28471913/answer/155332057)
* [Recommended ways to enter BIOS (Boot Menu) - ThinkPad, ThinkCentre, ThinkStation](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t460p/solutions/ht500222)





---
## Common Configuration
### Chinese Input
* [Fcitx (简体中文)](https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Fcitx_%28%E7%AE%2580%E4%BD%2593%E4%B8%AD%E6%2596%2587%29.html)
* [Fcibutx Chinese Input Setup on Ubuntu for Gaming](https://leimao.github.io/blog/Ubuntu-Gaming-Chinese-Input/)
* [How To Uninstall ibus On Ubuntu 16.04 LTS](https://installlion.com/ubuntu/xenial/main/i/ibus/uninstall/index.html)
* 在安装 `fictx` 后，系统默认有两种输入法，`fixtx` and `ibux`。此时 `Ctrl + Shift` 无法切换 `fictx` 的中英文。此时应该删掉
`Settings -> Region & Language -> Input Sources` 中加入的中文输入，只留下 `English(US)` 就好了。
    * ![](images/Input_Sources.png)
* [Can't change from iBus to fcitx](https://askubuntu.com/a/1194876)
* [ubuntu设置fcitx快捷键实现中英文输入法切换](https://blog.csdn.net/jumpingpig/article/details/104743917)
* [禁用 fcitx 额外键切换输入法 ](http://einverne.github.io/post/2019/08/disable-fcitx-extra-key-for-trigger-input-method.html)
* fcitx 无法在 firefox 使用 googlepinyin
* ![](images/fcitx_input_method_configuration.png)
    * `Trigger Input Method = Ctrl + Space`, 按下 `Ctrl + Spce` 的时候，会启动中文输入，随后可以通过 `Shift` 切换中英文输入。
    * 如果没有提前按过 `Ctrl + Space` 启动的话，单独按下 `Shift` 是没有反映的。
* [Ubuntu安装搜狗输入法后修改默认英文输入状态的方法](https://blog.csdn.net/ameyume/article/details/87091652)

### Ubuntu Shell 命令行路径缩短
* [Ubuntu shell 命令行路径缩短](https://blog.csdn.net/aiqianqi1796/article/details/101835940)
* [To change it for the current terminal instance only](https://askubuntu.com/a/145626)
    * 将 `\w` 改为 `\W`;
    * 删除 `@\h`.

### Install VS Code
* [Visual Studio Code on Linux](https://code.visualstudio.com/docs/setup/linux)
    * Once installed, the `Snap` daemon will take care of automatically updating S Code in the background.
    ```bash
    sudo snap install --classic code
    ```

### [Install Typora](https://typora.io/#linux)
```bash
# or run:
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -

# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update

# install typora
sudo apt-get install typora
```

### Copy and Paste in Terminal
* [为什么Ctrl + V不能粘贴在Bash（Linux Shell）中？](https://qastack.cn/superuser/421463/why-does-ctrl-v-not-paste-in-bash-linux-shell)
* [Gnome-Terminal - How do I reset keyboard shortcuts?](https://askubuntu.com/a/891203)
  ```
  dconf reset -f /org/gnome/terminal/legacy/keybindings/
  ```

### Ubuntu 20.04 Press ctrl c to cancel all filesystem checks in progress
* [How to skip filesystem checks during boot](https://askubuntu.com/questions/1250119/how-to-skip-filesystem-checks-during-boot)

### Ubuntu Hot Corners
* [How to Enable Hot Corners in Ubuntu 18.04, 19.04](http://ubuntuhandbook.org/index.php/2019/07/enable-hot-corners-ubuntu-18-04-19-04/)


### Linux `/boot` 分区是否需要？
下次学习 UEFI 系统安装。

References:
* [Linux / boot分区的建议大小是多少？](https://qastack.cn/server/334663/what-is-the-recommended-size-for-a-linux-boot-partition)
* [Installing ubuntu do I really need a boot partition?](https://superuser.com/questions/66015/installing-ubuntu-do-i-really-need-a-boot-partition)
* [Linux分区方案不要划分/boot分区](https://blog.csdn.net/gao_yu_long/article/details/54783476)
* [GRUB (简体中文)](https://wiki.archlinux.org/index.php/GRUB_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#UEFI_%E7%B3%BB%E7%BB%9F)


### Install Git
* Install
    ```bash
    sudo apt install -y git
    ```
* [廖雪峰 - Git - 远程仓库](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)
    * 因为 GitHub 需要识别出你推送的提交确实是你推送的，而不是别人冒充的，而 Git 支持 SSH 协议，所以，GitHub 只要
    知道了你的公钥，就可以确认只有你自己推送。
    * GitHub 允许添加多个 Key。可以把公司和家里的每台电脑都添加到 GitHub，就可以在每台电脑上往 GitHub 推送。
    * 在 GitHub 上免费托管的 Git 仓库，任何人都可以看到（但是只有自己才能修改），所以不要把敏感信息放上去。
    * 如果不想让别人看到自己的 Git 仓库，有两个方法：1.交钱购买 private 仓库，这样别人就不可读，更不可写；2.自己
    手动搭建 Git 服务器。
* [Connecting to GitHub with SSH](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh)
    * Using the SSH protocol, you can connect and authenticate to remote servers and services. With SSH keys,
    you can connect to GitHub without supplying your username or password at each visit.
    * Checking for existing SSH keys.
    * Generating and adding a new SSH key to your GitHub account. 
* [Adding a new SSH key to your GitHub account](https://docs.github.com/en/enterprise-server@2.20/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

### Reset Shortcuts
* [Gnome-Terminal - How do I reset keyboard shortcuts?](https://askubuntu.com/questions/891199/gnome-terminal-how-do-i-reset-keyboard-shortcuts)

### snap 安装
* [Ubuntu 中 snap 包的安装、删除，更新使用入门教程](https://m.linuxidc.com/Linux/2018-05/152385.htm)
* [Ubuntu 推出的Snap应用架构有什么深远意义?](https://www.zhihu.com/question/47514122)
* [How Microsoft Lost the API War](https://www.joelonsoftware.com/2004/06/13/how-microsoft-lost-the-api-war/)

### Install Firefox-ESR
* 不同用户使用不同配置文件的 Firefox 安装：[如何使用两个Firefox配置文件？](https://qastack.cn/ubuntu/660147/how-can-i-use-two-firefox-profiles)
* [How To Install Firefox ESR In Ubuntu Or Linux Mint (PPA Or Snap) ](https://www.linuxuprising.com/2018/11/how-to-install-firefox-esr-in-ubuntu-or.html)
* `sudo apt install firefox-esr --fix-missing`
* firefox versions
    ```bash
    ylqi007:~$ ll /usr/bin/firefox*
    lrwxrwxrwx 1 root root 25 Oct 13 12:42 /usr/bin/firefox -> ../lib/firefox/firefox.sh*
    lrwxrwxrwx 1 root root 29 Oct 13 08:14 /usr/bin/firefox-esr -> ../lib/firefox-esr/firefox.sh*
    ```
* 此时我的电脑上有两个版本的 firefox (firefox, i.e. normal version 81; firefox-esr, i.e. 78.4 esr version).
* Set `firefox-esr` as the default `firefox` and development firefox version as `firefox-dev`.
此时将 firefox 添加到 dock 后，点击打开 firefox 就是 firefox-esr。
  ```bash
  sudo mv /usr/bin/firefox /usr/bin/firefox-dev     # Alias normal firefox as firefox-dev
  sudo mv /usr/bin/firefox-esr /usr/bin/firefox     # Alias firefox esr as default firefox
  ```

### Install Anaconda
* [Installing on Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
* Reopen terminal
* [Conda command not found](https://stackoverflow.com/questions/35246386/conda-command-not-found/44319368)
* [How do I prevent Conda from activating the base environment by default?](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default)
    * `conda config --set auto_activate_base false`

### Launch using Dedicated Graphics Card
* [Add "Launch using Dedicated Graphics Card" option when using proprietary Nvidia Graphics](https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/280)
* Currently the option to right click an app and "Launch using Dedicated Graphics Card" is only available
**when using grapics drivers**, as it reliefs of the detection of switcheroo for power management. 

### Install Mendeley
* [How to install a deb file, by dpkg -i or by apt?](https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt)
* Downlonad `deb` file.
* `sudo apt install ./mendeley*.deb`

### Snap - Install 
* Todoist
    `sudo snap install todoist`
* GitKraken
    `sudo snap install gitkraken --classic`


## Ubuntu Config
### Tweak Tool Installation
```bash
$ sudo apt install gnome-tweak-tool
```

### Extensions
* Dash to dock
* Lock screen background
    * [Ubuntu 18.04 - Preferences not opening](https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet/issues/456) 	`sudo apt install gir1.2-clutter-1.0`

### Ubuntu 18.04 Desktop – How to set ‘view items as a list’ as default

`gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'`


---
## References
* [The Ubuntu lifecycle and release cadence](https://ubuntu.com/about/release-cycle)
* [在 Linux 环境下能用 Homebrew 吗？](https://www.zhihu.com/question/20022687)
* [廖雪峰 - Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
* [Here’s How to Find Out Which Desktop Environment You are Using](https://itsfoss.com/find-desktop-environment/)
* [Fish shell 入门教程](http://www.ruanyifeng.com/blog/2017/05/fish_shell.html)
* [rsync 用法教程](http://www.ruanyifeng.com/blog/2020/08/rsync.html)

* [「固态科普」M.2接口、SATA接口有啥区别？](https://zhuanlan.zhihu.com/p/142976857)
