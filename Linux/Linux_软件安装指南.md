
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

## Reference:
1. [软件安装指南](https://wiki.ubuntu.org.cn/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97)









