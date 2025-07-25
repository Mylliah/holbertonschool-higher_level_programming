### Task 0 :
        Write a script that lists all databases of your MySQL server.
program [0-list_databases.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql)

### Task 1 : 
        Write a script that creates the database `hbtn_0c_0` in your MySQL server.
        - If the database `hbtn_0c_0` already exists, your script should not fail
        - You are not allowed to use the `SELECT` or `SHOW` statements
program [1-create_database_if_missing.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql)

### Task 2 :
        Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
        - If the database `hbtn_0c_0` doesn’t exist, your script should not fail
        - You are not allowed to use the `SELECT` or `SHOW` statements
program [2-remove_database.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql)

### Task 3 :
        Write a script that lists all the tables of a database in your MySQL server.
        - The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)
program [3-list_tables.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql)

### Task 4 :
        Write a script that creates a table called `first_table` in the current database in your MySQL server.
        first_table description:
        `id` INT
        `name` VARCHAR(256)
        The database name will be passed as an argument of the `mysql` command
        If the table `first_table` already exists, your script should not fail
        You are not allowed to use the `SELECT` or `SHOW` statements
program [4-first_table.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql)

### Task 5 :
        Write a script that prints the following description of the table `first_table` from the database hbtn_0c_0 in your MySQL server.
        - The database name will be passed as an argument of the `mysql` command
        - You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements
program [5-full_table.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/5-full_table.sql)

### Task 6 :
        Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
        - All fields should be printed
        - The database name will be passed as an argument of the `mysql` command
program [6-list_values.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/6-list_values.sql)

### Task 7 :
        Write a script that inserts a new row in the table first_table (database `hbtn_0c_0`) in your MySQL server.
        - New row:
            `id` = `89`
            `name` = `Best School`
        - The database name will be passed as an argument of the `mysql` command
program [7-insert_value.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/7-insert_value.sql)

### Task 8 :
        Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
        - The database name will be passed as an argument of the `mysql` command
program [8-count_89.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/8-count_89.sql)

### Task 9 :
        Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
        - `second_table` description:
            `id` INT
            `name` VARCHAR(256)
            `score` INT
        - The database `name` will be passed as an argument to the `mysql` command
        - If the table `second_table` already exists, your script should not fail
        - You are not allowed to use the `SELECT` and `SHOW` statements
        - Your script should create these records:
            `id` = 1, `name` = “John”, `score` = 10
            `id` = 2, `name` = “Alex”, `score` = 3
            `id` = 3, `name` = “Bob”, `score` = 14
            `id` = 4, `name` = “George”, `score` = 8
program [9-full_creation.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/9-full_creation.sql)

### Task 10 :
        Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - Results should display both the score and the name (in this order)
        - Records should be ordered by score (top first)
        - The database name will be passed as an argument of the `mysql` command
program [10-top_score.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/10-top_score.sql)

### Task 11 :
        Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - Results should display both the score and the name (in this order)
        - Records should be ordered by score (top first)
        - The database name will be passed as an argument of the `mysql` command
program [11-best_score.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/11-best_score.sql)

### Task 12 :
        Write a script that updates the score of Bob to `10` in the table `second_table`.
        - You are not allowed to use Bob’s id value, only the `name` field
        - The database name will be passed as an argument of the `mysql` command
program [12-no_cheating.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/12-no_cheating.sql)

### Task 13 :
        Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - The database name will be passed as an argument of the mysql command
program [13-change_class.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/13-change_class.sql)

### Task 14 :
        Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - The result column name should be `average`
        - The database name will be passed as an argument of the `mysql` command
program [14-average.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/14-average.sql)

### Task 15 :
        Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - The result should display:
            the `score`
            the number of records for this `score` with the label `number`
        - The list should be sorted by the number of records (descending)
        - The database name will be passed as an argument to the `mysql` command
program [15-groups.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/15-groups.sql)

### Task 16 :
        Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
        - Don’t list rows where the `name` column does not contain a value
        - Results should display the score and the name (in this order)
        - Records should be listed by descending score
        - The database name will be passed as an argument to the `mysql` command
        In this example, new data have been added to the table `second_table`.
program [16-no_link.sql](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/SQL_introduction/16-no_link.sql)