#!/usr/bin/env bash

PROJECT=/home/yq0033/work1/Tutorials

docker run -it --name Tutorials \
    --mount type=bind,source=${PROJECT},target=/Tutorials   \
    --runtime=nvidia \
    tensorflow/tensorflow:2.1.1-gpu-jupyter bash


#docker exec -it Tutorials bash


## Install vim and set the color of prompt
# apt update
# apt install vim
#
# cd /
# vim .bashrc
## then add
# PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
# source .bashrc