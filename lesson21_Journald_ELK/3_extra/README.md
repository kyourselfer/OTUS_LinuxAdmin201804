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

#Filebeat(client) передаёт логи в logstash(server of ELK) 
/etc/filebeat/[filebeat.yml](https://)

#Logstash(server of ELK) принимает логи(секция input) фильтрует, сортирует, переименовывает по условию(секция filter), отправляет в elasticsearch(секция output) 
/etc/logstash/conf.d/[pipeline.conf](https://)

#Elasticsearch 
/etc/elasticsearch/[elasticsearch.yml](https://)

#Kibana 
/etc/kibana/[kibana.yml](https://)
#Подгрузим шаблоны beats-dashboards`curl -L -O http://download.elastic.co/beats/dashboards/beats-dashboards-1.3.1.zip`

#tcp порты для прослушки на loopback
#9200 - elasticsearch, logstash - 5044, kibana - 5601

##### Troubleshouting
```
curl 'localhost:9200/_cat/nodes?v'
curl 'localhost:9200/_cat/health?v'
curl 'localhost:9200/_cat/indices?v'
/usr/share/logstash/bin/logstash --path.settings /etc/logstash -t #проверка ошибок в конфиге
/usr/share/filebeat/bin/filebeat -path.home /usr/share/filebeat/ -path.data /usr/share/filebeat/bin/data/ -path.config /etc/filebeat/ -path.logs /var/log/filebeat/ -e -v #интерактивный режим filebeat
```
