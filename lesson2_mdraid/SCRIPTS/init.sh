### copy key.pub to root
mkdir -p ~root/.ssh
cp ~vagrant/.ssh/auth* ~root/.ssh
yum install -y mdadm smartmontools hdparm gdisk


### create mdraid5
LetterOfException=`lsblk | grep sd | grep -E "sd(a|b|c|d|e)(1|2|3)" | cut -c5 | uniq`
LettersOfMDRaid=`lsblk | grep sd | grep -vE "sd(a|b|c|d|e)(1|2|3)" | cut -c3 | grep -v $LetterOfException`
SortLettersOfMDRaid=`echo $LettersOfMDRaid | sort | xargs echo | tr ' ' ,`
# concatenation
eval "mdadm --zero-superblock /dev/sd{$SortLettersOfMDRaid}"
eval "echo y | mdadm --create /dev/md0 --level=5 --raid-devices=4 /dev/sd{$SortLettersOfMDRaid}"
mdadm --detail --scan > /etc/mdadm.conf

# creat GPT and partitions
fdisk /dev/md0 << EOF
g
n
1
2048
+256M
n
2
526336
+256M
n
3
1050624
+256M
n
4
1574912
+256M
n
5
2099200
+256M
w
EOF

# make fs, create catalogs and add in fstab
for VAL in 1 2 3 4 5
do
	mkfs -t xfs -f /dev/md0p$VAL
	mkdir -p /raid5/slice$VAL
	echo "/dev/md0p$VAL          /raid5/slice$VAL        xfs     defaults        0 0" >> /etc/fstab
done

# mounting 
mount -a

