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
 * base_srv
  - Пересобираем ядро по конфигу
  - Меняем sysctl (net.core.somaxconn=1024, sysctl -w net.core.rmem_max=8388608, net.core.wmem_max=8388608, net.core.rmem_default=65536, net.core.wmem_default=65536, net.ipv4.tcp_rmem='4096 87380 8388608', net.ipv4.tcp_wmem='4096 65536 8388608', net.ipv4.tcp_mem='8388608 8388608 8388608', vm.swappiness=1)
  - Отключаем ненужные службы (NM, )
  - Включяем zram
  - Создаем набор пакетов (-sar, -croni-noanacron, +wget, +ntp, +net-tools, +strace, +lsof, +fuser, +bind-utils, +nc, atop, iftop)
 * web_lamp
  - Создаем набор пакетов (+apache24(AcceptFilter), +mariadb, +php-fpm, +curl)
 * web_lemp
  - Создаем набор пакетов (+nginx(listen deferred), +mariadb, +php-fpm, +curl)

