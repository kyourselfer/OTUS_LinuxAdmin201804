##### Preview
```
ELK на базе библиотеки Apache Lucene поисковый движок Elasticsearch для индексирования 
и поиска информации в любом типе документов.
Logstash - сбор журналов из многочисленных источников и централизованного хранения, 
поддерживает множество входных типов данных - журналы, метрики разных сервисов и служб.
Kibana - это веб-интерфейс для вывода индексированных Elasticsearch логов. 
### Agents (client_side) ###
Packetbeat - Анализ сетевых пакетных данных.
Filebeat - Анализ лог-данных в реальном режиме времени.
Topbeat - Получает представление о данных инфраструктуры.
Metricbeat - Ship метрики для Elasticsearch.
```

#Filebeat(client) передаёт логи nginx в logstash(server of ELK) 
/etc/filebeat/[filebeat.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/files/filebeat.yml)

#Logstash(server of ELK) принимает логи(секция input) фильтрует(grok,...), сортирует, переименовывает по условию(секция filter), отправляет в elasticsearch(секция output) /etc/logstash/conf.d/[pipeline.conf](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/ELK/files/logstash_pipeline.yml) слушает 0.0.0.0:5044

#Роль [ELK](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/ELK/tasks/main.yml)
#Elasticsearch слушает localhost:9200

#Kibana на прослушку на 0.0.0.0:5601
/etc/kibana/[kibana.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/ELK/files/kibana.yml)

#Подгружается шаблоны beats-dashboards`curl -L -O http://download.elastic.co/beats/dashboards/beats-dashboards-1.3.1.zip`

#Останется только зайти на kibana:5601 и поставить filebeat* шаблон по умолчанию
![kibana](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/kibana1.gif)

#Проверка методом GET на 80/tcp порт через попадания в лог nginx error.log и access.log `for i in 100/snbjsbjnbsj.error.php 100/ ; do curl -X GET http://192.168.168.$i ; done`
![kibana2](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/img/kibana2.gif)
и отправка через [filebeat](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/nginx/files/filebeat.yml) также на стороне клиента
```
filebeat.prospectors:
- input_type: log
  paths:
    - /var/log/nginx/access.log*
    - /var/log/nginx/error.log*
  exclude_files: [".gz$"]
  multiline:
    pattern: "^\\s"
    match: after
output.logstash:
  hosts: ["192.168.168.110:5044"]
```
Вырезки из конфигов logstash/conf.d/[pipeline.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/ELK/files/logstash_pipeline.yml)
```
filter {
  if [source] =~ "access" {
    mutate {
      replace => { type => "nginx_access" }
      rename => { "@timestamp" => "read_timestamp" }
    }
```
```
else if [source] =~ "error" {
    mutate {
      replace => { type => "nginx_error" }
      rename => { "@timestamp" => "read_timestamp" }
    }
    grok {
```
и затем отправляем в ElasticSearch через output в logstash/conf.d/[pipeline.yml](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson21_Journald_ELK/roles/ELK/files/logstash_pipeline.yml)
```
output {
  elasticsearch {
    hosts => "127.0.0.1:9200"
    manage_template => false
    index => "%{[@metadata][beat]}-%{+YYYY.MM.dd}"
    document_type => "%{[@metadata][type]}"
  }
```
##### Troubleshouting
```
curl 'localhost:9200/_cat/nodes?v'
curl 'localhost:9200/_cat/health?v'
curl 'localhost:9200/_cat/indices?v'
/usr/share/logstash/bin/logstash --path.settings /etc/logstash -t #проверка ошибок в конфиге
/usr/share/filebeat/bin/filebeat -path.home /usr/share/filebeat/ -path.data /usr/share/filebeat/bin/data/ -path.config /etc/filebeat/ -path.logs /var/log/filebeat/ -e -v #интерактивный режим filebeat
```
