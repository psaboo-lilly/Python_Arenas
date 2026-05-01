'''
Question -> Consecutive Days (Stratascratch) | Hard
ID 2054

Find all the users who were active for 3 consecutive days or more.

-------Sample Input---------
Table -> sf_events

record_date	account_id	user_id
2021-01-01	A1	U1
2021-01-01	A1	U2
2021-01-10	A2	U4
2021-01-11	A2	U4
2021-01-12	A2	U4
2021-01-15	A2	U5

-------Sample Output---------
user_id
U4

'''

# Import your libraries
import pyspark
from pyspark.sql.window import Window
from pyspark.sql import functions as f

# Start writing code
sf_events

'''
Long logic:- Create 2 columns contaning next_day and prev_day for every record_date
Then create 2 more flag columns contaning diff(next/prev days and record_date)
If both the flags = 1 then that particular row will be middle term of 3 consecutive entries

CONS -> Add 5 new columns in DB is coslty

window_frame = Window.partitionBy(sf_events.user_id).orderBy(sf_events.record_date.asc())


df = sf_events.withColumn('row_num', f.row_number().over(window_frame))
df = df.withColumn('next_day', f.lead('record_date',1).over(window_frame))
df = df.withColumn('prev_day', f.lead('record_date',-1).over(window_frame))

df = df.withColumn('next_diff', f.datediff(df['next_day'],df['record_date']))
df = df.withColumn('prev_diff', f.datediff(df['record_date'],df['prev_day']))

result_df = df[(df['next_diff']==1) & (df['prev_diff']==1)]

result_df = result_df.select('user_id').distinct()
'''

# Using Anchor Date column and Aggregation

# 1. Remove duplicates
df = sf_events.select('user_id', 'record_date').distinct()

# 2. Calculate row_number for each record_date partitioned by user
window_frame = Window.partitionBy(df.user_id).orderBy(df.record_date.asc())

df = df.withColumn('row_num', f.row_number().over(window_frame))

# 3. LOGIC -> Find anchor_date = (Record_date - row_number) ||Use date_sub() function
df = df.withColumn('anchor_date', f.date_sub(df['record_date'], df['row_num']))

# 4. Group by on Anchor_Date and if it's count() >= 3 then you have consecutive dates
df = df.groupBy(df['user_id'], df['anchor_date']).agg(f.count(df['anchor_date']).alias('cnt'))
result_df = df.filter(df['cnt']>=3)

result_df = result_df.select('user_id')

#result_df.show()
result_df.toPandas()
