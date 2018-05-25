Работа с mdadm.
----------------------
добавить в Vagrantfile еще дисков
сломать/починить raid
собрать R0/R5/R10 на выбор 
прописать собранный рейд в конф, чтобы рейд собирался при загрузке
создать GPT раздел и 5 партиций

в качестве проверки принимаются - измененный Vagrantfile, скрипт для создания рейда, конф для автосборки рейда при загрузке
* доп. задание - Vagrantfile, который сразу собирает систему с подключенным рейдом

#### Скрипт выбирает не размеченные диски (из 5 дисков 4) и создаёт mdraid5 с нарезением партиций и монтирования.
##### В Vagrantfle область для подключения скрипта `box.vm.provision "shell", path: "./SCRIPTS/init.sh"`
##### и сам скрипт автоматизации создания mdraid5 
##### [init.sh](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson2_mdraid/SCRIPTS/init.sh)
![lsblk](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson2_mdraid/lsblk.jpeg)
