'''
Question -> Best Selling Item [Platform - stratascratch) | Hard

ID 10172

Find the best-selling item for each month (no need to separate months by year). 
The best-selling item is determined by the highest total sales amount, calculated as: total_paid = unitprice * quantity. 
A negative quantity indicates a return or cancellation (the invoice number begins with 'C'. 
To calculate sales, ignore returns and cancellations. Output the month, description of the item, and the total amount paid.

'''

'''
-----Sample Input--------
invoiceno	stockcode	description	quantity	invoicedate	unitprice	customerid	country
544586	21890	S/6 WOODEN SKITTLES IN COTTON BAG	3	2011-02-21	2.95	17338	United Kingdom
541104	84509G	SET OF 4 FAIRY CAKE PLACEMATS	3	2011-01-13	3.29		United Kingdom
560772	22499	WOODEN UNION JACK BUNTING	3	2011-07-20	4.96		United Kingdom

-----Sample Output--------
month	description	total_paid
1	LUNCH BAG SPACEBOY DESIGN	74.26
2	REGENCY CAKESTAND 3 TIER	38.25
3	PAPER BUNTING WHITE LACE	102
4	SPACEBOY LUNCH BOX	23.4
5	PAPER BUNTING WHITE LACE	51
'''

# Import your libraries
import pyspark
from pyspark.sql import functions as f
from pyspark.sql.window import Window

# Start writing code
online_retail = online_retail.withColumn('month', f.month(online_retail['invoicedate']))


online_retail = online_retail.withColumn('total_paid', online_retail.quantity * online_retail.unitprice)

# Multiple inovices for a product can be present in a single month
df = online_retail.groupBy('month','description').agg(f.sum('total_paid').alias('total_paid')).orderBy('month')

# Use of WINDOW functions in Pyspark
window_frame = Window.partitionBy('month').orderBy(df['total_paid'].desc())
df = df.withColumn('rankk', f.rank().over(window_frame))

result_df = df.filter(df['rankk']==1)
result_df['month','description','total_paid'].toPandas()

#result_df.show()



