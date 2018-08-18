##### Простая защита от DDOS
Написать конфигурацию nginx, которая даёт доступ клиенту только с определенной cookie.
Если у клиента её нет, нужно выполнить редирект на location, в котором кука будет добавлена, после чего клиент будет обратно отправлен (редирект) на запрашиваемый ресурс.

Смысл: умные боты попадаются редко, тупые боты по редиректам с куками два раза не пойдут

Для выполнения ДЗ понадобятся
https://nginx.org/ru/docs/http/ngx_http_rewrite_module.html
https://nginx.org/ru/docs/http/ngx_http_headers_module.html


##### configs
/etc/[nginx.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson24_websrv/nginx.conf)

/etc/conf.d/[default.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson24_websrv/default.conf)
#####
Перейдем в браузере на example.com и получим cookie через `(302 -> (add_header Set-Cookie) -> 302 -> rewrite break;)`

![check 
through browser](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson24_websrv/check_browser.gif)

Через curl

![check 
through curl](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson24_websrv/check_curl.gif)

Логи

![logs](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson24_websrv/logs.gif)
