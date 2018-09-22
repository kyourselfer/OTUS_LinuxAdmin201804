### Написать свою реализацию ps ax используя анализ /proc.

[psax](https://github.com/kyourselfer/OTUS_LinuxAdmin201804/blob/master/lesson7_procfs/1/psax)

Для выполнения задания понадобились только следующие файлы на procfs
```
/proc/PID/cmdline – аргументы командной строки (где PID – идентификатор процесса или self);
/proc/PID/environ – переменные окружения для данного процесса;
/proc/PID/fd – директория, содержащая символьные ссылки на каждый открытый файловый дескриптор;
/proc/PID/stat – статус процесса:
* State (flags):
<    high-priority (not nice to other users)
N    low-priority (nice to other users)
L    has pages locked into memory (for real-time and custom IO)
s    is a session leader (Лидер сессии - это процесс, который создал сессию вызо­вом setsid(2). Идентификатор процесса лидера сессии совпадает с его sid)
l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
+    is in the foreground process group (данный процесс входит в группу процессов, с которыми в данный момент идёт работа пользователя (то есть foreground processes — в противоположность background processes, работающим в фоновом режиме))
```

