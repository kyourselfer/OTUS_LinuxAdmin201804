TYPE=VIEW
query=select `c`.`sortname` AS `sortname`,count(1) AS `cnt`,max(if((`c`.`bookmaker_id` = 3),`c`.`id`,0)) AS `bk1`,max(if((`c`.`bookmaker_id` = 4),`c`.`id`,0)) AS `bk2`,max(if((`c`.`bookmaker_id` = 5),`c`.`id`,0)) AS `bk3`,max(if((`c`.`bookmaker_id` = 3),`c`.`bookmaker_competition`,0)) AS `bk1_event`,max(if((`c`.`bookmaker_id` = 4),`c`.`bookmaker_competition`,0)) AS `bk2_event`,max(if((`c`.`bookmaker_id` = 5),`c`.`bookmaker_competition`,0)) AS `bk3_event`,`c`.`match_date` AS `match_date`,max(`c`.`_updated`) AS `last_updated` from `bet2`.`competition` `c` group by `c`.`sortname`,`c`.`match_date` having (`cnt` > 1)
md5=756a81e2acc5af4a9f966d337401c3d2
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-08-18 19:44:30
create-version=1
source=select `c`.`sortname` AS `sortname`,count(1) AS `cnt`,max(if((`c`.`bookmaker_id` = 3),`c`.`id`,0)) AS `bk1`,max(if((`c`.`bookmaker_id` = 4),`c`.`id`,0)) AS `bk2`,max(if((`c`.`bookmaker_id` = 5),`c`.`id`,0)) AS `bk3`,max(if((`c`.`bookmaker_id` = 3),`c`.`bookmaker_competition`,0)) AS `bk1_event`,max(if((`c`.`bookmaker_id` = 4),`c`.`bookmaker_competition`,0)) AS `bk2_event`,max(if((`c`.`bookmaker_id` = 5),`c`.`bookmaker_competition`,0)) AS `bk3_event`,`c`.`match_date` AS `match_date`,max(`c`.`_updated`) AS `last_updated` from `competition` `c` group by `c`.`sortname`,`c`.`match_date` having (`cnt` > 1)
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select `c`.`sortname` AS `sortname`,count(1) AS `cnt`,max(if((`c`.`bookmaker_id` = 3),`c`.`id`,0)) AS `bk1`,max(if((`c`.`bookmaker_id` = 4),`c`.`id`,0)) AS `bk2`,max(if((`c`.`bookmaker_id` = 5),`c`.`id`,0)) AS `bk3`,max(if((`c`.`bookmaker_id` = 3),`c`.`bookmaker_competition`,0)) AS `bk1_event`,max(if((`c`.`bookmaker_id` = 4),`c`.`bookmaker_competition`,0)) AS `bk2_event`,max(if((`c`.`bookmaker_id` = 5),`c`.`bookmaker_competition`,0)) AS `bk3_event`,`c`.`match_date` AS `match_date`,max(`c`.`_updated`) AS `last_updated` from `bet2`.`competition` `c` group by `c`.`sortname`,`c`.`match_date` having (`cnt` > 1)
