[TOC]

## Installation

1. Adding MySQL APT Repository

2. Update repository

3. Install MySQL with APT: `sudo apt install mysql-server`

4. Starting and Stopping the MySQL server

   ```bash
   shell> sudo service mysql status
   shell> sudo service mysql stop
   shell> sudo service mysql start
   ```

   

5. 

## Get Start

```bash
$ mysql -u root -p		# then input password
```



## Creating Databases and Tables

```bash
show databases;					# List available databases:
CREATE DATABASE <name>;			# The general command for creating a database:
DROP DATABASE database_name;	# To drop a database:Remember to be careful with this command! Once you drop a database, it's gone!
USE <database name>;			# 

CREATE TABLE tablename			# Creating tables
(
column_name data_type,
column_name data_type
);

CREATE TABLE cats
(
name VARCHAR(100),
age INT
);

SHOW TABLES;					# Show table information
SHOW COLUMNS FROM tablename;
DESC tablename;

DROP TABLE <tablename>; 		# Dropping Tables, Be careful with this command!
```





## Reference

* [A Quick Guide to Using the MySQL APT Repository](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
* [在 Ubuntu 上安装 MySQL](https://blog.csdn.net/liang19890820/article/details/105071479)
* [Employees Sample Database](https://dev.mysql.com/doc/employee/en/employees-installation.html)