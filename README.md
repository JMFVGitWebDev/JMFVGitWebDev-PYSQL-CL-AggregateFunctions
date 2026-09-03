# Background

SQL sublanguage: DQL (Data Query Language)

Aggregate functions perform operations on multiple rows to produce a single output. Some commonly used ones:

- SUM() - outputs the sum of the values in a single column
- COUNT() - outputs the number of rows in the result set
- MIN() - outputs the least value among the values in a single column
- MAX() - outputs the greatest value among the values in a single column

SELECT SUM(salary) FROM employee;

## Problem 1

Assume the following table already exists.

| id | first_name | last_name | salary |
|----|------------|-----------|--------|
| 1 | Steve | Garcia | 67400.00 |
| 2 | Alexa | Smith | 42500.00 |
| 3 | Steve | Jones | 99890.99 |
| 4 | Brandon | Smith | 120000 |
| 5 | Adam | Jones | 55050.50 |

In `problem1.sql`, use SUM() to output the total of all salaries found in the table.

## Problem 2

Using the same table above, in `problem2.sql`, use COUNT() to output the number of employees with the last name
"Smith".

## Problem 3

Using the same table above, in `problem3.sql`, use MIN() to return the lowest salary.

## Problem 4

Using the same table above, in `problem4.sql`, use MAX() to return the highest salary.
