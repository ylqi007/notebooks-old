[TOC]

---

## 1. `mv`

* `mv` is a UNIX and Linux command to **move** and **rename** files.
The `mv` command is a command line utility that moves files or directories from one place to another. 
It supports moving single files, multiple files and directories.
```bash
man mv

mv - move (rename) files
```

### 1.1 Move a file and give a new name for the file
```bash
mv <file_name> <new_file_name>
mv foo.txt bar.txt
```

### 1.2 Move a file into a directory
```bash
mv <file_name> <dir>
mv foo.txt bar  # bar is a directory
```

### 1.3 Move multiple files into a directory
```bash
mv <file1> <file2> <file3> <dir>
mv file1.txt file.2.txt file3.txt folder
mv *.txt folder
```

### 1.4 Move a directory
```bash
mv <dir> <destination>
```

### 1.5 Prompt before overwriting a file [在覆盖一个文件之前，先进行提示]
By default the `mv` command will overwrite an existing file.
To prompt before overwriting a file the `-i` option can be used.
```bash
mv -i <new_file> <old_file>
```

### 1.6 Not overwrite an existing file
To prevent an exsiting file from being overwritten pass the `-n` option.
```bash
mv -n <file1> <file2>
```

### 1.7 Only move files newer than the destination
To only move files that are newer than the destination pass the `-u` option.

### 1.8 Take a backup of an existing file
To take a backup of an existing file that will be written as a result of the `mv` command pass the `-b` option. 
This will create a backup file with the tilde character appended to it. To change the backup suffer the `-S` option may be used.         
被覆盖的文件会创建一个备份文件，备份文件名会在在后面添加一个 `~`。如果想要修改备份文件的后缀名，可以使用 `-S` 选项。

[Linux and Unix mv command tutorial with examples](https://shapeshed.com/unix-mv/)


## 2. [`ln`](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/)
```bash
ln -s [OPTIONS] FILE LINK
```

## Reference
* [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html)