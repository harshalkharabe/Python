# SQL stands for structure query language

# DDL - Data Defination language
# DML - Data Manipulation languages
# DCL - Data control languages
# TCL - Transaction control languages
# DRL - Data Reading Language

# DDL is uesd for defining database objects 
# like Table viwe...
# these lang. is used for creating modifying and delteing database  objects
# 1.Create
# 2.Alter
# 3. Delete

# Table : In database data is stored in tables
# table is collection of rows and columns

# How to create table ??
#SYNTAX :- CREATE TBALE <TABLE_NAME>(COLUMN-1 datatype,COLUMN-2 datatype,COLUMN-3 datatype);

# How to alter table ??
# Adding colums, Removing Columns for extisting table
# SYNTAX :- ALTER TABLE <TABLE_NAME> [ADD,DROP,REPLACE] (COLUMN_NAME datatype)

# How to delete table ??
# SYNTAX :- DROP TABLE <TABLE_NAME>

# Enter password: **********
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 8
# Server version: 8.0.39 MySQL Community Server - GPL

# Copyright (c) 2000, 2024, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# mysql> create database harshalk
#     -> create database harshalk;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create database harshalk' at line 2
# mysql> create database harshalk;
# Query OK, 1 row affected (0.07 sec)

# mysql> use harshalk
# Database changed
# mysql> CREATE TABLE Emp(emp_no integer primary key, emp_name varchar(20),job varchar(20), salary float);
# Query OK, 0 rows affected (0.06 sec)

# mysql> show tables;
# +--------------------+
# | Tables_in_harshalk |
# +--------------------+
# | emp                |
# +--------------------+
# 1 row in set (0.03 sec)

# mysql> desc Emp;
# +----------+-------------+------+-----+---------+-------+
# | Field    | Type        | Null | Key | Default | Extra |
# +----------+-------------+------+-----+---------+-------+
# | emp_no   | int         | NO   | PRI | NULL    |       |
# | emp_name | varchar(20) | YES  |     | NULL    |       |
# | job      | varchar(20) | YES  |     | NULL    |       |
# | salary   | float       | YES  |     | NULL    |       |
# +----------+-------------+------+-----+---------+-------+
# 4 rows in set (0.01 sec)


# DML
# 1.insert
# 2.update
# 3.delete
# DML commands always returned row count (how many insert,update,delete)

# 1.insert command
# these is used to insert data in table
# insert in all columns
# syntax :- insert into table-name values(val-1,val-2...)
#  for selected columns
# syntax :- insert into table-name(col-1,col-2) values(val-1,val-2...) 

# mysql> insert into Emp values(1,'Harshal','Python Developer',35000);
# Query OK, 1 row affected (0.01 sec)

# mysql> insert into Emp values(1,'Aniket','Frontend Developer',25000);
# ERROR 1062 (23000): Duplicate entry '1' for key 'emp.PRIMARY'
# mysql> insert into Emp values(2,'Aniket','Frontend Developer',25000);
# Query OK, 1 row affected (0.01 sec)

# mysql> insert into Emp(emp_no,emp_name) values(3,'Kunal');
# Query OK, 1 row affected (0.02 sec)

# SELECT Command
# use for reading data from database table
# it returns all rows and columns
# syntax :- SELECT * FROM <TABLE_NAME>

# Retrive selected rows
# syntax :- SELECT col-1,col-2 FROM <TABLE_NAME>

# mysql> SELECT * FROM Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      1 | Harshal  | Python Developer   |  35000 |
# |      2 | Aniket   | Frontend Developer |  25000 |
# |      3 | Kunal    | NULL               |   NULL |
# +--------+----------+--------------------+--------+
# 3 rows in set (0.00 sec)

# mysql> SELECT emp_no,emp_name FROM Emp;
# +--------+----------+
# | emp_no | emp_name |
# +--------+----------+
# |      1 | Harshal  |
# |      2 | Aniket   |
# |      3 | Kunal    |
# +--------+----------+
# 3 rows in set (0.00 sec)

# WHERE CLAUSE
# used to reading rows based on condition
# -- SELECT * FROM TABLE_NMAE WHERE CONDITION

# mysql> SELECT * FROM Emp WHERE job = 'Pyhton Developer';
# Empty set (0.00 sec)

# mysql> SELECT * FROM Emp WHERE salary>25000;
# +--------+----------+------------------+--------+
# | emp_no | emp_name | job              | salary |
# +--------+----------+------------------+--------+
# |      1 | Harshal  | Python Developer |  35000 |
# +--------+----------+------------------+--------+
# 1 row in set (0.00 sec)

