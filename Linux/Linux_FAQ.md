[TOC]

---
`yq` 

`coreutils`



## TODO

- [ ] 下次需要重新装系统的时候，好好研究、记录分区安装的问题。 GPT + UEFI

---
## Linux FAQ

* [How can I check if a directory exists in a Bash shell script?](https://stackoverflow.com/questions/59838/how-can-i-check-if-a-directory-exists-in-a-bash-shell-script)
* [How to create a link to a directory [closed]](https://stackoverflow.com/questions/9587445/how-to-create-a-link-to-a-directory)
* [Missing System Settings after removing some packages](https://askubuntu.com/questions/453440/missing-system-settings-after-removing-some-packages)
    * [ubuntu 系统设置东西少了很多，重新安装系统设置选项。](https://blog.csdn.net/hanshileiai/article/details/45868577)
    * unity-control-center
    * gnome-control-center
* [How to Fix the No Sound Issue in Ubuntu](https://www.maketecheasier.com/fix-no-sound-issue-ubuntu/)

* [Setting up permissions on a script](https://bash.cyberciti.biz/guide/Setting_up_permissions_on_a_script)
* [Fcitx Chinese Input Setup on Ubuntu for Gaming](https://leimao.github.io/blog/Ubuntu-Gaming-Chinese-Input/)
* [Ln Command in Linux (Create Symbolic Links)](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/)
* [REISUB stopped working [SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=256388)
  * **For ThinkPad T460p:** Press and hold Alt, then press PrScn and release, then enter **reisub** to reboot; and the same procedure using **reisuo** to shutdown.
* 'grub rescue>` error: symbol 'grub_file_filters' not found.
* [如何使用 U 盘安装 Ubuntu 操作系统？](https://www.zhihu.com/question/20565314)
  * 启动 Startup Disk Creator

### DiskSpace
1. UEFI、GPT是“新”技术，那么就必然有较旧技术（BIOS+MBR）更先进、更NB的地方。

2. **GPT及其优势:** **GPT**和**MBR**是两种不同的分区方案。目前在Windows下广泛采用的磁盘分区方案仍然是MBR分区结构，但不容怀疑GPT是今后的趋势。

   1. 为了方便计算机访问硬盘，把硬盘上的空间划分成许许多多的区块（英文叫sectors，即扇区），然后给每个区块(sector)分配一个地址，称为逻辑块地址（即LBA）。

   2. 在MBR磁盘的第一个扇区内保存着**启动代码**和**硬盘分区表**。**启动代码**的作用是指引计算机从活动分区引导启动操作系统（BIOS下启动操作系统的方式）；**分区表**的作用是记录硬盘的分区信息。**在MBR中，分区表的大小是固定的，一共可容纳4个主分区信息。**在MBR分区表中逻辑块地址采用32位二进制数表示，因此一共可表示2^32（2的32次方）个逻辑块地址。如果一个扇区大小为512字节，那么硬盘最大分区容量仅为2TB。

   3. 在GTP磁盘的第一个数据块中同样有一个与**MBR**（主引导记录）类似的标记，叫做PMBR。**PMBR的作用是，当使用不支持GPT的分区工具时，整个硬盘将显示为一个受保护的分区，以防止分区表及硬盘数据遭到破坏。**UEFI并不从PMBR中获取GPT磁盘的分区信息，它有自己的分区表，即GPT分区表。

   4. GPT的分区方案之所以比MBR更先进，是因为**在GPT分区表头中可自定义分区数量的最大值**，也就是说**GPT分区表的大小不是固定的。**在Windows中，微软设定GPT磁盘最大分区数量为128个。另外，GPT分区方案中逻辑块地址（LBA）采用64位二进制数表示，可以计算一下2^64是一个多么庞大的数据，以我们的需求来讲完全有理由认为这个大小约等于无限。**除此之外，GPT分区方案在硬盘的末端还有一个备份分区表，保证了分区信息不容易丢失。**

   5. | ![](https://www.iruanmi.com/img/2013/06/1306MBR.jpg) | ![](https://www.iruanmi.com/img/2013/06/1306gpt.jpg) |
      | ---------------------------------------------------- | ---------------------------------------------------- |
      | MBR分区结构                                          | GPT分区结构                                          |

3. **UEFI及其优势：**UEFI是BIOS的一种升级替代方案。UEFI之所以比BIOS强大，是因为UEFI本身已经相当于一个微型操作系统，其带来的便利之处在于：

   1. **首先，**UEFI已具备文件系统的支持，它能够直接读取FAT分区中的文件；什么是文件系统？简单说，文件系统是操作系统组织管理文件的一种方法，直白点说就是把硬盘上的数据以文件的形式呈现给用户。Fat32、NTFS都是常见的文件系统类型。
   2. **其次，**可开发出直接在UEFI下运行的应用程序，这类程序文件通常以efi结尾。既然UEFI可以直接识别FAT分区中的文件，又有可直接在其中运行的应用程序。那么完全可以**将Windows安装程序做成efi类型应用程序，然后把它放到任意fat分区中直接运行即可**，如此一来安装Windows操作系统这件过去看上去稍微有点复杂的事情突然就变非常简单了，就像在Windows下打开QQ一样简单。而事实上，也就是这么一回事。要知道，这些都是BIOS做不到的。因为BIOS下启动操作系统之前，必须从硬盘上指定扇区读取系统启动代码（包含在主引导记录中），然后从活动分区中引导启动操作系统。对扇区的操作远比不上对分区中文件的操作更直观更简单，所以在BIOS下引导安装Windows操作系统，我们不得不使用一些工具对设备进行配置以达到启动要求。而在UEFI下，这些统统都不需要，**不再需要主引导记录，不再需要活动分区，不需要任何工具，只要复制安装文件到一个FAT32（主）分区/U盘中，然后从这个分区/U盘启动，安装Windows就是这么简单**。

4. **MBR+BIOS** 该退出历史舞台了。**GPT+UEFI** 拥有更好的性能与更高的安全性。

5. If you have already installed Linux system such as Ubuntu and you want to check if it's MBR, you the `gdisk -l` command:

   ![](https://linoxide.com/wp-content/uploads/2019/09/02-check-mbr-partition.png)

6. With GPT there is no need for primary, extended partitions or logical drives, which means all of the partitions are the same.

7. Convert a Ubuntu MBR drive to a GPT, and make Ubuntu boot from EFI

8. 

### Linux 磁盘管理
1. Linux 分区建议：
    * `swap`分区，即虚拟内存；该分区没有对应的目录，故用户无法访问。Linux下的 swap 分区即为虚拟内存.虚拟内存用于当系统内存空间不足时，
    先将临时数据存放在swap分区，等待一段时间后，然后再将数据调入到内存中执行.所以说，**虚拟内存只是暂时存放数据，在该空间内并没有执行。**
    **Ps 虚拟内存:** 虚拟内存是指将硬盘上某个区域模拟为内存.因此虚拟内存的实际物理地址仍然在硬盘上.虚拟内存，
    或者说swap分区只能由系统访问，其大小为物理内存的2倍。
    * `boot`分区，存放操作系统的内核该分区。对应于`/boot`目录，约100MB.该分区存放Linux的Grub(bootloader)和内核源码。
    用户可通过访问`/boot`目录来访问该分区.换句话说，用户对`/boot`目录的操作就是操作该分区。
    * `/` 根分区，整个操作系统的根目录；在Linux操作系统中，除`/boot`目录外的其它所有目录都对应于该分区.因此，用户可通过访问除`/boot`目录外的其它所有目录来访问该分区。
    * `/var`分区，可以避免日志文件的大小失控；
    * `/home`分区，控制用户占用的空间大小。

* [Linux系统分区认识总结](https://blog.csdn.net/lxlong89940101/article/details/84643480)
* [5.1. 系统分区](https://gtcsq.readthedocs.io/en/latest/linux_tools/disk_note.html#id2)
* [Linux磁盘管理之常用命令](https://blog.csdn.net/Leichelle/article/details/8763823)

### References:

* [DiskSpace](https://help.ubuntu.com/community/DiskSpace)
* [How can I detect whether my disk is using GPT or MBR from a terminal?](https://askubuntu.com/questions/387351/how-can-i-detect-whether-my-disk-is-using-gpt-or-mbr-from-a-terminal)
    * To check if the disk is using GPT or MBR: `sudo gdisk -l /dev/sda`
* [UEFI+GPT引导基础篇 ：什么是GPT，什么是UEFI？ ](https://www.cnblogs.com/sddai/p/6351715.html)
* [BIOS, UEFI, MBR, Legacy, GPT等概念整理](https://zhuanlan.zhihu.com/p/36976698)
* [对硬盘进行分区时，GPT和MBR有什么区别？](https://blog.csdn.net/hunanchenxingyu/article/details/47049663)
* [如何免重装无损磁盘MBR转GPT？](https://www.disktool.cn/content-center/gpt-mbr/how-to-convert-gpt-to-mbr-without-data-loss.html)
* [最好的方法是将磁盘GPT转换为MBR（或者MBR到GPT）而不会丢失数据](https://www.remosoftware.com/info/cn/convert-gpt-mbr-without-data-loss/)
* [How can I change/convert a Ubuntu MBR drive to a GPT, and make Ubuntu boot from EFI?](https://askubuntu.com/questions/84501/how-can-i-change-convert-a-ubuntu-mbr-drive-to-a-gpt-and-make-ubuntu-boot-from)
* [如何将Ubuntu MBR驱动器更改/转换为GPT，并使Ubuntu从EFI引导？](https://qastack.cn/ubuntu/84501/how-can-i-change-convert-a-ubuntu-mbr-drive-to-a-gpt-and-make-ubuntu-boot-from)
* [How do I convert my EC2 Ubuntu instance's default MBR partitioning scheme  to GPT in order to bypass the 2 TiB limit for MBR partitions on my EBS  volume?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-ubuntu-convert-mbr-to-gpt/)
* [UEFI](https://help.ubuntu.com/community/UEFI)
* [Boot-Repair](https://help.ubuntu.com/community/Boot-Repair)



---
## Linux Tricky Usage
* [ubuntu - 如何最大化左/右半屏窗口？ ](https://www.coder.work/article/4057137)
* [How to Enable Hot Corners in Ubuntu 18.04, 19.04](http://ubuntuhandbook.org/index.php/2019/07/enable-hot-corners-ubuntu-18-04-19-04/)

---
## Linux Configuration
* [Ubuntu 16.04 右上角标题栏实时显示网速、CPU及内存使用率](https://www.geek-share.com/detail/2791512777.html)

---
## Ubuntu Documentation
* [What do the icons in the top bar mean?](https://help.ubuntu.com/stable/ubuntu-help/status-icons.html.en)
* [DiskSpace](https://help.ubuntu.com/community/DiskSpace)
* [How can I detect whether my disk is using GPT or MBR from a terminal?](https://askubuntu.com/questions/387351/how-can-i-detect-whether-my-disk-is-using-gpt-or-mbr-from-a-terminal)
    * To check if the disk is using GPT or MBR: `sudo gdisk -l /dev/sda`
* [UEFI+GPT引导基础篇 ：什么是GPT，什么是UEFI？ ](https://www.cnblogs.com/sddai/p/6351715.html)

---
* [ubuntu系统，anaconda3安装后，命令行界面打开默认进入base环境解决办法](https://blog.csdn.net/jy1023408440/article/details/95211921?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase) 

---
## Get the size of a directory:
Use command: `du -sh file_path`:        
Explanation:
* `du` (disk usage) command estimates file_path space usage;
* The options `-sh` are (from `man du`):
  ```
    -s, --summarize
         display only a total for each argument
    -h, --human-readable
         print sizes in human readable format (e.g., 1K 234M 2G)
  ```
* `df -h .; du -sh -- * | sort -hr`
* [How do I get the size of a directory on the command line?](https://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line)

---
## References 

* [Grub2/Installing](https://help.ubuntu.com/community/Grub2/Installing)
    * Reinstalling GRUB2 from a Working System
