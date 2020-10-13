Problem: 电脑上只有一块 256G 的 SDD 硬盘，需要分区给 `/`,`/home/`,`/boot/` 等必要的目录。导致最终分给 `/home/` 的空间不够用。
我的习惯是在 `/home/<user>/` 目录下另设一个 `work/` 目录存放工作文件。由于训练的时候，训练记录文件比ijao大，常常空间不够用。
因此，我想另添加一块硬盘，单独挂载到 `/home/<user>/work/`。

前期准备：
* `lsblk` 列出系统上的所有磁盘列表，可以看成“list block device”，就是列出所有存储设备的意思。
![output of lsblk](./images/lsblk_res.png)
    * 从图中的输出结果可以看出，现在有三块磁盘，`sda`, `sdb` and `sdc`。
      其中 `sda` 是最初的 256G 的 SDD 硬盘，可以看出分别有 `/`, `/home/`, `/swap/`, `/boot/`等分区；
      `sdb` 是 8T 的移动硬盘，没有特别指定挂载的目录，因此默认挂载到 `/media/<user>/`；
      `sdc` 是 1T 的移动硬盘，因对其进行了特别的挂载处理，所以其挂载在了 `/home/<user>/work/` 目录上。
    * 每个栏目的具体含义如下：
        * `NAME` 表示设备的文件名，会省略 `/dev/` 等前导目录；
        * `MAJ:MIN` 分别是主要：次要设备代码，还未深入了解；
        * `RM` 表示是否为可卸载设备(removeable device)，如管盘、USB磁盘等等；
        * `SIZE` 给出了磁盘的大小信息；
        * `RO` 表示是否为只读设备；
        * `TYPE` 表示是磁盘(disk)，分区(part)还是只读存储器(rom)等输出。
        * `MOUNTPOINT` 给出了磁盘的挂在点。比如 `sdc1` 是个 1T 的分区，挂载在 `/home/<user>/work/`；`sda6` 是个 60G 的分区并挂载在 `/`，也就是根目录；`sda7` 是个 150G 左右的分区，挂载在 `/home/` 目录。 
* `blkid` 列出设备的UUID等参数
![output of blkid](./images/blkid_res.png)
    * 一块磁盘可以被分成多个分区，而`blkid` 给出了磁盘的每个分区的一些信息，比如 UUID，TYPE等。
      其中 UUID 在设置开机自动挂载的时候会用到；TYPE 列出了磁盘的格式。
    * UUID (Universally Unique Identifier，通用唯一识别码)，目的是让分布式系统中的所有元素都能有唯一的辨识信息。
    * TYPE
* `parted` 列出磁盘的分区表类型与分区信息
![output of parted](./images/parted_res.png)
    * `parted device_name print`，可以获知磁盘的分区类型。
    * `Model`，磁盘的模块名称（厂商）
    * `Disk`，磁盘的总容量
    * `Sector size`，磁盘的每个逻辑/物理扇区的容量
    * `Partition Table`，分区表的格式（MBR/GPT等），此时为 MSDOS
    * `Disk Flags`，每个分区的信息。
  

综上，通过 `lsblk` 可以获知所有的存储设备，通过 `blkid` 可以知道所有的文件系统，最后可以通过 `parted` 可以获知磁盘的分区类型。
下面就可以进行挂载，或是开机自动挂载。


进行挂载前，先要确定几件事：
* 单一文件系统不应该被重复挂载在不同的挂载点(目录)中;
* 单一目录不应该重复挂载多个文件系统;
* 要作为挂载点的目录,理论上应该都是空目录才是。

进行简单挂载（关于 mount 的命令实际更复杂，可以指定各种参数，此处仅是简单的挂载）：
```bash
mount device_name mountpoint
```

进行简单的卸载
```bash
umount [-fn] device_name/mountpoint

umount /dev/vda4    # 用设备文件名(device_name)进行卸载
umount /data/ext4   # 用挂载点(mountpoint)进行卸载
```

如果每次开机后都要进行手动挂载就太不人性了，所以我们需要让系统**自动**在开机的时候进行挂载。
那就需要直接到 `/etc/fstab` 进行设置。
系统挂载有一些限制：
* 根目录	`/` 是必须挂载的,而且一定要先于其它	`mount point` 被挂载进来。
* 其它 `mount point` 必须为已创建的目录,可任意指定,但一定要遵守必须的系统目录架构原则(FHS)
* 所有 `mount point` 在同一时间之内,只能挂载一次。
* 所有 `partition` 在同一时间之内,只能挂载一次。
* 如若进行卸载,您必须先将**工作目录(pwd)**移到 `mount point(及其子目录)`之外。

下面查看写 `/etc/fstab` 文件：
![content of /est/fstab](./images/fstab_result.png)
`/etc/fstab`文件中的信息:

| 设备/UUID等(Filesystem) | 挂载点(Mount Point) | 文件系统(type) | 文件系统参数(options) | dump | pass |
| :------------- | :------------- |:------------- |:------------- |:------------- |:------------- |
* 第一栏: 第一栏:磁盘设备文件名/UUID/LABEL name,
* 第二栏: 挂载点(mount point),挂载点一定是目录.
* 第三栏: 磁盘分区的文件系统,在手动挂载时可以让系统自动测试挂载,但在这个文件当中我们必须要手动写入文件系统才行! 包括	xfs, ext4, vfat, reiserfs, nfs等等。
* 第四栏:文件系统参数:
* 第五栏:能否被	dump	备份指令作用
* 第六栏:是否以	fsck	检验扇区

`/etc/fastab` 的最后一行就是我的进行开机自动挂载的设置命令。
