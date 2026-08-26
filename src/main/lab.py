import os
import sqlite3

"""
SQL sublanguage: DQL (Data Query Language)

Aggregate functions in SQL are functions which perform operations on multiple rows to produce a single output.

There are many aggregate functions built into SQL, some commonly used ones include:
- SUM() - outputs the sum of the values in a single column from the result set
- COUNT() - outputs the number of rows in the result set
- MIN() - outputs the least value among the values in a single column from the result set
- MAX() - similar to MIN but outputs the greatest value
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def _seeded_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE employee ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "first_name VARCHAR(255),"
        "last_name VARCHAR(255),"
        "salary DOUBLE PRECISION"
        ");"
    )
    cur.execute(
        "INSERT INTO employee (first_name, last_name, salary) VALUES "
        "('Steve', 'Garcia', 67400.00),"
        "('Alexa', 'Smith', 42500.00),"
        "('Steve', 'Jones', 99890.99),"
        "('Brandon', 'Smith', 120000),"
        "('Adam', 'Jones', 55050.50);"
    )
    conn.commit()
    return conn, cur


def problem1():
    """
    employee table
    |  id  |   first_name   |   last_name   |  salary  |
    --------------------------------------------------
    |1     |'Steve'         |'Garcia'       |67400.00  |
    |2     |'Alexa'         |'Smith'        |42500.00  |
    |3     |'Steve'         |'Jones'        |99890.99  |
    |4     |'Brandon'       |'Smith'        |120000    |
    |5     |'Adam'          |'Jones'        |55050.50  |

    Problem 1: use the SUM() aggregate function to output the total of all salaries found in the table.
    """
    sql = _read_sql("problem1.sql")

    conn, cur = _seeded_connection()

    total = None
    try:
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            total = row[0]
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return total


def problem2():
    """
    Problem 2: use the COUNT() aggregate function to output the number of employees with the last name "Smith".
    """
    sql = _read_sql("problem2.sql")

    conn, cur = _seeded_connection()

    count = None
    try:
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            count = row[0]
    except Exception as e:
        print(f"problem2: {e}\n")
    finally:
        conn.close()

    return count


def problem3():
    """
    Problem 3: use the MIN() aggregate function to return the lowest salary.
    """
    sql = _read_sql("problem3.sql")

    conn, cur = _seeded_connection()

    minimum = None
    try:
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            minimum = row[0]
    except Exception as e:
        print(f"problem3: {e}\n")
    finally:
        conn.close()

    return minimum


def problem4():
    """
    Problem 4: use the MAX() aggregate function to return the highest salary.
    """
    sql = _read_sql("problem4.sql")

    conn, cur = _seeded_connection()

    maximum = None
    try:
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            maximum = row[0]
    except Exception as e:
        print(f"problem4: {e}\n")
    finally:
        conn.close()

    return maximum
