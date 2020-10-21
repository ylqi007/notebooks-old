[TOC]

## Manage application data

### Storage overview

####  Choose the right type of mount

Docker has two options for containers to store files in the host machine, so that the files are persisted even after the container stops: **volumes**, and **bind mounts**. 
If you’re running Docker on Linux you can also use a **tmpfs mount**. 
If you’re running Docker on Windows you can also use a **named pipe**.

| <img src="/home/yq0033/work1/Tutorials/Docker/images/types-of-mounts.png" style="zoom:80%;" /> |
| ------------------------------------------------------------ |
| Type of mounts                                               |

* `Bind mounts` may be stored *anywhere* on the host system. They may even be important system files or directories. Non-Docker processes on the Docker host or a Docker container can modify them at any time. `bind mounts` 可以将 host 任何地方或文件挂载到 container 中，并且 host 和 container 都可以进行访问和修改。
* `Volumns` are stored in a part of the host file system which in *managed* by Docker (`/var/lib/docker/volumnes/` on Linux). Non-Docker processes should not modify this part of the file system. Volumes are the best way to persist data in Docker. `Volumns` 将 container 的文件存放到 host 系统中的一个地方，并且只能由 container 进行操作，non-docker process 无法修改 volumes 中的内容。
* `tmpfs` mounts are stored in the host system's memory only, and are never written to the host system's file system. `tmpfs` 的内容之存在在 memory 中。 

##### More details about mount types

* **Volumes:**
* **Bind mounts:**
* **tmpfs mounts:**
* **named pipes:**

#### Good use cases for volumes

#### Good use cases for bind mounts
* Sharing configuration files from the host machine to containers. 比如 Docker 通过 `/etc/resolv.conf` 向每个 container 提供 DNS resolution。
* Sharing source code or build artifacts between a development environment on the Docker host and a container.
* When the file or directory structure of the Docker host is guaranteed to be consistent with the bind mounts the containers required.

#### Tips for using bind mounts or volumes
* If you mount an empty volume into a directory in the container in which files or directories exist,
* If you mount a bind mount or non-empty volume into a directory in the container in which some files or directories exists, these files or directories are obscured by the mount, just as if you saved files into `/mnt` on a Linux host and then mounted a USB drive into `/mnt`. The contents of `/mnt` would be obscured by the contents of the USB drive until the USB drive were unmounted. The obscured files are not removed or altered, but are not accessible while the bindmount or volume is mounted.
* 

### Volumes

### Bind mounts
### tmpfs mounts


















## Reference:
* []()
* []()
* []()
* []()
* []()
* []()
* []()












