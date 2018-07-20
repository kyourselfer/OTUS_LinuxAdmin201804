Роль nginx:
```
roles/
└── nginx
    ├── files
    │   └── nginx.repo
    ├── handlers
    └── tasks
        └── main.yml
```
Копируем файл из files/ в /etc/yum.repos.d/,
инсталируем по списку,
перезапуск и авто включение при загрузке
```
---
- name: Add nginx repo
  copy: src=nginx.repo dest=/etc/yum.repos.d/

- name: Install packages
  yum: pkg={{ item }} state=latest
  with_items:
    - nginx

- name: ensure nginx is running and enabled
  service: name=nginx state=restarted enabled=yes
  ```
[main.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson16_ansible/roles/nginx/tasks/main.yml)
