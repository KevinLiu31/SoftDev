# Team WeLoveTrees - Kevin Liu, Ravindra Mangar, Mahir Riki
## K17: Shell Game
## SoftDev
## 24-10-2022
## Time Spent: ~30 minutes

---

## Table of Contents
- [0. How To Run SQLITE in Terminal](#0)
- [1. Creating a New Table](#1)
- [2. SQLITE Dot-Commands (.read)](#2)
- [3. SQLITE Dot-Commands (.exit)](#3)
- [4. SQLITE Dot-Commands (.mode)](#4)
- [5. SQLITE Dot-Commands (.output)](#5)

---

<br>

## <a id = 0> </a> 0. How to Run SQLITE in Terminal
<br>

Open a new terminal and type 

```$ sqlite3```

<b> REMEMBER THE "3".</b>

<br>

## <a id = 1> </a> 1. Creating a New Table

<br>

To create a new table, type ```CREATE TABLE <TABLE NAME>(<COLUMN NAME> <DATA TYPE>);```. <br>
* For example, to create a table called "students" with a column called "name" that stores strings, type ```CREATE TABLE students(name TEXT);```.

To insert into this table, you type ```INSERT INTO <TABLE NAME> VALUES(<VALUE>);```. <br>
* For example, to insert "Qiu Qiu Kachu" into the "students" table, type ```INSERT INTO students VALUES("Qiu Qiu Kachu");```.

To view the table, type ```SELECT * FROM <TABLE NAME>;```. <br>
* For example, to view the "students" table, type ```SELECT * FROM students;```.

<br>

## <a id = 2> </a> 2. Importing a SQL File (via Terminal)

<br>

<b>.read DEFINITION</b>

```.read``` - Inputs a SQL file via TERMINAL

<br>

<b>.read USAGE</b>

```
$ .read myhappiness.sql

INPUTS sql file into sqlite3
```

<br>

<b>.read | DEFINITION</b>

```.read | ``` - RUNS a SQL file via TERMINAL

<br>

<b>.read | USAGE</b>

```
$ .read |myhappiness.sql

RUNS sql file into sqlite3
```

<br>

## <a id = 3> </a> 3. SQLITE Dot-Commands (.exit)

<br>

<b>.exit DEFINITION</b>

```.exit``` - Exits sqlite3

<br>

<b>.exit USAGE</b>

```
$ .exit

--> $

Returns to the terminal
```

<br>

## <a id = 4> </a> 4. SQLITE Dot-Commands (.mode)

<br>

<b>.mode DEFINITION</b>


```.mode``` - Choose between a variety of output formats, including but not limited to:
- csv
- html
- json
- list
- markdown
- table

<br>

<b>.mode USAGE</b>

```
$ .mode

--> current output mode: csv

Will return the current mode.
```

```
$ .mode list
$ .seperator ", "
$ select * from tbl1

--> this is a, csv
    ripoff, yknow

Will return the inputted table and separate each table value with ", "
```

<br>

## <a id = 5> </a> 5. SQLITE Dot-Commands (.output)

<b>.output DEFINITION</b>

```.output ``` - Exports a sqlite3 Table

<br>

<b>.output USAGE</b>

```
$ .output test.txt

--> $

Saves sqlite3 table to test.txt
```

<br>
