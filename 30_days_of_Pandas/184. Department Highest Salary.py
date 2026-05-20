"""
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 
Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.
The result format is in the following example.

"""
#---------SOLTUION----------_#
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'inner')

    # === dense_rank() over(partition by deprtmentId order by Salary) as rank ===
    df['rank'] = df.groupby(['departmentId'])['salary'].rank(method = 'dense', ascending = False)
    
    df = df[df['rank'] == 1]

    result_df = df[['name_y', 'name_x', 'salary']]
    result_df = result_df.rename(
        columns = {
            'name_y': 'Department',
            'name_x': 'Employee',
            'salary': 'Salary'
        }
    )
    return result_df
    
