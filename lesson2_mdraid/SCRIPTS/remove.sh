#!/bin/bash
#
umount /raid5/*
mdadm --manage --stop /dev/md0
mdadm --zero-superblock /dev/sd{b,c,d,e}


