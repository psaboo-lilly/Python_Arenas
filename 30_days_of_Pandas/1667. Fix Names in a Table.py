"""
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 
Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id. The result format is in the following example.

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
"""

#------_SOLUTION--------#
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
    # Avoid doing:- df = users // since this will assign df variable to users's location and can modify it
    df = users.copy()

    """
    ---- 1-line shortcut using In-built function str.capitalise()-----

    df['name'] = df['name'].str.capitalize() // THis will captialize 1st letter and lower case remaining letter of string
    """

    # Row-wise operations using apply()
    df['name'] = df.apply(
            lambda row: row['name'][0].upper() + row['name'][1:].lower(), 
            axis=1
            )
  
    result_df = df[['user_id', 'name']].sort_values(['user_id'], ascending = [True])

    return result_df
