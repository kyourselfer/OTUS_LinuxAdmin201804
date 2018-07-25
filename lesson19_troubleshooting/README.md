### Домашнее задание
Linux Troubleshooting
--------
1. Написать playbook для первоначальной настройки хоста после инсталляции по всем прошедшим лекциям
- установка нужных инструментов для анализа и траблшутинга
- избавление ядра и сетевых настроек от "десктопности"
- установка разнообразных параметров ядра под работу в качестве сервера
2. Опубликовать ссылку на плейбук в общем чатике
3. Взять любой опубликованный плейбук, прокомментировать.

Создаем роли:
 * CentOS_Srv
  - Пересобираем ядро по конфигу
  - Меняем sysctl (net.core.somaxconn=1024 net.core.rmem_max=8388608 net.core.wmem_max=8388608 net.core.rmem_default=65536 net.core.wmem_default=65536 net.ipv4.tcp_rmem='4096 87380 8388608' net.ipv4.tcp_wmem='4096 65536 8388608' net.ipv4.tcp_mem='8388608 8388608 8388608' vm.swappiness=1)
  - Отключаем ненужные службы (-NM, -NM_dependences)
  - Включяем zram
  - Создаем набор пакетов (-sar, -cronie-anacron, +cronie-noanacron, +wget, +epel-release, +ntp, +net-tools, +strace, +lsof, +psmisc, +bind-utils, +nc, +atop, +iftop)
  - files(ntp.conf,firewall.conf)
 * nginx
  - Создаем набор пакетов (+nginx(listen deferred), +mariadb, +php-fpm, +curl)
 * httpd
  - Создаем набор пакетов (+apache24(AcceptFilter), +mariadb, +php-fpm, +curl)

