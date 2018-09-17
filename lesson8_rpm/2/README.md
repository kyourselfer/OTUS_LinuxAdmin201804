## 2. Создать свой репо и разместить там свой RPM реализовать это все либо в вагранте, либо развернуть у себя через nginx и дать ссылку на репо

Создаем репозиторий используя утилиту генерации метаданных `createrepo $name` и `createrepo --update $name` для добавления пакетов

[test.repo](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson8_rpm/2/test.repo)

Просмотрим репозиторий и список пакетов с информацией об измененном пакете httpd.

![rpm_repo](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson8_rpm/2/rpm_repo.gif)
