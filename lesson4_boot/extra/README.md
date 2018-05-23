### 4(*). Сконфигурировать систему без отдельного раздела с /boot, а только с LVM
### Репозиторий с пропатченым grub: https://yum.rumyantsev.com/centos/7/x86_64/
### PV необходимо инициализировать с параметром --bootloaderareasize 1m

* Инициализируем блочные устройства `pvcreate --bootloaderareasize 1m /dev/sd{b,d}` с созданием Boot Area для grub
![centos7_pvs](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson4_boot/extra/lvmgrub2_boot_pvs.jpeg)


![centos7_grub2](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson4_boot/extra/lvmgrub2_boot.jpeg)
![centos7_lsblk](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson4_boot/extra/lvmgrub2_boot_lsblk.jpeg)
