#!/usr/bin/env bash

# 1. Start a container with specific filesystem
VOC2007=/home/yq0033/work/PycharmProjects/DATA/VOC2007/
CODE=/home/yq0033/work/PycharmProjects/YOLO/tensorflow-yolov3

docker run -it --name tf-yolo-v3 \
    --mount type=bind,source="${VOC2007}",target=/VOC2007 \
    --mount type=bind,source="${CODE}",target=/tensorflow-yolov3 \
    tensorflow/tensorflow:1.14.0-gpu-py3-jupyter bash

# 2. Exit a container
Ctrl + D

# 3. Restart a container
docker ps -a    # list all containers
docker container restart <container-name>

# 4. Go into a container and run
docker exec -it tf-yolo-v3 bash

#5. Install vim and set the color of prompt
# apt update
# apt install vim
#
# cd /
# vim .bashrc
## then add
# PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
# source .bashrc