# mysql> SELECT * FROM Emp WHERE salary>25000;
# +--------+----------+------------------+--------+
# | emp_no | emp_name | job              | salary |
# +--------+----------+------------------+--------+
# |      1 | Harshal  | Python Developer |  35000 |
# +--------+----------+------------------+--------+
# 1 row in set (0.00 sec)

# mysql> SELECT * FROM Emp WHERE emp_no=1;
# +--------+----------+------------------+--------+
# | emp_no | emp_name | job              | salary |
# +--------+----------+------------------+--------+
# |      1 | Harshal  | Python Developer |  35000 |
# +--------+----------+------------------+--------+
# 1 row in set (0.00 sec)

# 2.update
# used for replacing values or data 

# syntax :- update table-name set column-name=value, column-name=value;

# syntax :- update table-name set column-name=value, column-name=value where column-name = value;

# mysql> update Emp set job = 'Python Developer' where emp_no=1;
# Query OK, 0 rows affected (0.00 sec)
# Rows matched: 1  Changed: 0  Warnings: 0

# mysql> Select * from Emp where job = 'Python Developer';
# +--------+----------+------------------+--------+
# | emp_no | emp_name | job              | salary |
# +--------+----------+------------------+--------+
# |      1 | Harshal  | Python Developer |  35000 |
# +--------+----------+------------------+--------+
# 1 row in set (0.00 sec)

# mysql> update Emp set job = 'Database Developer' where emp_no=3;
# Query OK, 1 row affected (0.01 sec)
# Rows matched: 1  Changed: 1  Warnings: 0

# mysql> Select * from Emp where job = 'Python Developer';
# +--------+----------+------------------+--------+
# | emp_no | emp_name | job              | salary |
# +--------+----------+------------------+--------+
# |      1 | Harshal  | Python Developer |  35000 |
# +--------+----------+------------------+--------+
# 1 row in set (0.00 sec)

# mysql> Select * from Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      1 | Harshal  | Python Developer   |  35000 |
# |      2 | Aniket   | Frontend Developer |  25000 |
# |      3 | Kunal    | Database Developer |   NULL |
# +--------+----------+--------------------+--------+
# 3 rows in set (0.00 sec)

# mysql> update Emp set salary = 65000;
# Query OK, 3 rows affected (0.01 sec)
# Rows matched: 3  Changed: 3  Warnings: 0

# mysql> Select * from Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      1 | Harshal  | Python Developer   |  65000 |
# |      2 | Aniket   | Frontend Developer |  65000 |
# |      3 | Kunal    | Database Developer |  65000 |
# +--------+----------+--------------------+--------+
# 3 rows in set (0.00 sec)


# 3.Delete
# used to delete record form table 
# syntax :- Delete from table-name; all rows from table 

# syntax :- Delete from table-name where condition; particular rows from table 

# mysql> Delete from Emp where emp_name = 'kunal';
# Query OK, 1 row affected (0.01 sec)

# mysql> Select * from Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      1 | Harshal  | Python Developer   |  65000 |
# |      2 | Aniket   | Frontend Developer |  65000 |
# +--------+----------+--------------------+--------+
# 2 rows in set (0.00 sec)

# mysql> Select * from Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      2 | Aniket   | Frontend Developer |  65000 |
# +--------+----------+--------------------+--------+
# 1 row in set (0.00 sec)

# mysql> rollback;
# Query OK, 0 rows affected (0.00 sec)

# mysql> set autocommit = 0;
# Query OK, 0 rows affected (0.00 sec)

# mysql> Delete from Emp where emp_no = 2;
# Query OK, 1 row affected (0.00 sec)

# mysql> Select * from Emp;
# Empty set (0.00 sec)

# mysql> rollback;
# Query OK, 0 rows affected (0.00 sec)

# mysql> Select * from Emp;
# +--------+----------+--------------------+--------+
# | emp_no | emp_name | job                | salary |
# +--------+----------+--------------------+--------+
# |      2 | Aniket   | Frontend Developer |  65000 |
# +--------+----------+--------------------+--------+
# 1 row in set (0.00 sec)

# Database        Library
# mysql     -->  Mysql-connector-python
# oracle    -->  Cx_Oracle
# PostgreSQL --> psycopg2
# SQL Server  -->   pymssql  

# Rules are given by :-
# DB_API --> Database Application Programing Interface

# Basic steps to communicate with database

# 1. Open connection (Establish connection)
# 2. Create currsor object (for sending SQL statements)
# 3. Read result inside currsor object 
# 4. Close connection
