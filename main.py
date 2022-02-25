#!/c/Program Files (x86)/Python38-32/python
import csv
import sqlite3


# connection = None
# cursor = None
# create_table = ""
# file = open('employees.csv')
# csv_file = ""
# contents = None
# insert_records = ""
# select_all = ""
# rows = None


def employees(param, param1, param2, param3, param4, param5):
    pass


def CreateTable(cur):
    create_table = '''CREATE TABLE IF NOT EXISTS employees (
                        empid INTEGER PRIMARY KEY NOT NULL,
                        fname TEXT NOT NULL,
                        lname TEXT NOT NULL,
                        salary INTEGER NOT NULL,
                        position TEXT NOT NULL,
                        startdate TEXT NOT NULL);
                        '''
    cur.execute(create_table)
    return

def DropTable(cur):
    drop_table = '''DROP TABLE employees;'''
    cur.execute(drop_table)
    return

if __name__ == "__main__":
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    csv_file = "employees.csv"
    insert_records = ('''INSERT INTO employees (empid, fname, lname, salary, position, startdate) 
VALUES(?, ?, ?, ?, ?, ?);''')
    select_all = '''SELECT * FROM employees;'''
    emp_count = '''SELECT COUNT(empid) FROM employees;'''
    max_salary = '''SELECT MAX(salary) FROM employees;'''
    max_position = '''SELECT position FROM employees
        WHERE salary = (SELECT max(salary) FROM employees);'''
    # LPE = lowest paid employee
    lpe = '''SELECT fname, lname, position, min(salary) FROM employees;'''

    DropTable(cursor)

    CreateTable(cursor)

    file = open('employees.csv')

    reader = csv.reader(file)

    next(reader, None)

    cursor.executemany(insert_records, reader)

    connection.commit()


    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    count = cursor.execute(emp_count).fetchall()
    # Count is a list, lists have values stored in index positions
    # We are going to bind the value of count index position 0 to variable tupe1

    tupe1 = count[0]
    # Now that tupe1 has the value of index position of list count[0]
    # Convert int to str for tupe1[0]

    tupe1str = str(tupe1[0])

    print("You have " + tupe1str + " employees!")

    # Find maximum salary of all employees and what position they have with the company

    salary = cursor.execute(max_salary).fetchall()
    # salary is a list, lists have values stored in index positions
    # We are going to bind the value of salary index position 0 to variable tupe2
    position = cursor.execute(max_position).fetchall()
    tupe2 = salary[0]
    # Now that tupe2 has the value of index position of list salary_position[0]
    # Convert int to str for tupe2[0]

    tupe2str = str(tupe2[0])
    results = position[0]
    pos1str = str(position[0])

    print(type(pos1str))

    print("Your highest paid employee makes $" + tupe2str + ". Their position with the company is " + pos1str)

    # Find the employee with the lowest salary, the name of that employee, and what position they have with the company

    records = cursor.execute(lpe).fetchall()

    # for item in records:
    #     print(item)

    results = records[0]
    fname = str(results[0])
    lname = str(results[1])
    pos = str(results[2])
    sal = str(results[3])

    print("Your lowest paid employee is" + lname + "," + fname + ". This employee makes $" + sal + " annually. This employee was hired on as a" + pos + ".")
