
### 最常见的安装方法
```bash
sudo apt-get install <software>
```
前提是你的软件列表里有这个软件，这就要求你的源要配好，并且经常 `sudo apt-get update` 保证你的列表最新。这种方法会自动下载软件包到

### .deb 安装包
```bash 
sudo dkpg -i package.deb
```
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

### 二进制安装包
bin或run或sh文件或没有扩展名的文件安装（需要安装的二进制包installer） 


## [Difference Between apt and apt-get Explained](https://itsfoss.com/apt-vs-apt-get-difference/)
#### 1. Why apt was introduced in the first place? 为啥那么引入 `apt`?
Debian uses a set of tools called **Advanced Packaging Tool (APT)** to manage this packaging system. Don’t confuse it with the command apt, it’s not the same.      
Debian 是 Ubuntu，Linux Mint 等系统的母本系统。Debian 使用一组高级打包工具(APT)管理包系统。这里的 APT 和命令 apt 是不一样，不要搞混。
          
The `apt` commands have been introduced to solve this problem. apt consists some of the most widely used features from `apt-get` and `apt-cache` leaving aside obscure and seldom used features.            
`apt-get` and `apt-cache` 这种命令涉及的内容太底层，Linux 的普通用户并不会涉及，为了简化不必要的复杂性，`apt` 对这些底层的命令做了整合，对用户更加友好。

**Bottom line: apt=most common used command options from apt-get and apt-cache.**

#### 2. Difference between apt and apt-get
While apt does have some similar command options as `apt-get`, it’s not backward compatible with `apt-get`. 
That means it won’t always work if you just replace the `apt-get` part of an `apt-get` command with apt.            
`apt` 是不向后兼容的，也就是说，简单地用 `apt` 替换 `apt-get` 可能会导致命令不工作。          

![](images/apt_commands_1.png)
![](images/apt_commands_2.png)

#### 3. Conclusion
* `apt` is a subset of `apt-get` and `apt-cache` commands providing necessary commands for package management
* while `apt-get` won’t be deprecated, as a regular user, you should start using `apt `more often. 作为普通用户，尽量使用 `apt` 就好。

#### 4. [Using apt Commands in Linux [Complete Guide]](https://itsfoss.com/apt-command-guide/) 
1. `sudo apt update`: Using apt commands to manage packages in Debian and Ubuntu based Linux distributions     
    `apt` actually works on a database of available packages. If the database is not updated, the system won’t know if there are any newer packages available. 
    This is why updating the repository should be the first thing to do in in any Linux system after a fresh install. 仅仅更新信息，而不更新软件。
2. `sudo apt upgrade`: 
    Once you have updated the package database, you can now upgrade the installed packages. The most convenient way is to upgrade all the packages that have available updates. 
    当用 `sudo apt update` 更新过信息之后，可以直接使用 `sudo apt upgrade` 更新软件。            
    The fastest and the most convenient way to update Ubuntu system is by this command: `sudo apt update && sudo apt upgrade -y`
3. `sudo apt install <package1> <package2> <package3>`
4. `sudo apt search <package>`
5. `sudo apt remove <package>`
6. `sudo apt autoremove`
    This command removes libs and packages that were installed automatically to satisfy the dependencies of an installed package. If the package is removed, these automatically installed packages, though useless, remains in the system.
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
1. [软件安装指南](https://wiki.ubuntu.org.cn/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97)









