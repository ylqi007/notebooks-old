
在Linux中，有一种特殊的块设备叫 **loop device**,这种 **loop device** 设备是通过影射操作系统上的正常的文件而形成的虚拟块设备。
因为这种设备的存在，就为我们提供了一种创建一个存在于其他文件中的虚拟文件系统的机制。

---
首先我们在命令行终端中输入 `man loop`

出现如下内容：

摘要： 
Loop设备是一种块设备，但是它并不指向硬盘或者光驱，而是指向一个文件块或者另一种块设备。
一种应用的例子：将另外一种文件系统的镜像文件保存到一个文件中，例如iso文件，然后将一个Loop设备指向该文件，紧接着就可以通过mount挂载该loop设备到主文件系统的一个目录下了，我们就可以正常访问该镜像中的内容，就像访问一个文件系统一样。

---
>> In Unix-like operating systems, a loop device, vnd (vnode disk), or lofi (loop file interface) is a pseudo-device that makes a file accessible as a block device.      
> [`loop device` 是一个伪设备，使文件可以如同 `block device` 一样被访问。]
> 
> Before using, a `loop device` must be connected to an existing file in the filesystem.        
> [在使用之前，循环设备必须与现存文件系统上的文件相关联。]

---
> Having Snap images which consume 100% of their filesystem is perfectly acceptable. In fact, it's supposed to work that way.
>
> Because Snap uses `SquashFS`, which is a compressed read-only filesystem, the filesystem size is **always** just large enough to contain its contents.
> In addition, because the filesystem is read-only, there's no need to allow for any additional storage, as such additional space can never be used anyway.

---
[What is /dev/loopx? [duplicate]](https://askubuntu.com/questions/906581/what-is-dev-loopx)

> `/dev/loop*` are loop devices making plain files accessible as block devices. They have nothing to do with RAM occupation. 
> They are typically used for mounting disk images, in your case apparently for Ubuntu Snap. See this Wikipedia article for details.

> Also note that it is a Good Thing(TM) your RAM is full. Unused RAM is wasted RAM, so Linux makes an effort to put all of your RAM to good use. 
> See [this info page](https://www.linuxatemyram.com/) for details.


## Reference:
1. [Loop device](https://en.wikipedia.org/wiki/Loop_device)
2. [loop device介绍及losetup使用](https://blog.51cto.com/wushank/1212647)
3. [/dev/loop与设备文件系统](https://blog.csdn.net/trochiluses/article/details/9988791)
4. [linux的dev目录系列之设备详解--loop详解](https://blog.csdn.net/lengye7/article/details/80247437?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-5.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-5.edu_weight)
5. [【OS】Linux下 /dev 常见特殊设备介绍与应用[loop] ](http://blog.itpub.net/26736162/viewspace-2142668/)
6. [The snap format](https://snapcraft.io/docs/snap-format)
7. [snap /dev/loop at 100% utilization — no free space](https://unix.stackexchange.com/questions/406534/snap-dev-loop-at-100-utilization-no-free-space)
8. [loop(4) — Linux manual page](https://man7.org/linux/man-pages/man4/loop.4.html)
9. [Linux ate my ram!](https://www.linuxatemyram.com/)
