### copy key.pub to root
mkdir -p ~root/.ssh
cp ~vagrant/.ssh/auth* ~root/.ssh
yum install -y mdadm smartmontools hdparm gdisk


### create mdraid5
LetterOfException=`lsblk | grep sd | grep -E "sd(a|b|c|d|e)(1|2|3)" | cut -c5 | uniq`
LettersOfMDRaid=`lsblk | grep sd | grep -vE "sd(a|b|c|d|e)(1|2|3)" | cut -c3 | grep -v $LetterOfException`
SortLettersOfMDRaid=`echo $LettersOfMDRaid | sort | xargs echo | tr ' ' ,`
# concatenation
eval "echo y | mdadm --create /dev/md0 --level=5 --raid-devices=4 /dev/sd{$SortLettersOfMDRaid}"
mdadm --detail --scan > /etc/mdadm.conf

# creat gpt slices
parted -s /dev/md0 mklabel gpt
parted -s /dev/md0 mkpart 1 ext4 1.54MB 258MB
parted -s /dev/md0 mkpart 2 ext4 258MB 514MB
parted -s /dev/md0 mkpart 3 ext4 514MB 770MB
parted -s /dev/md0 mkpart 4 ext4 771MB 1027MB
parted -s /dev/md0 mkpart 5 ext4 1027MB 1283MB

# make fs, create catalogs and add in fstab
for i in 1 2 3 4 5
do
	mkfs -t ext4 /dev/md0p$i
	mkdir -p /raid5/slice$i
	echo "/dev/md0p$i          /raid5/slice$i        ext4     defaults        0 0" >> /etc/fstab
done

# mounting 
mount -a

