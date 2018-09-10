4*. Скачать демо-версию Atlassian Jira и переписать основной скрипт запуска на unit-файл 
---------------------------------------
#####
В Unit прописываем переменные CATALINA_HOME, CATALINA_BASE, CATALINA_TMPDIR, JIRA_HOME, CATALINA_OPTS, JRE_HOME, CLASSPATH, CATALINA_PID и опции для JVM такие как выделение памяти (heap,stack) [jira.service] (https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/jira_unit/jira.service)

[systemctl](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/jira_unit/systemctl.gif)

Лог вывода для диагностики /opt/atlassian/jira/logs/catalina.out

![catalina.out](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson6_SystemD/SCRIPTS/jira_unit/catalina_out.gif)



