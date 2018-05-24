### 2. Установить систему с LVM, после чего переименовать VG 2

##### slicing
parted -s /dev/sdb print
parted -s /dev/sdb mklabel msdos
parted -s /dev/sdb mkpart primary ext2 1049kB 2097kB
parted -s /dev/sdb mkpart primary xfs 2MB 1076MB
parted -s /dev/sdb mkpart primary ext2 1076MB 4291MB
parted -s /dev/sdb set 2 boot on
parted -s /dev/sdb set 3 lvm on
sfdisk -l /dev/sd{a,b}

##### lvm
pvcreate /dev/sdb3
vgcreate VG00 /dev/sdb3
lvcreate -n LV00 -L 2G VG00
lvcreate -n LV01 -l100%FREE VG00

##### fs 
mkfs.xfs -f /dev/sdb2
mkfs.xfs -f /dev/mapper/VG00-LV00

##### mount
mkdir -p /mnt/{boot,root}
mount /dev/mapper/VG00-LV00 /mnt/root

##### rsync
rsync -axu / /mnt/root/
mount /dev/sdb2 /mnt/root/boot
rsync -axu /boot/ /mnt/root/boot

##### fstab
sed 's/VolGroup00-LogVol00/VG00-LV00/g' /mnt/root/etc/fstab > /mnt/root/etc/fstab.tmp
awk '$3 != "'swap'" {print $0} /swap/ {print "#"$0}' /mnt/root/etc/fstab.tmp > /mnt/root/etc/fstab
uuidnew=`blkid | grep sdb2 | cut -d ' ' -f 2 | tr \" ' '`
uuidnew=${uuidnew// /}
uuidold=`grep boot /mnt/root/etc/fstab | cut -d ' ' -f 1`
awk -v uuidold="$uuidold" -v uuidnew="$uuidnew" '{ gsub(uuidold,uuidnew); print }' /mnt/root/etc/fstab > /mnt/root/etc/fstab.tmp && echo y | cp -a /mnt/root/etc/fstab.tmp /mnt/root/etc/fstab

##### selinux disable
sed 's/SELINUX=enforcing/SELINUX=disabled/g' /mnt/etc/sysconfig/selinux > /mnt/etc/sysconfig/selinux.tmp && echo y | cp /mnt/etc/sysconfig/selinux.tmp /mnt/etc/sysconfig/selinux

##### mount pseudofs
for i in proc dev sys run ; do mount --bind /$i /mnt/root/$i ; done && chroot /mnt/root

##### grub
sed 's/VolGroup00\/LogVol00/VG00\/LV00/g' /etc/default/grub > /etc/default/grub.tmp
sed 's/rd.lvm.lv=VolGroup00\/LogVol01/ /g' /etc/default/grub.tmp > /etc/default/grub
sed 's/rhgb quiet/ /g' /etc/default/grub > /etc/default/grub.tmp && echo y | cp /etc/default/grub.tmp /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg && grub2-install /dev/sdb && exit
reboot

##### we booted on new volume and made changes on old volume
sudo -s
vgrename VolGroup00 VGnew
mount /dev/mapper/VGnew-LogVol00 /mnt && rsync -axu / /mnt
mount /dev/sda2 /mnt/boot && rsync -axu /boot /mnt/boot
for i in proc dev sys run ; do mount --bind /$i /mnt/$i ; done && chroot /mnt/
sed 's/rhgb quiet/ /g' /etc/default/grub.tmp > /etc/default/grub
sed 's/VolGroup00/VGnew/g' /etc/fstab > /etc/fstab.tmp && echo y | cp /etc/fstab.tmp /etc/fstab
grub2-mkconfig -o /boot/grub2/grub.cfg && grub2-install /dev/sda && exit
reboot

![centos7_vgrename](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson4_boot/vgrename/vgrename.png)
![centos7_bgrename_done](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson4_boot/vgrename/bgrename_done.jpeg)
