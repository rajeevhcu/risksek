create database risksek;

create table risksek.access_history(
  id int(11) unsigned NOT NULL AUTO_INCREMENT,
  created_date_time bigint(20) NOT NULL,
  parameter TEXT NOT NULL,
  PRIMARY KEY (`id`)
  );