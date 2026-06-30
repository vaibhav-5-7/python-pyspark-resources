Impt Coding Pyspark Interview Question:
========================================================
1.Write a spark code snippet to calculate the sum of a salary in a Df?
soln:
=========
from pyspark.sql.functions import *
from pyspark.sql.types import *
data = [("John Doe","john@example.com",50000.0),\
        ("Jane Smith","jane@example.com",60000.0),\
        ("Bob Johnson","bob@example.com",5500.0)
        ]
schema = "Name string,Email string,Salary double"
df = spark.createDataFrame(data=data,schema=schema)
display(df)
df.printSchema()
o/p:
=========
Name	        Email	        Salary
John Doe	john@example.com	50000
Jane Smith	jane@example.com	60000
Bob Johnson	bob@example.com	    5500

root
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Salary: double (nullable = true)
 
i. 1stMethod:
====================
a.  df_salary = df.agg(sum(col("Salary")).alias("total_salary"))
display(df_salary)
b.  df.createOrReplaceTempView("df_salary")
    df_final = spark.sql("select sum(Salary) as total_salary from df_salary")
    display(df_final)

o/p:
==========
115500

ii. To get data in form of variable:
======================================
a. df_salary = df.agg(sum(col("Salary")).alias("total_salary"))
   df_salary.collect()[0][0]
b. df_salary = df.agg(sum(col("Salary")).alias("total_salary"))
   df_salary.first()[0]
   
o/p:
=========
115500.0


2. Pyspark Code:
    ======================================

1. Load the data into a Pyspark Df.
2. Calculate the total purchase amount for each customer.
3. Find the customer with the highest total purchase amount.

Solution:
=================
1. Load the data into a Pyspark Df.
===========================================
from pyspark.sql.types import *
data = [(1,100,'2023-01-15'),\
        (2,150,'2023-02-20'),\
        (1,200,'2023-03-10'),\
        (3,50,'2023-04-05'),\
        (2,120,'2023-05-15'),\
        (1,300,'2023-06-25')
        ]
schema = StructType([
         StructField("customer_id",IntegerType(),True),\
         StructField("purchase_amount",IntegerType(),True),\
         StructField("purchase_date",StringType(),True),\
])
df = spark.createDataFrame(data=data,schema=schema)
display(df)
df.printSchema()
0/p:
=======
customer_id	   purchase_amount	  purchase_date
1	             100	          2023-01-15
2	             150	          2023-02-20
1	             200	          2023-03-10
3	             50	              2023-04-05
2	             120	          2023-05-15
1	             300	          2023-06-25

root
 |-- customer_id: integer (nullable = true)
 |-- purchase_amount: integer (nullable = true)
 |-- purchase_date: string (nullable = true)
 
1. Converting the datatype of purchase_date column:
==============================================================
df_cast = df.withColumn("purchase_date",col("purchase_date").cast("date"))
display(df_cast)
df_cast.printSchema()
0/p:
======
customer_id	   purchase_amount	  purchase_date
1	             100	          2023-01-15
2	             150	          2023-02-20
1	             200	          2023-03-10
3	             50	              2023-04-05
2	             120	          2023-05-15
1	             300	          2023-06-25
root
 |-- customer_id: integer (nullable = true)
 |-- purchase_amount: integer (nullable = true)
 |-- purchase_date: date (nullable = true)
 
3. Calculate the total purchase amount for each customer (Using Pyspark Df, sparksql):
=============================================================================================
i. df_total_purchase_amount = df_cast.groupBy(col("customer_id"))\
                                  .agg(sum(col("purchase_amount"))\
                                  .alias("total_purchase_amount"))

display(df_total_purchase_amount)

ii. df_cast.createOrReplaceTempView("df_cast1")
df_total_purchase_amount_1 = spark.sql("select customer_id,sum(purchase_amount) as total_purchase_amount from df_cast1 group by customer_id")
display(df_total_purchase_amount_1)

o/p:
==========
customer_id	   total_purchase_amount
1	             600
2	             270
3	              50

4. Find the customer with the highest total purchase amount.
==================================================================
i. df_customer_with_highest_purchase_amount = df_total_purchase_amount.sort(col("total_purchase_amount").desc())\
.limit(1)
display(df_customer_with_highest_purchase_amount)

ii. df_total_purchase_amount_1.createOrReplaceTempView("df_customer_with_highest_purchase_amount")
df_customer_with_highest_purchase_amount_1 = spark.sql("select * from df_customer_with_highest_purchase_amount order by  total_purchase_amount desc limit 1")
display(df_customer_with_highest_purchase_amount_1)

o/p:
=========
customer_id	    total_purchase_amount
1	              600

3. Solve Word count problem using pyspark:
=======================================================
i. Using Lower Level Api rdd():
===================================================
from pyspark.sql import SparkSession
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [
    'big data is very interesting',
    'big data is one of the most trending technology',
    'my name is prem and i love big data',
    'my current company is deloitte',
    ''
]
rdd1 = spark.sparkContext.parallelize(rdd1)
rdd1.collect()
o/p:
=========
['big data is very interesting',
 'big data is one of the most trending technology',
 'my name is prem and i love big data',
 'my current company is deloitte',
 '']
rdd2 = rdd1.flatMap(lambda x:x.split(" "))
rdd2.collect()
o/p:
=======
['big',
 'data',
 'is',
 'very',
 'interesting',
 'big',
 'data',
 'is',
 'one',
 'of',
 'the',
 'most',
 'trending',
 'technology',
 'my',
 'name',
 'is',
 'prem',
 'and',
 'i',
 'love',
 'big',
 'data',
 'my',
 'current',
 'company',
 'is',
 'deloitte',
 '']
rdd3 = rdd2.map(lambda x:(x,1))
rdd3.collect()
o/p:
=======
[('big', 1),
 ('data', 1),
 ('is', 1),
 ('very', 1),
 ('interesting', 1),
 ('big', 1),
 ('data', 1),
 ('is', 1),
 ('one', 1),
 ('of', 1),
 ('the', 1),
 ('most', 1),
 ('trending', 1),
 ('technology', 1),
 ('my', 1),
 ('name', 1),
 ('is', 1),
 ('prem', 1),
 ('and', 1),
 ('i', 1),
 ('love', 1),
 ('big', 1),
 ('data', 1),
 ('my', 1),
 ('current', 1),
 ('company', 1),
 ('is', 1),
 ('deloitte', 1),
 ('', 1)]
rdd4 = rdd3.reduceByKey(lambda x,y:x+y)
rdd4.collect()
rdd4.saveAsTextFile("/user/itv022641/outputwc")
o/p:
=========
[('name', 1),
 ('is', 4),
 ('i', 1),
 ('love', 1),
 ('current', 1),
 ('', 1),
 ('very', 1),
 ('interesting', 1),
 ('of', 1),
 ('trending', 1),
 ('technology', 1),
 ('big', 3),
 ('data', 3),
 ('one', 1),
 ('the', 1),
 ('most', 1),
 ('my', 2),
 ('prem', 1),
 ('and', 1),
 ('company', 1),
 ('deloitte', 1)]
To check the output folder:
=================================
hadoop fs -ls /user/itv022641/outputwc
0/p:
========
-rw-r--r--   3 itv022641 supergroup          0 2026-02-14 02:17 /user/itv022641/outputwc/_SUCCESS
-rw-r--r--   3 itv022641 supergroup        141 2026-02-14 02:17 /user/itv022641/outputwc/part-00000
-rw-r--r--   3 itv022641 supergroup        121 2026-02-14 02:17 /user/itv022641/outputwc/part-00001
hadoop fs -cat /user/itv022641/outputwc/*
o/p:
=======
('name', 1)
('is', 4)
('i', 1)
('love', 1)
('current', 1)
('', 1)
('very', 1)
('interesting', 1)
('of', 1)
('trending', 1)
('technology', 1)
('big', 3)
('data', 3)
('one', 1)
('the', 1)
('most', 1)
('my', 2)
('prem', 1)
('and', 1)
('company', 1)
('deloitte', 1)

ii. Using higher level api df():
==========================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [
    ('big data is very interesting',),
    ('big data is one of the most trending technology',),
    ('my name is prem and i love big data',),
    ('my current company is deloitte',),
    ('',)
]

schema = ['word']

df = spark.createDataFrame(data, schema)

display(df)
df.printSchema()
o/p:
============
word
=========
big data is very ...
big data is one o...
my name is prem a...
my current compan...

root
 |-- word: string (nullable = true)
df_explode = df.withColumn("singleword",explode(split(col("word")," ")))\
               .drop(col("word"))
display(df_explode)
o/p:
========
singleword:
=================
big
data
is
very
interesting
big
data
is
one
of
the
most
trending
technology
my
name
is
prem
and
i
df_word_count = df_explode.groupBy(col("singleword"))\
                          .count()
display(df_word_count)
o/p:
===========
singleword	   count
name	        1
technology	    1
love	        1
one	            1
deloitte	    1
is	            4
data	        3
current	        1
the	            1
my	            2
i	            1
and	            1
prem	        1
of	            1
very	        1
interesting	    1
company	        1
most	        1
                1
trending	    1
df_word_count.write.format("csv")\
            .option("mode","overwrite")\
            .option("path","/user/itv022641/outputwc2")\
            .save()
To check the output folder:
=================================
hadoop fs -cat /user/itv022641/outputwc2/*
o/p:
============
name,1
technology,1
love,1
one,1
deloitte,1
is,4
data,3
the,1
current,1
my,2
i,1
and,1
prem,1
of,1
very,1
interesting,1
company,1
most,1
"",1
trending,1
big,3

iii. Using sparksql()":
=================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

data = [
    ('big data is very interesting',),
    ('big data is one of the most trending technology',),
    ('my name is prem and i love big data',),
    ('my current company is deloitte',),
    ('',)
]

schema = ['word']

df = spark.createDataFrame(data, schema)

display(df)
df.printSchema()
o/p:
===========
word
=========
big data is very ...
big data is one o...
my name is prem a...
my current compan...

root
 |-- word: string (nullable = true)
 df.createOrReplaceTempView("df_word_count")
df_final = spark.sql("""
SELECT word, COUNT(*) AS count
FROM (
    SELECT explode(split(word, ' ')) AS word
    FROM df_word_count
) temp
GROUP BY word
""")

display(df_final)
o/p:
=================
word	      count
name	        1
technology	    1
love	        1
one	            1
deloitte	    1
is	            4
data	        3
current	        1
the	            1
my	            2
i	            1
and	            1
prem	        1
of	            1
very	        1
interesting	    1
company	        1
most	        1
                1
trending	    1



Impt Concept from this code is:
==========================================
1. Use of collect():
==============================
i. It is not recommended to use .collect() in production because collect store/print entire result on driver machine so if the data size is too huge than in that case it 
leads to OOM issue.
ii. Instead of using .collect() use .saveAsTextFile() in production.
iii. .collect() is an action , so it is eager operation.

2. SparkSession():
=============================
i. It is an entry point to spark cluster.
ii. It ia an unified session like umbrella that encapsulate all the other smaller session like (sparkcontext,hivecontext,sqlcontext).
iii. It is given from spark version 2.
iv. To deal with DF/SparkSql we mainly use SparkSession().
v. To deal with Rdd we mainly use sparkcontext().
syntax for sparksession is:
=================================
from pyspark.sql import SparkSession
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

3. map() vs flatMap():
================================
i. map():
===================
a. It is one to one function which means it takes one line as input and give one line as output in form of (K,V) pair.
b. It is a transformation which means it is an lazy operation.
c. for example:
===========================
i/p to map():
['big',
 'data',
 'is',
 'very',
 'interesting',
 'big',
 'data',
 'is',
 'one',
 'of',
 'the',
 'most',
 'trending',
 'technology',
 'my',
 'name',
 'is',
 'prem',
 'and',
 'i',
 'love',
 'big',
 'data',
 'my',
 'current',
 'company',
 'is',
 'deloitte',
 '']
rdd3 = rdd2.map(lambda x:(x,1))
rdd3.collect()
o/p from map():
==================
[('big', 1),
 ('data', 1),
 ('is', 1),
 ('very', 1),
 ('interesting', 1),
 ('big', 1),
 ('data', 1),
 ('is', 1),
 ('one', 1),
 ('of', 1),
 ('the', 1),
 ('most', 1),
 ('trending', 1),
 ('technology', 1),
 ('my', 1),
 ('name', 1),
 ('is', 1),
 ('prem', 1),
 ('and', 1),
 ('i', 1),
 ('love', 1),
 ('big', 1),
 ('data', 1),
 ('my', 1),
 ('current', 1),
 ('company', 1),
 ('is', 1),
 ('deloitte', 1),
 ('', 1)]

ii. flatMap():
=========================
a. It is one to many function which means it takes each row as input and gives multiple row as output.
b. It is transformation which maens it is an lazy operation.
c. For example:
====================
i/p to flatMap():
=====================
['big data is very interesting',
 'big data is one of the most trending technology',
 'my name is prem and i love big data',
 'my current company is deloitte',
 '']
rdd2 = rdd1.flatMap(lambda x:x.split(" "))
rdd2.collect()
o/p from flatMap():
==========================
['big',
 'data',
 'is',
 'very',
 'interesting',
 'big',
 'data',
 'is',
 'one',
 'of',
 'the',
 'most',
 'trending',
 'technology',
 'my',
 'name',
 'is',
 'prem',
 'and',
 'i',
 'love',
 'big',
 'data',
 'my',
 'current',
 'company',
 'is',
 'deloitte',
 '']    

5. Pyspark Code:
==============================
1. Count the orders under each status:
2. Find the Premium customers (Top 10 who placed the most number of orders).
3. Distinct count of customers who placed atleast one order.
4. Which customers has the maximum number of CLOSED orders.

Solution:
===================
1. Count the orders under each status:
===========================================
i. Using rdd() :
==============================
from pyspark.sql import SparkSession
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
orders_rdd = spark.sparkContext.textFile("/public/trendytech/retail_db/orders/*")
orders_rdd.take(10)
o/p:
=========
['1,2013-07-25 00:00:00.0,11599,CLOSED',
 '2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT',
 '3,2013-07-25 00:00:00.0,12111,COMPLETE',
 '4,2013-07-25 00:00:00.0,8827,CLOSED',
 '5,2013-07-25 00:00:00.0,11318,COMPLETE',
 '6,2013-07-25 00:00:00.0,7130,COMPLETE',
 '7,2013-07-25 00:00:00.0,4530,COMPLETE',
 '8,2013-07-25 00:00:00.0,2911,PROCESSING',
 '9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT',
 '10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT']
mapped_rdd = orders_rdd.map(lambda x:(x.split(",")[3],1))
mapped_rdd.take(10)
o/p:
========
[('CLOSED', 1),
 ('PENDING_PAYMENT', 1),
 ('COMPLETE', 1),
 ('CLOSED', 1),
 ('COMPLETE', 1),
 ('COMPLETE', 1),
 ('COMPLETE', 1),
 ('PROCESSING', 1),
 ('PENDING_PAYMENT', 1),
 ('PENDING_PAYMENT', 1)]
reduced_rdd = mapped_rdd.reduceByKey(lambda x,y:x+y)
reduced_rdd.collect()
o/p:
==========
[('CLOSED', 7556),
 ('CANCELED', 1428),
 ('PENDING_PAYMENT', 15030),
 ('COMPLETE', 22899),
 ('PROCESSING', 8275),
 ('PAYMENT_REVIEW', 729),
 ('PENDING', 7610),
 ('ON_HOLD', 3798),
 ('SUSPECTED_FRAUD', 1558)]

Ascending order:
====================
reduced_sorted = reduced_rdd.sortBy(lambda x:x[1])
reduced_sorted.collect()
o/p:
=========
[('PAYMENT_REVIEW', 729),
 ('CANCELED', 1428),
 ('SUSPECTED_FRAUD', 1558),
 ('ON_HOLD', 3798),
 ('CLOSED', 7556),
 ('PENDING', 7610),
 ('PROCESSING', 8275),
 ('PENDING_PAYMENT', 15030),
 ('COMPLETE', 22899)]
 
Descending order:
========================
reduced_sorted = reduced_rdd.sortBy(lambda x:x[1],False)
reduced_sorted.collect()
o/p:
==========
[('COMPLETE', 22899),
 ('PENDING_PAYMENT', 15030),
 ('PROCESSING', 8275),
 ('PENDING', 7610),
 ('CLOSED', 7556),
 ('ON_HOLD', 3798),
 ('SUSPECTED_FRAUD', 1558),
 ('CANCELED', 1428),
 ('PAYMENT_REVIEW', 729)]
 
2. Find the Premium customers (Top 10 who placed the most number of orders):
====================================================================================
i. Using rdd():
=========================
customers_mapped = orders_rdd.map(lambda x:(x.split(",")[2],1))
customers_mapped.take(10)
o/p:
============
[('11599', 1),
 ('256', 1),
 ('12111', 1),
 ('8827', 1),
 ('11318', 1),
 ('7130', 1),
 ('4530', 1),
 ('2911', 1),
 ('5657', 1),
 ('5648', 1)]
customers_aggregated = customers_mapped.reduceByKey(lambda x,y:x+y)
customers_aggregated.take(20)
o/p:
========
[('256', 10),
 ('12111', 6),
 ('11318', 6),
 ('7130', 7),
 ('2911', 6),
 ('5657', 12),
 ('9149', 4),
 ('9842', 7),
 ('7276', 5),
 ('9488', 7),
 ('2711', 3),
 ('333', 6),
 ('656', 5),
 ('6983', 6),
 ('4189', 3),
 ('4840', 2),
 ('5863', 6),
 ('8214', 5),
 ('7776', 8),
 ('1549', 4)]
customers_sorted = customers_aggregated.sortBy(lambda x:x[1],False)
customers_sorted.take(10)
o/p:
========
[('5897', 16),
 ('6316', 16),
 ('12431', 16),
 ('569', 16),
 ('4320', 15),
 ('221', 15),
 ('5624', 15),
 ('5283', 15),
 ('12284', 15),
 ('5654', 15)]
 
3. Distinct count of customers who placed atleast one order:
===================================================================
i. Using rdd():
======================
distinct_customers = orders_rdd.map(lambda x:x.split(",")[2]).distinct()
distinct_customers.count()
o/p:
=========
12405

orders_rdd.count()
o/p:
========
68883


4. Which customers has the maximum number of CLOSED orders:
=============================================================
i. Using rdd():
=====================
filtered_orders = orders_rdd.filter(lambda x:(x.split(",")[3] == 'CLOSED'))
filtered_orders.take(20)
o/p:
========
['1,2013-07-25 00:00:00.0,11599,CLOSED',
 '4,2013-07-25 00:00:00.0,8827,CLOSED',
 '12,2013-07-25 00:00:00.0,1837,CLOSED',
 '18,2013-07-25 00:00:00.0,1205,CLOSED',
 '24,2013-07-25 00:00:00.0,11441,CLOSED',
 '25,2013-07-25 00:00:00.0,9503,CLOSED',
 '37,2013-07-25 00:00:00.0,5863,CLOSED',
 '51,2013-07-25 00:00:00.0,12271,CLOSED',
 '57,2013-07-25 00:00:00.0,7073,CLOSED',
 '61,2013-07-25 00:00:00.0,4791,CLOSED',
 '62,2013-07-25 00:00:00.0,9111,CLOSED',
 '87,2013-07-25 00:00:00.0,3065,CLOSED',
 '90,2013-07-25 00:00:00.0,9131,CLOSED',
 '101,2013-07-25 00:00:00.0,5116,CLOSED',
 '116,2013-07-26 00:00:00.0,8763,CLOSED',
 '129,2013-07-26 00:00:00.0,9937,CLOSED',
 '133,2013-07-26 00:00:00.0,10604,CLOSED',
 '191,2013-07-26 00:00:00.0,16,CLOSED',
 '201,2013-07-26 00:00:00.0,9055,CLOSED',
 '211,2013-07-26 00:00:00.0,10372,CLOSED']
 
filtered_mapped = filtered_orders.map(lambda x:(x.split(",")[2],1))
filtered_mapped.take(20)
o/p:
=========
[('11599', 1),
 ('8827', 1),
 ('1837', 1),
 ('1205', 1),
 ('11441', 1),
 ('9503', 1),
 ('5863', 1),
 ('12271', 1),
 ('7073', 1),
 ('4791', 1),
 ('9111', 1),
 ('3065', 1),
 ('9131', 1),
 ('5116', 1),
 ('8763', 1),
 ('9937', 1),
 ('10604', 1),
 ('16', 1),
 ('9055', 1),
 ('10372', 1)]
filtered_aggregated = filtered_mapped.reduceByKey(lambda x,y : x+y)
filtered_aggregated.take(20)
o/p:
==========
[('3159', 1),
 ('5834', 2),
 ('10173', 1),
 ('2101', 1),
 ('6000', 1),
 ('1352', 2),
 ('10142', 1),
 ('12210', 1),
 ('6018', 2),
 ('2252', 1),
 ('10290', 2),
 ('9117', 1),
 ('7600', 2),
 ('6482', 1),
 ('9420', 1),
 ('11673', 3),
 ('7435', 2),
 ('7879', 4),
 ('11153', 3),
 ('9771', 1)]
filtered_sorted = filtered_aggregated.sortBy(lambda x:x[1],False)
filtered_sorted.take(20)
o/p:
=========
[('1833', 6),
 ('1363', 5),
 ('1687', 5),
 ('5493', 5),
 ('5011', 4),
 ('8974', 4),
 ('2321', 4),
 ('3736', 4),
 ('8368', 4),
 ('2236', 4),
 ('2403', 4),
 ('7879', 4),
 ('1764', 4),
 ('4588', 4),
 ('7948', 4),
 ('7850', 4),
 ('145', 4),
 ('4282', 4),
 ('9213', 4),
 ('3631', 4)]
 
1. Count the orders under each status:
===========================================
i. Using Df() :
==============================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

schema = StructType([\
                     StructField("order_id",IntegerType(),True),\
                     StructField("order_date",TimestampType(),True),\
                     StructField("customer_id",IntegerType(),True),\
                     StructField("order_status",StringType(),True)
                     ])
df = spark.read.format("csv")\
    .option("header","True")\
    .option("delimiter",",")\
    .schema(schema)\
    .load("/public/trendytech/retail_db/orders/*")
df.show(20)
o/p:
===========
+--------+-------------------+-----------+---------------+
|order_id|         order_date|customer_id|   order_status|
+--------+-------------------+-----------+---------------+
|       2|2013-07-25 00:00:00|        256|PENDING_PAYMENT|
|       3|2013-07-25 00:00:00|      12111|       COMPLETE|
|       4|2013-07-25 00:00:00|       8827|         CLOSED|
|       5|2013-07-25 00:00:00|      11318|       COMPLETE|
|       6|2013-07-25 00:00:00|       7130|       COMPLETE|
|       7|2013-07-25 00:00:00|       4530|       COMPLETE|
|       8|2013-07-25 00:00:00|       2911|     PROCESSING|
|       9|2013-07-25 00:00:00|       5657|PENDING_PAYMENT|
|      10|2013-07-25 00:00:00|       5648|PENDING_PAYMENT|
|      11|2013-07-25 00:00:00|        918| PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|         CLOSED|
|      13|2013-07-25 00:00:00|       9149|PENDING_PAYMENT|
|      14|2013-07-25 00:00:00|       9842|     PROCESSING|
|      15|2013-07-25 00:00:00|       2568|       COMPLETE|
|      16|2013-07-25 00:00:00|       7276|PENDING_PAYMENT|
|      17|2013-07-25 00:00:00|       2667|       COMPLETE|
|      18|2013-07-25 00:00:00|       1205|         CLOSED|
|      19|2013-07-25 00:00:00|       9488|PENDING_PAYMENT|
|      20|2013-07-25 00:00:00|       9198|     PROCESSING|
|      21|2013-07-25 00:00:00|       2711|        PENDING|
+--------+-------------------+-----------+---------------+
df.printSchema()
o/p:
=======
root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
 
df_count = df.groupBy(col("order_status"))\
             .agg(count(col("order_id")).alias("total_orders"))\
             .sort(col("total_orders").desc())
df_count.show(20)
ii. Using spark sql:
============================================
df.createOrReplaceTempView("count_1")
df_count = spark.sql("""select order_status,count(order_id) as total_orders 
                        from count_1 
                        group by order_status 
                        order by total_orders desc""")
df_count.show()
o/p:
=======
+---------------+------------+
|   order_status|total_orders|
+---------------+------------+
|       COMPLETE|       22899|
|PENDING_PAYMENT|       15030|
|     PROCESSING|        8275|
|        PENDING|        7610|
|         CLOSED|        7555|
|        ON_HOLD|        3798|
|SUSPECTED_FRAUD|        1558|
|       CANCELED|        1428|
| PAYMENT_REVIEW|         729|
+---------------+------------+

2. Find the Premium customers (Top 10 who placed the most number of orders):
====================================================================================
i. Using Df():
=========================
df_premium_customer = df.groupBy("customer_id")\
                        .count()\
                        .sort(col("count").desc())\
                        .limit(10)
ii. Using spark sql:
==============================
df_premium_customer = spark.sql("""select customer_id,count(1) as total_count
                                      from count_1
                                      group by customer_id 
                                      order by total_count desc
                                      limit(10)""")
                        
df_premium_customer.show()
o/p:
=========
+-----------+-----+
|customer_id|count|
+-----------+-----+
|       5897|   16|
|      12431|   16|
|        569|   16|
|       6316|   16|
|      12284|   15|
|       5624|   15|
|       4320|   15|
|       5283|   15|
|        221|   15|
|       5654|   15|
+-----------+-----+

3. Distinct count of customers who placed atleast one order:
===================================================================
i. Using Df():
======================
df_distinct_customer = df.select(countDistinct(col("customer_id")).alias("distinct_customer"))
df_distinct_customer.show()

ii. Using sparksql:
========================
df_distinct_customer = spark.sql("""select count(distinct(customer_id)) as distinct_customer from count_1""")
df_distinct_customer.show()
o/p:
========
+-----------------+
|distinct_customer|
+-----------------+
|            12405|
+-----------------+
df.count()
o/p:
=======
68882

4. Which customers has the maximum number of CLOSED orders:
=============================================================
i. Using Df():
=====================
df_customer_max_filter = df.filter(col("order_status")=="CLOSED")\
                           .groupBy(col("customer_id"))\
                           .agg(count("*").alias("total_closed_orders"))\
                           .sort(col("total_closed_orders").desc())
df_customer_max_filter.show()
ii. Using spark sql:
===========================================
df_premium_customer = spark.sql("""select customer_id,count(*) as total_closed_orders from count_1
                                   where order_status == "CLOSED"
                                   group by customer_id
                                   order by total_closed_orders desc""")
df_premium_customer.show()                                   
o/p:
=========
+-----------+-------------------+
|customer_id|total_closed_orders|
+-----------+-------------------+
|       1833|                  6|
|       1363|                  5|
|       1687|                  5|
|       5493|                  5|
|       7948|                  4|
|       2768|                  4|
|      10263|                  4|
|       2236|                  4|
|       2403|                  4|
|       7879|                  4|
|       4573|                  4|
|       7850|                  4|
|      12431|                  4|
|       1521|                  4|
|      10111|                  4|
|        437|                  4|
|      10018|                  4|
|       5319|                  4|
|       2774|                  4|
|       3631|                  4|
+-----------+-------------------+

6. Find out hashtag count for each quote using Pyspark:
=======================================================
i. Using df():
===================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [
    ("Work hard in #silence, let #success make the noise.",),
    ("Be #yourself; everyone else is already taken.",),
    ("The only way to do #greatwork is to #love what you do.",),
    ("#Believe you can and you're #halfway there.",),
    ("The #future belongs to those who #believe in the #beauty of their #dreams.",)
]
df = spark.createDataFrame(data, ["quote"])
df.show(truncate=False)
0/p:
=====
+--------------------------------------------------------------------------+
|quote                                                                     |
+--------------------------------------------------------------------------+
|Work hard in #silence, let #success make the noise.                       |
|Be #yourself; everyone else is already taken.                             |
|The only way to do #greatwork is to #love what you do.                    |
|#Believe you can and you're #halfway there.                               |
|The #future belongs to those who #believe in the #beauty of their #dreams.|
+--------------------------------------------------------------------------+
df_split = df.withColumn("split_quotes",split(col("quote"),"#"))
df_split.show(truncate=False)
o/p:
====
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|quote                                                                     |split_quotes                                                                    |
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|Work hard in #silence, let #success make the noise.                       |[Work hard in , silence, let , success make the noise.]                         |
|Be #yourself; everyone else is already taken.                             |[Be , yourself; everyone else is already taken.]                                |
|The only way to do #greatwork is to #love what you do.                    |[The only way to do , greatwork is to , love what you do.]                      |
|#Believe you can and you're #halfway there.                               |[, Believe you can and you're , halfway there.]                                 |
|The #future belongs to those who #believe in the #beauty of their #dreams.|[The , future belongs to those who , believe in the , beauty of their , dreams.]|
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------+
df_hasttag_count = df_split.select(
    col("quote"),(size(col("split_quotes")) - 1).alias("hashtag_count")
)  
df_hasttag_count.show(truncate=False)
0/p:
=====
+--------------------------------------------------------------------------+-------------+
|quote                                                                     |hashtag_count|
+--------------------------------------------------------------------------+-------------+
|Work hard in #silence, let #success make the noise.                       |2            |
|Be #yourself; everyone else is already taken.                             |1            |
|The only way to do #greatwork is to #love what you do.                    |2            |
|#Believe you can and you're #halfway there.                               |2            |
|The #future belongs to those who #believe in the #beauty of their #dreams.|4            |
+--------------------------------------------------------------------------+-------------+
ii. Using spark sql:
======================
df.createOrReplaceTempView("df_split")
df_hasttag_count = spark.sql(
    "select quote, (size(split(quote, '#')) - 1) as hashtag_count from df_split"
)
df_hasttag_count.show(truncate=False)
o/p:
=====
+--------------------------------------------------------------------------+-------------+
|quote                                                                     |hashtag_count|
+--------------------------------------------------------------------------+-------------+
|Work hard in #silence, let #success make the noise.                       |2            |
|Be #yourself; everyone else is already taken.                             |1            |
|The only way to do #greatwork is to #love what you do.                    |2            |
|#Believe you can and you're #halfway there.                               |2            |
|The #future belongs to those who #believe in the #beauty of their #dreams.|4            |
+--------------------------------------------------------------------------+-------------+

7. Customer Purchase Analysis with Pyspark/spark sql:
======================================================
i. Calculate the total payroll cost for the company.
ii. Find the average salary for each department.
iii. Identify the highest paid employee and their department.
iv. Calculate the total number of employee in each department.

Solution:
================
from pyspark.sql import SparkSession
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
from pyspark.sql.functions import *
from pyspark.sql.types import *
data = [(1,"John Doe","Engineering",90000),\
        (2,"Jane Smith","Marketing",75000),\
        (3,"Michael Johnson","Engineering",105000),\
        (4,"Emily Davis","Marketing",80000),\
        (5,"Robert Brown","Engineering",95000),\
        (6,"Linda Wilson","HR",60000)]
schema = "employee_id int,employee_name string,department string,salary int"
df = spark.createDataFrame(data,schema)
df.show()
o/p:
====
+-----------+---------------+-----------+------+
|employee_id|  employee_name| department|salary|
+-----------+---------------+-----------+------+
|          1|       John Doe|Engineering| 90000|
|          2|     Jane Smith|  Marketing| 75000|
|          3|Michael Johnson|Engineering|105000|
|          4|    Emily Davis|  Marketing| 80000|
|          5|   Robert Brown|Engineering| 95000|
|          6|   Linda Wilson|         HR| 60000|
+-----------+---------------+-----------+------+

i. Calculate the total payroll cost for the company:
===================================================
a. Using df():
======================
df_total_payroll_cost = df.agg(sum(col("salary")).alias("total_payroll_cost"))
df_total_payroll_cost.show()
o/p:
===
+------------------+
|total_payroll_cost|
+------------------+
|            505000|
+------------------+
df_total_payroll_cost.first()[0]
df_total_payroll_cost.collect()[0][0]
o/p:
=======
505000

b. Using spark sql:
=====================
df.createOrReplaceTempView("df_final")
df_total_payroll_cost = spark.sql("select sum(salary) as total_payroll_cost from df_final")
df_total_payroll_cost.show()
o/p:
=========
+------------------+
|total_payroll_cost|
+------------------+
|            505000|
+------------------+
df_total_payroll_cost.collect()[0][0]
df_total_payroll_cost.first()[0]
o/p:
====
505000

ii. Find the average salary for each department:
===================================================
a. Using Df:
=================
df_avg_salary_dept = df.groupBy(col("department"))\
                       .agg(avg(col("salary"))\
                       .alias("avg_salary"))

b. Using spark sql:
======================
df_avg_salary_dept = spark.sql("""select department,avg(salary) as avg_salary
             from df_final
             group by department""")
             
df_avg_salary_dept.show()
o/p:
========
+-----------+-----------------+
| department|       avg_salary|
+-----------+-----------------+
|Engineering|96666.66666666667|
|         HR|          60000.0|
|  Marketing|          77500.0|
+-----------+-----------------+

iii. Identify the highest paid employee and their department:
==============================================================
a. Using Df:
==============
df_highest_paid_employee_with_department = df.select("*") \
                                             .orderBy(col("salary").desc())\
                                             .limit(1)
df_highest_paid_employee_with_department.show()
o/p:
======
+-----------+---------------+-----------+------+
|employee_id|  employee_name| department|salary|
+-----------+---------------+-----------+------+
|          3|Michael Johnson|Engineering|105000|
+-----------+---------------+-----------+------+
df_highest_paid_employee_with_department = df.select("*") \
                                             .orderBy(col("salary").desc())\
df_highest_paid_employee_with_department.first()
o/p:
=========
Row(employee_id=3, employee_name='Michael Johnson', department='Engineering', salary=105000)

b. Using spark sql:
======================
df_highest_paid_employee_with_department = spark.sql("""select * from df_final
             order by salary desc
             limit(1)""")
df_highest_paid_employee_with_department.show()
o/p:
===
+-----------+---------------+-----------+------+
|employee_id|  employee_name| department|salary|
+-----------+---------------+-----------+------+
|          3|Michael Johnson|Engineering|105000|
+-----------+---------------+-----------+------+
df_highest_paid_employee_with_department = spark.sql("""select * from df_final
             order by salary desc
             """)
df_highest_paid_employee_with_department.first()
o/p:
====
Row(employee_id=3, employee_name='Michael Johnson', department='Engineering', salary=105000)

iv.Calculate the total number of employee in each department:
==============================================================
a. Using Df:
==============
df_total_count_employee_dept = df.groupBy(col("department"))\
                                 .agg(count(col("employee_id"))\
                                 .alias("total_employee"))
                                 
b. Using spark sql:
======================
df_total_count_employee_dept = spark.sql("""select department,count(employee_id) as total_employee from df_final
             group by department""")

df_total_count_employee_dept.show()
o/p:
========
+-----------+--------------+
| department|total_employee|
+-----------+--------------+
|Engineering|             3|
|         HR|             1|
|  Marketing|             2|
+-----------+--------------+

8. 

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [("Maheer","HR",2000),\
        ("Wafa","IT",3000),\
        ("Asi","HR",1500),\
        ("Annu","Payroll",3500),\
        ("Shakti","IT",3000),\
        ("Pradeep","IT",4000),\
        ("Karnthi","Payroll",2000),\
        ("Himanshu","IT",2000),\
        ("Bhargaya","HR",2000),\
        ("Martin","IT",2500)]
schema = StructType([\
         StructField("Name",StringType(),True),\
         StructField("Department",StringType(),True),\
         StructField("Salary",IntegerType(),True)])
df = spark.createDataFrame(data,schema)
df.show()
o/p:
=========
+--------+----------+------+
|    Name|Department|Salary|
+--------+----------+------+
|  Maheer|        HR|  2000|
|    Wafa|        IT|  3000|
|     Asi|        HR|  1500|
|    Annu|   Payroll|  3500|
|  Shakti|        IT|  3000|
| Pradeep|        IT|  4000|
| Karnthi|   Payroll|  2000|
|Himanshu|        IT|  2000|
|Bhargaya|        HR|  2000|
|  Martin|        IT|  2500|
+--------+----------+------+
winspec = Window.partitionBy(col("Department"))\
                .orderBy(col("Salary").desc())
                
df_final = df.withColumn("rn",row_number().over(winspec))\
             .withColumn("rnk",rank().over(winspec))\
             .withColumn("dnsk",dense_rank().over(winspec))

df_final.show()
o/p:
======
+--------+----------+------+---+---+----+
|    Name|Department|Salary| rn|rnk|dnsk|
+--------+----------+------+---+---+----+
|  Maheer|        HR|  2000|  1|  1|   1|
|Bhargaya|        HR|  2000|  2|  1|   1|
|     Asi|        HR|  1500|  3|  3|   2|
|    Annu|   Payroll|  3500|  1|  1|   1|
| Karnthi|   Payroll|  2000|  2|  2|   2|
| Pradeep|        IT|  4000|  1|  1|   1|
|    Wafa|        IT|  3000|  2|  2|   2|
|  Shakti|        IT|  3000|  3|  2|   2|
|  Martin|        IT|  2500|  4|  4|   3|
|Himanshu|        IT|  2000|  5|  5|   4|
+--------+----------+------+---+---+----+
df.createOrReplaceTempView("df_final_1")

df_final = spark.sql("""
with cte as (
    select *,
           row_number() over(partition by Department order by Salary desc) rn,
           rank() over(partition by Department order by Salary desc) rnk,
           dense_rank() over(partition by Department order by Salary desc) dnsk
    from df_final_1
)
select * from cte
""")
df_final.show()
o/p:
========
+--------+----------+------+---+---+----+
|    Name|Department|Salary| rn|rnk|dnsk|
+--------+----------+------+---+---+----+
|Bhargaya|        HR|  2000|  1|  1|   1|
|  Maheer|        HR|  2000|  2|  1|   1|
|     Asi|        HR|  1500|  3|  3|   2|
|    Annu|   Payroll|  3500|  1|  1|   1|
| Karnthi|   Payroll|  2000|  2|  2|   2|
| Pradeep|        IT|  4000|  1|  1|   1|
|    Wafa|        IT|  3000|  2|  2|   2|
|  Shakti|        IT|  3000|  3|  2|   2|
|  Martin|        IT|  2500|  4|  4|   3|
|Himanshu|        IT|  2000|  5|  5|   4|
+--------+----------+------+---+---+----+

winspec = Window.partitionBy(col("Department"))\
                .orderBy(col("Salary").asc())


df_lowest_salary_hr_dept = (
    df.withColumn("dnsk", dense_rank().over(winspec))
      .filter( (col("Department") == "HR") & (col("dnsk") == 1) )\
      .drop(col("dnsk"))
)

df_lowest_salary_hr_dept.show()
o/p:
=======
+----+----------+------+
|Name|Department|Salary|
+----+----------+------+
| Asi|        HR|  1500|
+----+----------+------+

df_lowest_salary_hr_dept = spark.sql("""with cte as(select *,dense_rank() over(partition by Department order by Salary asc) as dnsk
             from df_final_1)
             select Name,Department,Salary from cte
             where Department="HR" AND dnsk=1""")
             
df_lowest_salary_hr_dept.show()
o/p:
=====
+----+----------+------+
|Name|Department|Salary|
+----+----------+------+
| Asi|        HR|  1500|
+----+----------+------+

winspec = Window.partitionBy(col("Department"))\
                .orderBy(col("Salary").desc())
                
df_highest_salary_hr_dept = (
    df.withColumn("dnsk", dense_rank().over(winspec))
      .filter( (col("Department") == "HR") & (col("dnsk") == 1) )\
      .drop(col("dnsk"))
)
df_highest_salary_hr_dept.show()
o/p:
=======
+--------+----------+------+
|    Name|Department|Salary|
+--------+----------+------+
|  Maheer|        HR|  2000|
|Bhargaya|        HR|  2000|
+--------+----------+------+


df_highest_salary_hr_dept = spark.sql("""with cte as(select *,dense_rank() over(partition by Department order by Salary desc) as dnsk
             from df_final_1)
             select Name,Department,Salary from cte
             where Department="HR" AND dnsk=1""")

df_highest_salary_hr_dept.show()
o/p:
=======
+--------+----------+------+
|    Name|Department|Salary|
+--------+----------+------+
|  Maheer|        HR|  2000|
|Bhargaya|        HR|  2000|
+--------+----------+------+

9. Pyspark Coding Challenge:
==================================
i. I want to remove all the rows which are pending_payment status:
ii. To count each customers who has placed how many orders:
iii. I want to take all the customer_id which are less than 500:

Solution:
=============
i. I want to remove all the rows which are pending_payment status:
===================================================================
a. Using rdd():
=======================

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
orders_base = spark.sparkContext.textFile("/public/trendytech/orders/orders_1gb.csv")
schema1 = "order_id int,order_date timestamp,customer_id int,order_status string"
df =  spark.read.format("csv")\
           .option("header",True)\
           .schema(schema1)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/orders/orders_1gb.csv")\
           .load()
df.show()
o/p:
========
+--------+-------------------+-----------+---------------+
|order_id|         order_date|customer_id|   order_status|
+--------+-------------------+-----------+---------------+
|       2|2013-07-25 00:00:00|        256|PENDING_PAYMENT|
|       3|2013-07-25 00:00:00|      12111|       COMPLETE|
|       4|2013-07-25 00:00:00|       8827|         CLOSED|
|       5|2013-07-25 00:00:00|      11318|       COMPLETE|
|       6|2013-07-25 00:00:00|       7130|       COMPLETE|
|       7|2013-07-25 00:00:00|       4530|       COMPLETE|
|       8|2013-07-25 00:00:00|       2911|     PROCESSING|
|       9|2013-07-25 00:00:00|       5657|PENDING_PAYMENT|
|      10|2013-07-25 00:00:00|       5648|PENDING_PAYMENT|
|      11|2013-07-25 00:00:00|        918| PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|         CLOSED|
|      13|2013-07-25 00:00:00|       9149|PENDING_PAYMENT|
|      14|2013-07-25 00:00:00|       9842|     PROCESSING|
|      15|2013-07-25 00:00:00|       2568|       COMPLETE|
|      16|2013-07-25 00:00:00|       7276|PENDING_PAYMENT|
|      17|2013-07-25 00:00:00|       2667|       COMPLETE|
|      18|2013-07-25 00:00:00|       1205|         CLOSED|
|      19|2013-07-25 00:00:00|       9488|PENDING_PAYMENT|
|      20|2013-07-25 00:00:00|       9198|     PROCESSING|
|      21|2013-07-25 00:00:00|       2711|        PENDING|
+--------+-------------------+-----------+---------------+
df.printSchema()
o/p:
========
root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
 
a. Using rdd:
=================    
orders_filtered = orders_base.filter(lambda x:x.split(",")[3]!="PENDING_PAYMENT")
orders_filtered.take(10)
o/p:
======
['1,2013-07-25 00:00:00.0,11599,CLOSED',
 '3,2013-07-25 00:00:00.0,12111,COMPLETE',
 '4,2013-07-25 00:00:00.0,8827,CLOSED',
 '5,2013-07-25 00:00:00.0,11318,COMPLETE',
 '6,2013-07-25 00:00:00.0,7130,COMPLETE',
 '7,2013-07-25 00:00:00.0,4530,COMPLETE',
 '8,2013-07-25 00:00:00.0,2911,PROCESSING',
 '11,2013-07-25 00:00:00.0,918,PAYMENT_REVIEW',
 '12,2013-07-25 00:00:00.0,1837,CLOSED',
 '14,2013-07-25 00:00:00.0,9842,PROCESSING'] 
 
 b. Using Df:
================
df_filtered = df.filter(col("order_status")!="PENDING_PAYMENT")
df_filtered.show()
o/p:
=======
+--------+-------------------+-----------+--------------+
|order_id|         order_date|customer_id|  order_status|
+--------+-------------------+-----------+--------------+
|       3|2013-07-25 00:00:00|      12111|      COMPLETE|
|       4|2013-07-25 00:00:00|       8827|        CLOSED|
|       5|2013-07-25 00:00:00|      11318|      COMPLETE|
|       6|2013-07-25 00:00:00|       7130|      COMPLETE|
|       7|2013-07-25 00:00:00|       4530|      COMPLETE|
|       8|2013-07-25 00:00:00|       2911|    PROCESSING|
|      11|2013-07-25 00:00:00|        918|PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|        CLOSED|
|      14|2013-07-25 00:00:00|       9842|    PROCESSING|
|      15|2013-07-25 00:00:00|       2568|      COMPLETE|
|      17|2013-07-25 00:00:00|       2667|      COMPLETE|
|      18|2013-07-25 00:00:00|       1205|        CLOSED|
|      20|2013-07-25 00:00:00|       9198|    PROCESSING|
|      21|2013-07-25 00:00:00|       2711|       PENDING|
|      22|2013-07-25 00:00:00|        333|      COMPLETE|
|      24|2013-07-25 00:00:00|      11441|        CLOSED|
|      25|2013-07-25 00:00:00|       9503|        CLOSED|
|      26|2013-07-25 00:00:00|       7562|      COMPLETE|
|      28|2013-07-25 00:00:00|        656|      COMPLETE|
|      29|2013-07-25 00:00:00|        196|    PROCESSING|
+--------+-------------------+-----------+--------------+

c. Using sparksql:
======================
df.createOrReplaceTempView("df_practice")
df_filtered = spark.sql("""
    SELECT * 
    FROM df_practice 
    WHERE order_status != 'PENDING_PAYMENT'
""")
df_filtered.show()
o/p:
======
+--------+-------------------+-----------+--------------+
|order_id|         order_date|customer_id|  order_status|
+--------+-------------------+-----------+--------------+
|       3|2013-07-25 00:00:00|      12111|      COMPLETE|
|       4|2013-07-25 00:00:00|       8827|        CLOSED|
|       5|2013-07-25 00:00:00|      11318|      COMPLETE|
|       6|2013-07-25 00:00:00|       7130|      COMPLETE|
|       7|2013-07-25 00:00:00|       4530|      COMPLETE|
|       8|2013-07-25 00:00:00|       2911|    PROCESSING|
|      11|2013-07-25 00:00:00|        918|PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|        CLOSED|
|      14|2013-07-25 00:00:00|       9842|    PROCESSING|
|      15|2013-07-25 00:00:00|       2568|      COMPLETE|
|      17|2013-07-25 00:00:00|       2667|      COMPLETE|
|      18|2013-07-25 00:00:00|       1205|        CLOSED|
|      20|2013-07-25 00:00:00|       9198|    PROCESSING|
|      21|2013-07-25 00:00:00|       2711|       PENDING|
|      22|2013-07-25 00:00:00|        333|      COMPLETE|
|      24|2013-07-25 00:00:00|      11441|        CLOSED|
|      25|2013-07-25 00:00:00|       9503|        CLOSED|
|      26|2013-07-25 00:00:00|       7562|      COMPLETE|
|      28|2013-07-25 00:00:00|        656|      COMPLETE|
|      29|2013-07-25 00:00:00|        196|    PROCESSING|
+--------+-------------------+-----------+--------------+
 
 ii. To count each customers who has placed how many orders:
==================================================================
a. Using rdd:
==================
orders_mapped = orders_filtered.map(lambda x:(x.split(",")[2],1))
orders_reduced = orders_mapped.reduceByKey(lambda x,y:x+y)
orders_reduced.take(20)
o/p:
=======
[('8171', 3375),
 ('6900', 1875),
 ('11436', 1125),
 ('6138', 1125),
 ('4662', 750),
 ('10948', 2625),
 ('3522', 1500),
 ('10720', 3000),
 ('7995', 1125),
 ('2721', 2250),
 ('11894', 1500),
 ('3754', 2250),
 ('11238', 1500),
 ('6838', 2250),
 ('6807', 750),
 ('9230', 1125),
 ('11569', 1500),
 ('281', 1125),
 ('11422', 3375),
 ('4847', 2250)]
 
 b. Using Df:
================
df_order_count = df.groupBy(col("customer_id"))\
                   .agg(count(col("order_id"))\
                   .alias("total_count"))
df_order_count.show()
o/p:
=======
+-----------+-----------+
|customer_id|total_count|
+-----------+-----------+
|       6654|       2250|
|       5803|       4500|
|       1591|       2250|
|       2866|       1125|
|      11317|       2625|
|       3997|       1875|
|       7982|       2250|
|       5518|       3000|
|       6357|       2625|
|       7554|       1875|
|      11748|       2250|
|       7754|       2250|
|       7880|       1875|
|       8086|       2250|
|       3918|       2625|
|       6336|       2625|
|        833|       2250|
|       1088|       1500|
|       6397|       3000|
|      11858|       2625|
+-----------+-----------+

c. Using sparksql:
======================
df.createOrReplaceTempView("df_practice")
df_order_count = spark.sql("""select customer_id,count(order_id) as total_count
                              from df_practice
                              group by customer_id""")
df_order_count.show()
o/p:
======
+-----------+-----------+
|customer_id|total_count|
+-----------+-----------+
|        833|       2250|
|       1088|       1500|
|       6397|       3000|
|      11858|       2625|
|      11033|        750|
|       8389|       1500|
|      12046|       1500|
|       4900|       2250|
|       6357|       2625|
|      11458|       2625|
|       3175|       3375|
|       1959|       1500|
|      11748|       2250|
|       9900|        750|
|       9376|       2625|
|       7554|       1875|
|       7253|       2250|
|       4935|       2625|
|       8592|       2250|
|       5803|       4500|
+-----------+-----------+


b. Using Df:
================
df_filtered = df.filter(col("order_status")!="PENDING_PAYMENT")
df_filtered.show()
o/p:
=======
+--------+-------------------+-----------+--------------+
|order_id|         order_date|customer_id|  order_status|
+--------+-------------------+-----------+--------------+
|       3|2013-07-25 00:00:00|      12111|      COMPLETE|
|       4|2013-07-25 00:00:00|       8827|        CLOSED|
|       5|2013-07-25 00:00:00|      11318|      COMPLETE|
|       6|2013-07-25 00:00:00|       7130|      COMPLETE|
|       7|2013-07-25 00:00:00|       4530|      COMPLETE|
|       8|2013-07-25 00:00:00|       2911|    PROCESSING|
|      11|2013-07-25 00:00:00|        918|PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|        CLOSED|
|      14|2013-07-25 00:00:00|       9842|    PROCESSING|
|      15|2013-07-25 00:00:00|       2568|      COMPLETE|
|      17|2013-07-25 00:00:00|       2667|      COMPLETE|
|      18|2013-07-25 00:00:00|       1205|        CLOSED|
|      20|2013-07-25 00:00:00|       9198|    PROCESSING|
|      21|2013-07-25 00:00:00|       2711|       PENDING|
|      22|2013-07-25 00:00:00|        333|      COMPLETE|
|      24|2013-07-25 00:00:00|      11441|        CLOSED|
|      25|2013-07-25 00:00:00|       9503|        CLOSED|
|      26|2013-07-25 00:00:00|       7562|      COMPLETE|
|      28|2013-07-25 00:00:00|        656|      COMPLETE|
|      29|2013-07-25 00:00:00|        196|    PROCESSING|
+--------+-------------------+-----------+--------------+

c. Using sparksql:
======================
df.createOrReplaceTempView("df_practice")
df_filtered = spark.sql("""
    SELECT * 
    FROM df_practice 
    WHERE order_status != 'PENDING_PAYMENT'
""")
df_filtered.show()
o/p:
======
+--------+-------------------+-----------+--------------+
|order_id|         order_date|customer_id|  order_status|
+--------+-------------------+-----------+--------------+
|       3|2013-07-25 00:00:00|      12111|      COMPLETE|
|       4|2013-07-25 00:00:00|       8827|        CLOSED|
|       5|2013-07-25 00:00:00|      11318|      COMPLETE|
|       6|2013-07-25 00:00:00|       7130|      COMPLETE|
|       7|2013-07-25 00:00:00|       4530|      COMPLETE|
|       8|2013-07-25 00:00:00|       2911|    PROCESSING|
|      11|2013-07-25 00:00:00|        918|PAYMENT_REVIEW|
|      12|2013-07-25 00:00:00|       1837|        CLOSED|
|      14|2013-07-25 00:00:00|       9842|    PROCESSING|
|      15|2013-07-25 00:00:00|       2568|      COMPLETE|
|      17|2013-07-25 00:00:00|       2667|      COMPLETE|
|      18|2013-07-25 00:00:00|       1205|        CLOSED|
|      20|2013-07-25 00:00:00|       9198|    PROCESSING|
|      21|2013-07-25 00:00:00|       2711|       PENDING|
|      22|2013-07-25 00:00:00|        333|      COMPLETE|
|      24|2013-07-25 00:00:00|      11441|        CLOSED|
|      25|2013-07-25 00:00:00|       9503|        CLOSED|
|      26|2013-07-25 00:00:00|       7562|      COMPLETE|
|      28|2013-07-25 00:00:00|        656|      COMPLETE|
|      29|2013-07-25 00:00:00|        196|    PROCESSING|
+--------+-------------------+-----------+--------------+

 
 
 
iii. I want to take all the customer_id which are less than 500:
=====================================================================
a. Using rdd:
=================
result = orders_reduced.filter(lambda x:int(x[0])<501)
result.collect()
o/p:
========
  [('118', 1500),
 ('285', 2625),
 ('2', 1125),
 ('53', 1125),
 ('309', 1125),
 ('424', 2625),
 ('40', 1875),
 ('256', 2625),
 ('151', 1500),
 ('275', 1500),
 ('184', 1875),
 ('238', 2250),
 ('352', 2250),
 ('358', 1125),
 ('212', 1500),
 ('199', 1500),
 ('30', 375),
 ('389', 1125),
 ('97', 1875),
 ('91', 1875),
 ('289', 2250),
 ('99', 2250),
 ('171', 750),
 ('486', 2625),
 ('260', 1500),
 ('202', 2250),
 ('326', 2625),
 ('218', 1125),
 ('348', 1500),
 ('328', 2250),
 ('228', 1875),
 ('281', 1125),
 ('54', 1875),
 ('22', 1875),
 ('446', 1500),
 ('315', 1125)]  
 
 b. Using df:
===================
df_result = df.filter(col("customer_id")<=500)
df_result.show()
o/p:
========
+--------+-------------------+-----------+---------------+
|order_id|         order_date|customer_id|   order_status|
+--------+-------------------+-----------+---------------+
|       2|2013-07-25 00:00:00|        256|PENDING_PAYMENT|
|      22|2013-07-25 00:00:00|        333|       COMPLETE|
|      29|2013-07-25 00:00:00|        196|     PROCESSING|
|     106|2013-07-26 00:00:00|        395|     PROCESSING|
|     115|2013-07-26 00:00:00|        104|     PROCESSING|
|     117|2013-07-26 00:00:00|         58|SUSPECTED_FRAUD|
|     120|2013-07-26 00:00:00|        356|PENDING_PAYMENT|
|     132|2013-07-26 00:00:00|        289|        PENDING|
|     145|2013-07-26 00:00:00|        494|        ON_HOLD|
|     147|2013-07-26 00:00:00|        275|PENDING_PAYMENT|
|     150|2013-07-26 00:00:00|        236|     PROCESSING|
|     175|2013-07-26 00:00:00|        384|       COMPLETE|
|     184|2013-07-26 00:00:00|        210|       COMPLETE|
|     191|2013-07-26 00:00:00|         16|         CLOSED|
|     240|2013-07-26 00:00:00|         32|        PENDING|
|     243|2013-07-26 00:00:00|         32|        ON_HOLD|
|     247|2013-07-26 00:00:00|        173|       COMPLETE|
|     253|2013-07-26 00:00:00|         45|       COMPLETE|
|     264|2013-07-26 00:00:00|        230|       COMPLETE|
|     265|2013-07-26 00:00:00|        488|PENDING_PAYMENT|
+--------+-------------------+-----------+---------------+

c. Using spark sql:
=========================
df_result = spark.sql("select * from df_practice where customer_id<=500")
df_result.show()
o/p:
======
+--------+-------------------+-----------+---------------+
|order_id|         order_date|customer_id|   order_status|
+--------+-------------------+-----------+---------------+
|       2|2013-07-25 00:00:00|        256|PENDING_PAYMENT|
|      22|2013-07-25 00:00:00|        333|       COMPLETE|
|      29|2013-07-25 00:00:00|        196|     PROCESSING|
|     106|2013-07-26 00:00:00|        395|     PROCESSING|
|     115|2013-07-26 00:00:00|        104|     PROCESSING|
|     117|2013-07-26 00:00:00|         58|SUSPECTED_FRAUD|
|     120|2013-07-26 00:00:00|        356|PENDING_PAYMENT|
|     132|2013-07-26 00:00:00|        289|        PENDING|
|     145|2013-07-26 00:00:00|        494|        ON_HOLD|
|     147|2013-07-26 00:00:00|        275|PENDING_PAYMENT|
|     150|2013-07-26 00:00:00|        236|     PROCESSING|
|     175|2013-07-26 00:00:00|        384|       COMPLETE|
|     184|2013-07-26 00:00:00|        210|       COMPLETE|
|     191|2013-07-26 00:00:00|         16|         CLOSED|
|     240|2013-07-26 00:00:00|         32|        PENDING|
|     243|2013-07-26 00:00:00|         32|        ON_HOLD|
|     247|2013-07-26 00:00:00|        173|       COMPLETE|
|     253|2013-07-26 00:00:00|         45|       COMPLETE|
|     264|2013-07-26 00:00:00|        230|       COMPLETE|
|     265|2013-07-26 00:00:00|        488|PENDING_PAYMENT|
+--------+-------------------+-----------+---------------+

10. Pyspark Coding Challenge:
==================================
i. Calculate the total revenue generated from all orders.
ii. Find the avg order amount.
iii. Identify the highest total order amount and its corresponding customer.
iv. Calculate the total number or orders for each customer.

Solution:
===============
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
orders_schema = "order_id int,customer_id string,order_date timestamp,total_amount int"
from datetime import datetime

data = [
(1,"C101",datetime(2023,7,1),150),
(2,"C102",datetime(2023,7,2),200),
(3,"C101",datetime(2023,7,2),100),
(4,"C103",datetime(2023,7,3),300),
(5,"C102",datetime(2023,7,4),250),
(6,"C101",datetime(2023,7,5),120)
]
df_orders = spark.createDataFrame(data,orders_schema)
df_orders.show()
o/p:
======
+--------+-----------+-------------------+------------+
|order_id|customer_id|         order_date|total_amount|
+--------+-----------+-------------------+------------+
|       1|       C101|2023-07-01 00:00:00|         150|
|       2|       C102|2023-07-02 00:00:00|         200|
|       3|       C101|2023-07-02 00:00:00|         100|
|       4|       C103|2023-07-03 00:00:00|         300|
|       5|       C102|2023-07-04 00:00:00|         250|
|       6|       C101|2023-07-05 00:00:00|         120|
+--------+-----------+-------------------+------------+


i. Calculate the total revenue generated from all orders.
=========================================================
a. Using Pyspark:
==================
df_total_reveneue = df_orders.agg(sum(col("total_amount")).alias("total_revenue"))
df_total_reveneue.show(truncate=False) 
o/p:
=====
+-------------+
|total_revenue|
+-------------+
|1120         |
+-------------+

b. Using sparksql:
==================
df_orders.createOrReplaceTempView("df_final")
df_total_reveneue = spark.sql("select sum(total_amount) as total_revenue from df_final")
df_total_reveneue.show(truncate=False)
o/p:
====
+-------------+
|total_revenue|
+-------------+
|1120         |
+-------------+

ii. Find the avg order amount.
==============================
a. Using Pyspark:
=================
df_avg_amount = df_orders.agg(avg(col("total_Amount")).alias("avg_amount"))
df_avg_amount.show()
o/p:
=====
+------------------+
|        avg_amount|
+------------------+
|186.66666666666666|
+------------------+

b. using sparksql:
==================
df_avg_amount = spark.sql("select avg(total_amount) as avg_amount from df_final")
df_avg_amount.show()
o/p:
=====
+------------------+
|        avg_amount|
+------------------+
|186.66666666666666|
+------------------+

iii. Identify the highest total order amount and its corresponding customer.
============================================================================
a. Using Pyspark:
====================
df_highest_total_order_amount = df_orders.sort(col("total_amount").desc())\
                                         .limit(1)\
                                         .select(col("customer_id"),col("total_amount"))
df_highest_total_order_amount.show()
o/p:
======
+-----------+------------+
|customer_id|total_amount|
+-----------+------------+
|       C103|         300|
+-----------+------------+

b. using sparksql:
====================
df_highest_total_order_amount = spark.sql("""select customer_id,total_amount from df_final
                                             order by total_amount desc
                                             limit 1""")
df_highest_total_order_amount.show()
o/p:
=======
+-----------+------------+
|customer_id|total_amount|
+-----------+------------+
|       C103|         300|
+-----------+------------+

iv. Calculate the total number or orders for each customer.
============================================================
a. Using Pyspark:
====================
df_total_orders_customers = df_orders.groupBy(col("customer_id"))\
                              .agg(count(col("order_id"))\
                              .alias("total_orders"))
df_total_orders_customers.show()
o/p:
=====
+-----------+------------+
|customer_id|total_orders|
+-----------+------------+
|       C102|           2|
|       C103|           1|
|       C101|           3|
+-----------+------------+

b. Using sparksql:
===================
df_total_orders_customers = spark.sql("""select customer_id,count(order_id) as total_orders
                                         from df_final
                                         group by customer_id""")
df_total_orders_customers.show()
o/p:
=======
+-----------+------------+
|customer_id|total_orders|
+-----------+------------+
|       C102|           2|
|       C103|           1|
|       C101|           3|
+-----------+------------+


11. Pyspark coding challenge:
===============================
i/p:
=====
+----+-----+-------------------+
|item|sales|              date1|
+----+-----+-------------------+
| 123|  100|2023-01-28 00:00:00|
| 123|   50|2023-01-29 00:00:00|
| 456|   50|2023-01-27 00:00:00|
+----+-----+-------------------+
o/p:
=====
+----+---------+------------------------------------------+
|item|sales_arr|date_arr                                  |
+----+---------+------------------------------------------+
|456 |[50]     |[2023-01-27 00:00:00]                     |
|123 |[50, 100]|[2023-01-29 00:00:00, 2023-01-28 00:00:00]|
+----+---------+------------------------------------------+

Solution:
===========
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
schema1 = "item int, sales int, date1 timestamp"
from datetime import datetime

data = [
    (123,100,datetime(2023,1,28)),
    (123,50,datetime(2023,1,29)),
    (456,50,datetime(2023,1,27))
]

df = spark.createDataFrame(data, schema1)
df.show()
o/p:
=========
+----+-----+-------------------+
|item|sales|              date1|
+----+-----+-------------------+
| 123|  100|2023-01-28 00:00:00|
| 123|   50|2023-01-29 00:00:00|
| 456|   50|2023-01-27 00:00:00|
+----+-----+-------------------+
df.printSchema()
o/p:
=======
root
 |-- item: integer (nullable = true)
 |-- sales: integer (nullable = true)
 |-- date1: timestamp (nullable = true)


i. Using Pyspark:
=====================
df_final = df.groupBy(col("item")) \
    .agg(
        collect_list(col("sales")).alias("sales_arr"),
        collect_list(col("date1")).alias("date_arr"),
        count("*").alias("count")
    )
df_final.show(truncate = False)
o/p:
======
+----+---------+------------------------------------------+-----+
|item|sales_arr|date_arr                                  |count|
+----+---------+------------------------------------------+-----+
|456 |[50]     |[2023-01-27 00:00:00]                     |1    |
|123 |[50, 100]|[2023-01-29 00:00:00, 2023-01-28 00:00:00]|2    |
+----+---------+------------------------------------------+-----+

ii. Using sparksql:
=====================
df.createOrReplaceTempView("list_agg_practice")
df_final = spark.sql("""select item,collect_list(sales) as sales_arr,collect_list(date1) as date_arr,count(*)
                        from list_agg_practice
                        group by item""")
df_final.show(truncate = False)
o/p:
=====
+----+---------+------------------------------------------+--------+
|item|sales_arr|date_arr                                  |count(1)|
+----+---------+------------------------------------------+--------+
|456 |[50]     |[2023-01-27 00:00:00]                     |1       |
|123 |[100, 50]|[2023-01-28 00:00:00, 2023-01-29 00:00:00]|2       |
+----+---------+------------------------------------------+--------+

12. Write a Pyspark/spark sql code to select every 3rd (nth) row in the dataset:
====================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
schema = StructType([
 StructField("emp_id", IntegerType(), True),
 StructField("name", StringType(), True),
 StructField("salary", IntegerType(), True)
])
data = [
 (1001, "John Doe", 50000),
 (2001, "Jane Smith", 60000),
 (1003, "Michael Johnson", 75000),
 (4000, "Emily Davis", 55000),
 (1005, "Robert Brown", 70000),
 (6000, "Emma Wilson", 80000),
 (1700, "James Taylor", 65000),
 (8000, "Olivia Martinez", 72000),
 (2900, "William Anderson", 68000),
 (3310, "Sophia Garcia", 67000)
]
df = spark.createDataFrame(data, schema)
df.show()
o/p:
==========
+------+----------------+------+
|emp_id|            name|salary|
+------+----------------+------+
|  1001|        John Doe| 50000|
|  2001|      Jane Smith| 60000|
|  1003| Michael Johnson| 75000|
|  4000|     Emily Davis| 55000|
|  1005|    Robert Brown| 70000|
|  6000|     Emma Wilson| 80000|
|  1700|    James Taylor| 65000|
|  8000| Olivia Martinez| 72000|
|  2900|William Anderson| 68000|
|  3310|   Sophia Garcia| 67000|
+------+----------------+------+
i. Approach 1st:
===================
a. Using df:
=================
winspec = Window.orderBy(lit("1"))
df_final = df.withColumn("rn",row_number().over(winspec))\
             .filter(col("rn")%3==0)\
             .drop(col("rn"))
df_final.show(truncate=False)
o/p:
========
+------+----------------+------+
|emp_id|name            |salary|
+------+----------------+------+
|1003  |Michael Johnson |75000 |
|6000  |Emma Wilson     |80000 |
|2900  |William Anderson|68000 |
+------+----------------+------+
b. Using spark sql:
=========================
df.createOrReplaceTempView("df_third_row")
df_final = spark.sql("""WITH CTE as (select *,row_number() over(order by 1) as rn
                        from df_third_row
                        )
                        select emp_id,name,salary from CTE where rn%3==0 """)
df_final.show(truncate=False)
o/p:
========
+------+----------------+------+
|emp_id|name            |salary|
+------+----------------+------+
|1003  |Michael Johnson |75000 |
|6000  |Emma Wilson     |80000 |
|2900  |William Anderson|68000 |
+------+----------------+------+
ii. Approach 2nd:
===================
a. Using df:
=================
winspec1 = Window.orderBy(monotonically_increasing_id())
df_final1 = df.withColumn("rn",row_number().over(winspec1))\
             .filter(col("rn")%3==0)\
             .drop(col("rn"))
df_final1.show(truncate=False)
o/p:
========
+------+----------------+------+
|emp_id|name            |salary|
+------+----------------+------+
|1003  |Michael Johnson |75000 |
|6000  |Emma Wilson     |80000 |
|2900  |William Anderson|68000 |
+------+----------------+------+
b. Using spark sql:
=========================
df.createOrReplaceTempView("df_third_row")
df_final1 = spark.sql("""WITH CTE as (select *,row_number() over(order by monotonically_increasing_id()) as rn
                        from df_third_row
                        )
                        select emp_id,name,salary from CTE where rn%3==0 """)
df_final1.show(truncate=False)
o/p:
========
+------+----------------+------+
|emp_id|name            |salary|
+------+----------------+------+
|1003  |Michael Johnson |75000 |
|6000  |Emma Wilson     |80000 |
|2900  |William Anderson|68000 |
+------+----------------+------+

13. Write a Pyspark/spark sql code to Find the number of output rows for different types of joins:
========================================================================================================
i. INNER JOIN.
ii. LEFT JOIN.
iii. RIGHT JOIN.
iv. FULL OUTER JOIN.
v. CROSS JOIN.
vi. LEFT ANTI JOIN.
vii. LEFT SEMI JOIN.
Solution:
===================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data1 = [(1,),\
         (1,),\
         (1,),\
         (None,),\
         (0,)]
schema1 = "Id1 int"
df1 = spark.createDataFrame(data=data1,schema=schema1)
df1.show(truncate=False)
df1.printSchema()
o/p:
========
+----+
|Id1 |
+----+
|1   |
|1   |
|1   |
|null|
|0   |
+----+

root
 |-- Id1: integer (nullable = true)
data2 = [(1,),\
         (1,),\
         (None,),\
         (None,)
         ]
schema2 = "Id2 int"
df2 = spark.createDataFrame(data=data2,schema=schema2)
df2.show(truncate=False)
df2.printSchema()
o/p:
====
+----+
|Id2 |
+----+
|1   |
|1   |
|null|
|null|
+----+

root
 |-- Id2: integer (nullable = true)
i. INNER JOIN:
===================
a. Using df():
===================
df_inner = df1.join(df2,df1.Id1==df2.Id2,"inner")
df_inner.show(truncate=False)
print("Total count of records in inner join is:",df_inner.count())

b. Using sparksql:
========================
df1.createOrReplaceTempView("df_final1")
df2.createOrReplaceTempView("df_final2")
df_inner = spark.sql("""select Id1,Id2
                        from df_final1 
                        inner join df_final2
                        on df_final1.Id1 = df_final2.Id2""")
df_count_inner = spark.sql("""select count(*) as total_record_count from (select Id1,Id2
                        from df_final1 
                        inner join df_final2
                        on df_final1.Id1 = df_final2.Id2) temp""")
df_inner.show(truncate=False)
print("Total count of records in inner join is: ",df_count_inner.collect()[0][0])

o/p:
=========
+---+---+
|Id1|Id2|
+---+---+
|1  |1  |
|1  |1  |
|1  |1  |
|1  |1  |
|1  |1  |
|1  |1  |
+---+---+

Total count of records in inner join is:  6

ii.LEFT JOIN.:
===================
a. Using df():
===================
df_left = df1.join(df2,df1.Id1==df2.Id2,"left")
df_left.show(truncate=False)
print("Total count of records in inner join is:",df_left.count())

b. Using sparksql:
========================
df1.createOrReplaceTempView("df_final1")
df2.createOrReplaceTempView("df_final2")
df_left = spark.sql("""select Id1,Id2
                        from df_final1 
                        left join df_final2
                        on df_final1.Id1 = df_final2.Id2""")
df_count_left = spark.sql("""select count(*) as total_record_count from (select Id1,Id2
                        from df_final1 
                        left join df_final2
                        on df_final1.Id1 = df_final2.Id2) temp""")
df_left.show(truncate=False)
print("Total count of records in left join is: ",df_count_left.collect()[0][0])

o/p:
=========
+----+----+
|Id1 |Id2 |
+----+----+
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|0   |null|
+----+----+

Total count of records in left join is:  8

iii.RIGHT JOIN:
===================
a. Using df():
===================
df_right = df1.join(df2,df1.Id1==df2.Id2,"right")
df_right.show(truncate=False)
print("Total count of records in inner join is:",df_right.count())

b. Using sparksql:
========================
df_right = spark.sql("""select Id1,Id2
                        from df_final1 
                        right join df_final2
                        on df_final1.Id1 = df_final2.Id2""")
df_count_right = spark.sql("""select count(*) as total_record_count from (select Id1,Id2
                        from df_final1 
                        right join df_final2
                        on df_final1.Id1 = df_final2.Id2) temp""")
df_right.show(truncate=False)
print("Total count of records in left join is: ",df_count_right.collect()[0][0])

o/p:
=========
+----+----+
|Id1 |Id2 |
+----+----+
|null|null|
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
+----+----+

Total count of records in left join is:  8

iv.FULL OUTER JOIN:
===================
a. Using df():
===================
df_full_outer = df1.join(df2,df1.Id1==df2.Id2,"full")
df_full_outer.show(truncate=False)
print("Total count of records in inner join is:",df_full_outer.count())

b. Using sparksql:
========================
df_full_outer = spark.sql("""select Id1,Id2
                        from df_final1 
                        full join df_final2
                        on df_final1.Id1 = df_final2.Id2""")
df_count_full = spark.sql("""select count(*) as total_record_count from (select Id1,Id2
                        from df_final1 
                        full join df_final2
                        on df_final1.Id1 = df_final2.Id2) temp""")
df_full_outer.show(truncate=False)
print("Total count of records in left join is: ",df_count_full.collect()[0][0])

o/p:
=========
+----+----+
|Id1 |Id2 |
+----+----+
|null|null|
|null|null|
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|0   |null|
+----+----+

Total count of records in left join is:  10

v.CROSS JOIN:
===================
a. Using df():
===================
df_cross = df1.crossJoin(df2)
df_cross.show(truncate=False)
print("Total count of records in cross join is:",df_cross.count())

b. Using sparksql:
========================
df_cross = spark.sql("""select Id1,Id2
                        from df_final1 
                        join df_final2
                    """)
df_count_cross = spark.sql("""select count(*) as total_record_count from (
                             select Id1,Id2
                             from df_final1 
                             join df_final2) temp""")
df_cross.show(truncate=False)
print("Total count of records in left join is: ",df_count_cross.collect()[0][0])

o/p:
=========
+----+----+
|Id1 |Id2 |
+----+----+
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |null|
|1   |null|
|1   |null|
|1   |null|
|1   |1   |
|1   |1   |
|null|1   |
|null|1   |
|0   |1   |
|0   |1   |
|1   |null|
|1   |null|
|null|null|
|null|null|
|0   |null|
|0   |null|
+----+----+

Total count of records in left join is:  20

vi.LEFT ANTI JOIN:
===================
a. Using df():
===================
df_left_anti = df1.join(df2,df1.Id1==df2.Id2,"left_anti")
df_left_anti.show(truncate=False)
print("Total count of records in inner join is:",df_left_anti.count())

b. Using sparksql:
========================
df_left_anti = spark.sql("""select Id1
                        from df_final1 
                        left join df_final2
                        on df_final1.Id1 = df_final2.Id2
                        where df_final2.Id2 IS NULL """)
df_count_left_anti = spark.sql("""select count(*) as total_record_count from (select Id1
                        from df_final1 
                        left join df_final2
                        on df_final1.Id1 = df_final2.Id2
                        where df_final2.Id2 IS NULL ) temp""")
df_left_anti.show(truncate=False)
print("Total count of records in left join is: ",df_count_left_anti.collect()[0][0])

o/p:
=========
+----+
|Id1 |
+----+
|null|
|0   |
+----+

Total count of records in left join is:  2

vi.LEFT SEMI JOIN:
===================
a. Using df():
===================
df_left_semi = df1.join(df2,df1.Id1==df2.Id2,"left_semi")
df_left_semi.show(truncate=False)
print("Total count of records in left semi join is:",df_left_semi.count())

b. Using sparksql:
========================
df_left_semi = spark.sql("""
SELECT Id1
FROM df_final1
LEFT SEMI JOIN df_final2
ON df_final1.Id1 = df_final2.Id2
""")

df_count_left_semi = spark.sql("""
SELECT COUNT(*) AS total_record_count
FROM df_final1
LEFT SEMI JOIN df_final2
ON df_final1.Id1 = df_final2.Id2
""")
df_left_semi.show(truncate=False)
print("Total count of records in left join is: ",df_count_left_semi.collect()[0][0])

o/p:
=========
+---+
|Id1|
+---+
|1  |
|1  |
|1  |
+---+

Total count of records in left join is:  3

14. Write a Pyspark/spark sql code to find the latest transaction for each customer:
====================================================================================
Solution:
=================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
customers_schema = StructType([\
                   StructField("customer_id",IntegerType(),True),\
                   StructField("sale_date",StringType(),True),\
                   StructField("amount",IntegerType(),True)])
customers_data = [(1,"2024-01-05",100),\
                   (1,"2024-01-12",150),\
                   (1,"2024-02-01",200),\
                   (2,"2024-01-03",50),\
                   (2,"2024-01-20",75)]
df_customers = spark.createDataFrame(data=customers_data,schema=customers_schema)
df_customers.show(truncate=False)
df_customers.printSchema()
o/p:
===========
+-----------+----------+------+
|customer_id|sale_date |amount|
+-----------+----------+------+
|1          |2024-01-05|100   |
|1          |2024-01-12|150   |
|1          |2024-02-01|200   |
|2          |2024-01-03|50    |
|2          |2024-01-20|75    |
+-----------+----------+------+
root
 |-- customer_id: integer (nullable = true)
 |-- sale_date: string (nullable = true)
 |-- amount: integer (nullable = true)
 
Change the datatype of sale_date:
====================================
df_customers_transformed = df_customers.withColumn("sale_date_new",to_date(col("sale_date")))\
                                       .select(col("customer_id"),col("sale_date_new"),col("amount"))
df_customers_transformed.show(truncate=False)
df_customers_transformed.printSchema()
o/p:
==============
+-----------+-------------+------+
|customer_id|sale_date_new|amount|
+-----------+-------------+------+
|1          |2024-01-05   |100   |
|1          |2024-01-12   |150   |
|1          |2024-02-01   |200   |
|2          |2024-01-03   |50    |
|2          |2024-01-20   |75    |
+-----------+-------------+------+
root
 |-- customer_id: integer (nullable = true)
 |-- sale_date_new: date (nullable = true)
 |-- amount: integer (nullable = true)
 
Approach 1st using groupby + max():
========================================
a. Using df():
===================
df_latest_transaction = df_customers_transformed.groupBy(col("customer_id"))\
                                                .agg(max(col("sale_date_new")).alias("latest_transaction_date"))
df_latest_transaction.show(truncate=False)
df_latest_transaction.printSchema()

b. Using sparksql:
========================
df_customers_transformed.createOrReplaceTempView("df_final")
df_latest_transaction = spark.sql("""select * from (select customer_id,max(sale_date_new) as latest_transaction_date
                                     from df_final
                                     group by customer_id) temp""")
df_latest_transaction.show(truncate=False)
df_latest_transaction.printSchema()

o/p:
=======
+-----------+-----------------------+
|customer_id|latest_transaction_date|
+-----------+-----------------------+
|1          |2024-02-01             |
|2          |2024-01-20             |
+-----------+-----------------------+

root
 |-- customer_id: integer (nullable = true)
 |-- latest_transaction_date: date (nullable = true)
 
Approach 2nd using Windowinf function:
==========================================
a. Using df():
=================
winspec = Window.partitionBy(col("customer_id"))\
                .orderBy(col("sale_date_new").desc())
                
df_latest_transaction = df_customers_transformed.withColumn("dnsk",dense_rank().over(winspec))\
                                                .filter(col("dnsk")==1)\
                                                .drop(col("dnsk"))
df_latest_transaction.show(truncate=False)
df_latest_transaction.printSchema()

b. Using sparksql:
==========================
df_latest_transaction = spark.sql("""WITH cte as (
                                     select *,dense_rank() over(partition by customer_id order by sale_date_new desc) dnsk
                                     from df_final)
                                     select customer_id,sale_date_new,amount from cte where dnsk =1""")
df_latest_transaction.show(truncate=False)
df_latest_transaction.printSchema()

o/p:
===========
+-----------+-------------+------+
|customer_id|sale_date_new|amount|
+-----------+-------------+------+
|1          |2024-02-01   |200   |
|2          |2024-01-20   |75    |
+-----------+-------------+------+

root
 |-- customer_id: integer (nullable = true)
 |-- sale_date_new: date (nullable = true)
 |-- amount: integer (nullable = true)
 
 Note: Best recommended approach is using Windowing function.


15. Write a Pyspark/spark sql code to find the rolling sum of ammount for each customer:
=============================================================================================
Solution:
=================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
customers_schema = StructType([\
                   StructField("customer_id",IntegerType(),True),\
                   StructField("sale_date",StringType(),True),\
                   StructField("amount",IntegerType(),True)])
customers_data = [(1,"2024-01-05",100),\
                   (1,"2024-01-12",150),\
                   (1,"2024-02-01",200),\
                   (2,"2024-01-03",50),\
                   (2,"2024-01-20",75)]
df_customers = spark.createDataFrame(data=customers_data,schema=customers_schema)
df_customers.show(truncate=False)
df_customers.printSchema()
o/p:
===========
+-----------+----------+------+
|customer_id|sale_date |amount|
+-----------+----------+------+
|1          |2024-01-05|100   |
|1          |2024-01-12|150   |
|1          |2024-02-01|200   |
|2          |2024-01-03|50    |
|2          |2024-01-20|75    |
+-----------+----------+------+
root
 |-- customer_id: integer (nullable = true)
 |-- sale_date: string (nullable = true)
 |-- amount: integer (nullable = true)
 
Change the datatype of sale_date:
====================================
df_customers_transformed = df_customers.withColumn("sale_date_new",to_date(col("sale_date")))\
                                       .select(col("customer_id"),col("sale_date_new"),col("amount"))
df_customers_transformed.show(truncate=False)
df_customers_transformed.printSchema()
o/p:
==============
+-----------+-------------+------+
|customer_id|sale_date_new|amount|
+-----------+-------------+------+
|1          |2024-01-05   |100   |
|1          |2024-01-12   |150   |
|1          |2024-02-01   |200   |
|2          |2024-01-03   |50    |
|2          |2024-01-20   |75    |
+-----------+-------------+------+
root
 |-- customer_id: integer (nullable = true)
 |-- sale_date_new: date (nullable = true)
 |-- amount: integer (nullable = true)

Approach 1st using self join (Not efficent for larger dataset):
======================================================================
a. Using df():
=====================
t1 = df_transformed.alias("t1")
t2 = df_transformed.alias("t2")

df_rolling = t1.join(
    t2,
    (col("t1.customer_id") == col("t2.customer_id")) &
    (col("t1.sale_date_new") >= col("t2.sale_date_new")),
    "inner"
).groupBy(
    col("t1.customer_id"),
    col("t1.sale_date_new")
).agg(
    sum(col("t2.amount")).alias("rolling_sum")
).orderBy("customer_id", "sale_date_new")

df_rolling.show()

b. Using sparksql():
===========================
df_transformed.createOrReplaceTempView("t1")
df_transformed.createOrReplaceTempView("t2")
df_rolling = spark.sql("""SELECT 
    t1.customer_id,
    t1.sale_date_new,
    SUM(t2.amount) AS rolling_sum
FROM t1
JOIN t2
ON t1.customer_id = t2.customer_id
AND t1.sale_date_new >= t2.sale_date_new
GROUP BY t1.customer_id, t1.sale_date_new
ORDER BY t1.customer_id, t1.sale_date_new""")
df_rolling.show(truncate = False)

o/p:
============
+-----------+-------------------+-----------+
|customer_id|sale_date_new      |rolling_sum|
+-----------+-------------------+-----------+
|1          |2024-01-05 00:00:00|100        |
|1          |2024-01-12 00:00:00|250        |
|1          |2024-02-01 00:00:00|450        |
|2          |2024-01-03 00:00:00|50         |
|2          |2024-01-20 00:00:00|125        |
+-----------+-------------------+-----------+

ii. Approach 2nd using Windowing Function ( more efficient for larger dataset)
==================================================================================
a. Using df():
========================
winspec = Window.partitionBy(col("customer_id"))\
                .orderBy(col("sale_date_new").asc())\
                .rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_rolling = df_transformed.withColumn("rolling_sum",sum(col("amount")).over(winspec))\
                           .select(col("customer_id"),col("sale_date_new"),col("rolling_sum"))
                           
df_rolling.show(truncate=False)

b. Using sparksql():
============================
df_transformed.createOrReplaceTempView("rolling_final")

df_rolling = spark.sql("""
WITH cte as (SELECT *,
       SUM(amount) OVER (
           PARTITION BY customer_id 
           ORDER BY sale_date_new ASC
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS rolling_sum
FROM rolling_final)
select customer_id,sale_date_new,rolling_sum from cte
""")

df_rolling.show(truncate=False)

o/p:
============
+-----------+-------------------+-----------+
|customer_id|sale_date_new      |rolling_sum|
+-----------+-------------------+-----------+
|1          |2024-01-05 00:00:00|100        |
|1          |2024-01-12 00:00:00|250        |
|1          |2024-02-01 00:00:00|450        |
|2          |2024-01-03 00:00:00|50         |
|2          |2024-01-20 00:00:00|125        |
+-----------+-------------------+-----------+

16. Write a Pyspark/sql code to find:
===========================================
i. Top 15 customers who placed the most number of orders.
ii. Find the numbers of orders under each order_status.
iii. Number of active customers (who placed atleast one order)
iv. Customer with most number of closed orders

solution:
==================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
orders_schema = StructType([\
                StructField("order_id",IntegerType(),True),\
                StructField("order_date",TimestampType(),True),\
                StructField("customer_id",IntegerType(),True),\
                StructField("order_status",StringType(),True)])
orders_df = spark.read.format("csv")\
.option("header",True)\
.schema(orders_schema)\
.option("delimeter",",")\
.option("path","/public/trendytech/orders_wh/*")\
.load() 
orders_df.show(truncate=False) 
orders_df.printSchema()
o/p:
===========
+--------+-------------------+-----------+---------------+
|order_id|order_date         |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|1       |2013-07-25 00:00:00|11599      |CLOSED         |
|2       |2013-07-25 00:00:00|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00|8827       |CLOSED         |
|5       |2013-07-25 00:00:00|11318      |COMPLETE       |
|6       |2013-07-25 00:00:00|7130       |COMPLETE       |
|7       |2013-07-25 00:00:00|4530       |COMPLETE       |
|8       |2013-07-25 00:00:00|2911       |PROCESSING     |
|9       |2013-07-25 00:00:00|5657       |PENDING_PAYMENT|
|10      |2013-07-25 00:00:00|5648       |PENDING_PAYMENT|
|11      |2013-07-25 00:00:00|918        |PAYMENT_REVIEW |
|12      |2013-07-25 00:00:00|1837       |CLOSED         |
|13      |2013-07-25 00:00:00|9149       |PENDING_PAYMENT|
|14      |2013-07-25 00:00:00|9842       |PROCESSING     |
|15      |2013-07-25 00:00:00|2568       |COMPLETE       |
|16      |2013-07-25 00:00:00|7276       |PENDING_PAYMENT|
|17      |2013-07-25 00:00:00|2667       |COMPLETE       |
|18      |2013-07-25 00:00:00|1205       |CLOSED         |
|19      |2013-07-25 00:00:00|9488       |PENDING_PAYMENT|
|20      |2013-07-25 00:00:00|9198       |PROCESSING     |
+--------+-------------------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)

orders_df.createOrReplaceTempView("orders")

i. Top 15 customers who placed the most number of orders:
===============================================================
a. Approach 1st using df():
==================================
result = orders_df.groupBy(col("customer_id"))\
                  .count()\
                  .sort(col("count").desc())\
                  .limit(15)
result.show(truncate=False)
result.printSchema()

b. Approach 2nd using sparksql:
=========================================
result = spark.sql("""select customer_id,count(order_id) as count 
                      from orders
                      group by customer_id
                      order by count desc
                      limit 15""")
result.show(truncate=False)
result.printSchema()
o/p:
========
+-----------+-----+
|customer_id|count|
+-----------+-----+
|5897       |16   |
|12431      |16   |
|569        |16   |
|6316       |16   |
|12284      |15   |
|4320       |15   |
|5624       |15   |
|5283       |15   |
|221        |15   |
|5654       |15   |
|791        |14   |
|6248       |14   |
|4249       |14   |
|3708       |14   |
|5821       |14   |
+-----------+-----+

root
 |-- customer_id: integer (nullable = true)
 |-- count: long (nullable = false)

ii. Find the numbers of orders under each order_status:
==============================================================
a. Approach 1st using df():
=================================
result = orders_df.groupBy(col("order_status"))\
                  .count()
result.show(truncate=False)
result.printSchema()

b. Approach 2nd using sparksql:
==========================================
result = spark.sql("""select order_status,count(order_id) as count
                      from orders
                      group by order_status""")
result.show(truncate=False)
result.printSchema()
o/p:
===========
+---------------+-----+
|order_status   |count|
+---------------+-----+
|PENDING_PAYMENT|15030|
|COMPLETE       |22899|
|ON_HOLD        |3798 |
|PAYMENT_REVIEW |729  |
|PROCESSING     |8275 |
|CLOSED         |7556 |
|SUSPECTED_FRAUD|1558 |
|PENDING        |7610 |
|CANCELED       |1428 |
+---------------+-----+

root
 |-- order_status: string (nullable = true)
 |-- count: long (nullable = false)

iii. Number of active customers (who placed atleast one order):
===================================================================
a. Approach 1st using df():
=====================================
 result = orders_df.select(col("customer_id")).distinct().count()
print("No of active customers are: ",result) 
o/p:
=========
No of active customers are:  12405

b. using sparksql:
===========================
result = spark.sql("""select count(distinct(customer_id)) as active_customers
                      from orders""")
result.show(truncate=False)
result.printSchema()
o/p:
==========
+----------------+
|active_customers|
+----------------+
|12405           |
+----------------+

root
 |-- active_customers: long (nullable = false)

iv. Customer with most number of closed orders:
======================================================
a. Approach 1st using df():
====================================
result = orders_df.filter(col("order_status")=="CLOSED")\
                  .groupBy(col("customer_id"))\
                  .count()\
                  .sort(col("count").desc())
result.show(truncate=False)
result.printSchema()

b. Approach 2nd using sparksql:
==============================================
result = spark.sql("""select customer_id,count(order_id) as count
                      from orders
                      where order_status = 'CLOSED'
                      group by customer_id
                      order by count desc""")
result.show(truncate=False)
result.printSchema()
o/p:
==========
+-----------+-----+
|customer_id|count|
+-----------+-----+
|1833       |6    |
|1363       |5    |
|1687       |5    |
|5493       |5    |
|7948       |4    |
|2768       |4    |
|10263      |4    |
|2236       |4    |
|2403       |4    |
|7879       |4    |
|4573       |4    |
|7850       |4    |
|12431      |4    |
|1521       |4    |
|10111      |4    |
|437        |4    |
|10018      |4    |
|5319       |4    |
|2774       |4    |
|3631       |4    |
+-----------+-----+
only showing top 20 rows

root
 |-- customer_id: integer (nullable = true)
 |-- count: long (nullable = false)

17. Write a Pyspark/sparksql code to rank the product based on their total sales amount for each month and return the top product for each month:
=================================================================================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
sales_data = [
 {"product_id": 1, "sale_date": "2023-01-05", "amount": 100},
 {"product_id": 2, "sale_date": "2023-01-08", "amount": 150},
 {"product_id": 1, "sale_date": "2023-01-15", "amount": 100},
 {"product_id": 3, "sale_date": "2023-01-20", "amount": 100},
 {"product_id": 2, "sale_date": "2023-02-03", "amount": 180},
 {"product_id": 3, "sale_date": "2023-02-10", "amount": 250},
 {"product_id": 1, "sale_date": "2023-02-15", "amount": 300},
]
schema="product_id int ,sale_date string,amount long"
df=spark.createDataFrame(sales_data,schema)
df.show()
df.printSchema()
o/p:
============
+----------+----------+------+
|product_id| sale_date|amount|
+----------+----------+------+
|         1|2023-01-05|   100|
|         2|2023-01-08|   150|
|         1|2023-01-15|   100|
|         3|2023-01-20|   100|
|         2|2023-02-03|   180|
|         3|2023-02-10|   250|
|         1|2023-02-15|   300|
+----------+----------+------+

root
 |-- product_id: integer (nullable = true)
 |-- sale_date: string (nullable = true)
 |-- amount: long (nullable = true)

Change the datatype of existing column + extracting the month from date column:
========================================================================================
df_transformed = df.withColumn("sale_date_new",to_date(col("sale_date")))\
                   .withColumn("month1",month(col("sale_date_new")))\
                   .select(col("product_id"),col("month1"),col("amount"))
df_transformed.show(truncate=False)
df_transformed.printSchema()
o/p:
============
+----------+------+------+
|product_id|month1|amount|
+----------+------+------+
|1         |1     |100   |
|2         |1     |150   |
|1         |1     |100   |
|3         |1     |100   |
|2         |2     |180   |
|3         |2     |250   |
|1         |2     |300   |
+----------+------+------+

root
 |-- product_id: integer (nullable = true)
 |-- month1: integer (nullable = true)
 |-- amount: long (nullable = true)

i. Using df():
========================
df_final = df_transformed.groupBy(col("product_id"),col("month1"))\
                         .agg(sum(col("amount")).alias("total_sales_amount"))\
                         .sort(col("total_sales_amount").desc())
                         


df_final.show(truncate=False)
df_final.printSchema()
o/p:
===========
+----------+------+------------------+
|product_id|month1|total_sales_amount|
+----------+------+------------------+
|1         |2     |300               |
|3         |2     |250               |
|1         |1     |200               |
|2         |2     |180               |
|2         |1     |150               |
|3         |1     |100               |
+----------+------+------------------+

root
 |-- product_id: integer (nullable = true)
 |-- month1: integer (nullable = true)
 |-- total_sales_amount: long (nullable = true)
winspec = Window.partitionBy(col("month1"))\
                .orderBy(col("total_sales_amount").desc())
df_final_output = df_final.withColumn("dnsk",dense_rank().over(winspec))\
                          .filter(col("dnsk")==1)\
                          .select(col("product_id"),col("month1"),col("total_sales_amount"))
df_final_output.show(truncate=False)
df_final_output.printSchema()
o/p:
=========
+----------+------+------------------+
|product_id|month1|total_sales_amount|
+----------+------+------------------+
|1         |1     |200               |
|1         |2     |300               |
+----------+------+------------------+

root
 |-- product_id: integer (nullable = true)
 |-- month1: integer (nullable = true)
 |-- total_sales_amount: long (nullable = true)

ii. Using sparksql():
==============================
df.createOrReplaceTempView("final")
df_final = spark.sql("""with cte1 as (select product_id,month(to_date(sale_date)) as month1,sum(amount) as total_sales_amount
                        from final
                        group by product_id,month1
                        order by total_sales_amount desc)
                        ,cte2 as (select *,dense_rank() over(partition by month1 order by total_sales_amount desc) as dnsk
                                  from cte1)
                          select product_id,month1,total_sales_amount from cte2
                          where dnsk=1""")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
==========
+----------+------+------------------+
|product_id|month1|total_sales_amount|
+----------+------+------------------+
|1         |1     |200               |
|1         |2     |300               |
+----------+------+------------------+

root
 |-- product_id: integer (nullable = true)
 |-- month1: integer (nullable = true)
 |-- total_sales_amount: long (nullable = true)


18. Pyspark/sparksql coding question:
=================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [('Maheer','HR',2000),\
        ('Wafa','IT',3000),\
        ('Asi','HR',1500),\
        ('Annu','Payroll',3500),\
        ('Shakti','IT',3000),\
        ('Pradeep','IT',3000),\
        ('Karnthi','Payroll',2000),\
        ('Himanshu','IT',2000),\
        ('Bhargava','HR',2000),\
        ('Martin','IT',2500)]
schema = StructType([\
         StructField("Name",StringType(),True),\
         StructField("Dept",StringType(),True),\
         StructField("Salary",IntegerType(),True)])
df = spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()
o/p:
=========
+--------+-------+------+
|Name    |Dept   |Salary|
+--------+-------+------+
|Maheer  |HR     |2000  |
|Wafa    |IT     |3000  |
|Asi     |HR     |1500  |
|Annu    |Payroll|3500  |
|Shakti  |IT     |3000  |
|Pradeep |IT     |3000  |
|Karnthi |Payroll|2000  |
|Himanshu|IT     |2000  |
|Bhargava|HR     |2000  |
|Martin  |IT     |2500  |
+--------+-------+------+

root
 |-- Name: string (nullable = true)
 |-- Dept: string (nullable = true)
 |-- Salary: integer (nullable = true)

df.createOrReplaceTempView("final")

i. Find departmentwise highest salary:
==============================================
a. Using df():
=======================
winspechigh = Window.partitionBy(col("Dept"))\
                    .orderBy(col("Salary").desc())

df_final1 = df.withColumn("dnsk",dense_rank().over(winspechigh))\
              .filter(col("dnsk")==1)\
              .select(col("Name"),col("Dept"),col("Salary"))
df_final1.show(truncate=False)
df_final1.printSchema()

b. Using sparksql:
===========================
df_final1 = spark.sql("""with cte as(
                         select *,dense_rank() over(partition by Dept order by Salary desc) as dnsk
                         from final)
                         select Name,Dept,Salary
                         from cte
                         where dnsk=1 AND dnsk=1""")
df_final1.show(truncate=False)
o/p:
========
+--------+-------+------+
|Name    |Dept   |Salary|
+--------+-------+------+
|Maheer  |HR     |2000  |
|Bhargava|HR     |2000  |
|Annu    |Payroll|3500  |
|Pradeep |IT     |3000  |
|Wafa    |IT     |3000  |
|Shakti  |IT     |3000  |
+--------+-------+------+

ii. Find departmentwise lowest salary:
===============================================
a. Using df():
================================================

winspeclow = Window.partitionBy(col("Dept"))\
                    .orderBy(col("Salary"))

df_final2 = df.withColumn("dnsk",dense_rank().over(winspeclow))\
              .filter(col("dnsk")==1)\
              .select(col("Name"),col("Dept"),col("Salary"))
df_final2.show(truncate=False)
df_final2.printSchema()

b. Using sparksql():
================================

df_final2 = spark.sql("""with cte as(
                         select *,dense_rank() over(partition by Dept order by Salary asc) as dnsk
                         from final)
                         select Name,Dept,Salary
                         from cte
                         where dnsk=1""")
df_final2.show(truncate=False)
df_final2.printSchema()
o/p:
===========
+--------+-------+------+
|Name    |Dept   |Salary|
+--------+-------+------+
|Asi     |HR     |1500  |
|Karnthi |Payroll|2000  |
|Himanshu|IT     |2000  |
+--------+-------+------+

root
 |-- Name: string (nullable = true)
 |-- Dept: string (nullable = true)
 |-- Salary: integer (nullable = true)

iii. Find lowest salary in HR dept:
============================================
a. Using df():
=================================

winspec1 = Window.partitionBy(col("Dept"))\
                 .orderBy(col("Salary"))

df_lowest_salary = df.withColumn("dnsk", dense_rank().over(winspec1)) \
    .filter((col("dnsk") == 1) & (col("Dept") == 'HR')) \
    .select(col("Name"), col("Dept"), col("Salary"))

df_lowest_salary.show(truncate=False)
df_lowest_salary.printSchema()

b. Using sparksql():
==================================
df_lowest_salary = spark.sql("""with cte as(
                                select *,dense_rank() over(partition by Dept order by Salary ) as dnsk
                                from final)
                                select Name,Dept,Salary
                                from cte
                                where Dept='HR' AND dnsk=1""")
df_lowest_salary.show(truncate=False)
df_lowest_salary.printSchema()
o/p:
===========
+----+----+------+
|Name|Dept|Salary|
+----+----+------+
|Asi |HR  |1500  |
+----+----+------+

root
 |-- Name: string (nullable = true)
 |-- Dept: string (nullable = true)
 |-- Salary: integer (nullable = true)

iv. Find highest salary in HR dept:
===============================================
a. Using df():
==========================
winspec2 = Window.partitionBy(col("Dept"))\
                 .orderBy(col("Salary").desc())

df_highest_salary = df.withColumn("dnsk",dense_rank().over(winspec2))\
                                    .filter((col("dnsk")==1) & (col("Dept")=='HR'))\
                                    .select(col("Name"),col("Dept"),col("Salary"))
df_highest_salary.show(truncate=False)
df_highest_salary.printSchema()

b. Using sparksql():
================================
df_highest_salary  = spark.sql("""with cte as(
                                  select*,dense_rank() over(partition by Dept order by Salary desc) as dnsk
                                  from final)
                                  select Name,Dept,Salary
                                  from cte
                                  where dnsk=1 AND dept='HR'""")
df_highest_salary.show(truncate=False)
df_highest_salary.printSchema()
o/p:
=============
+--------+----+------+
|Name    |Dept|Salary|
+--------+----+------+
|Bhargava|HR  |2000  |
|Maheer  |HR  |2000  |
+--------+----+------+

root
 |-- Name: string (nullable = true)
 |-- Dept: string (nullable = true)
 |-- Salary: integer (nullable = true)

19. Pyspark/sparksql coding question:
=================================================
solution:
===============
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()
spark
employees_schema = StructType([
StructField("id", IntegerType(), True),
StructField("name", StringType(), True),
StructField("salary", IntegerType(), True),
StructField("managerId", IntegerType(), True)])

employees_data = [
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, None),
(4, 'Max', 90000, None)
]

df_employee=spark.createDataFrame(employees_data,employees_schema)
df_employee.show()
df_employee.printSchema()
o/p:
========
+---+-----+------+---------+
| id| name|salary|managerId|
+---+-----+------+---------+
|  1|  Joe| 70000|        3|
|  2|Henry| 80000|        4|
|  3|  Sam| 60000|     null|
|  4|  Max| 90000|     null|
+---+-----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

df_employee.createOrReplaceTempView("e1")
df_employee.createOrReplaceTempView("e2")

i. Employee salary greater than manager:
=========================================
a. Approach 1st using df():
==============================
from pyspark.sql.functions import col

df_join = df_employee.alias("e1").join(df_employee.alias("e2"),col("e1.managerId") == col("e2.id"),"inner") \
                                 .filter(col("e1.salary") > col("e2.salary"))

df_join.show(truncate=False)
df_join.printSchema()
o/p:
=======
+---+----+------+---------+---+----+------+---------+
|id |name|salary|managerId|id |name|salary|managerId|
+---+----+------+---------+---+----+------+---------+
|1  |Joe |70000 |3        |3  |Sam |60000 |null     |
+---+----+------+---------+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

from pyspark.sql.functions import col

df_join = df_employee.alias("e1").join(df_employee.alias("e2"),col("e1.managerId") == col("e2.id"),"inner") \
                                 .filter(col("e1.salary") > col("e2.salary")) \
                                 .select(col("e1.id"),col("e1.name"),col("e1.salary"),col("e1.managerId"))
df_join.show(truncate=False)
df_join.printSchema()
o/p:
========
+---+----+------+---------+
|id |name|salary|managerId|
+---+----+------+---------+
|1  |Joe |70000 |3        |
+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)


b. Approach 2nd using sparksql:
====================================
df_join = spark.sql("""select * from e1 join e2
                       on e1.managerId == e2.id
                       where e1.salary > e2.salary""")

df_join.show(truncate=False)
df_join.printSchema()
o/p:
=======
+---+----+------+---------+---+----+------+---------+
|id |name|salary|managerId|id |name|salary|managerId|
+---+----+------+---------+---+----+------+---------+
|1  |Joe |70000 |3        |3  |Sam |60000 |null     |
+---+----+------+---------+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

df_join = spark.sql("""select e1.id,e1.name,e1.salary,e1.managerId from e1 join e2
                       on e1.managerId == e2.id
                       where e1.salary > e2.salary""")

df_join.show(truncate=False)
df_join.printSchema()
o/p:
=========
+---+----+------+---------+
|id |name|salary|managerId|
+---+----+------+---------+
|1  |Joe |70000 |3        |
+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

ii. Employee not having manager:
=================================
a. Approach 1st using df():
============================
from pyspark.sql.functions import col

df_not_having_manager = df_employee.alias("e1").join(df_employee.alias("e2"),col("e1.managerId") == col("e2.id"),"left") \
                                               .filter(col("e1.managerId").isNull())
                                               

df_not_having_manager.show(truncate=False)
df_not_having_manager.printSchema()
o/p:
=======
+---+----+------+---------+----+----+------+---------+
|id |name|salary|managerId|id  |name|salary|managerId|
+---+----+------+---------+----+----+------+---------+
|3  |Sam |60000 |null     |null|null|null  |null     |
|4  |Max |90000 |null     |null|null|null  |null     |
+---+----+------+---------+----+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

df_not_having_manager = df_employee.alias("e1").join(df_employee.alias("e2"),col("e1.managerId") == col("e2.id"),"left") \
                                               .filter(col("e1.managerId").isNull())\
                                               .select(col("e1.id"),col("e1.name"),col("e1.salary"),col("e1.managerId"))

df_not_having_manager.show(truncate=False)
df_not_having_manager.printSchema()
o/p:
==========
+---+----+------+---------+
|id |name|salary|managerId|
+---+----+------+---------+
|3  |Sam |60000 |null     |
|4  |Max |90000 |null     |
+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

b.Approach 2nd using sparksql:
===================================
df_not_having_manager = spark.sql("""select * from e1 left join e2
                                     on e1.managerId = e2.id
                                     where e1.managerId is Null""")
df_not_having_manager.show(truncate=False)
df_not_having_manager.printSchema()
o/p:
=========
+---+----+------+---------+----+----+------+---------+
|id |name|salary|managerId|id  |name|salary|managerId|
+---+----+------+---------+----+----+------+---------+
|3  |Sam |60000 |null     |null|null|null  |null     |
|4  |Max |90000 |null     |null|null|null  |null     |
+---+----+------+---------+----+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)

df_not_having_manager = spark.sql("""select e1.id,e1.name,e1.salary,e1.managerId from e1 left join e2
                                     on e1.managerId = e2.id
                                     where e1.managerId is Null""")
df_not_having_manager.show(truncate=False)
df_not_having_manager.printSchema()
o/p:
=========
+---+----+------+---------+
|id |name|salary|managerId|
+---+----+------+---------+
|3  |Sam |60000 |null     |
|4  |Max |90000 |null     |
+---+----+------+---------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- managerId: integer (nullable = true)


19. Pyspark/sparksql coding question:
=================================================
solution:
======================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()
spark
schema = "Id INT,Email string"
data = [(1,"abc@g.com"),\
        (2,"xyz@g.com"),\
        (3,"abc@g.com"),\
        (4,"pqr@g.com")]
df = spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()
o/p:
======
+---+---------+
|Id |Email    |
+---+---------+
|1  |abc@g.com|
|2  |xyz@g.com|
|3  |abc@g.com|
|4  |pqr@g.com|
+---+---------+

root
 |-- Id: integer (nullable = true)
 |-- Email: string (nullable = true)
df.createOrReplaceTempView("duplicate_email")

Approach 1st using df() (Find duplicate email using group by):
================================================================
i. df_duplicate_email = df.groupBy(col("Email"))\
                       .count()\
                       .filter(col("count")>1)\
                       .select(col("Email"))
df_duplicate_email.show(truncate=False)
df_duplicate_email.printSchema()

ii. using sparksql:
=======================
df_duplicate_email = spark.sql("""select Email from (select Email,count(*) as duplicate_count
                                  from duplicate_email
                                  group by email
                                  having duplicate_count > 1) temp""")
df_duplicate_email.show(truncate=False)
df_duplicate_email.printSchema()
o/p:
=======
+---------+
|Email    |
+---------+
|abc@g.com|
+---------+

root
 |-- Email: string (nullable = true)

Approach 2nd using df() (Find duplicate email using windowing function):
============================================================================
i. winspec = Window.partitionBy(col("Email"))\
                .orderBy(col("Id").desc())

df_duplicate_email = df.withColumn("rn",row_number().over(winspec))\
                       .filter(col("rn")>1)\
                       .select(col("Email"))
df_duplicate_email.show(truncate=False)
df_duplicate_email.printSchema()

ii. using sparksql:
=======================
df_duplicate_email = spark.sql("""With cte as (
                                select *,row_number() over(partition by Email order by Id desc) as rn
                                from duplicate_email)
                                select Email from cte
                                where rn>1""")
df_duplicate_email.show(truncate=False)
df_duplicate_email.printSchema()
o/p:
=======
+---------+
|Email    |
+---------+
|abc@g.com|
+---------+

root
 |-- Email: string (nullable = true)


Remove duplicate using multiple approach:
===============================================
i. Remove duplicate using distinct():
===========================================
a. df.distinct().show(truncate=False)
b. spark.sql("select distinct Id,Email from duplicate_email").show(truncate=False)
o/p:
======
+---+---------+
|Id |Email    |
+---+---------+
|1  |abc@g.com|
|3  |abc@g.com|
|2  |xyz@g.com|
|4  |pqr@g.com|
+---+---------+

ii. Remove duplicate using dropDuplicates():
==============================================
a. df.dropDuplicates(["Email"]).show(truncate=False)
o/p:
========
+---+---------+
|Id |Email    |
+---+---------+
|1  |abc@g.com|
|4  |pqr@g.com|
|2  |xyz@g.com|
+---+---------+

b. spark.sql("""with cte as (
             select *,row_number() over(partition by Email order by Id desc) as rn
             from duplicate_email
             )
             select Id,Email from cte
             where rn=1""").show(truncate=False)
o/p:
=======
+---+---------+
|Id |Email    |
+---+---------+
|3  |abc@g.com|
|4  |pqr@g.com|
|2  |xyz@g.com|
+---+---------+

20. Find the missing numbers in the column:
================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
data = [(1,),\
        (2,),\
        (3,),\
        (6,),\
        (7,),\
        (8,)]
df = spark.createDataFrame(data).toDF("Id")
df.show(truncate=False)
df.printSchema()
o/p:
=========
+---+
|Id |
+---+
|1  |
|2  |
|3  |
|6  |
|7  |
|8  |
+---+

root
 |-- Id: long (nullable = true)

df.createOrReplaceTempView("missing_number")

i. Approach 1st using df() range()+subtract():
=================================================
from pyspark.sql.functions import min, max, col

df_min_max = df.agg(
    min(col("Id")).alias("min_id"),
    max(col("Id")).alias("max_id")
)

df_min_max.show(truncate=False)
o/p:
=====
+------+------+
|min_id|max_id|
+------+------+
|1     |8     |
+------+------+

df_final = spark.range(df_min_max.collect()[0][0],df_min_max.collect()[0][1])
df_final.show(truncate=False)
o/p:
======
+---+
|id |
+---+
|1  |
|2  |
|3  |
|4  |
|5  |
|6  |
|7  |
+---+

df_final = spark.range(df_min_max.collect()[0][0],df_min_max.collect()[0][1]+1)
df_final.show(truncate=False)
o/p:
======
+---+
|id |
+---+
|1  |
|2  |
|3  |
|4  |
|5  |
|6  |
|7  |
|8  |
+---+

df_missing_number = df_final.subtract(df)
df_missing_number.show(truncate=False)
df_missing_number.printSchema()
o/p:
=======
+---+
|id |
+---+
|5  |
|4  |
+---+

root
 |-- id: long (nullable = false)

ii. Approach 2nd using df() range()+left join:
=================================================
df_missing_number = df_final.alias("fr").join(df.alias("d"),col("fr.Id")==col("d.Id"),'leftouter')\
                                        .filter(col("d.Id").isNull())\
                                        .select(col("fr.Id"))
df_missing_number.show(truncate=False)
df_missing_number.printSchema()
o/p:
======
+---+
|Id |
+---+
|5  |
|4  |
+---+

root
 |-- Id: long (nullable = false)

iii. Approach 1st using sparksql() explode(sequence()) + except():
===================================================================
df_missing_number = spark.sql("""WITH min_max AS (
    SELECT MIN(Id) AS min_id, MAX(Id) AS max_id
    FROM missing_number
),

full_range AS (
    SELECT explode(sequence(min_id, max_id)) AS Id
    FROM min_max
)

SELECT Id FROM full_range
EXCEPT
SELECT Id FROM missing_number""")
df_missing_number.show(truncate=False)
df_missing_number.printSchema()
o/p:
=======
+---+
|Id |
+---+
|5  |
|4  |
+---+

root
 |-- Id: long (nullable = false)

iv. Approach 2nd using sparksql() explode(sequence()) + left join:
=====================================================================
df_missing_number = spark.sql("""WITH min_max AS (
    SELECT MIN(Id) AS min_id, MAX(Id) AS max_id
    FROM missing_number
),

full_range AS (
    SELECT explode(sequence(min_id, max_id)) AS Id
    FROM min_max
)

SELECT fr.Id AS missing_id
FROM full_range fr
LEFT JOIN missing_number mn
ON fr.Id = mn.Id
WHERE mn.Id IS NULL""")
df_missing_number.show(truncate=False)
df_missing_number.printSchema()
o/p:
=======
+----------+
|missing_id|
+----------+
|5         |
|4         |
+----------+

root
 |-- missing_id: long (nullable = false)

Note: 
======
Mapping from PySpark → SQL
PySpark	              Spark SQL
spark.range()	      sequence() + explode()
subtract()	          LEFT JOIN ... WHERE NULL / EXCEPT
min/max	              same

21. Total no of partitions and total rows in each partitions:
==============================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
df = spark.range(1,1000000)
df.show(50,truncate=False)
df.printSchema()
o/p:
=======

+---+
|id |
+---+
|1  |
|2  |
|3  |
|4  |
|5  |
|6  |
|7  |
|8  |
|9  |
|10 |
|11 |
|12 |
|13 |
|14 |
|15 |
|16 |
|17 |
|18 |
|19 |
|20 |
|21 |
|22 |
|23 |
|24 |
|25 |
|26 |
|27 |
|28 |
|29 |
|30 |
|31 |
|32 |
|33 |
|34 |
|35 |
|36 |
|37 |
|38 |
|39 |
|40 |
|41 |
|42 |
|43 |
|44 |
|45 |
|46 |
|47 |
|48 |
|49 |
|50 |
+---+
only showing top 50 rows

root
 |-- id: long (nullable = false)

df_partitioned.createOrReplaceTempView("count_partition")

i. Approach 1st using pyspark df:
====================================
Check no of partitions in a df:
==================================
df.rdd.getNumPartitions()
o/p:
======
2

df_partitioned = df.repartition(8)
df_partitioned.rdd.getNumPartitions()
o/p:
=====
8

To check data is evenly distributed in each partition:
======================================================
df_count_check_in_each_partition = df_partitioned.select(spark_partition_id().alias("partition_id"))\
                                                 .groupBy(col("partition_id"))\
                                                 .count()\
                                                 .sort(col("partition_id"))
df_count_check_in_each_partition.show(truncate=False)
o/p:
===
+------------+------+
|partition_id|count |
+------------+------+
|0           |125000|
|1           |125000|
|2           |125000|
|3           |125000|
|4           |125000|
|5           |124999|
|6           |125000|
|7           |125000|
+------------+------+

ii. Approach 2nd using sparksql:
====================================
df_count_check_in_each_partition = spark.sql("""select spark_partition_id() as partition_id,count(*) as total_count
                                                from count_partition
                                                group by partition_id
                                                order by partition_id asc""")
df_count_check_in_each_partition.show(truncate=False)
df_count_check_in_each_partition.printSchema()
o/p:
======
+------------+-----------+
|partition_id|total_count|
+------------+-----------+
|0           |125000     |
|1           |125000     |
|2           |125000     |
|3           |125000     |
|4           |125000     |
|5           |124999     |
|6           |125000     |
|7           |125000     |
+------------+-----------+

root
 |-- partition_id: integer (nullable = false)
 |-- total_count: long (nullable = false)

22. Write a pyspark program to format the scientific notation and show them as decimal numbers:
===============================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
df = spark.createDataFrame([(101, 0.000000987), (102, 0.0000554467), (103, 0.00050345678)], ["observation_id", "result"])
df.show(truncate=False)
df.printSchema()
o/p:
====
+--------------+------------+
|observation_id|result      |
+--------------+------------+
|101           |9.87E-7     |
|102           |5.54467E-5  |
|103           |5.0345678E-4|
+--------------+------------+

root
 |-- observation_id: long (nullable = true)
 |-- result: double (nullable = true)

df.createOrReplaceTempView("final")

i. Approach 1st using df():
=============================
df_final = df.withColumn("format_result",format_number(col("result"),10))\
             .drop(col("result"))
df_final.show(truncate=False)
df_final.printSchema()
o/p:
====
+--------------+-------------+
|observation_id|format_result|
+--------------+-------------+
|101           |0.0000009870 |
|102           |0.0000554467 |
|103           |0.0005034568 |
+--------------+-------------+

root
 |-- observation_id: long (nullable = true)
 |-- format_result: string (nullable = true)

ii. Approach 2nd using sparksql:
===================================
df_final = spark.sql("""select observation_id,format_number(result,10) as format_result from final""")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
======
+--------------+-------------+
|observation_id|format_result|
+--------------+-------------+
|101           |0.0000009870 |
|102           |0.0000554467 |
|103           |0.0005034568 |
+--------------+-------------+

root
 |-- observation_id: long (nullable = true)
 |-- format_result: string (nullable = true)


23. Write a Pyspark or sparksql code to find start_week_date,end_week_date for each weeknum and year:
=======================================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()
spark
data=[(2024,1,'2024-01-01'),
      (2024,1,'2024-01-02'),
      (2024,1,'2024-01-03'),
      (2024,1,'2024-01-04'),
      (2024,1,'2024-01-05'),
      (2024,1,'2024-01-06'),
      (2024,1,'2024-01-07'),
      (2024,2,'2024-01-08'),
      (2024,2,'2024-01-09'),
      (2024,2,'2024-01-10'),
      (2024,2,'2024-01-11'),
      (2024,2,'2024-01-12'),
      (2024,2,'2024-01-13'),
      (2024,2,'2024-01-14')]
schema=StructType([StructField('year',IntegerType(),True),StructField('weeknum',IntegerType(),True),StructField('dates',StringType(),True)])
df=spark.createDataFrame(data,schema)
df.show()
df.printSchema()
O/P:
======
+----+-------+----------+
|year|weeknum|     dates|
+----+-------+----------+
|2024|      1|2024-01-01|
|2024|      1|2024-01-02|
|2024|      1|2024-01-03|
|2024|      1|2024-01-04|
|2024|      1|2024-01-05|
|2024|      1|2024-01-06|
|2024|      1|2024-01-07|
|2024|      2|2024-01-08|
|2024|      2|2024-01-09|
|2024|      2|2024-01-10|
|2024|      2|2024-01-11|
|2024|      2|2024-01-12|
|2024|      2|2024-01-13|
|2024|      2|2024-01-14|
+----+-------+----------+

root
 |-- year: integer (nullable = true)
 |-- weeknum: integer (nullable = true)
 |-- dates: string (nullable = true)

df.createOrReplaceTempView("final")

change the datatype of column "dates":
===========================================
df_transformed = df.withColumn("dates",to_date(col("dates")))\
                   .select(col("year"),col("weeknum"),col("dates"))
df_transformed.show(truncate=False)
df_transformed.printSchema()
o/p:
=====
+----+-------+----------+
|year|weeknum|dates     |
+----+-------+----------+
|2024|1      |2024-01-01|
|2024|1      |2024-01-02|
|2024|1      |2024-01-03|
|2024|1      |2024-01-04|
|2024|1      |2024-01-05|
|2024|1      |2024-01-06|
|2024|1      |2024-01-07|
|2024|2      |2024-01-08|
|2024|2      |2024-01-09|
|2024|2      |2024-01-10|
|2024|2      |2024-01-11|
|2024|2      |2024-01-12|
|2024|2      |2024-01-13|
|2024|2      |2024-01-14|
+----+-------+----------+

root
 |-- year: integer (nullable = true)
 |-- weeknum: integer (nullable = true)
 |-- dates: date (nullable = true)

i. Approach 1st using df():
============================
df_final = df_transformed.groupBy(col("year"),col("weeknum"))\
                         .agg(min(col("dates")).alias("start_day_week"),\
                              max(col("dates")).alias("end_day_week"))

df_final.show(truncate=False)
df_final.printSchema()
o/p:
=====
+----+-------+--------------+------------+
|year|weeknum|start_day_week|end_day_week|
+----+-------+--------------+------------+
|2024|2      |2024-01-08    |2024-01-14  |
|2024|1      |2024-01-01    |2024-01-07  |
+----+-------+--------------+------------+

root
 |-- year: integer (nullable = true)
 |-- weeknum: integer (nullable = true)
 |-- start_day_week: date (nullable = true)
 |-- end_day_week: date (nullable = true)

ii. Approach 2nd using sparksql:
=================================
df_final = spark.sql("""select year,weeknum,min(to_date(dates)) as start_day_week,max(to_date(dates)) as end_day_week
                        from final
                        group by year,weeknum""")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
========
+----+-------+--------------+------------+
|year|weeknum|start_day_week|end_day_week|
+----+-------+--------------+------------+
|2024|2      |2024-01-08    |2024-01-14  |
|2024|1      |2024-01-01    |2024-01-07  |
+----+-------+--------------+------------+

root
 |-- year: integer (nullable = true)
 |-- weeknum: integer (nullable = true)
 |-- start_day_week: date (nullable = true)
 |-- end_day_week: date (nullable = true)


24. Difference b/t explode vs explode_outer vs posexplode: Using Pyspark/sparksql
==================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

client_schema_ddl = "Id int, Name string, Address string"

client_schema_programmatic = StructType([\
                                        StructField("Id",IntegerType(),True),\
                                        StructField("Name",StringType(),True),\
                                        StructField("Address",StringType(),True)])

client_data = [
    (1, 'Dnyan', 'Pune,Mumbai,Latur'),
    (2, 'Rahul', 'Nanded,Mumbai'),
    (3, 'Sonali', 'Pune,Mumbai'),
    (4, 'Yogesh', None)
]
raw_df = spark.createDataFrame(data = client_data,schema = client_schema_ddl)
raw_df.show(truncate=False)
raw_df.printSchema()
o/p:
=======
+---+------+-----------------+
|Id |Name  |Address          |
+---+------+-----------------+
|1  |Dnyan |Pune,Mumbai,Latur|
|2  |Rahul |Nanded,Mumbai    |
|3  |Sonali|Pune,Mumbai      |
|4  |Yogesh|null             |
+---+------+-----------------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: string (nullable = true)

raw_df.createOrReplaceTempView("final")

i. Use of explode():
========================
a. Using df():
================
df_explode = raw_df.withColumn("city",explode(split(col("Address"),",")))
df_explode.show(truncate=False)
df_explode.printSchema()

b. Using sparksql():
======================
df_explode = spark.sql("""
SELECT 
    Id,
    Name,
    Address,
    explode(split(Address, ',')) AS city 
FROM final
""")

df_explode.show(truncate=False)
df_explode.printSchema()
o/p:
======
+---+------+-----------------+------+
|Id |Name  |Address          |city  |
+---+------+-----------------+------+
|1  |Dnyan |Pune,Mumbai,Latur|Pune  |
|1  |Dnyan |Pune,Mumbai,Latur|Mumbai|
|1  |Dnyan |Pune,Mumbai,Latur|Latur |
|2  |Rahul |Nanded,Mumbai    |Nanded|
|2  |Rahul |Nanded,Mumbai    |Mumbai|
|3  |Sonali|Pune,Mumbai      |Pune  |
|3  |Sonali|Pune,Mumbai      |Mumbai|
+---+------+-----------------+------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: string (nullable = true)
 |-- city: string (nullable = true)

Conclusion: From above we conclude that explode() does not tackle null values properly, it does not include null values.

ii. Use of explode_outer():
============================
a. Using df():
================
df_explode_outer = raw_df.withColumn("city",explode_outer(split(col("Address"),",")))
df_explode_outer.show(truncate=False)
df_explode_outer.printSchema()

b. Using sparksql():
======================
df_explode_outer = spark.sql("""
SELECT 
    Id,
    Name,
    Address,
    explode_outer(split(Address, ',')) AS city 
FROM final
""")

df_explode_outer.show(truncate=False)
df_explode_outer.printSchema()
o/p:
======
+---+------+-----------------+------+
|Id |Name  |Address          |city  |
+---+------+-----------------+------+
|1  |Dnyan |Pune,Mumbai,Latur|Pune  |
|1  |Dnyan |Pune,Mumbai,Latur|Mumbai|
|1  |Dnyan |Pune,Mumbai,Latur|Latur |
|2  |Rahul |Nanded,Mumbai    |Nanded|
|2  |Rahul |Nanded,Mumbai    |Mumbai|
|3  |Sonali|Pune,Mumbai      |Pune  |
|3  |Sonali|Pune,Mumbai      |Mumbai|
|4  |Yogesh|null             |null  |
+---+------+-----------------+------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: string (nullable = true)
 |-- city: string (nullable = true)

Conclusion: From above we conclude that explode_outer() tackle null values properly, it include null values.

iii. Use of posexplode_outer():
===============================
a. Using df():
================
df_posexplode_outer = raw_df.select(col("*"),posexplode_outer(split(col("Address"),",").alias("city")))
df_posexplode_outer.show(truncate=False)
df_posexplode_outer.printSchema()

b. Using sparksql():
======================
df_posexplode_outer = spark.sql("""
SELECT 
    Id,
    Name,
    Address,
    posexplode_outer(split(Address, ',')) AS (pos, city)
FROM final
""")
df_posexplode_outer.show(truncate=False)
df_posexplode_outer.printSchema()
o/p:
======
+---+------+-----------------+----+------+
|Id |Name  |Address          |pos |city  |
+---+------+-----------------+----+------+
|1  |Dnyan |Pune,Mumbai,Latur|0   |Pune  |
|1  |Dnyan |Pune,Mumbai,Latur|1   |Mumbai|
|1  |Dnyan |Pune,Mumbai,Latur|2   |Latur |
|2  |Rahul |Nanded,Mumbai    |0   |Nanded|
|2  |Rahul |Nanded,Mumbai    |1   |Mumbai|
|3  |Sonali|Pune,Mumbai      |0   |Pune  |
|3  |Sonali|Pune,Mumbai      |1   |Mumbai|
|4  |Yogesh|null             |null|null  |
+---+------+-----------------+----+------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: string (nullable = true)
 |-- pos: integer (nullable = true)
 |-- city: string (nullable = true)

Conclusion: 
================
i. From above we conclude that posexplode_outer() tackle null values properly, it include null values.
ii. It gives position/indexes to each row in a df.
iii. It does not work with (.withColumn()).

🔥 Key Differences:
=======================
Function	       Handles NULL	      Returns Index
explode()	        ❌ No	               ❌ No
explode_outer()	    ✅ Yes	               ❌ No
posexplode_outer()	✅ Yes	               ✅ Yes


25. Difference b/t explode vs explode_outer vs posexplode: Using Pyspark/sparksql
==================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

education_schema_ddl = "Name string,Age int,Education string"

education_schema_programmatic = StructType([\
                                           StructField("Name",StringType(),True),\
                                           StructField("Age",IntegerType(),True),\
                                           StructField("Education",StringType(),True)])

education_data = [("Azar",25,'MBA,BE,BSC'),\
                  ("Hari",32,None),\
                  ("Kumar",35,'ME,BE,Diploma')]
education_df = spark.createDataFrame(data=education_data,schema=education_schema_ddl)
education_df.show(truncate=False)
education_df.printSchema()
o/p:
=======
+-----+---+-------------+
|Name |Age|Education    |
+-----+---+-------------+
|Azar |25 |MBA,BE,BSC   |
|Hari |32 |null         |
|Kumar|35 |ME,BE,Diploma|
+-----+---+-------------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Education: string (nullable = true)

education_df.createOrReplaceTempView("final")

i. Use of explode():
========================
a. Using df():
================
df_explode = education_df.withColumn("Qualification",explode(split(col("Education"),",")))\
               .drop(col("Education"))

df_explode.show(truncate=False)
df_explode.printSchema()

b. Using sparksql():
======================
df_explode = spark.sql("""select Name,
                                 Age,
                                 explode(split(Education,",")) as Qualification
                                 from final""")
df_explode.show(truncate=False)
df_explode.printSchema()
o/p:
======
+-----+---+-------------+
|Name |Age|Qualification|
+-----+---+-------------+
|Azar |25 |MBA          |
|Azar |25 |BE           |
|Azar |25 |BSC          |
|Kumar|35 |ME           |
|Kumar|35 |BE           |
|Kumar|35 |Diploma      |
+-----+---+-------------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Qualification: string (nullable = true)

Conclusion: From above we conclude that explode() does not tackle null values properly, it does not include null values.

ii. Use of explode_outer():
============================
a. Using df():
================
df_explode_outer = education_df.withColumn("Qualification",explode_outer(split(col("Education"),",")))\
               .drop(col("Education"))

df_explode_outer.show(truncate=False)
df_explode_outer.printSchema()

b. Using sparksql():
======================
df_explode_outer = spark.sql("""select Name,
                                 Age,
                                 explode_outer(split(Education,",")) as Qualification
                                 from final""")
df_explode_outer.show(truncate=False)
df_explode_outer.printSchema()
o/p:
======
+-----+---+-------------+
|Name |Age|Qualification|
+-----+---+-------------+
|Azar |25 |MBA          |
|Azar |25 |BE           |
|Azar |25 |BSC          |
|Hari |32 |null         |
|Kumar|35 |ME           |
|Kumar|35 |BE           |
|Kumar|35 |Diploma      |
+-----+---+-------------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Qualification: string (nullable = true)

Conclusion: From above we conclude that explode_outer() tackle null values properly, it include null values.

iii. Use of posexplode_outer():
===============================
a. Using df():
================
df_posexplode_outer = education_df.select(col("*"),posexplode_outer(split(col("Education"),",")))\
               .drop(col("Education"))

df_posexplode_outer.show(truncate=False)
df_posexplode_outer.printSchema()

b. Using sparksql():
======================
df_posexplode_outer = spark.sql("""select Name,
                                 Age,
                                 posexplode_outer(split(Education,",")) as (pos,Qualification)
                                 from final""")
df_posexplode_outer.show(truncate=False)
df_posexplode_outer.printSchema()
o/p:
======
+-----+---+----+-------------+
|Name |Age|pos |Qualification|
+-----+---+----+-------------+
|Azar |25 |0   |MBA          |
|Azar |25 |1   |BE           |
|Azar |25 |2   |BSC          |
|Hari |32 |null|null         |
|Kumar|35 |0   |ME           |
|Kumar|35 |1   |BE           |
|Kumar|35 |2   |Diploma      |
+-----+---+----+-------------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- pos: integer (nullable = true)
 |-- Qualification: string (nullable = true)

Conclusion: 
================
i. From above we conclude that posexplode_outer() tackle null values properly, it include null values.
ii. It gives position/indexes to each row in a df.
iii. It does not work with (.withColumn()).

🔥 Key Differences:
=======================
Function	       Handles NULL	      Returns Index
explode()	        ❌ No	               ❌ No
explode_outer()	    ✅ Yes	               ❌ No
posexplode_outer()	✅ Yes	               ✅ Yes


25. Pyspark/sparksql:
=========================
i/p:
========
+----+------------+
|name|phone       |
+----+------------+
|ABC |040-20215632|
|XYZ |044-23651023|
|PQR |086-1245678 |
+----+------------+

o/p:
=======
+----+--------+--------+
|name|std_code|landline|
+----+--------+--------+
|ABC |040     |20215632|
|XYZ |044     |23651023|
|PQR |086     |1245678 |
+----+--------+--------+
solution:
============
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark

phone_schema_prog = StructType([\
                          StructField("name",StringType(),True),\
                          StructField("phone",StringType(),True)])

phone_schema_ddl = "name string,phone string"

phone_data = [("ABC","040-20215632"),\
              ("XYZ","044-23651023"),\
             ("PQR","086-1245678")]

phone_df = spark.createDataFrame(data=phone_data,schema=phone_schema_prog)
phone_df.show(truncate=False)
phone_df.printSchema()
o/p:
========
+----+------------+
|name|phone       |
+----+------------+
|ABC |040-20215632|
|XYZ |044-23651023|
|PQR |086-1245678 |
+----+------------+

root
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)

phone_df.createOrReplaceTempView("split_final")

i.Approach 1st using df():
=====================================
df_transformed = phone_df.withColumn("std_code",split(col("phone"),"-")[0])\
                         .withColumn("landline",split(col("phone"),"-")[1])\
                         .drop(col("phone"))

df_transformed.show(truncate=False)
df_transformed.printSchema()

ii. Approach 2nd using sparksql:
-===================================
df_transformed = spark.sql("""select name,split(phone,'-')[0] as std_code,split(phone,'-')[1] as landline
                              from split_final
                            """)
df_transformed.show(truncate=False)
df_transformed.printSchema()
o/p:
========
+----+--------+--------+
|name|std_code|landline|
+----+--------+--------+
|ABC |040     |20215632|
|XYZ |044     |23651023|
|PQR |086     |1245678 |
+----+--------+--------+

root
 |-- name: string (nullable = true)
 |-- std_code: string (nullable = true)
 |-- landline: string (nullable = true)


26. Pyspark/sparksql code:
===================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark
o/p:
====
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

ddl_schema = "col1 int,value string"
data = [(1,"a,b,c"),\
        (2,"d,e,f")]

df = spark.createDataFrame(data,ddl_schema)
df.show(truncate=False)
df.printSchema()
o/p:
======
+----+-----+
|col1|value|
+----+-----+
|1   |a,b,c|
|2   |d,e,f|
+----+-----+

root
 |-- col1: integer (nullable = true)
 |-- value: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Using df():
=====================
df_final = df.withColumn("col2",split(col("value"),",")[0])\
             .withColumn("col3",split(col("value"),",")[1])\
             .withColumn("col4",split(col("value"),",")[2])\
             .drop(col("value"))

df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+----+----+----+----+
|col1|col2|col3|col4|
+----+----+----+----+
|1   |a   |b   |c   |
|2   |d   |e   |f   |
+----+----+----+----+

root
 |-- col1: integer (nullable = true)
 |-- col2: string (nullable = true)
 |-- col3: string (nullable = true)
 |-- col4: string (nullable = true)

ii. Using sparksql:
==========================
df_final = spark.sql("""
select 
    col1,
    split(value, ',')[0] as col2,
    split(value, ',')[1] as col3,
    split(value, ',')[2] as col4
from practice
""")

df_final.show(truncate=False)
df_final.printSchema()
o/p:
========
+----+----+----+----+
|col1|col2|col3|col4|
+----+----+----+----+
|1   |a   |b   |c   |
|2   |d   |e   |f   |
+----+----+----+----+

root
 |-- col1: integer (nullable = true)
 |-- col2: string (nullable = true)
 |-- col3: string (nullable = true)
 |-- col4: string (nullable = true)


27. Pyspark/sparksql code to create Arraytype() column:
==============================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
spark

o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [(1,"Sagar",[23,34,10]),\
        (2,"Alex",[40,60,20])]

schema = "Id int,Name string,Marks array<int>"

df = spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()
o/p:
=======
+---+-----+------------+
|Id |Name |Marks       |
+---+-----+------------+
|1  |Sagar|[23, 34, 10]|
|2  |Alex |[40, 60, 20]|
+---+-----+------------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Marks: array (nullable = true)
 |    |-- element: integer (containsNull = true)

df.createOrReplaceTempView("practice")

i. using df():
======================================
a. df_final = df.select(col("Id"),col("Name"),explode(col("Marks")).alias("Marks"))
df_final.show(truncate=False)
df_final.printSchema()


b. df_final = df.withColumn("Marks",explode(col("Marks")))\
             .select(col("Id"),col("Name"),col("Marks"))
df_final.show(truncate=False)
df_final.printSchema()


ii.  using sparksql:
=======================================
df_final = spark.sql("select Id,Name,explode(Marks) as Marks from practice")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=======
+---+-----+-----+
|Id |Name |Marks|
+---+-----+-----+
|1  |Sagar|23   |
|1  |Sagar|34   |
|1  |Sagar|10   |
|2  |Alex |40   |
|2  |Alex |60   |
|2  |Alex |20   |
+---+-----+-----+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Marks: integer (nullable = true)

Find total marks for each student:
==========================================
i. Using df():
=====================
df_total = df_final.groupBy(col("Id"),col("Name"))\
                   .agg(sum(col("Marks")).alias("total_marks"))

df_total.show(truncate=False)
df_total.printSchema()

ii. Using sparksql:
=======================
df_final.createOrReplaceTempView("total")
df_total = spark.sql("""select Id,Name,sum(Marks) as total_marks
                      from total
                     group by Id,Name
                     """)
                     
df_total.show(truncate=False)
df_total.printSchema()
o/p:
========
+---+-----+-----------+
|Id |Name |total_marks|
+---+-----+-----------+
|2  |Alex |120        |
|1  |Sagar|67         |
+---+-----+-----------+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- total_marks: long (nullable = true)


Find highest marks for each student:
==========================================
i. Using df():
===========================
winspec = Window.partitionBy(col("Id"),col("Name"))\
                .orderBy(col("Marks").desc())

df_highest_marks = df_final.withColumn("dnsk",dense_rank().over(winspec))\
                     .filter(col("dnsk")==1)\
                     .drop(col("dnsk"))

df_highest_marks.show(truncate=False)
df_highest_marks.printSchema()

ii. Using sparksql:
============================
df_highest_marks = spark.sql("""With cte as(
                                 select Id,Name,Marks,dense_rank() over(partition by Id,Name order by Marks desc) as dnsk
                                 from total)
                                 select Id,Name,Marks from cte where dnsk=1
                                 """)
df_highest_marks.show(truncate=False)
df_highest_marks.printSchema()
o/p:
==========
+---+-----+-----+
|Id |Name |Marks|
+---+-----+-----+
|2  |Alex |60   |
|1  |Sagar|34   |
+---+-----+-----+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Marks: integer (nullable = true)


28. How to combine many lists to form a pyspark df:
========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

names = ['Alice','Bob','Charlie']
ages = [30,25,35]
cities = ['New York','Los Angeles','Chicago']

combined_data = list(zip(names,ages,cities))
print(type(combined_data))
print(combined_data)
o/p:'
=========
<class 'list'>
[('Alice', 30, 'New York'), ('Bob', 25, 'Los Angeles'), ('Charlie', 35, 'Chicago')]

combined_schema_prog = StructType([\
                                  StructField("Name",StringType(),True),\
                                  StructField("Ages",IntegerType(),True),\
                                  StructField("Cities",StringType(),True)])

combined_schema_ddl = "Name string,Ages int,Cities string"

df = spark.createDataFrame(data=combined_data,schema=combined_schema_prog)
df.show(truncate=False)
df.printSchema()
o/p:
=========
+-------+----+-----------+
|Name   |Ages|Cities     |
+-------+----+-----------+
|Alice  |30  |New York   |
|Bob    |25  |Los Angeles|
|Charlie|35  |Chicago    |
+-------+----+-----------+

root
 |-- Name: string (nullable = true)
 |-- Ages: integer (nullable = true)
 |-- Cities: string (nullable = true)


29. Pyspark/spark sql coding problem:
============================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/retail_db
o/p:
=======
Found 9 items
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/categories
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/customers
drwxr-xr-x   - itv005857 supergroup          0 2023-07-06 13:59 /public/trendytech/retail_db/customersnew
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/departments
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/order_items
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 16:18 /public/trendytech/retail_db/orders
drwxr-xr-x   - itv005857 supergroup          0 2023-07-06 14:45 /public/trendytech/retail_db/ordersnew
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/products
-rw-r--r--   3 itv005857 supergroup       4965 2023-04-26 16:47 /public/trendytech/retail_db/wordcount.rtf

! hadoop fs -ls /public/trendytech/retail_db/products
o/p:
========
Found 1 items
-rw-r--r--   3 itv005857 supergroup     174155 2023-04-26 16:47 /public/trendytech/retail_db/products/part-00000

! hadoop fs -cat /public/trendytech/retail_db/products/part-00000 | head
o/p:
=======
1,2,Quest Q64 10 FT. x 10 FT. Slant Leg Instant U,,59.98,http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy
2,2,Under Armour Men's Highlight MC Football Clea,,129.99,http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat
3,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
4,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
5,2,Riddell Youth Revolution Speed Custom Footbal,,199.99,http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet
6,2,Jordan Men's VI Retro TD Football Cleat,,134.99,http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat
7,2,Schutt Youth Recruit Hybrid Custom Football H,,99.99,http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014
8,2,Nike Men's Vapor Carbon Elite TD Football Cle,,129.99,http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat
9,2,Nike Adult Vapor Jet 3.0 Receiver Gloves,,50.0,http://images.acmesports.sports/Nike+Adult+Vapor+Jet+3.0+Receiver+Gloves
10,2,Under Armour Men's Highlight MC Football Clea,,129.99,http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat
cat: Unable to write to output stream.

! hadoop fs -head /public/trendytech/retail_db/products/part-00000 
o/p:
===========
1,2,Quest Q64 10 FT. x 10 FT. Slant Leg Instant U,,59.98,http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy
2,2,Under Armour Men's Highlight MC Football Clea,,129.99,http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat
3,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
4,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
5,2,Riddell Youth Revolution Speed Custom Footbal,,199.99,http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet
6,2,Jordan Men's VI Retro TD Football Cleat,,134.99,http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat
7,2,Schutt Youth Recruit Hybrid Custom Football H,,99.99,http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014
8,2,Nike Men's Vapor Carbon Elite TD Football C

product_ddl_schema = "product_id int,product_category_id int,product_name string,product_description string,product_price float,product_image string"
product_df = spark.read.format("csv")\
                  .schema(product_ddl_schema)\
                  .option("sep",",")\
                  .option("path","/public/trendytech/retail_db/products/part-00000")\
                  .load()

product_df.show(truncate=False)
product_df.printSchema()
o/p:
=========
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+
|product_id|product_category_id|product_name                                 |product_description|product_price|product_image                                                                                   |
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+
|1         |2                  |Quest Q64 10 FT. x 10 FT. Slant Leg Instant U|null               |59.98        |http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy           |
|2         |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|3         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|4         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|5         |2                  |Riddell Youth Revolution Speed Custom Footbal|null               |199.99       |http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet           |
|6         |2                  |Jordan Men's VI Retro TD Football Cleat      |null               |134.99       |http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat                       |
|7         |2                  |Schutt Youth Recruit Hybrid Custom Football H|null               |99.99        |http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014         |
|8         |2                  |Nike Men's Vapor Carbon Elite TD Football Cle|null               |129.99       |http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat               |
|9         |2                  |Nike Adult Vapor Jet 3.0 Receiver Gloves     |null               |50.0         |http://images.acmesports.sports/Nike+Adult+Vapor+Jet+3.0+Receiver+Gloves                        |
|10        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|11        |2                  |Fitness Gear 300 lb Olympic Weight Set       |null               |209.99       |http://images.acmesports.sports/Fitness+Gear+300+lb+Olympic+Weight+Set                          |
|12        |2                  |Under Armour Men's Highlight MC Alter Ego Fla|null               |139.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Alter+Ego+Flash+Football...   |
|13        |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|14        |2                  |Quik Shade Summit SX170 10 FT. x 10 FT. Canop|null               |199.99       |http://images.acmesports.sports/Quik+Shade+Summit+SX170+10+FT.+x+10+FT.+Canopy                  |
|15        |2                  |Under Armour Kids' Highlight RM Alter Ego Sup|null               |59.99        |http://images.acmesports.sports/Under+Armour+Kids%27+Highlight+RM+Alter+Ego+Superman+Football...|
|16        |2                  |Riddell Youth 360 Custom Football Helmet     |null               |299.99       |http://images.acmesports.sports/Riddell+Youth+360+Custom+Football+Helmet                        |
|17        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|18        |2                  |Reebok Men's Full Zip Training Jacket        |null               |29.97        |http://images.acmesports.sports/Reebok+Men%27s+Full+Zip+Training+Jacket                         |
|19        |2                  |Nike Men's Fingertrap Max Training Shoe      |null               |124.99       |http://images.acmesports.sports/Nike+Men%27s+Fingertrap+Max+Training+Shoe                       |
|20        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+
only showing top 20 rows

root
 |-- product_id: integer (nullable = true)
 |-- product_category_id: integer (nullable = true)
 |-- product_name: string (nullable = true)
 |-- product_description: string (nullable = true)
 |-- product_price: float (nullable = true)
 |-- product_image: string (nullable = true)


product_df.createOrReplaceTempView("practice")

i. Increase the product price by 120 percent:
====================================================
a. Using df():
=======================
i. product_new_df = product_df.withColumn("product_price",(col("product_price")*1.2))\
                           .select(col("*"))

product_new_df.show(truncate=False)
product_new_df.printSchema()

ii. product_new_df = product_df.withColumn("product_price",expr("product_price*1.2"))\
                           .select(col("*"))

product_new_df.show(truncate=False)
product_new_df.printSchema()

iii. product_new_df = product_df.selectExpr("product_id","product_category_id","product_name","product_description","product_price*1.2 as product_price","product_image")
                           

product_new_df.show(truncate=False)
product_new_df.printSchema()

b. Using sparksql:
================================
product_new_df = spark.sql("""select product_id,product_category_id,product_name,product_description,(product_price*1.2) as product_price,
                              product_image from practice
                              """)

product_new_df.show(truncate=False)
product_new_df.printSchema()
o/p:
=================
+----------+-------------------+---------------------------------------------+-------------------+------------------+------------------------------------------------------------------------------------------------+
|product_id|product_category_id|product_name                                 |product_description|product_price     |product_image                                                                                   |
+----------+-------------------+---------------------------------------------+-------------------+------------------+------------------------------------------------------------------------------------------------+
|1         |2                  |Quest Q64 10 FT. x 10 FT. Slant Leg Instant U|null               |71.97599945068359 |http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy           |
|2         |2                  |Under Armour Men's Highlight MC Football Clea|null               |155.98800659179688|http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|3         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |107.98799743652343|http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|4         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |107.98799743652343|http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|5         |2                  |Riddell Youth Revolution Speed Custom Footbal|null               |239.98800659179688|http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet           |
|6         |2                  |Jordan Men's VI Retro TD Football Cleat      |null               |161.98800659179688|http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat                       |
|7         |2                  |Schutt Youth Recruit Hybrid Custom Football H|null               |119.98799743652343|http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014         |
|8         |2                  |Nike Men's Vapor Carbon Elite TD Football Cle|null               |155.98800659179688|http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat               |
|9         |2                  |Nike Adult Vapor Jet 3.0 Receiver Gloves     |null               |60.0              |http://images.acmesports.sports/Nike+Adult+Vapor+Jet+3.0+Receiver+Gloves                        |
|10        |2                  |Under Armour Men's Highlight MC Football Clea|null               |155.98800659179688|http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|11        |2                  |Fitness Gear 300 lb Olympic Weight Set       |null               |251.98800659179688|http://images.acmesports.sports/Fitness+Gear+300+lb+Olympic+Weight+Set                          |
|12        |2                  |Under Armour Men's Highlight MC Alter Ego Fla|null               |167.98800659179688|http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Alter+Ego+Flash+Football...   |
|13        |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |107.98799743652343|http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |
|14        |2                  |Quik Shade Summit SX170 10 FT. x 10 FT. Canop|null               |239.98800659179688|http://images.acmesports.sports/Quik+Shade+Summit+SX170+10+FT.+x+10+FT.+Canopy                  |
|15        |2                  |Under Armour Kids' Highlight RM Alter Ego Sup|null               |71.98800201416016 |http://images.acmesports.sports/Under+Armour+Kids%27+Highlight+RM+Alter+Ego+Superman+Football...|
|16        |2                  |Riddell Youth 360 Custom Football Helmet     |null               |359.98798828125   |http://images.acmesports.sports/Riddell+Youth+360+Custom+Football+Helmet                        |
|17        |2                  |Under Armour Men's Highlight MC Football Clea|null               |155.98800659179688|http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
|18        |2                  |Reebok Men's Full Zip Training Jacket        |null               |35.96399917602539 |http://images.acmesports.sports/Reebok+Men%27s+Full+Zip+Training+Jacket                         |
|19        |2                  |Nike Men's Fingertrap Max Training Shoe      |null               |149.98799743652344|http://images.acmesports.sports/Nike+Men%27s+Fingertrap+Max+Training+Shoe                       |
|20        |2                  |Under Armour Men's Highlight MC Football Clea|null               |155.98800659179688|http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |
+----------+-------------------+---------------------------------------------+-------------------+------------------+------------------------------------------------------------------------------------------------+
only showing top 20 rows

root
 |-- product_id: integer (nullable = true)
 |-- product_category_id: integer (nullable = true)
 |-- product_name: string (nullable = true)
 |-- product_description: string (nullable = true)
 |-- product_price: double (nullable = true)
 |-- product_image: string (nullable = true)


ii. Want to increase the price of product_name-:
i. Nike by 20%
ii. Armour by 10%
iii. other by 0%
==============================================================
a. Using df():
====================
i. product_new_df1 = product_df.selectExpr("*",
    """CASE 
           WHEN product_name LIKE '%Nike%' THEN product_price * 0.2
           WHEN product_name LIKE '%Armour%' THEN product_price * 0.1
           ELSE product_price 
       END AS updated_price"""
)


product_new_df1.show(truncate=False)
product_new_df1.printSchema()


ii. product_new_df1 = product_df.withColumn("updated_price",
   expr("""CASE 
           WHEN product_name LIKE '%Nike%' THEN product_price * 0.2
           WHEN product_name LIKE '%Armour%' THEN product_price * 0.1
           ELSE product_price 
       END""")
)


product_new_df1.show(truncate=False)
product_new_df1.printSchema()

iii. product_new_df1 = product_df.withColumn(
    "updated_price",
    when(col("product_name").like("%Nike%"), col("product_price") * 0.2)
    .when(col("product_name").like("%Armour%"), col("product_price") * 0.1)
    .otherwise(col("product_price"))
)

product_new_df1.show(truncate=False)
product_new_df1.printSchema()

b. Using sparksql:
==============================
product_new_df1 = spark.sql("""
SELECT *, 
    CASE 
        WHEN product_name LIKE '%NIKE%' THEN product_price * 0.2
        WHEN product_name LIKE '%Armour%' THEN product_price * 0.1
        ELSE product_price
    END AS updated_price
FROM practice
""")

product_new_df1.show(truncate=False)
product_new_df1.printSchema()
o/p:
================
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+------------------+
|product_id|product_category_id|product_name                                 |product_description|product_price|product_image                                                                                   |updated_price     |
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+------------------+
|1         |2                  |Quest Q64 10 FT. x 10 FT. Slant Leg Instant U|null               |59.98        |http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy           |59.97999954223633 |
|2         |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |12.999000549316406|
|3         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |8.998999786376954 |
|4         |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |8.998999786376954 |
|5         |2                  |Riddell Youth Revolution Speed Custom Footbal|null               |199.99       |http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet           |199.99000549316406|
|6         |2                  |Jordan Men's VI Retro TD Football Cleat      |null               |134.99       |http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat                       |134.99000549316406|
|7         |2                  |Schutt Youth Recruit Hybrid Custom Football H|null               |99.99        |http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014         |99.98999786376953 |
|8         |2                  |Nike Men's Vapor Carbon Elite TD Football Cle|null               |129.99       |http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat               |129.99000549316406|
|9         |2                  |Nike Adult Vapor Jet 3.0 Receiver Gloves     |null               |50.0         |http://images.acmesports.sports/Nike+Adult+Vapor+Jet+3.0+Receiver+Gloves                        |50.0              |
|10        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |12.999000549316406|
|11        |2                  |Fitness Gear 300 lb Olympic Weight Set       |null               |209.99       |http://images.acmesports.sports/Fitness+Gear+300+lb+Olympic+Weight+Set                          |209.99000549316406|
|12        |2                  |Under Armour Men's Highlight MC Alter Ego Fla|null               |139.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Alter+Ego+Flash+Football...   |13.999000549316406|
|13        |2                  |Under Armour Men's Renegade D Mid Football Cl|null               |89.99        |http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat              |8.998999786376954 |
|14        |2                  |Quik Shade Summit SX170 10 FT. x 10 FT. Canop|null               |199.99       |http://images.acmesports.sports/Quik+Shade+Summit+SX170+10+FT.+x+10+FT.+Canopy                  |199.99000549316406|
|15        |2                  |Under Armour Kids' Highlight RM Alter Ego Sup|null               |59.99        |http://images.acmesports.sports/Under+Armour+Kids%27+Highlight+RM+Alter+Ego+Superman+Football...|5.99900016784668  |
|16        |2                  |Riddell Youth 360 Custom Football Helmet     |null               |299.99       |http://images.acmesports.sports/Riddell+Youth+360+Custom+Football+Helmet                        |299.989990234375  |
|17        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |12.999000549316406|
|18        |2                  |Reebok Men's Full Zip Training Jacket        |null               |29.97        |http://images.acmesports.sports/Reebok+Men%27s+Full+Zip+Training+Jacket                         |29.969999313354492|
|19        |2                  |Nike Men's Fingertrap Max Training Shoe      |null               |124.99       |http://images.acmesports.sports/Nike+Men%27s+Fingertrap+Max+Training+Shoe                       |124.98999786376953|
|20        |2                  |Under Armour Men's Highlight MC Football Clea|null               |129.99       |http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat                |12.999000549316406|
+----------+-------------------+---------------------------------------------+-------------------+-------------+------------------------------------------------------------------------------------------------+------------------+
only showing top 20 rows

root
 |-- product_id: integer (nullable = true)
 |-- product_category_id: integer (nullable = true)
 |-- product_name: string (nullable = true)
 |-- product_description: string (nullable = true)
 |-- product_price: float (nullable = true)
 |-- product_image: string (nullable = true)
 |-- updated_price: double (nullable = true)


30. Pyspark sparksql coding problem:
====================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/retail_db
o/p:
==========
Found 9 items
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/categories
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/customers
drwxr-xr-x   - itv005857 supergroup          0 2023-07-06 13:59 /public/trendytech/retail_db/customersnew
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/departments
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/order_items
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 16:18 /public/trendytech/retail_db/orders
drwxr-xr-x   - itv005857 supergroup          0 2023-07-06 14:45 /public/trendytech/retail_db/ordersnew
drwxr-xr-x   - itv005857 supergroup          0 2023-04-26 16:47 /public/trendytech/retail_db/products
-rw-r--r--   3 itv005857 supergroup       4965 2023-04-26 16:47 /public/trendytech/retail_db/wordcount.rtf

! hadoop fs -ls /public/trendytech/retail_db/order_items
o/p:
===========
Found 1 items
-rw-r--r--   3 itv005857 supergroup    5408880 2023-04-26 16:47 /public/trendytech/retail_db/order_items/part-00000

! hadoop fs -cat /public/trendytech/retail_db/order_items/part-00000 |head
o/p:
==========
1,1,957,1,299.98,299.98
2,2,1073,1,199.99,199.99
3,2,502,5,250.0,50.0
4,2,403,1,129.99,129.99
5,4,897,2,49.98,24.99
6,4,365,5,299.95,59.99
7,4,502,3,150.0,50.0
8,4,1014,4,199.92,49.98
9,5,957,1,299.98,299.98
10,5,365,5,299.95,59.99
cat: Unable to write to output stream.

orders_item_ddl = "order_item_id int,order_id int,product_id long,quantity int,subtotal float,product_price float "
orders_item_prog = StructType([\
                   StructField("order_item_id",IntegerType(),True),\
                   StructField("order_id",IntegerType(),True),\
                   StructField("product_id",LongType(),True),\
                   StructField("quantity",IntegerType(),True),\
                   StructField("subtotal",FloatType(),True),\
                   StructField("product_price",FloatType(),True)])

raw_df = spark.read.format("csv")\
                   .schema(orders_item_ddl)\
                   .option("sep",",")\
                   .option("path","/public/trendytech/retail_db/order_items/part-00000")\
                   .load()

raw_df.show(truncate=False)
raw_df.printSchema()
o/p:
===========
+-------------+--------+----------+--------+--------+-------------+
|order_item_id|order_id|product_id|quantity|subtotal|product_price|
+-------------+--------+----------+--------+--------+-------------+
|1            |1       |957       |1       |299.98  |299.98       |
|2            |2       |1073      |1       |199.99  |199.99       |
|3            |2       |502       |5       |250.0   |50.0         |
|4            |2       |403       |1       |129.99  |129.99       |
|5            |4       |897       |2       |49.98   |24.99        |
|6            |4       |365       |5       |299.95  |59.99        |
|7            |4       |502       |3       |150.0   |50.0         |
|8            |4       |1014      |4       |199.92  |49.98        |
|9            |5       |957       |1       |299.98  |299.98       |
|10           |5       |365       |5       |299.95  |59.99        |
|11           |5       |1014      |2       |99.96   |49.98        |
|12           |5       |957       |1       |299.98  |299.98       |
|13           |5       |403       |1       |129.99  |129.99       |
|14           |7       |1073      |1       |199.99  |199.99       |
|15           |7       |957       |1       |299.98  |299.98       |
|16           |7       |926       |5       |79.95   |15.99        |
|17           |8       |365       |3       |179.97  |59.99        |
|18           |8       |365       |5       |299.95  |59.99        |
|19           |8       |1014      |4       |199.92  |49.98        |
|20           |8       |502       |1       |50.0    |50.0         |
+-------------+--------+----------+--------+--------+-------------+
only showing top 20 rows

root
 |-- order_item_id: integer (nullable = true)
 |-- order_id: integer (nullable = true)
 |-- product_id: long (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- subtotal: float (nullable = true)
 |-- product_price: float (nullable = true)

raw_df.createOrReplaceTempView("practice")

i. Remove the subtotal column:
=======================================
a. new_df = raw_df.drop(col("subtotal"))
new_df.show(truncate=False)
new_df.printSchema()
o/p:
===============
+-------------+--------+----------+--------+-------------+
|order_item_id|order_id|product_id|quantity|product_price|
+-------------+--------+----------+--------+-------------+
|1            |1       |957       |1       |299.98       |
|2            |2       |1073      |1       |199.99       |
|3            |2       |502       |5       |50.0         |
|4            |2       |403       |1       |129.99       |
|5            |4       |897       |2       |24.99        |
|6            |4       |365       |5       |59.99        |
|7            |4       |502       |3       |50.0         |
|8            |4       |1014      |4       |49.98        |
|9            |5       |957       |1       |299.98       |
|10           |5       |365       |5       |59.99        |
|11           |5       |1014      |2       |49.98        |
|12           |5       |957       |1       |299.98       |
|13           |5       |403       |1       |129.99       |
|14           |7       |1073      |1       |199.99       |
|15           |7       |957       |1       |299.98       |
|16           |7       |926       |5       |15.99        |
|17           |8       |365       |3       |59.99        |
|18           |8       |365       |5       |59.99        |
|19           |8       |1014      |4       |49.98        |
|20           |8       |502       |1       |50.0         |
+-------------+--------+----------+--------+-------------+
only showing top 20 rows

root
 |-- order_item_id: integer (nullable = true)
 |-- order_id: integer (nullable = true)
 |-- product_id: long (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- product_price: float (nullable = true)

ii. Generate new column subtotal:
==========================================
Using df():
======================
a. new_df1 = new_df.withColumn("subtotal",col("quantity")*col("product_price"))\
      .select(col("*"))

new_df1.show(truncate=False)
new_df1.printSchema()

b. new_df1 = new_df.withColumn("subtotal",expr("quantity*product_price"))\
                .select("*")

new_df1.show(truncate=False)
new_df1.printSchema()

c. new_df1 = new_df.selectExpr("*","quantity*product_price as subtotal")
new_df1.show(truncate=False)
new_df1.printSchema()

Using sparksql():
============================
new_df1 = spark.sql("select *,(quantity*product_price) as subtotal from practice")
new_df1.show(truncate=False)
new_df1.printSchema()
o/p:
=========
+-------------+--------+----------+--------+--------+-------------+--------+
|order_item_id|order_id|product_id|quantity|subtotal|product_price|subtotal|
+-------------+--------+----------+--------+--------+-------------+--------+
|1            |1       |957       |1       |299.98  |299.98       |299.98  |
|2            |2       |1073      |1       |199.99  |199.99       |199.99  |
|3            |2       |502       |5       |250.0   |50.0         |250.0   |
|4            |2       |403       |1       |129.99  |129.99       |129.99  |
|5            |4       |897       |2       |49.98   |24.99        |49.98   |
|6            |4       |365       |5       |299.95  |59.99        |299.95  |
|7            |4       |502       |3       |150.0   |50.0         |150.0   |
|8            |4       |1014      |4       |199.92  |49.98        |199.92  |
|9            |5       |957       |1       |299.98  |299.98       |299.98  |
|10           |5       |365       |5       |299.95  |59.99        |299.95  |
|11           |5       |1014      |2       |99.96   |49.98        |99.96   |
|12           |5       |957       |1       |299.98  |299.98       |299.98  |
|13           |5       |403       |1       |129.99  |129.99       |129.99  |
|14           |7       |1073      |1       |199.99  |199.99       |199.99  |
|15           |7       |957       |1       |299.98  |299.98       |299.98  |
|16           |7       |926       |5       |79.95   |15.99        |79.95   |
|17           |8       |365       |3       |179.97  |59.99        |179.97  |
|18           |8       |365       |5       |299.95  |59.99        |299.95  |
|19           |8       |1014      |4       |199.92  |49.98        |199.92  |
|20           |8       |502       |1       |50.0    |50.0         |50.0    |
+-------------+--------+----------+--------+--------+-------------+--------+
only showing top 20 rows

root
 |-- order_item_id: integer (nullable = true)
 |-- order_id: integer (nullable = true)
 |-- product_id: long (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- subtotal: float (nullable = true)
 |-- product_price: float (nullable = true)
 |-- subtotal: float (nullable = true)


31. Week 3rd Assignment Solution:
==============================================
1. Write PySpark code to create a new dataframe with the data given below
having 2 columns (‘season’) and (‘windspeed’).
[ Datatypes of the column names can be inferred ]
# Data
[("Spring", 12.3),
("Summer", 10.5),
("Autumn", 8.2),
("Winter", 15.1)]

Solution:
=====================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

schema = ['season','windspeed']

data = [("Spring",12.3),\
        ("Summer",10.5),\
        ("Autumn",8.2),\
        ("Winter",15.1)]
df = spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()


df = spark.createDataFrame(data).toDF(*schema)
df.show(truncate=False)
df.printSchema()

df = spark.createDataFrame(data).toDF("season","windspeed")
df.show(truncate=False)
df.printSchema()
o/p:
=========
+------+---------+
|season|windspeed|
+------+---------+
|Spring|12.3     |
|Summer|10.5     |
|Autumn|8.2      |
|Winter|15.1     |
+------+---------+

root
 |-- season: string (nullable = true)
 |-- windspeed: double (nullable = true)

schema_ddl = "season string,winspeed float"

schema_prog = StructType([\
              StructField("season",StringType(),True),\
              StructField("windspeed",FloatType(),True)])

df = spark.createDataFrame(data=data,schema=schema_ddl)
df.show(truncate=False)
df.printSchema()

df = spark.createDataFrame(data=data,schema=schema_prog)
df.show(truncate=False)
df.printSchema()
o/p:
============
+------+---------+
|season|windspeed|
+------+---------+
|Spring|12.3     |
|Summer|10.5     |
|Autumn|8.2      |
|Winter|15.1     |
+------+---------+

root
 |-- season: string (nullable = true)
 |-- windspeed: float (nullable = true)


2. Consider the library management dataset located at the following path
(/public/trendytech/datasets/library_data.json). Using PySpark, load the
data into a Dataframe and enforce schema using StructType.
=====================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets/library_data.json
o/p:
========
-rw-r--r--   3 itv005857 supergroup        925 2023-05-23 13:05 /public/trendytech/datasets/library_data.json

! hadoop fs -cat /public/trendytech/datasets/library_data.json | head
o/p:
========
{"library_name": "Central Library","location": "City Center","books": [{"book_id": "B001","book_name": "The Great Gatsby","author": "F. Scott Fitzgerald","copies_available": 5},{"book_id": "B002","book_name": "To Kill a Mockingbird","author": "Harper Lee","copies_available": 3}],"members": [{"member_id": "M001","member_name": "John Smith","age": 28,"books_borrowed": ["B001"]},{"member_id": "M002","member_name": "Emma Johnson","age": 35,"books_borrowed": []}]},
{"library_name": "Community Library","location": "Suburb","books": [{"book_id": "B003","book_name": "1984","author": "George Orwell","copies_available": 2},{"book_id": "B004","book_name": "Pride and Prejudice","author": "Jane Austen","copies_available": 4}],"members": [{"member_id": "M003","member_name": "Michael Brown","age": 42,"books_borrowed": ["B003","B004"]},{"member_id": "M004","member_name": "Sophia Davis","age": 31,"books_borrowed": ["B004"]}]}

json_schema_ddl = """
library_name STRING,
location STRING,
books ARRAY<STRUCT<
    book_id: STRING,
    book_name: STRING,
    author: STRING,
    copies_available: INT
>>,
members ARRAY<STRUCT<
    member_id: STRING,
    member_name: STRING,
    age: INT,
    books_borrowed: ARRAY<STRING>
>>
"""


schema_programmatic = StructType([
    
    StructField("library_name", StringType(), True),
    StructField("location", StringType(), True),

    StructField("books", ArrayType(
        StructType([
            StructField("book_id", StringType(), True),
            StructField("book_name", StringType(), True),
            StructField("author", StringType(), True),
            StructField("copies_available", IntegerType(), True)
        ])
    ), True),

    StructField("members", ArrayType(
        StructType([
            StructField("member_id", StringType(), True),
            StructField("member_name", StringType(), True),
            StructField("age", IntegerType(), True),
            StructField("books_borrowed", ArrayType(StringType()), True)
        ])
    ), True)

])

df_json_ddl = spark.read.format("json")\
               .schema(json_schema_ddl)\
               .option("path","/public/trendytech/datasets/library_data.json")\
               .load()

df_json_ddl.show(truncate=False)
df_json_ddl.printSchema()
o/p:
==========
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
|library_name     |location   |books                                                                                           |members                                                                    |
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
|Central Library  |City Center|[{B001, The Great Gatsby, F. Scott Fitzgerald, 5}, {B002, To Kill a Mockingbird, Harper Lee, 3}]|[{M001, John Smith, 28, [B001]}, {M002, Emma Johnson, 35, []}]             |
|Community Library|Suburb     |[{B003, 1984, George Orwell, 2}, {B004, Pride and Prejudice, Jane Austen, 4}]                   |[{M003, Michael Brown, 42, [B003, B004]}, {M004, Sophia Davis, 31, [B004]}]|
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

root
 |-- library_name: string (nullable = true)
 |-- location: string (nullable = true)
 |-- books: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- book_id: string (nullable = true)
 |    |    |-- book_name: string (nullable = true)
 |    |    |-- author: string (nullable = true)
 |    |    |-- copies_available: integer (nullable = true)
 |-- members: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- member_id: string (nullable = true)
 |    |    |-- member_name: string (nullable = true)
 |    |    |-- age: integer (nullable = true)
 |    |    |-- books_borrowed: array (nullable = true)
 |    |    |    |-- element: string (containsNull = true)


df_json_prog = spark.read.format("json")\
               .schema(schema_programmatic)\
               .option("path","/public/trendytech/datasets/library_data.json")\
               .load()

df_json_prog.show(truncate=False)
df_json_prog.printSchema()
o/p:
===========
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
|library_name     |location   |books                                                                                           |members                                                                    |
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
|Central Library  |City Center|[{B001, The Great Gatsby, F. Scott Fitzgerald, 5}, {B002, To Kill a Mockingbird, Harper Lee, 3}]|[{M001, John Smith, 28, [B001]}, {M002, Emma Johnson, 35, []}]             |
|Community Library|Suburb     |[{B003, 1984, George Orwell, 2}, {B004, Pride and Prejudice, Jane Austen, 4}]                   |[{M003, Michael Brown, 42, [B003, B004]}, {M004, Sophia Davis, 31, [B004]}]|
+-----------------+-----------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

root
 |-- library_name: string (nullable = true)
 |-- location: string (nullable = true)
 |-- books: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- book_id: string (nullable = true)
 |    |    |-- book_name: string (nullable = true)
 |    |    |-- author: string (nullable = true)
 |    |    |-- copies_available: integer (nullable = true)
 |-- members: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- member_id: string (nullable = true)
 |    |    |-- member_name: string (nullable = true)
 |    |    |-- age: integer (nullable = true)
 |    |    |-- books_borrowed: array (nullable = true)
 |    |    |    |-- element: string (containsNull = true)


3. Given the dataset (/public/trendytech/datasets/train.csv), create a
Dataframe using PySpark and perform the following operations
a) Drop the columns passenger_name and age from the dataset.
b) Count the number of rows after removing duplicates of columns
train_number and ticket_number.
c) Count the number of unique train names.

Soln:
=============
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets/train.csv
o/p:
=========
-rw-r--r--   3 itv005857 supergroup        324 2023-05-23 13:04 /public/trendytech/datasets/train.csv

! hadoop fs -cat /public/trendytech/datasets/train.csv | head
o/p:
==========
train_number,train_name,seats_available,passenger_name,age,ticket_number,seat_number
123,Express,100,John,25,T123,A1
123,Express,100,Emma,30,T124,B2
456,Superfast,150,Michael,35,T125,C3
456,Superfast,150,Sophia,40,T126,D4
789,Local,50,William,28,T127,E5
789,Local,50,Sophia,32,T128,F6
789,Local,50,Oliver,45,T129,G7

schema_ddl = "train_number long,train_name string,seats_available long,passenger_name string,age integer,ticket_number string,seat_number string"
schema_prog = StructType([\
              StructField("train_number",LongType(),True),
              StructField("train_name",StringType(),True),
              StructField("seats_available",LongType(),True),
              StructField("passenger_name",StringType(),True),
              StructField("age",IntegerType(),True),
              StructField("ticket_number",StringType(),True),
              StructField("seat_number",StringType(),True),
              ])

df_raw = spark.read.format("csv")\
              .option("header",True)\
              .schema(schema_prog)\
              .option("sep",",")\
              .option("path","/public/trendytech/datasets/train.csv")\
              .load()

df_raw.show(truncate=False)
df_raw.printSchema()
o/p:
=============
+------------+----------+---------------+--------------+---+-------------+-----------+
|train_number|train_name|seats_available|passenger_name|age|ticket_number|seat_number|
+------------+----------+---------------+--------------+---+-------------+-----------+
|123         |Express   |100            |John          |25 |T123         |A1         |
|123         |Express   |100            |Emma          |30 |T124         |B2         |
|456         |Superfast |150            |Michael       |35 |T125         |C3         |
|456         |Superfast |150            |Sophia        |40 |T126         |D4         |
|789         |Local     |50             |William       |28 |T127         |E5         |
|789         |Local     |50             |Sophia        |32 |T128         |F6         |
|789         |Local     |50             |Oliver        |45 |T129         |G7         |
+------------+----------+---------------+--------------+---+-------------+-----------+

root
 |-- train_number: long (nullable = true)
 |-- train_name: string (nullable = true)
 |-- seats_available: long (nullable = true)
 |-- passenger_name: string (nullable = true)
 |-- age: integer (nullable = true)
 |-- ticket_number: string (nullable = true)
 |-- seat_number: string (nullable = true)

a) Drop the columns passenger_name and age from the dataset.
===================================================================
new_df = df_raw.drop(col("passenger_name"))\
               .drop(col("age"))
new_df.show(truncate=False)
new_df.printSchema()

new_df = df_raw.drop("passenger_name")\
               .drop("age")
new_df.show(truncate=False)
new_df.printSchema()
o/p:
==========
+------------+----------+---------------+-------------+-----------+
|train_number|train_name|seats_available|ticket_number|seat_number|
+------------+----------+---------------+-------------+-----------+
|123         |Express   |100            |T123         |A1         |
|123         |Express   |100            |T124         |B2         |
|456         |Superfast |150            |T125         |C3         |
|456         |Superfast |150            |T126         |D4         |
|789         |Local     |50             |T127         |E5         |
|789         |Local     |50             |T128         |F6         |
|789         |Local     |50             |T129         |G7         |
+------------+----------+---------------+-------------+-----------+

root
 |-- train_number: long (nullable = true)
 |-- train_name: string (nullable = true)
 |-- seats_available: long (nullable = true)
 |-- ticket_number: string (nullable = true)
 |-- seat_number: string (nullable = true)


b. Count the number of rows after removing duplicates of columns train_number and ticket_number.
=======================================================================================================
i. Using df():
=====================
new_df_duplicates = new_df.dropDuplicates(["train_number","ticket_number"])
new_df_duplicates.show(truncate=False)
new_df_duplicates.printSchema()
o/p:
=========
+------------+----------+---------------+-------------+-----------+
|train_number|train_name|seats_available|ticket_number|seat_number|
+------------+----------+---------------+-------------+-----------+
|456         |Superfast |150            |T126         |D4         |
|789         |Local     |50             |T127         |E5         |
|123         |Express   |100            |T124         |B2         |
|123         |Express   |100            |T123         |A1         |
|789         |Local     |50             |T128         |F6         |
|789         |Local     |50             |T129         |G7         |
|456         |Superfast |150            |T125         |C3         |
+------------+----------+---------------+-------------+-----------+

root
 |-- train_number: long (nullable = true)
 |-- train_name: string (nullable = true)
 |-- seats_available: long (nullable = true)
 |-- ticket_number: string (nullable = true)
 |-- seat_number: string (nullable = true)

new_df.count()
o/p:
========
7

new_df_duplicates.count()
o/p:
=========
7


ii. Using sparksql:
=========================================
new_df.createOrReplaceTempView("practice")
new_df_duplicates = spark.sql("""SELECT DISTINCT train_number,ticket_number
                                 FROM practice
                                             """)
new_df_duplicates.show(truncate=False)
new_df_duplicates.printSchema()
o/p:
=========
+------------+-------------+
|train_number|ticket_number|
+------------+-------------+
|456         |T126         |
|789         |T127         |
|123         |T124         |
|123         |T123         |
|789         |T128         |
|789         |T129         |
|456         |T125         |
+------------+-------------+

root
 |-- train_number: long (nullable = true)
 |-- ticket_number: string (nullable = true)

new_df_duplicates.count()
o/p:
========
7

new_df.count()
o/p:
==========
7

c) Count the number of unique train names.
======================================================
i. Using df(():
=======================
unique_count_df = df_raw.select(countDistinct(col("train_name")).alias("unique_count"))
unique_count_df.show(truncate=False)
unique_count_df.printSchema()

ii. sparksql:
=======================
unique_count_df = spark.sql("select count(distinct(train_name)) as unique_count from practice")
unique_count_df.show(truncate=False)
unique_count_df.printSchema()
o/p:
==========
+------------+
|unique_count|
+------------+
|3           |
+------------+

root
 |-- unique_count: long (nullable = false)

4. You are working as a Data Engineer in a large retail company. The
company has a dataset named "sales_data.json" that contains sales records
from various stores. The dataset is stored in JSON format and may have
some corrupt or malformed records due to occasional data quality issues.
Your task is to read the "sales_data.json" dataset
(/public/trendytech/datasets/sales_data.json) using PySpark, utilizing
different read modes to handle corrupt records. You need to create a
Dataframe using pyspark and perform the following operations:
1. Read the dataset using the "permissive" mode and count the number of
records read.
2. Read the dataset using the "dropmalformed" mode and display the
number of malformed records.
3. Read the dataset using the "failfast" mode

soln:
===========
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets/sales_data.json
o/p:
=========
-rw-r--r--   3 itv005857 supergroup       1602 2023-05-23 13:05 /public/trendytech/datasets/sales_data.json

! hadoop fs -cat /public/trendytech/datasets/sales_data.json | head
o/p:
========
{"store_id": 1, "product": "Apple", "quantity": 10, "revenue": 100.0}
{"store_id": 2, "product": "Banana", "quantity": 15, "revenue": 75.0}
{"store_id": 3, "product": "Orange", "quantity": 12, "revenue": 90.0}
{"store_id": 4, "product": "Mango", "quantity": 8, "revenue": 120.0}
{"store_id": 5, "product": "Grape", "quantity": 20, "revenue": 150.0}
{"store_id": 6, "product": "Watermelon", "quantity": 5, "revenue": 50.0}
{"store_id": 7, "product": "Strawberry", "quantity": 18, "revenue": 108.0}
{"store_id": 8, "product": "Pineapple", "quantity": 14, "revenue": 140.0}
{"store_id": 9, "product": "Cherry", "quantity": 7, "revenue": 105.0}
{"store_id": 10, "product": "Pear", "quantity": 9, "revenue": 81.0}

schema_ddl = "store_id integer,product string,quantity integer,revenue float"
schema_prog = StructType([\
              StructField("store_id",IntegerType(),True),\
              StructField("product",StringType(),True),\
              StructField("quantity",IntegerType(),True),\
              StructField("revenue",FloatType(),True)])

1. Read the dataset using the "permissive" mode and count the number of records read:
============================================================================================
df_json_permessive = spark.read.format("json")\
                          .schema(schema_ddl)\
                          .option("mode","PERMESSIVE")\
                          .option("path","/public/trendytech/datasets/sales_data.json")\
                          .load()

df_json_permessive.show(truncate=False)
df_json_permessive.printSchema()
o/p:
=======
+--------+----------+--------+-------+
|store_id|product   |quantity|revenue|
+--------+----------+--------+-------+
|1       |Apple     |10      |100.0  |
|2       |Banana    |15      |75.0   |
|3       |Orange    |12      |90.0   |
|4       |Mango     |8       |120.0  |
|5       |Grape     |20      |150.0  |
|6       |Watermelon|5       |50.0   |
|7       |Strawberry|18      |108.0  |
|8       |Pineapple |14      |140.0  |
|9       |Cherry    |7       |105.0  |
|10      |Pear      |9       |81.0   |
|11      |Blueberry |11      |88.0   |
|12      |Kiwi      |16      |128.0  |
|13      |Peach     |13      |91.0   |
|14      |Plum      |6       |54.0   |
|15      |Lemon     |10      |70.0   |
|16      |Raspberry |17      |136.0  |
|17      |Coconut   |4       |80.0   |
|18      |Avocado   |11      |99.0   |
|19      |Blackberry|8       |64.0   |
|20      |G         |null    |NaN    |
+--------+----------+--------+-------+
only showing top 20 rows

root
 |-- store_id: integer (nullable = true)
 |-- product: string (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- revenue: float (nullable = true)

df_json_permessive.count()
o/p:
========
22

schema_ddl_corrupt = "store_id integer,product string,quantity integer,revenue float,_corrupt_record string"
df_json_permessive = spark.read.format("json")\
                          .schema(schema_ddl_corrupt)\
                          .option("mode","PERMESSIVE")\
                          .option("columnNameOfCorruptRecord","_corrupt_record")\
                          .option("path","/public/trendytech/datasets/sales_data.json")\
                          .load()

df_json_permessive.show(truncate=False)
df_json_permessive.printSchema()
o/p:
=========
+--------+----------+--------+-------+-------------------------------------------------------------------------+
|store_id|product   |quantity|revenue|_corrupt_record                                                          |
+--------+----------+--------+-------+-------------------------------------------------------------------------+
|1       |Apple     |10      |100.0  |null                                                                     |
|2       |Banana    |15      |75.0   |null                                                                     |
|3       |Orange    |12      |90.0   |null                                                                     |
|4       |Mango     |8       |120.0  |null                                                                     |
|5       |Grape     |20      |150.0  |null                                                                     |
|6       |Watermelon|5       |50.0   |null                                                                     |
|7       |Strawberry|18      |108.0  |null                                                                     |
|8       |Pineapple |14      |140.0  |null                                                                     |
|9       |Cherry    |7       |105.0  |null                                                                     |
|10      |Pear      |9       |81.0   |null                                                                     |
|11      |Blueberry |11      |88.0   |null                                                                     |
|12      |Kiwi      |16      |128.0  |null                                                                     |
|13      |Peach     |13      |91.0   |null                                                                     |
|14      |Plum      |6       |54.0   |null                                                                     |
|15      |Lemon     |10      |70.0   |null                                                                     |
|16      |Raspberry |17      |136.0  |null                                                                     |
|17      |Coconut   |4       |80.0   |null                                                                     |
|18      |Avocado   |11      |99.0   |null                                                                     |
|19      |Blackberry|8       |64.0   |null                                                                     |
|20      |G         |null    |NaN    |{"store_id": 20, "product": "G", "quantity": "Invalid", "revenue": "NaN"}|
+--------+----------+--------+-------+-------------------------------------------------------------------------+
only showing top 20 rows

root
 |-- store_id: integer (nullable = true)
 |-- product: string (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- revenue: float (nullable = true)
 |-- _corrupt_record: string (nullable = true)

df_json_permessive.count()
o/p:
=======
22

df_json_permessive.filter(col("_corrupt_record").isNotNull()).show(truncate=False)
o/p:
=====
+--------+----------+--------+-------+------------------------------------------------------------------------------+
|store_id|product   |quantity|revenue|_corrupt_record                                                               |
+--------+----------+--------+-------+------------------------------------------------------------------------------+
|20      |G         |null    |NaN    |{"store_id": 20, "product": "G", "quantity": "Invalid", "revenue": "NaN"}     |
|null    |null      |null    |null   |{"store_id": 21, "product": "Pineapple", "quantity": 14, "revenue": 140.0     |
|22      |Watermelon|5       |null   |{"store_id": 22, "product": "Watermelon", "quantity": 5, "revenue": "Invalid"}|
+--------+----------+--------+-------+------------------------------------------------------------------------------+

df_json_permessive.filter(col("_corrupt_record").isNull()).show(truncate=False)
o/p:
========
+--------+----------+--------+-------+---------------+
|store_id|product   |quantity|revenue|_corrupt_record|
+--------+----------+--------+-------+---------------+
|1       |Apple     |10      |100.0  |null           |
|2       |Banana    |15      |75.0   |null           |
|3       |Orange    |12      |90.0   |null           |
|4       |Mango     |8       |120.0  |null           |
|5       |Grape     |20      |150.0  |null           |
|6       |Watermelon|5       |50.0   |null           |
|7       |Strawberry|18      |108.0  |null           |
|8       |Pineapple |14      |140.0  |null           |
|9       |Cherry    |7       |105.0  |null           |
|10      |Pear      |9       |81.0   |null           |
|11      |Blueberry |11      |88.0   |null           |
|12      |Kiwi      |16      |128.0  |null           |
|13      |Peach     |13      |91.0   |null           |
|14      |Plum      |6       |54.0   |null           |
|15      |Lemon     |10      |70.0   |null           |
|16      |Raspberry |17      |136.0  |null           |
|17      |Coconut   |4       |80.0   |null           |
|18      |Avocado   |11      |99.0   |null           |
|19      |Blackberry|8       |64.0   |null           |
+--------+----------+--------+-------+---------------+

2. Read the dataset using the "dropmalformed" mode and display the number of malformed records:
=======================================================================================================
df_json_dropmalformed = spark.read.format("json")\
                          .schema(schema_ddl)\
                          .option("mode","DROPMALFORMED")\
                          .option("path","/public/trendytech/datasets/sales_data.json")\
                          .load()

df_json_dropmalformed.show(truncate=False)
df_json_dropmalformed.printSchema()
o/p:
========
+--------+----------+--------+-------+
|store_id|product   |quantity|revenue|
+--------+----------+--------+-------+
|1       |Apple     |10      |100.0  |
|2       |Banana    |15      |75.0   |
|3       |Orange    |12      |90.0   |
|4       |Mango     |8       |120.0  |
|5       |Grape     |20      |150.0  |
|6       |Watermelon|5       |50.0   |
|7       |Strawberry|18      |108.0  |
|8       |Pineapple |14      |140.0  |
|9       |Cherry    |7       |105.0  |
|10      |Pear      |9       |81.0   |
|11      |Blueberry |11      |88.0   |
|12      |Kiwi      |16      |128.0  |
|13      |Peach     |13      |91.0   |
|14      |Plum      |6       |54.0   |
|15      |Lemon     |10      |70.0   |
|16      |Raspberry |17      |136.0  |
|17      |Coconut   |4       |80.0   |
|18      |Avocado   |11      |99.0   |
|19      |Blackberry|8       |64.0   |
+--------+----------+--------+-------+

root
 |-- store_id: integer (nullable = true)
 |-- product: string (nullable = true)
 |-- quantity: integer (nullable = true)
 |-- revenue: float (nullable = true)

df_json_dropmalformed.count()
o/p:
========
21

permessive_count = df_json_permessive.count()
print("No of permessive count: ",permessive_count)
o/p:
========
No of permessive count:  22

dropmalformed_count = df_json_dropmalformed.count()
print("No of dropmalformed count: ",dropmalformed_count)
o/p:
=======
No of dropmalformed count:  21

total_no_of_corrupt_record_dropmalformed = permessive_count - dropmalformed_count
print("No of corrupt record dropmalformed: ",total_no_of_corrupt_record_dropmalformed)
o/p:
=======
No of corrupt record dropmalformed:  1



3. Read the dataset using the "failfast" mode:
======================================================
df_json_failfast = spark.read.format("json")\
                          .schema(schema_ddl)\
                          .option("mode","FAILFAST")\
                          .option("path","/public/trendytech/datasets/sales_data.json")\
                          .load()

df_json_failfast.show(truncate=False)
df_json_failfast.printSchema()
o/p:
========
Malformed records are detected in record parsing. Parse Mode: FAILFAST. To process malformed records as null result, try setting the option 'mode' as 'PERMISSIVE'.

5. You have a hospital dataset with the following fields:
===============================================================================
● patient_id (integer): Unique identifier for each patient.
● admission_date (date): The date the patient was admitted to the
hospital. (MM-dd-yyyy)
● discharge_date (date): The date the patient was discharged from the
hospital. (yyyy-MM-dd)
● diagnosis (string): The diagnosed medical condition of the patient.
● doctor_id (integer): The identifier of the doctor responsible for the
patient's care.
● total_cost (float): The total cost of the hospital stay for the patient.
Using PySpark, load the data into a Dataframe and perform the following
operations on the hospital dataset
(/public/trendytech/datasets/hospital.csv):
1. Drop the "doctor_id" column from the dataset.
2. Rename the "total_cost" column to "hospital_bill".
3. Add a new column called "duration_of_stay" that represents the number
of days a patient stayed in the hospital. (hint: The duration should be
calculated as the difference between the "discharge_date" and
"admission_date" columns.)
4. Create a new column called "adjusted_total_cost" that calculates the
adjusted total cost based on the diagnosis as follows:
If the diagnosis is "Heart Attack", multiply the hospital_bill by 1.5.
If the diagnosis is "Appendicitis", multiply the hospital_bill by 1.2.
For any other diagnosis, keep the hospital_bill as it is.
5. Select the "patient_id", "diagnosis", "hospital_bill", and
"adjusted_total_cost" columns.

Solution:
=====================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets/hospital.csv
o/p:
========
-rw-r--r--   3 itv005857 supergroup       1319 2023-05-23 13:04 /public/trendytech/datasets/hospital.csv

! hadoop fs -cat /public/trendytech/datasets/hospital.csv | head
o/p:
=======
patient_id,admission_date,discharge_date,diagnosis,doctor_id,total_cost
1,01-01-2022,2022-01-10,Pneumonia,101,5000.00
2,02-05-2022,2022-02-09,Appendicitis,102,7000.00
3,03-12-2022,2022-03-18,Fractured Arm,103,3500.00
4,04-02-2022,2022-04-08,Heart Attack,104,15000.00
5,05-05-2022,2022-05-07,Influenza,105,2500.00
6,06-10-2022,2022-06-15,Appendicitis,106,8000.00
7,07-20-2022,2022-07-25,Pneumonia,107,5500.00
8,08-25-2022,2022-09-01,Heart Attack,108,20000.00
9,09-15-2022,2022-09-22,Fractured Leg,109,6000.00

patient_schema_ddl = "patient_id integer,admission_date string,discharge_date string,diagnosis string,doctor_id integer,total_cost float"
patient_schema_prog = StructType([\
                      StructField("patient_id",IntegerType(),True),\
                      StructField("admission_date",StringType(),True),\
                      StructField("discharge_date",StringType(),True),\
                      StructField("diagnosis",StringType(),True),\
                      StructField("doctor_id",IntegerType(),True),\
                      StructField("total_cost",FloatType(),True)])

patient_df = spark.read.format("csv")\
                  .option("header",True)\
                  .schema(patient_schema_prog)\
                  .option("sep",",")\
                  .option("path","/public/trendytech/datasets/hospital.csv")\
                  .load()

patient_df.show(truncate=False)
patient_df.printSchema()
o/p:
=========
+----------+--------------+--------------+-------------+---------+----------+
|patient_id|admission_date|discharge_date|diagnosis    |doctor_id|total_cost|
+----------+--------------+--------------+-------------+---------+----------+
|1         |01-01-2022    |2022-01-10    |Pneumonia    |101      |5000.0    |
|2         |02-05-2022    |2022-02-09    |Appendicitis |102      |7000.0    |
|3         |03-12-2022    |2022-03-18    |Fractured Arm|103      |3500.0    |
|4         |04-02-2022    |2022-04-08    |Heart Attack |104      |15000.0   |
|5         |05-05-2022    |2022-05-07    |Influenza    |105      |2500.0    |
|6         |06-10-2022    |2022-06-15    |Appendicitis |106      |8000.0    |
|7         |07-20-2022    |2022-07-25    |Pneumonia    |107      |5500.0    |
|8         |08-25-2022    |2022-09-01    |Heart Attack |108      |20000.0   |
|9         |09-15-2022    |2022-09-22    |Fractured Leg|109      |6000.0    |
|10        |10-05-2022    |2022-10-10    |Appendicitis |110      |7500.0    |
|11        |11-02-2022    |2022-11-05    |Influenza    |111      |2800.0    |
|12        |12-10-2022    |2022-12-18    |Pneumonia    |112      |6000.0    |
|13        |01-02-2023    |2023-01-09    |Heart Attack |113      |18000.0   |
|14        |02-14-2023    |2023-02-18    |Appendicitis |114      |7200.0    |
|15        |03-20-2023    |2023-03-28    |Fractured Arm|115      |3800.0    |
|16        |04-05-2023    |2023-04-11    |Influenza    |116      |2700.0    |
|17        |05-08-2023    |2023-05-11    |Heart Attack |117      |16000.0   |
|18        |06-15-2023    |2023-06-20    |Pneumonia    |118      |4800.0    |
|19        |07-22-2023    |2023-07-27    |Fractured Leg|119      |6500.0    |
|20        |08-10-2023    |2023-08-16    |Appendicitis |120      |7800.0    |
+----------+--------------+--------------+-------------+---------+----------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: string (nullable = true)
 |-- discharge_date: string (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- doctor_id: integer (nullable = true)
 |-- total_cost: float (nullable = true)

change the datatype of col admission_date,discharge_date:
==============================================================
new_patient_df = patient_df.withColumn("admission_date", to_date(col("admission_date"), "MM-dd-yyyy")) \
                       .withColumn("discharge_date", to_date(col("discharge_date"), "yyyy-MM-dd"))
          

new_patient_df.show(truncate=False)
new_patient_df.printSchema()
o/p:
=========
+----------+--------------+--------------+-------------+---------+----------+
|patient_id|admission_date|discharge_date|diagnosis    |doctor_id|total_cost|
+----------+--------------+--------------+-------------+---------+----------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |101      |5000.0    |
|2         |2022-02-05    |2022-02-09    |Appendicitis |102      |7000.0    |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|103      |3500.0    |
|4         |2022-04-02    |2022-04-08    |Heart Attack |104      |15000.0   |
|5         |2022-05-05    |2022-05-07    |Influenza    |105      |2500.0    |
|6         |2022-06-10    |2022-06-15    |Appendicitis |106      |8000.0    |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |107      |5500.0    |
|8         |2022-08-25    |2022-09-01    |Heart Attack |108      |20000.0   |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|109      |6000.0    |
|10        |2022-10-05    |2022-10-10    |Appendicitis |110      |7500.0    |
|11        |2022-11-02    |2022-11-05    |Influenza    |111      |2800.0    |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |112      |6000.0    |
|13        |2023-01-02    |2023-01-09    |Heart Attack |113      |18000.0   |
|14        |2023-02-14    |2023-02-18    |Appendicitis |114      |7200.0    |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|115      |3800.0    |
|16        |2023-04-05    |2023-04-11    |Influenza    |116      |2700.0    |
|17        |2023-05-08    |2023-05-11    |Heart Attack |117      |16000.0   |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |118      |4800.0    |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|119      |6500.0    |
|20        |2023-08-10    |2023-08-16    |Appendicitis |120      |7800.0    |
+----------+--------------+--------------+-------------+---------+----------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- doctor_id: integer (nullable = true)
 |-- total_cost: float (nullable = true)

1. Drop the "doctor_id" column from the dataset:
======================================================
new_patient_df = new_patient_df.drop(col("doctor_id"))
new_patient_df.show(truncate=False)
new_patient_df.printSchema()
o/p:
=========
+----------+--------------+--------------+-------------+----------+
|patient_id|admission_date|discharge_date|diagnosis    |total_cost|
+----------+--------------+--------------+-------------+----------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |5000.0    |
|2         |2022-02-05    |2022-02-09    |Appendicitis |7000.0    |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|3500.0    |
|4         |2022-04-02    |2022-04-08    |Heart Attack |15000.0   |
|5         |2022-05-05    |2022-05-07    |Influenza    |2500.0    |
|6         |2022-06-10    |2022-06-15    |Appendicitis |8000.0    |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |5500.0    |
|8         |2022-08-25    |2022-09-01    |Heart Attack |20000.0   |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|6000.0    |
|10        |2022-10-05    |2022-10-10    |Appendicitis |7500.0    |
|11        |2022-11-02    |2022-11-05    |Influenza    |2800.0    |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |6000.0    |
|13        |2023-01-02    |2023-01-09    |Heart Attack |18000.0   |
|14        |2023-02-14    |2023-02-18    |Appendicitis |7200.0    |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|3800.0    |
|16        |2023-04-05    |2023-04-11    |Influenza    |2700.0    |
|17        |2023-05-08    |2023-05-11    |Heart Attack |16000.0   |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |4800.0    |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|6500.0    |
|20        |2023-08-10    |2023-08-16    |Appendicitis |7800.0    |
+----------+--------------+--------------+-------------+----------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- total_cost: float (nullable = true)

2. Rename the "total_cost" column to "hospital_bill":
===========================================================
new_patient_df = new_patient_df.withColumnRenamed("total_cost","hospital_bill")
new_patient_df.show(truncate=False)
new_patient_df.printSchema()
o/p:
=========
+----------+--------------+--------------+-------------+-------------+
|patient_id|admission_date|discharge_date|diagnosis    |hospital_bill|
+----------+--------------+--------------+-------------+-------------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |5000.0       |
|2         |2022-02-05    |2022-02-09    |Appendicitis |7000.0       |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|3500.0       |
|4         |2022-04-02    |2022-04-08    |Heart Attack |15000.0      |
|5         |2022-05-05    |2022-05-07    |Influenza    |2500.0       |
|6         |2022-06-10    |2022-06-15    |Appendicitis |8000.0       |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |5500.0       |
|8         |2022-08-25    |2022-09-01    |Heart Attack |20000.0      |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|6000.0       |
|10        |2022-10-05    |2022-10-10    |Appendicitis |7500.0       |
|11        |2022-11-02    |2022-11-05    |Influenza    |2800.0       |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |6000.0       |
|13        |2023-01-02    |2023-01-09    |Heart Attack |18000.0      |
|14        |2023-02-14    |2023-02-18    |Appendicitis |7200.0       |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|3800.0       |
|16        |2023-04-05    |2023-04-11    |Influenza    |2700.0       |
|17        |2023-05-08    |2023-05-11    |Heart Attack |16000.0      |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |4800.0       |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|6500.0       |
|20        |2023-08-10    |2023-08-16    |Appendicitis |7800.0       |
+----------+--------------+--------------+-------------+-------------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- hospital_bill: float (nullable = true)

3. Add a new column called "duration_of_stay" that represents the number
of days a patient stayed in the hospital. (hint: The duration should be
calculated as the difference between the "discharge_date" and
"admission_date" columns.)
===============================================================================
i. new_patient_df = new_patient_df.withColumn("duration_of_stay",datediff(col("discharge_date"),col("admission_date")))
new_patient_df.show(truncate=False)
new_patient_df.printSchema()

ii. new_patient_df.createOrReplaceTempView("practice")
new_patient_df_1 = spark.sql("""select patient_id,admission_date,discharge_date,diagnosis,hospital_bill,datediff(discharge_date,admission_date) as duration_day
                              from practice
                              """)
new_patient_df_1.show(truncate=False)
new_patient_df_1.printSchema()
o/p:
==========
+----------+--------------+--------------+-------------+-------------+------------+
|patient_id|admission_date|discharge_date|diagnosis    |hospital_bill|duration_day|
+----------+--------------+--------------+-------------+-------------+------------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |5000.0       |9           |
|2         |2022-02-05    |2022-02-09    |Appendicitis |7000.0       |4           |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|3500.0       |6           |
|4         |2022-04-02    |2022-04-08    |Heart Attack |15000.0      |6           |
|5         |2022-05-05    |2022-05-07    |Influenza    |2500.0       |2           |
|6         |2022-06-10    |2022-06-15    |Appendicitis |8000.0       |5           |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |5500.0       |5           |
|8         |2022-08-25    |2022-09-01    |Heart Attack |20000.0      |7           |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|6000.0       |7           |
|10        |2022-10-05    |2022-10-10    |Appendicitis |7500.0       |5           |
|11        |2022-11-02    |2022-11-05    |Influenza    |2800.0       |3           |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |6000.0       |8           |
|13        |2023-01-02    |2023-01-09    |Heart Attack |18000.0      |7           |
|14        |2023-02-14    |2023-02-18    |Appendicitis |7200.0       |4           |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|3800.0       |8           |
|16        |2023-04-05    |2023-04-11    |Influenza    |2700.0       |6           |
|17        |2023-05-08    |2023-05-11    |Heart Attack |16000.0      |3           |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |4800.0       |5           |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|6500.0       |5           |
|20        |2023-08-10    |2023-08-16    |Appendicitis |7800.0       |6           |
+----------+--------------+--------------+-------------+-------------+------------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- hospital_bill: float (nullable = true)
 |-- duration_day: integer (nullable = true)

4. Create a new column called "adjusted_total_cost" that calculates the
adjusted total cost based on the diagnosis as follows:
If the diagnosis is "Heart Attack", multiply the hospital_bill by 1.5.
If the diagnosis is "Appendicitis", multiply the hospital_bill by 1.2.
For any other diagnosis, keep the hospital_bill as it is.
===============================================================================
i. new_patient_df1 = new_patient_df.selectExpr("*","""CASE 
                                                   WHEN diagnosis LIKE '%Heart Attack%' THEN hospital_bill*1.5
                                                   WHEN diagnosis LIKE '%Appendicitis%' THEN hospital_bill*1.2
                                                   ELSE hospital_bill
                                                   END AS adjusted_total_cost
                                                   """ 
                                                    )
new_patient_df1.show(truncate=False)
new_patient_df1.printSchema()

ii. new_patient_df1 = new_patient_df.select("*",expr("""CASE 
                                                   WHEN diagnosis LIKE '%Heart Attack%' THEN hospital_bill*1.5
                                                   WHEN diagnosis LIKE '%Appendicitis%' THEN hospital_bill*1.2
                                                   ELSE hospital_bill
                                                   END AS adjusted_total_cost
                                                   """
                                               )
                                                    )
new_patient_df1.show(truncate=False)
new_patient_df1.printSchema()

iii. new_patient_df1 = new_patient_df.withColumn("adjusted_total_cost", 
                                                   when (col("diagnosis").like('%Heart Attack%'),col("hospital_bill")*1.5)\
                                                   .when (col("diagnosis").like('%Appendicitis%'),col("hospital_bill")*1.2)\
                                                   .otherwise(col("hospital_bill"))
                                            )
                           
new_patient_df1.show(truncate=False)
new_patient_df.printSchema()
o/p:
==========
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
|patient_id|admission_date|discharge_date|diagnosis    |hospital_bill|duration_of_stay|adjusted_total_cost|
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |5000.0       |9               |5000.0             |
|2         |2022-02-05    |2022-02-09    |Appendicitis |7000.0       |4               |8400.0             |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|3500.0       |6               |3500.0             |
|4         |2022-04-02    |2022-04-08    |Heart Attack |15000.0      |6               |22500.0            |
|5         |2022-05-05    |2022-05-07    |Influenza    |2500.0       |2               |2500.0             |
|6         |2022-06-10    |2022-06-15    |Appendicitis |8000.0       |5               |9600.0             |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |5500.0       |5               |5500.0             |
|8         |2022-08-25    |2022-09-01    |Heart Attack |20000.0      |7               |30000.0            |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|6000.0       |7               |6000.0             |
|10        |2022-10-05    |2022-10-10    |Appendicitis |7500.0       |5               |9000.0             |
|11        |2022-11-02    |2022-11-05    |Influenza    |2800.0       |3               |2800.0             |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |6000.0       |8               |6000.0             |
|13        |2023-01-02    |2023-01-09    |Heart Attack |18000.0      |7               |27000.0            |
|14        |2023-02-14    |2023-02-18    |Appendicitis |7200.0       |4               |8640.0             |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|3800.0       |8               |3800.0             |
|16        |2023-04-05    |2023-04-11    |Influenza    |2700.0       |6               |2700.0             |
|17        |2023-05-08    |2023-05-11    |Heart Attack |16000.0      |3               |24000.0            |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |4800.0       |5               |4800.0             |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|6500.0       |5               |6500.0             |
|20        |2023-08-10    |2023-08-16    |Appendicitis |7800.0       |6               |9360.0             |
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- hospital_bill: float (nullable = true)
 |-- duration_of_stay: integer (nullable = true)

iv. Using sparksql:
==========================
new_patient_df.createOrReplaceTempView("practice1")
new_patient_df1 = spark.sql("""SELECT *,CASE 
                                                  WHEN diagnosis LIKE '%Heart Attack%' THEN hospital_bill*1.5
                                                   WHEN diagnosis LIKE '%Appendicitis%' THEN hospital_bill*1.2
                                                   ELSE hospital_bill
                                                   END AS adjusted_total_cost 
                                                   FROM practice1
                                                   """)
new_patient_df1.show(truncate=False)
new_patient_df1.printSchema()
o/p:
========
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
|patient_id|admission_date|discharge_date|diagnosis    |hospital_bill|duration_of_stay|adjusted_total_cost|
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
|1         |2022-01-01    |2022-01-10    |Pneumonia    |5000.0       |9               |5000.0             |
|2         |2022-02-05    |2022-02-09    |Appendicitis |7000.0       |4               |8400.0             |
|3         |2022-03-12    |2022-03-18    |Fractured Arm|3500.0       |6               |3500.0             |
|4         |2022-04-02    |2022-04-08    |Heart Attack |15000.0      |6               |22500.0            |
|5         |2022-05-05    |2022-05-07    |Influenza    |2500.0       |2               |2500.0             |
|6         |2022-06-10    |2022-06-15    |Appendicitis |8000.0       |5               |9600.0             |
|7         |2022-07-20    |2022-07-25    |Pneumonia    |5500.0       |5               |5500.0             |
|8         |2022-08-25    |2022-09-01    |Heart Attack |20000.0      |7               |30000.0            |
|9         |2022-09-15    |2022-09-22    |Fractured Leg|6000.0       |7               |6000.0             |
|10        |2022-10-05    |2022-10-10    |Appendicitis |7500.0       |5               |9000.0             |
|11        |2022-11-02    |2022-11-05    |Influenza    |2800.0       |3               |2800.0             |
|12        |2022-12-10    |2022-12-18    |Pneumonia    |6000.0       |8               |6000.0             |
|13        |2023-01-02    |2023-01-09    |Heart Attack |18000.0      |7               |27000.0            |
|14        |2023-02-14    |2023-02-18    |Appendicitis |7200.0       |4               |8640.0             |
|15        |2023-03-20    |2023-03-28    |Fractured Arm|3800.0       |8               |3800.0             |
|16        |2023-04-05    |2023-04-11    |Influenza    |2700.0       |6               |2700.0             |
|17        |2023-05-08    |2023-05-11    |Heart Attack |16000.0      |3               |24000.0            |
|18        |2023-06-15    |2023-06-20    |Pneumonia    |4800.0       |5               |4800.0             |
|19        |2023-07-22    |2023-07-27    |Fractured Leg|6500.0       |5               |6500.0             |
|20        |2023-08-10    |2023-08-16    |Appendicitis |7800.0       |6               |9360.0             |
+----------+--------------+--------------+-------------+-------------+----------------+-------------------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- admission_date: date (nullable = true)
 |-- discharge_date: date (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- hospital_bill: float (nullable = true)
 |-- duration_of_stay: integer (nullable = true)
 |-- adjusted_total_cost: double (nullable = true)

5. Select the "patient_id", "diagnosis", "hospital_bill", and "adjusted_total_cost" columns:
================================================================================================
i. new_patient_df1 = new_patient_df1.select(col("patient_id"),col("diagnosis"),col("hospital_bill"),col("adjusted_total_cost"))
new_patient_df1.show(truncate=False)
new_patient_df1.printSchema()

ii. new_patient_df1.createOrReplaceTempView("practice2")
new_patient_df1 = new_patient_df1.select(col("patient_id"),col("diagnosis"),col("hospital_bill"),col("adjusted_total_cost"))
new_patient_df1.show(truncate=False)
new_patient_df1.printSchema()
o/p:
==========
+----------+-------------+-------------+-------------------+
|patient_id|diagnosis    |hospital_bill|adjusted_total_cost|
+----------+-------------+-------------+-------------------+
|1         |Pneumonia    |5000.0       |5000.0             |
|2         |Appendicitis |7000.0       |8400.0             |
|3         |Fractured Arm|3500.0       |3500.0             |
|4         |Heart Attack |15000.0      |22500.0            |
|5         |Influenza    |2500.0       |2500.0             |
|6         |Appendicitis |8000.0       |9600.0             |
|7         |Pneumonia    |5500.0       |5500.0             |
|8         |Heart Attack |20000.0      |30000.0            |
|9         |Fractured Leg|6000.0       |6000.0             |
|10        |Appendicitis |7500.0       |9000.0             |
|11        |Influenza    |2800.0       |2800.0             |
|12        |Pneumonia    |6000.0       |6000.0             |
|13        |Heart Attack |18000.0      |27000.0            |
|14        |Appendicitis |7200.0       |8640.0             |
|15        |Fractured Arm|3800.0       |3800.0             |
|16        |Influenza    |2700.0       |2700.0             |
|17        |Heart Attack |16000.0      |24000.0            |
|18        |Pneumonia    |4800.0       |4800.0             |
|19        |Fractured Leg|6500.0       |6500.0             |
|20        |Appendicitis |7800.0       |9360.0             |
+----------+-------------+-------------+-------------------+
only showing top 20 rows

root
 |-- patient_id: integer (nullable = true)
 |-- diagnosis: string (nullable = true)
 |-- hospital_bill: float (nullable = true)
 |-- adjusted_total_cost: double (nullable = true)


32. """
Given the table LogInfo containing login and logout data for Leetflex accounts. It also contains the IP address from which the account logged in and out.

Task -
Find the accounts that should be banned. An account should be banned if it was logged in from two different IP addresses at any moment.
"""
solution:
======================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
 (1, 1, "2021-02-01 09:00:00", "2021-02-01 09:30:00"),
 (1, 2, "2021-02-01 08:00:00", "2021-02-01 11:30:00"),
 (2, 6, "2021-02-01 20:30:00", "2021-02-01 22:00:00"),
 (2, 7, "2021-02-02 20:30:00", "2021-02-02 22:00:00"),
 (3, 9, "2021-02-01 16:00:00", "2021-02-01 16:59:59"),
 (3, 13, "2021-02-01 17:00:00", "2021-02-01 17:59:59"),
 (4, 10, "2021-02-01 16:00:00", "2021-02-01 17:00:00"),
 (4, 11, "2021-02-01 17:00:00", "2021-02-01 17:59:59")
]

# DataFrame
df = spark.createDataFrame(data, ["account_id", "ip_address", "login", "logout"])
df.show()
o/p:
========
+----------+----------+-------------------+-------------------+
|account_id|ip_address|              login|             logout|
+----------+----------+-------------------+-------------------+
|         1|         1|2021-02-01 09:00:00|2021-02-01 09:30:00|
|         1|         2|2021-02-01 08:00:00|2021-02-01 11:30:00|
|         2|         6|2021-02-01 20:30:00|2021-02-01 22:00:00|
|         2|         7|2021-02-02 20:30:00|2021-02-02 22:00:00|
|         3|         9|2021-02-01 16:00:00|2021-02-01 16:59:59|
|         3|        13|2021-02-01 17:00:00|2021-02-01 17:59:59|
|         4|        10|2021-02-01 16:00:00|2021-02-01 17:00:00|
|         4|        11|2021-02-01 17:00:00|2021-02-01 17:59:59|
+----------+----------+-------------------+-------------------+

df.createOrReplaceTempView("practice")


i. Using df():
==========================================
winspec = Window.partitionBy(col("account_id"))\
                .orderBy(col("login"))

df_account_banned = df.withColumn("next_login",lead(col("login")).over(winspec))
df_account_banned.show(truncate=False)
df_account_banned.printSchema()
                      
o/p:
========
+----------+----------+-------------------+-------------------+-------------------+
|account_id|ip_address|login              |logout             |next_login         |
+----------+----------+-------------------+-------------------+-------------------+
|1         |2         |2021-02-01 08:00:00|2021-02-01 11:30:00|2021-02-01 09:00:00|
|1         |1         |2021-02-01 09:00:00|2021-02-01 09:30:00|null               |
|3         |9         |2021-02-01 16:00:00|2021-02-01 16:59:59|2021-02-01 17:00:00|
|3         |13        |2021-02-01 17:00:00|2021-02-01 17:59:59|null               |
|2         |6         |2021-02-01 20:30:00|2021-02-01 22:00:00|2021-02-02 20:30:00|
|2         |7         |2021-02-02 20:30:00|2021-02-02 22:00:00|null               |
|4         |10        |2021-02-01 16:00:00|2021-02-01 17:00:00|2021-02-01 17:00:00|
|4         |11        |2021-02-01 17:00:00|2021-02-01 17:59:59|null               |
+----------+----------+-------------------+-------------------+-------------------+

root
 |-- account_id: long (nullable = true)
 |-- ip_address: long (nullable = true)
 |-- login: string (nullable = true)
 |-- logout: string (nullable = true)
 |-- next_login: string (nullable = true)

df_account_banned = df.withColumn("next_login",lead(col("login")).over(winspec))\
                      .filter(col("logout")>=col("next_login"))
df_account_banned.show(truncate=False)
df_account_banned.printSchema()
o/p:
=========
+----------+----------+-------------------+-------------------+-------------------+
|account_id|ip_address|login              |logout             |next_login         |
+----------+----------+-------------------+-------------------+-------------------+
|1         |2         |2021-02-01 08:00:00|2021-02-01 11:30:00|2021-02-01 09:00:00|
|4         |10        |2021-02-01 16:00:00|2021-02-01 17:00:00|2021-02-01 17:00:00|
+----------+----------+-------------------+-------------------+-------------------+

root
 |-- account_id: long (nullable = true)
 |-- ip_address: long (nullable = true)
 |-- login: string (nullable = true)
 |-- logout: string (nullable = true)
 |-- next_login: string (nullable = true)

df_account_banned = df.withColumn("next_login",lead(col("login")).over(winspec))\
                      .filter(col("logout")>=col("next_login"))\
                      .select(col("account_id"))
df_account_banned.show(truncate=False)
df_account_banned.printSchema()
o/p:
==========
+----------+
|account_id|
+----------+
|1         |
|4         |
+----------+

root
 |-- account_id: long (nullable = true)

df_account_banned = df.withColumn("next_login",lead(col("login")).over(winspec))\
                      .filter(col("logout")>=col("next_login"))\
                      .select(col("account_id"))\
                      .distinct()
df_account_banned.show(truncate=False)
df_account_banned.printSchema()
o/p:
========
+----------+
|account_id|
+----------+
|1         |
|4         |
+----------+

root
 |-- account_id: long (nullable = true)

ii. Using sparksql:
==============================
df_account_banned = spark.sql("""With cte as(
                                 select *,lead(login) over(partition by account_id order by login) as next_login
                                 from practice)
                                 select account_id from cte
                                 where logout>=next_login""")

df_account_banned.show(truncate=False)
df_account_banned.printSchema()
o/p:
=========
+----------+
|account_id|
+----------+
|1         |
|4         |
+----------+

root
 |-- account_id: long (nullable = true)


33. Find cummulative salary:
==========================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
(1, "A", 1000),
(2, "B", 2000),
(3, "C", 3000),
(4, "D", 4000),
]

# Define the schema for the DataFrame
schema1 = StructType([
  StructField("ID", IntegerType(), True),
  StructField("Name", StringType(), True),
  StructField("Sal", IntegerType(), True)
])
df2 = spark.createDataFrame(data, schema=schema1)
df2.show()
o/p:
========
+---+----+----+
| ID|Name| Sal|
+---+----+----+
|  1|   A|1000|
|  2|   B|2000|
|  3|   C|3000|
|  4|   D|4000|
+---+----+----+

df2.createOrReplaceTempView("practice")


i. Using df():
==========================================
winspec = Window.orderBy(col("ID"))

df_cummulative_salary = df2.withColumn("total_sal",sum(col("Sal")).over(winspec))
df_cummulative_salary.show(truncate=False)
df_cummulative_salary.printSchema()
o/p:
==========
+---+----+----+---------+
|ID |Name|Sal |total_sal|
+---+----+----+---------+
|1  |A   |1000|1000     |
|2  |B   |2000|3000     |
|3  |C   |3000|6000     |
|4  |D   |4000|10000    |
+---+----+----+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sal: integer (nullable = true)
 |-- total_sal: long (nullable = true)

ii. Using sparksql:
=======================================
df_cummulative_salary = spark.sql("select *,sum(Sal) over(order by ID) as total_sal from practice")
df_cummulative_salary.show(truncate=False)
df_cummulative_salary.printSchema()
o/p:
=========
+---+----+----+---------+
|ID |Name|Sal |total_sal|
+---+----+----+---------+
|1  |A   |1000|1000     |
|2  |B   |2000|3000     |
|3  |C   |3000|6000     |
|4  |D   |4000|10000    |
+---+----+----+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sal: integer (nullable = true)
 |-- total_sal: long (nullable = true)



34.  Find cummulative salary:
==========================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
(1, "A", 1000),
(1, "A", 100),
(2, "B", 2000),
(3, "C", 3000),
(4, "D", 4000),
]

# Define the schema for the DataFrame
schema1 = StructType([
  StructField("ID", IntegerType(), True),
  StructField("Name", StringType(), True),
  StructField("Sal", IntegerType(), True)
])
df2 = spark.createDataFrame(data, schema=schema1)
df2.show()
o/p:
========
+---+----+----+
| ID|Name| Sal|
+---+----+----+
|  1|   A|1000|
|  1|   A| 100|
|  2|   B|2000|
|  3|   C|3000|
|  4|   D|4000|
+---+----+----+

df2.createOrReplaceTempView("practice")


i. Using df():
==========================================
winspec = Window.partitionBy(col("ID"))\
                .orderBy(col("ID"))

df_cummulative_salary = df2.withColumn("total_sal",sum(col("Sal")).over(winspec))
df_cummulative_salary.show(truncate=False)
df_cummulative_salary.printSchema()
o/p:
==========
+---+----+----+---------+
|ID |Name|Sal |total_sal|
+---+----+----+---------+
|1  |A   |1000|1100     |
|1  |A   |100 |1100     |
|3  |C   |3000|3000     |
|4  |D   |4000|4000     |
|2  |B   |2000|2000     |
+---+----+----+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sal: integer (nullable = true)
 |-- total_sal: long (nullable = true)

ii. Using sparksql:
=======================================
df_cummulative_salary = spark.sql("""select *,sum(Sal) over(partition by ID order by ID) as total_sal from practice""")
df_cummulative_salary.show(truncate=False)
df_cummulative_salary.printSchema()
o/p:
=========
+---+----+----+---------+
|ID |Name|Sal |total_sal|
+---+----+----+---------+
|1  |A   |1000|1100     |
|1  |A   |100 |1100     |
|3  |C   |3000|3000     |
|4  |D   |4000|4000     |
|2  |B   |2000|2000     |
+---+----+----+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sal: integer (nullable = true)
 |-- total_sal: long (nullable = true)


34.  Write a Pyspark/spark sql code to Find the number of output rows for different types of joins:
========================================================================================================
i. INNER JOIN.
ii. LEFT JOIN.
iii. RIGHT JOIN.
iv. FULL OUTER JOIN.
v. CROSS JOIN.
vi. LEFT ANTI JOIN.
vii. LEFT SEMI JOIN.
Solution:
===================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()
spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

df_1 = spark.createDataFrame(
    [(1,),
     (2,),
     (3,),
     (1,),
     (1,),
     (1,),
     (None,),
      (None,)
     ], 
    schema="id_1 int"
)
df_2 = spark.createDataFrame(
  [(1,), 
   (1,),
   (2,),
    (None,)
   ], schema="id_2 int")

df_1.show(truncate=False)
df_2.show(truncate=False)
o/p:
==========
+----+
|id_1|
+----+
|1   |
|2   |
|3   |
|1   |
|1   |
|1   |
|null|
|null|
+----+

+----+
|id_2|
+----+
|1   |
|1   |
|2   |
|null|
+----+

df_1.createOrReplaceTempView("practice_1")
df_2.createOrReplaceTempView("practice_2")

i. INNER JOIN:
===================
a. Using df():
===================
df_inner_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"inner")
df_inner_join.show(truncate=False)
df_inner_join.count()
print("Total count of records in inner join: ",df_inner_join.count())

b. Using sparksql:
========================
df_inner_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             inner join practice_2 p_2
                             on p_1.id_1 = p_2.id_2""")
df_inner_join.show(truncate=False)
df_inner_join.count()
print("Total count of records in inner join: ",df_inner_join.count())

o/p:
+----+----+
|id_1|id_2|
+----+----+
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|2   |2   |
+----+----+

Total count of records in inner join:  9

ii.LEFT JOIN.:
===================
a. Using df():
===================
df_left_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"left")
df_left_join.show(truncate=False)
df_left_join.count()
print("Total count of records in left join: ",df_left_join.count())

b. Using sparksql:
========================
df_left_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             left join practice_2 p_2
                             on p_1.id_1 = p_2.id_2""")
df_left_join.show(truncate=False)
df_left_join.count()
print("Total count of records in left join: ",df_left_join.count())

o/p:
=========
+----+----+
|id_1|id_2|
+----+----+
|null|null|
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|3   |null|
|2   |2   |
+----+----+

Total count of records in left join:  12

iii.RIGHT JOIN:
===================
a. Using df():
===================
df_right_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"right")
df_right_join.show(truncate=False)
df_right_join.count()
print("Total count of records in left join: ",df_right_join.count())

b. Using sparksql:
========================
df_right_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             right join practice_2 p_2
                             on p_1.id_1 = p_2.id_2""")
df_right_join.show(truncate=False)
df_right_join.count()
print("Total count of records in right join: ",df_right_join.count())

o/p:
=========
+----+----+
|id_1|id_2|
+----+----+
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|2   |2   |
+----+----+

Total count of records in left join:  10

iv.FULL OUTER JOIN:
===================
a. Using df():
===================
df_full_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"full")
df_full_join.show(truncate=False)
df_full_join.count()
print("Total count of records in full outer join: ",df_full_join.count())

b. Using sparksql:
========================
df_full_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             FULL OUTER JOIN practice_2 p_2
                             on p_1.id_1 = p_2.id_2""")
df_full_join.show(truncate=False)
df_full_join.count()
print("Total count of records in full join: ",df_full_join.count())

o/p:
=========
+----+----+
|id_1|id_2|
+----+----+
|null|null|
|null|null|
|null|null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
|3   |null|
|2   |2   |
+----+----+

Total count of records in full join:  13

v.CROSS JOIN:
===================
a. Using df():
===================
df_cross_join = df_1.join(df_2)
df_cross_join.show(truncate=False)
df_cross_join.count()
print("Total count of records in full outer join: ",df_cross_join.count())

b. Using sparksql:
========================
df_cross_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             JOIN practice_2 p_2
                          """)
df_cross_join.show(truncate=False)
df_cross_join.count()
print("Total count of records in full join: ",df_cross_join.count())

o/p:
=========
+----+----+
|id_1|id_2|
+----+----+
|1   |1   |
|1   |1   |
|2   |1   |
|2   |1   |
|3   |1   |
|3   |1   |
|1   |1   |
|1   |1   |
|1   |2   |
|1   |null|
|2   |2   |
|2   |null|
|3   |2   |
|3   |null|
|1   |2   |
|1   |null|
|1   |1   |
|1   |1   |
|1   |1   |
|1   |1   |
+----+----+
only showing top 20 rows

Total count of records in full join:  32

vi.LEFT ANTI JOIN:
===================
a. Using df():
===================
df_left_anti_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"left_anti")
df_left_anti_join.show(truncate=False)
df_left_anti_join.count()
print("Total count of records in left anti join: ",df_left_anti_join.count())
o/p:
=====
+----+
|id_1|
+----+
|null|
|null|
|3   |
+----+

Total count of records in left anti join:  3

b. Using sparksql:
========================
df_left_anti_join = spark.sql("""select id_1,id_2 from practice_1 p_1
                             LEFT JOIN practice_2 p_2
                             on p_1.id_1 = p_2.id_2
                             where p_2.id_2 is null""")
df_left_anti_join.show(truncate=False)
df_left_anti_join.count()
print("Total count of records in left anti join: ",df_left_anti_join.count())

o/p:
=========
+----+----+
|id_1|id_2|
+----+----+
|null|null|
|null|null|
|3   |null|
+----+----+

Total count of records in left anti join:  3

vi.LEFT SEMI JOIN:
===================
a. Using df():
===================
df_left_semi_join = df_1.join(df_2,df_1["id_1"]==df_2["id_2"],"left_semi")
df_left_semi_join.show(truncate=False)
df_left_semi_join.count()
print("Total count of records in left semi join: ",df_left_semi_join.count())

b. Using sparksql:
========================
df_left_semi_join = spark.sql("""select id_1 from practice_1 p_1
                             LEFT SEMI JOIN practice_2 p_2
                             on p_1.id_1 = p_2.id_2
                             """)
df_left_semi_join.show(truncate=False)
df_left_semi_join.count()
print("Total count of records in left semi join: ",df_left_semi_join.count())

o/p:
=========
+----+
|id_1|
+----+
|1   |
|1   |
|1   |
|1   |
|2   |
+----+

Total count of records in left semi join:  5


35. Pyspark and sparksql coding question:
=========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [(1,"Nagesh",["Add1","Add2","Add3"])]

ddl_schema = "CustomerId int, Name string, Address array<string>"

prog_schema = StructType([
    StructField("CustomerId", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("Address", ArrayType(StringType()), True)
])

df = spark.createDataFrame(data, prog_schema)

df.show(truncate=False)
df.printSchema()
o/p:
=========
+----------+------+------------------+
|CustomerId|Name  |Address           |
+----------+------+------------------+
|1         |Nagesh|[Add1, Add2, Add3]|
+----------+------+------------------+

root
 |-- CustomerId: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: array (nullable = true)
 |    |-- element: string (containsNull = true)

df.createOrReplaceTempView("practice")

i. Using df():
=======================
df_array = df.select(col("CustomerId"),col("Name"),explode(col("Address")).alias("Address"))
df_array.show(truncate=False)
df_array.printSchema()

ii. Using sparksql:
===========================
df_array = spark.sql("""select CustomerId,Name,explode(Address) as Address
                        from practice""")
df_array.show(truncate=False)
df_array.printSchema()
o/p:
=========
+----------+------+-------+
|CustomerId|Name  |Address|
+----------+------+-------+
|1         |Nagesh|Add1   |
|1         |Nagesh|Add2   |
|1         |Nagesh|Add3   |
+----------+------+-------+

root
 |-- CustomerId: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Address: string (nullable = true)


36. Pyspark and sparksql coding question:
=========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [(1,"Prem-Ojha"),\
        (2,"Alex-John"),\
        (3,"John-Cena"),\
        (4,"Kim-Joe")]

ddl_schema = "ID int,Name string"
prog_schema = StructType([\
                         StructField("ID",IntegerType(),True),\
                         StructField("Name",StringType(),True)])

df = spark.createDataFrame(data=data,schema=prog_schema)
df.show(truncate=False)
df.printSchema()
o/p:
=======
+---+---------+
|ID |Name     |
+---+---------+
|1  |Prem-Ojha|
|2  |Alex-John|
|3  |John-Cena|
|4  |Kim-Joe  |
+---+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Using df():
=======================
df_final = df.withColumn("First_Name",split(col("Name"),"-")[0])\
             .withColumn("Last_Name",split(col("Name"),"-")[1])\
             .select(col("ID"),col("Name"),col("First_Name"),col("Last_Name"))

df_final.show(truncate=False)
df_final.printSchema()
o/p:
===========
+---+---------+----------+---------+
|ID |Name     |First_Name|Last_Name|
+---+---------+----------+---------+
|1  |Prem-Ojha|Prem      |Ojha     |
|2  |Alex-John|Alex      |John     |
|3  |John-Cena|John      |Cena     |
|4  |Kim-Joe  |Kim       |Joe      |
+---+---------+----------+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- First_Name: string (nullable = true)
 |-- Last_Name: string (nullable = true)

ii. Using sparksql:
===========================
df_final = spark.sql("""select ID,Name,split(Name,'-')[0] as First_Name,split(Name,'-')[1] as Last_Name  
                        from practice""")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+---+---------+----------+---------+
|ID |Name     |First_Name|Last_Name|
+---+---------+----------+---------+
|1  |Prem-Ojha|Prem      |Ojha     |
|2  |Alex-John|Alex      |John     |
|3  |John-Cena|John      |Cena     |
|4  |Kim-Joe  |Kim       |Joe      |
+---+---------+----------+---------+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- First_Name: string (nullable = true)
 |-- Last_Name: string (nullable = true)



37. Pyspark and sparksql coding question:
=========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [("Anil Kumar",),
        ("Mohan Yadav",),
        ("Shrithi Reddy",),
        ("Sayed Jamal",)]

ddl_schema = "Fullname string"

prog_schema = StructType([
    StructField("Fullname", StringType(), True)
])

df = spark.createDataFrame(data, ddl_schema)

df.show(truncate=False)
df.printSchema()
o/p:
=======
+-------------+
|Fullname     |
+-------------+
|Anil Kumar   |
|Mohan Yadav  |
|Shrithi Reddy|
|Sayed Jamal  |
+-------------+

root
 |-- Fullname: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Using df():
=======================
df_final = df.withColumn("F_Name",split(col("Fullname"),' ')[0])\
             .withColumn("L_Name",split(col("Fullname"),' ')[1])\
             .drop(col("Fullname"))

df_final.show(truncate=False)
df_final.printSchema()
o/p:
===========
+-------+------+
|F_Name |L_Name|
+-------+------+
|Anil   |Kumar |
|Mohan  |Yadav |
|Shrithi|Reddy |
|Sayed  |Jamal |
+-------+------+

root
 |-- F_Name: string (nullable = true)
 |-- L_Name: string (nullable = true)

ii. Using sparksql:
===========================
df_final = spark.sql("""select split(Fullname,' ')[0] as F_Name,split(Fullname,' ')[1] as L_Name  
                        from practice""")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+-------+------+
|F_Name |L_Name|
+-------+------+
|Anil   |Kumar |
|Mohan  |Yadav |
|Shrithi|Reddy |
|Sayed  |Jamal |
+-------+------+

root
 |-- F_Name: string (nullable = true)
 |-- L_Name: string (nullable = true)


38. Pyspark/sparksql coding interview question:
=============================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data_email = [("abc12@gmail.coom",),\
              ("bdc12@gmail.coom",),\
              ("psrt23@outlook.com",),\
              ("mno12@rediffmail.com",),\
              ("prt10@outlook.com",)]

ddl_schema_email = "emailid string"
prog_schema_email = StructType([\
                               StructField("emailid",StringType(),True)])

df = spark.createDataFrame(data=data_email,schema=ddl_schema_email)
df.show(truncate=False)
df.printSchema()
o/p:
=========
+--------------------+
|emailid             |
+--------------------+
|abc12@gmail.coom    |
|bdc12@gmail.coom    |
|psrt23@outlook.com  |
|mno12@rediffmail.com|
|prt10@outlook.com   |
+--------------------+

root
 |-- emailid: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Approach 1st using df():
===========================================
df_email = df.withColumn("emailid_1",split(col("emailid"),'@')[0])\
             .withColumn("emailid_2",split(col("emailid"),'@')[1])

df_email.show(truncate=False)
df_email.printSchema()
o/p:
==========
+--------------------+---------+--------------+
|emailid             |emailid_1|emailid_2     |
+--------------------+---------+--------------+
|abc12@gmail.coom    |abc12    |gmail.coom    |
|bdc12@gmail.coom    |bdc12    |gmail.coom    |
|psrt23@outlook.com  |psrt23   |outlook.com   |
|mno12@rediffmail.com|mno12    |rediffmail.com|
|prt10@outlook.com   |prt10    |outlook.com   |
+--------------------+---------+--------------+

root
 |-- emailid: string (nullable = true)
 |-- emailid_1: string (nullable = true)
 |-- emailid_2: string (nullable = true)

df_final = df_email.groupBy(col("emailid_2"))\
                   .count()
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=======
+--------------+-----+
|emailid_2     |count|
+--------------+-----+
|gmail.coom    |2    |
|outlook.com   |2    |
|rediffmail.com|1    |
+--------------+-----+

root
 |-- emailid_2: string (nullable = true)
 |-- count: long (nullable = false)

df_final_1 = df_final.withColumnRenamed("emailid_2","emailid")

df_final_1.show(truncate=False)
df_final_1.printSchema()
o/p:
========
+--------------+-----+
|emailid       |count|
+--------------+-----+
|gmail.coom    |2    |
|outlook.com   |2    |
|rediffmail.com|1    |
+--------------+-----+

root
 |-- emailid: string (nullable = true)
 |-- count: long (nullable = false)

ii. Approach 2nd using sparksql:
========================================
df_final_1 = spark.sql("""
WITH cte AS (
    SELECT 
        emailid,
        split(emailid, '@')[0] AS emailid_1,
        split(emailid, '@')[1] AS emailid_2
    FROM practice
)

SELECT 
    emailid_2 AS emailid,
    count(*) AS count
FROM cte
GROUP BY emailid_2
""")

df_final_1.show(truncate=False)
df_final_1.printSchema()
o/p:
=========
+--------------+-----+
|emailid       |count|
+--------------+-----+
|gmail.coom    |2    |
|outlook.com   |2    |
|rediffmail.com|1    |
+--------------+-----+

root
 |-- emailid: string (nullable = true)
 |-- count: long (nullable = false)


39. Pyspark/sparksql coding problem:
=================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.ui.port", "0") \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.1.2") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()

spark
o/p"
======
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [("Sagar Prajapati 23,34",),\
        ("James bond 24,56",),\
        ("Kim John 30,45",)]

schema_ddl = "value string"
df = spark.createDataFrame(data,schema_ddl)
df.show(truncate=False)
df.printSchema()
o/p:
=========
+---------------------+
|value                |
+---------------------+
|Sagar Prajapati 23,34|
|James bond 24,56     |
|Kim John 30,45       |
+---------------------+

root
 |-- value: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Approach 1st using split:
===========================================
a. using df():
===============================
df_final = df.withColumn("first_name", split(col("value"), " ")[0]) \
             .withColumn("last_name", split(col("value"), " ")[1]) \
             .withColumn("age", split(split(col("value"), " ")[2], ",")[0]) \
             .withColumn("marks", split(split(col("value"), " ")[2], ",")[1]) \
             .drop("value")

df_final.show(truncate=False)
df_final.printSchema()

b. using sparksql:
================================
df_final = spark.sql("""
SELECT 
    split(value,' ')[0] AS first_name,
    split(value,' ')[1] AS last_name,
    split(split(value,' ')[2],',')[0] AS age,
    split(split(value,' ')[2],',')[1] AS marks
FROM practice
""")

df_final.show(truncate=False)
df_final.printSchema()
o/p:
============
+----------+---------+---+-----+
|first_name|last_name|age|marks|
+----------+---------+---+-----+
|Sagar     |Prajapati|23 |34   |
|James     |bond     |24 |56   |
|Kim       |John     |30 |45   |
+----------+---------+---+-----+

root
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- age: string (nullable = true)
 |-- marks: string (nullable = true)

ii. Approach 2nd using split and regex pattern "[ ']":
==============================================================
a. using df():
==========================
df_final = df.withColumn("first_name",split(col("value"),'[ ,]')[0])\
             .withColumn("last_name",split(col("value"),'[ ,]')[1])\
             .withColumn("age",split(col("value"),'[ ,]')[2])\
             .withColumn("marks",split(col("value"),'[ ,]')[3])\
             .drop(col("value"))

df_final.show(truncate=False)
df_final.printSchema()

b. using sparksql:
================================
df_final = spark.sql("""
SELECT 
    split(value,'[ ,]')[0] AS first_name,
    split(value,'[ ,]')[1] AS last_name,
    split(value,'[ ,]')[2] AS age,
    split(value,'[ ,]')[3] AS marks
FROM practice
""")

df_final.show(truncate=False)
df_final.printSchema()
o/p:
===========
+----------+---------+---+-----+
|first_name|last_name|age|marks|
+----------+---------+---+-----+
|Sagar     |Prajapati|23 |34   |
|James     |bond     |24 |56   |
|Kim       |John     |30 |45   |
+----------+---------+---+-----+

root
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- age: string (nullable = true)
 |-- marks: string (nullable = true)



39. How to write pyspark code for this , suppose on mobile number 10 digit are there , write a code to mask off middle 8 digits and show only first and last 2 digits:
=================================================================================================================================================================================
Solution:
================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [("87654537291",),\
        ("8794637281",),\
        ("9988776655",)]

ddl_schema = "mobile_number string"
df = spark.createDataFrame(data=data,schema=ddl_schema)
df.show(truncate=False)
df.printSchema()
o/p:
========
+-------------+
|mobile_number|
+-------------+
|87654537291  |
|8794637281   |
|9988776655   |
+-------------+

root
 |-- mobile_number: string (nullable = true)

df.createOrReplaceTempView("practice")

i. Approach 1st using udf (Not Recommended):
============================================================
def mask_mobile_number(mobile_number):
    return mobile_number[0:2]+"*"*len(mobile_number)+mobile_number[-2:]

Register the udf function:
======================================
mask_mobile_number = udf(mask_mobile_number,StringType())

df_final = df.withColumn("masked_mobile_number",mask_mobile_number('mobile_number'))
df_final.show(truncate=False)
df_final.printSchema()
o/p:'
===========
+-------------+--------------------+
|mobile_number|masked_mobile_number|
+-------------+--------------------+
|87654537291  |87***********91     |
|8794637281   |87**********81      |
|9988776655   |99**********55      |
+-------------+--------------------+

root
 |-- mobile_number: string (nullable = true)
 |-- masked_mobile_number: string (nullable = true)

i. This udf() approach is not recommended because it does not give good performance because it resides on driver machine so it does not give parallelismn.
ii. So instead use pyspark inbuilt function like in above case we can use (regexp_replace).

ii. Approach 2nd using regexp_replace():
=================================================
a. df_final = df.withColumn(
    "masked_mobile_number",
    regexp_replace(col("mobile_number"), r"(\d{2})\d+(\d{2})", r"$1******$2")
)

df_final.show(truncate=False)
df_final.printSchema()

b. df_final = spark.sql("""
SELECT 
    mobile_number,
    regexp_replace(
        mobile_number,
        '(\\d{2})\\d+(\\d{2})',
        '$1******$2'
    ) AS masked_mobile_number
FROM practice
""")

df_final.show(truncate=False)
df_final.printSchema()

o/p:
=============
+-------------+--------------------+
|mobile_number|masked_mobile_number|
+-------------+--------------------+
|87654537291  |87654537291         |
|8794637281   |8794637281          |
|9988776655   |9988776655          |
+-------------+--------------------+

root
 |-- mobile_number: string (nullable = true)
 |-- masked_mobile_number: string (nullable = true)


40. Pyspark/sparksql coding question:
======================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

ddl_schema_sales = """
OrderNumber     integer,
LineItem        integer,
OrderDate       string,
DeliveryDate    string,
CustomerKey     integer,
StoreKey        integer,
ProductKey      integer,
Quantity        integer,
CurrencyCode    string
"""

prog_schema_sales = StructType([\
                         StructField("OrderNumber",IntegerType(),True),\
                         StructField("LineItem",IntegerType(),True),\
                         StructField("OrderDate",StringType(),True),\
                         StructField("DeliveryDate",StringType(),True),\
                         StructField("CustomerKey",IntegerType(),True),\
                         StructField("StoreKey",IntegerType(),True),\
                         StructField("ProductKey",IntegerType(),True),\
                         StructField("Quantity",IntegerType(),True),\
                         StructField("CurrencyCode",StringType(),True)])

data_sales = [
    (366001,1,'2016-01-01','2016-01-13',1269051,0,1048,2,'USD'),
    (366001,2,'2016-01-01','2016-01-13',1269051,0,2007,1,'USD'),
    (366002,1,'2016-01-01','2016-01-12',266019,0,1106,7,'CAD'),
    (366002,2,'2016-01-01','2016-01-12',266019,0,373,1,'CAD'),
    (366002,3,'2016-01-01','2016-01-12',266019,0,1080,4,'CAD'),
    (366010,1,'2016-01-01','2016-01-08',370077,0,618,5,'CAD'),
    (366014,1,'2016-01-01','2016-01-06',738549,0,123,1,'EUR'),
    (366014,2,'2016-01-01','2016-01-06',738549,0,1700,2,'EUR'),
    (367005,1,'2016-01-02','2016-01-10',758280,0,1691,1,'EUR'),
    (367005,2,'2016-01-02','2016-01-10',758280,0,319,2,'EUR'),
    (367005,3,'2016-01-02','2016-01-10',758280,0,1674,8,'EUR'),
    (367005,4,'2016-01-02','2016-01-10',758280,0,2511,9,'EUR')
]

df_sales = spark.createDataFrame(data=data_sales,schema=prog_schema_sales)
df_sales.show(truncate=False)
df_sales.printSchema()
o/p:
===========
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+
|OrderNumber|LineItem|OrderDate |DeliveryDate|CustomerKey|StoreKey|ProductKey|Quantity|CurrencyCode|
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+
|366001     |1       |2016-01-01|2016-01-13  |1269051    |0       |1048      |2       |USD         |
|366001     |2       |2016-01-01|2016-01-13  |1269051    |0       |2007      |1       |USD         |
|366002     |1       |2016-01-01|2016-01-12  |266019     |0       |1106      |7       |CAD         |
|366002     |2       |2016-01-01|2016-01-12  |266019     |0       |373       |1       |CAD         |
|366002     |3       |2016-01-01|2016-01-12  |266019     |0       |1080      |4       |CAD         |
|366010     |1       |2016-01-01|2016-01-08  |370077     |0       |618       |5       |CAD         |
|366014     |1       |2016-01-01|2016-01-06  |738549     |0       |123       |1       |EUR         |
|366014     |2       |2016-01-01|2016-01-06  |738549     |0       |1700      |2       |EUR         |
|367005     |1       |2016-01-02|2016-01-10  |758280     |0       |1691      |1       |EUR         |
|367005     |2       |2016-01-02|2016-01-10  |758280     |0       |319       |2       |EUR         |
|367005     |3       |2016-01-02|2016-01-10  |758280     |0       |1674      |8       |EUR         |
|367005     |4       |2016-01-02|2016-01-10  |758280     |0       |2511      |9       |EUR         |
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+

root
 |-- OrderNumber: integer (nullable = true)
 |-- LineItem: integer (nullable = true)
 |-- OrderDate: string (nullable = true)
 |-- DeliveryDate: string (nullable = true)
 |-- CustomerKey: integer (nullable = true)
 |-- StoreKey: integer (nullable = true)
 |-- ProductKey: integer (nullable = true)
 |-- Quantity: integer (nullable = true)
 |-- CurrencyCode: string (nullable = true)


df_sales_transformed = df_sales.withColumn("OrderDate",to_date(col("OrderDate"),'yyyy-MM-dd'))\
                               .withColumn("DeliveryDate",to_date(col("DeliveryDate"),'yyyy-MM-dd'))

df_sales_transformed.show(truncate=False)
df_sales_transformed.printSchema()
o/p:
========
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+
|OrderNumber|LineItem|OrderDate |DeliveryDate|CustomerKey|StoreKey|ProductKey|Quantity|CurrencyCode|
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+
|366001     |1       |2016-01-01|2016-01-13  |1269051    |0       |1048      |2       |USD         |
|366001     |2       |2016-01-01|2016-01-13  |1269051    |0       |2007      |1       |USD         |
|366002     |1       |2016-01-01|2016-01-12  |266019     |0       |1106      |7       |CAD         |
|366002     |2       |2016-01-01|2016-01-12  |266019     |0       |373       |1       |CAD         |
|366002     |3       |2016-01-01|2016-01-12  |266019     |0       |1080      |4       |CAD         |
|366010     |1       |2016-01-01|2016-01-08  |370077     |0       |618       |5       |CAD         |
|366014     |1       |2016-01-01|2016-01-06  |738549     |0       |123       |1       |EUR         |
|366014     |2       |2016-01-01|2016-01-06  |738549     |0       |1700      |2       |EUR         |
|367005     |1       |2016-01-02|2016-01-10  |758280     |0       |1691      |1       |EUR         |
|367005     |2       |2016-01-02|2016-01-10  |758280     |0       |319       |2       |EUR         |
|367005     |3       |2016-01-02|2016-01-10  |758280     |0       |1674      |8       |EUR         |
|367005     |4       |2016-01-02|2016-01-10  |758280     |0       |2511      |9       |EUR         |
+-----------+--------+----------+------------+-----------+--------+----------+--------+------------+

root
 |-- OrderNumber: integer (nullable = true)
 |-- LineItem: integer (nullable = true)
 |-- OrderDate: date (nullable = true)
 |-- DeliveryDate: date (nullable = true)
 |-- CustomerKey: integer (nullable = true)
 |-- StoreKey: integer (nullable = true)
 |-- ProductKey: integer (nullable = true)
 |-- Quantity: integer (nullable = true)
 |-- CurrencyCode: string (nullable = true)



df_sales_transformed.createOrReplaceTempView("practice")

i. . You need to analyze orders that are billed in USD for financial reporting¶
purposes. Retrieve all orders from the Sales table where the Currency
Code is 'USD'. Include only the OrderNumber, OrderDate, and
DeliveryDate in the results.
=====================================================================================
a. df_sales_data_transformed_filtered = df_sales_transformed.filter(col("CurrencyCode")=="USD")\
                    .select(col("OrderNumber"),col("OrderDate"),col("DeliveryDate"))

df_sales_data_transformed_filtered.show(truncate=False)
df_sales_data_transformed_filtered.printSchema()


b. df_sales_data_transformed_filtered = spark.sql("""select OrderNumber,OrderDate,DeliveryDate 
                                                  from practice
                                                  where CurrencyCode = 'USD'
                                                """)

df_sales_data_transformed_filtered.show(truncate=False)
df_sales_data_transformed_filtered.printSchema()
o/p:
============
+-----------+----------+------------+
|OrderNumber|OrderDate |DeliveryDate|
+-----------+----------+------------+
|366001     |2016-01-01|2016-01-13  |
|366001     |2016-01-01|2016-01-13  |
+-----------+----------+------------+

root
 |-- OrderNumber: integer (nullable = true)
 |-- OrderDate: date (nullable = true)
 |-- DeliveryDate: date (nullable = true)


ii. Write a query to list the ProductKey and total Quantity sold for each
product from the Sales table. Include only those products where the
total quantity sold is greater than 5. Use the HAVING clause to filter
the results.
==============================================================================
a. df_total_qty_sold = df_sales_transformed.groupBy(col("ProductKey"))\
                    .agg(sum(col("Quantity")).alias("total_quantity"))\
                    .filter(col("total_quantity")>5)

df_total_qty_sold.show(truncate=False)
df_total_qty_sold.printSchema()


b. df_total_qty_sold = spark.sql("""select ProductKey,sum(Quantity) as total_quantity
                                 from practice
                                 group by ProductKey
                                 having total_quantity>5""")

df_total_qty_sold.show(truncate=False)
df_total_qty_sold.printSchema()
o/p:
============
+----------+--------------+
|ProductKey|total_quantity|
+----------+--------------+
|1106      |7             |
|1674      |8             |
|2511      |9             |
+----------+--------------+

root
 |-- ProductKey: integer (nullable = true)
 |-- total_quantity: long (nullable = true)


iii. Retrieve the distinct currencies used in sales transactions and the
count of transactions per currency.
====================================================================================
a. df_cnt_transaction = df_sales_transformed.groupBy(col("CurrencyCode"))\
                    .agg(count(col("*")).alias("cnt_of_transactions"))\
                    .sort(col("cnt_of_transactions").desc())

df_cnt_transaction.show(truncate=False)
df_cnt_transaction.printSchema()

b. df_cnt_transaction = spark.sql("""select CurrencyCode,count(*) as cnt_of_transactions
                                  from practice
                                  group by CurrencyCode
                                  order by cnt_of_transactions desc""")

df_cnt_transaction.show(truncate=False)
df_cnt_transaction.printSchema()
o/p:
=============
+------------+-------------------+
|CurrencyCode|cnt_of_transactions|
+------------+-------------------+
|EUR         |6                  |
|CAD         |4                  |
|USD         |2                  |
+------------+-------------------+

root
 |-- CurrencyCode: string (nullable = true)
 |-- cnt_of_transactions: long (nullable = false)


iv. Analyzing High-Value Customers¶
You are tasked with identifying high-value customers who have
made significant purchases in 2016. Specifically, you need to find
customers who have purchased more than 6 items in total in 2016
and whose average quantity per order is greater than 2.

Retrieve the CustomerKey and the total quantity of products
purchased by each customer for orders placed in 2016, only
including customers who have purchased more than 2 items in total
and whose average quantity per order is greater than 2. Order the
results by the total quantity in descending order.
==========================================================================
i. df_final = df_sales_transformed.filter(
                year(col("OrderDate")) == 2016
            ).groupBy(
                col("CustomerKey")
            ).agg(
                sum(col("Quantity")).alias("total_quantity"),
                avg(col("Quantity")).alias("avg_quantity"),
                count(col("OrderNumber")).alias("total_cnt_orders")
            ).filter(
                (col("total_cnt_orders") > 2) &
                (col("avg_quantity") > 2)
            ).sort(
                col("total_quantity").desc()
            )\
            .select(col("CustomerKey"),col("total_quantity"))

df_final.show(truncate=False)   
df_final.printSchema()


ii. df_final = spark.sql("""select CustomerKey,total_quantity from (
                               select CustomerKey,sum(quantity) as total_quantity,
                               avg(quantity) as avg_quantity,
                               count(OrderNumber) as total_cnt_orders
                               from practice
                               where year(OrderDate)='2016'
                               group by CustomerKey
                               having total_cnt_orders>2 AND avg_quantity>2
                               order by total_quantity desc) temp
                               """)
df_final.show(truncate=False)
df_final.printSchema()
o/p:
========
+-----------+--------------+
|CustomerKey|total_quantity|
+-----------+--------------+
|758280     |20            |
|266019     |12            |
+-----------+--------------+

root
 |-- CustomerKey: integer (nullable = true)
 |-- total_quantity: long (nullable = true)


v. Evaluating Store Performance
The sales team wants to evaluate the performance of different
stores by looking at the total quantity of products sold in each store
for 2016. They are particularly interested in stores that have sold
more than 50 items in total.
Retrieve the StoreKey and the total quantity of products sold by
each store for orders placed in 2016, only including stores that have
sold more than 50 items in total. Order the results by the total
quantity in descending order
==============================================================================
a. df_store_performance = df_sales_transformed.filter(
                            year(col("OrderDate")) == 2016
                        ).groupBy(
                            col("StoreKey")
                        ).agg(
                            sum(col("Quantity")).alias("total_quantity"),
                            count(col("OrderNumber")).alias("total_cnt_orders")
                        ).filter(
                            col("total_cnt_orders") > 2
                        ).orderBy(
                            col("total_quantity").desc()
                        ).select(
                            col("StoreKey"),
                            col("total_quantity")
                        )

df_store_performance.show(truncate=False)
df_store_performance.printSchema()


b. df_store_performance = spark.sql("""select StoreKey,total_quantity from (
                                           select StoreKey,sum(quantity) as total_quantity,
                                           count(OrderNumber) as total_cnt_orders
                                           from practice
                                           where year(OrderDate) = '2016'
                                           group by StoreKey
                                           having total_cnt_orders>2
                                           order by total_quantity desc
                                           ) temp
                                           """)

df_store_performance.show(truncate=False)
df_store_performance.printSchema()
o/p:
============
+--------+--------------+
|StoreKey|total_quantity|
+--------+--------------+
|0       |43            |
+--------+--------------+

root
 |-- StoreKey: integer (nullable = true)
 |-- total_quantity: long (nullable = true)



41. Problem statement:
==================================
Given the following dataset, concatenate the values from three columns (col1,col2,col3) with "-" as the separator , ignoring null values.
===============================================================================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()


spark
o/p:
============
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


schema = "col1 string,col2 string, col3 string"

data = [("ab","ad",None),\
        ("aa",None,None),\
        ("df",None,"dd")]

df = spark.createDataFrame(data=data,schema=schema)
df.show(truncate=False)
df.printSchema()
o/p:
==========
+----+----+----+
|col1|col2|col3|
+----+----+----+
|ab  |ad  |null|
|aa  |null|null|
|df  |null|dd  |
+----+----+----+

root
 |-- col1: string (nullable = true)
 |-- col2: string (nullable = true)
 |-- col3: string (nullable = true)
 
 
 df.createOrReplaceTempView("practice")
 
 i. df_final = df.withColumn("result",concat_ws("-",col("col1"),col("col2"),col("col3")))
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+----+----+----+------+
|col1|col2|col3|result|
+----+----+----+------+
|ab  |ad  |null|ab-ad |
|aa  |null|null|aa    |
|df  |null|dd  |df-dd |
+----+----+----+------+

root
 |-- col1: string (nullable = true)
 |-- col2: string (nullable = true)
 |-- col3: string (nullable = true)
 |-- result: string (nullable = false)
 
 ii. df_final = spark.sql("""select col1,col2,col3,concat_ws('-',col1,col2,col3) as result
                        from practice""")

df_final.show(truncate=False)
df_final.printSchema()
o/p:
==========
+----+----+----+------+
|col1|col2|col3|result|
+----+----+----+------+
|ab  |ad  |null|ab-ad |
|aa  |null|null|aa    |
|df  |null|dd  |df-dd |
+----+----+----+------+

root
 |-- col1: string (nullable = true)
 |-- col2: string (nullable = true)
 |-- col3: string (nullable = true)
 |-- result: string (nullable = false)


42. Pyspark/sparksql coding problem:
================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
(301,'Female','Lilly Harding','WANDEARAH EAST','SA','South Australia','5523','Australia','Australia','1939-07-03'),
(325,'Female','Madison Hull','MOUNT BUDD','WA','Western Australia','6522','Australia','Australia','1979-09-27'),
(554,'Female','Claire Ferres','WINJALLOK','VIC','Victoria','3380','Australia','Australia','1947-05-26'),
(786,'Male','Jai Poltpalingada','MIDDLE RIVER','SA','South Australia','5223','Australia','Australia','1957-09-17'),
(1042,'Male','Aidan Pankhurst','TAWONGA SOUTH','VIC','Victoria','3698','Australia','Australia','1965-11-19'),
(1086,'Male','Hayden Clegg','TEMPLERS','SA','South Australia','5371','Australia','Australia','1954-01-20'),
(1133,'Male','Nicholas Caffyn','JUBILEE POCKET','QLD','Queensland','4802','Australia','Australia','1969-11-22'),
(1256,'Male','Lincoln Jenks','KULLOGUM','QLD','Queensland','4660','Australia','Australia','1950-03-12'),
(1314,'Male','Isaac Israel','EDITH RIVER','NT','Northern Territory','852','Australia','Australia','1965-12-21'),
(1568,'Male','Luke Virtue','KOTTA','VIC','Victoria','3565','Australia','Australia','1975-07-25'),
(1675,'Female','Sophia Turner','BALLARAT','VIC','Victoria','3350','Australia','Australia','1985-08-11'),
(1789,'Male','Ethan Brown','CAIRNS','QLD','Queensland','4870','Australia','Australia','1990-02-14'),
(1822,'Female','Olivia Smith','BROOME','WA','Western Australia','6725','Australia','Australia','1988-12-03'),
(1945,'Male','Noah Wilson','DARWIN','NT','Northern Territory','0800','Australia','Australia','1972-06-30'),
(2056,'Female','Amelia Johnson','HOBART','TAS','Tasmania','7000','Australia','Australia','1995-09-19'),
(2198,'Male','William Taylor','GEELONG','VIC','Victoria','3220','Australia','Australia','1983-04-21'),
(2245,'Female','Charlotte White','TOOWOOMBA','QLD','Queensland','4350','Australia','Australia','1978-01-17'),
(2376,'Male','James Martin','ALBANY','WA','Western Australia','6330','Australia','Australia','1968-10-12'),
(2480,'Female','Mia Anderson','MACKAY','QLD','Queensland','4740','Australia','Australia','1992-03-05'),
(2599,'Male','Benjamin Thomas','PORT LINCOLN','SA','South Australia','5606','Australia','Australia','1981-07-27'),
(2678,'Female','Harper Lee','BENDIGO','VIC','Victoria','3550','Australia','Australia','1987-11-09'),
(2789,'Male','Lucas Harris','ROCKHAMPTON','QLD','Queensland','4700','Australia','Australia','1974-05-16'),
(2890,'Female','Ella Walker','KALGOORLIE','WA','Western Australia','6430','Australia','Australia','1998-08-28'),
(2956,'Male','Henry Young','MILDURA','VIC','Victoria','3500','Australia','Australia','1962-12-22'),
(3012,'Female','Grace Hall','BUNBURY','WA','Western Australia','6230','Australia','Australia','1993-06-13')
]

schema_prog = StructType([
    StructField("CustomerID", IntegerType(), True),
    StructField("Gender", StringType(), True),
    StructField("CustomerName", StringType(), True),
    StructField("City", StringType(), True),
    StructField("StateCode", StringType(), True),
    StructField("State", StringType(), True),
    StructField("ZipCode", StringType(), True),
    StructField("Country", StringType(), True),
    StructField("Continent", StringType(), True),
    StructField("DOB", StringType(), True)
])

schema_ddl = "CustomerID int, Gender string, CustomerName string, City string, StateCode string, State string, ZipCode string, Country string, Continent string, DOB string"

df_customers = spark.createDataFrame(data=data,schema=schema_prog)
df_customers.show(truncate=False)
df_customers.printSchema()
o/p:
========
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|CustomerID|Gender|CustomerName     |City          |StateCode|State             |ZipCode|Country  |Continent|DOB       |
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|301       |Female|Lilly Harding    |WANDEARAH EAST|SA       |South Australia   |5523   |Australia|Australia|1939-07-03|
|325       |Female|Madison Hull     |MOUNT BUDD    |WA       |Western Australia |6522   |Australia|Australia|1979-09-27|
|554       |Female|Claire Ferres    |WINJALLOK     |VIC      |Victoria          |3380   |Australia|Australia|1947-05-26|
|786       |Male  |Jai Poltpalingada|MIDDLE RIVER  |SA       |South Australia   |5223   |Australia|Australia|1957-09-17|
|1042      |Male  |Aidan Pankhurst  |TAWONGA SOUTH |VIC      |Victoria          |3698   |Australia|Australia|1965-11-19|
|1086      |Male  |Hayden Clegg     |TEMPLERS      |SA       |South Australia   |5371   |Australia|Australia|1954-01-20|
|1133      |Male  |Nicholas Caffyn  |JUBILEE POCKET|QLD      |Queensland        |4802   |Australia|Australia|1969-11-22|
|1256      |Male  |Lincoln Jenks    |KULLOGUM      |QLD      |Queensland        |4660   |Australia|Australia|1950-03-12|
|1314      |Male  |Isaac Israel     |EDITH RIVER   |NT       |Northern Territory|852    |Australia|Australia|1965-12-21|
|1568      |Male  |Luke Virtue      |KOTTA         |VIC      |Victoria          |3565   |Australia|Australia|1975-07-25|
|1675      |Female|Sophia Turner    |BALLARAT      |VIC      |Victoria          |3350   |Australia|Australia|1985-08-11|
|1789      |Male  |Ethan Brown      |CAIRNS        |QLD      |Queensland        |4870   |Australia|Australia|1990-02-14|
|1822      |Female|Olivia Smith     |BROOME        |WA       |Western Australia |6725   |Australia|Australia|1988-12-03|
|1945      |Male  |Noah Wilson      |DARWIN        |NT       |Northern Territory|0800   |Australia|Australia|1972-06-30|
|2056      |Female|Amelia Johnson   |HOBART        |TAS      |Tasmania          |7000   |Australia|Australia|1995-09-19|
|2198      |Male  |William Taylor   |GEELONG       |VIC      |Victoria          |3220   |Australia|Australia|1983-04-21|
|2245      |Female|Charlotte White  |TOOWOOMBA     |QLD      |Queensland        |4350   |Australia|Australia|1978-01-17|
|2376      |Male  |James Martin     |ALBANY        |WA       |Western Australia |6330   |Australia|Australia|1968-10-12|
|2480      |Female|Mia Anderson     |MACKAY        |QLD      |Queensland        |4740   |Australia|Australia|1992-03-05|
|2599      |Male  |Benjamin Thomas  |PORT LINCOLN  |SA       |South Australia   |5606   |Australia|Australia|1981-07-27|
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+

root
 |-- CustomerID: integer (nullable = true)
 |-- Gender: string (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 |-- StateCode: string (nullable = true)
 |-- State: string (nullable = true)
 |-- ZipCode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Continent: string (nullable = true)
 |-- DOB: string (nullable = true)
 
 i. Change the datatype of existing column:
==================================================
df_customers_transformed = df_customers.withColumn("DOB",to_date(col("DOB"),'yyyy-MM-dd'))
                                       

df_customers_transformed.show(truncate=False)
df_customers_transformed.printSchema()
o/p:
=========
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|CustomerID|Gender|CustomerName     |City          |StateCode|State             |ZipCode|Country  |Continent|DOB       |
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|301       |Female|Lilly Harding    |WANDEARAH EAST|SA       |South Australia   |5523   |Australia|Australia|1939-07-03|
|325       |Female|Madison Hull     |MOUNT BUDD    |WA       |Western Australia |6522   |Australia|Australia|1979-09-27|
|554       |Female|Claire Ferres    |WINJALLOK     |VIC      |Victoria          |3380   |Australia|Australia|1947-05-26|
|786       |Male  |Jai Poltpalingada|MIDDLE RIVER  |SA       |South Australia   |5223   |Australia|Australia|1957-09-17|
|1042      |Male  |Aidan Pankhurst  |TAWONGA SOUTH |VIC      |Victoria          |3698   |Australia|Australia|1965-11-19|
|1086      |Male  |Hayden Clegg     |TEMPLERS      |SA       |South Australia   |5371   |Australia|Australia|1954-01-20|
|1133      |Male  |Nicholas Caffyn  |JUBILEE POCKET|QLD      |Queensland        |4802   |Australia|Australia|1969-11-22|
|1256      |Male  |Lincoln Jenks    |KULLOGUM      |QLD      |Queensland        |4660   |Australia|Australia|1950-03-12|
|1314      |Male  |Isaac Israel     |EDITH RIVER   |NT       |Northern Territory|852    |Australia|Australia|1965-12-21|
|1568      |Male  |Luke Virtue      |KOTTA         |VIC      |Victoria          |3565   |Australia|Australia|1975-07-25|
|1675      |Female|Sophia Turner    |BALLARAT      |VIC      |Victoria          |3350   |Australia|Australia|1985-08-11|
|1789      |Male  |Ethan Brown      |CAIRNS        |QLD      |Queensland        |4870   |Australia|Australia|1990-02-14|
|1822      |Female|Olivia Smith     |BROOME        |WA       |Western Australia |6725   |Australia|Australia|1988-12-03|
|1945      |Male  |Noah Wilson      |DARWIN        |NT       |Northern Territory|0800   |Australia|Australia|1972-06-30|
|2056      |Female|Amelia Johnson   |HOBART        |TAS      |Tasmania          |7000   |Australia|Australia|1995-09-19|
|2198      |Male  |William Taylor   |GEELONG       |VIC      |Victoria          |3220   |Australia|Australia|1983-04-21|
|2245      |Female|Charlotte White  |TOOWOOMBA     |QLD      |Queensland        |4350   |Australia|Australia|1978-01-17|
|2376      |Male  |James Martin     |ALBANY        |WA       |Western Australia |6330   |Australia|Australia|1968-10-12|
|2480      |Female|Mia Anderson     |MACKAY        |QLD      |Queensland        |4740   |Australia|Australia|1992-03-05|
|2599      |Male  |Benjamin Thomas  |PORT LINCOLN  |SA       |South Australia   |5606   |Australia|Australia|1981-07-27|
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
only showing top 20 rows

root
 |-- CustomerID: integer (nullable = true)
 |-- Gender: string (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 |-- StateCode: string (nullable = true)
 |-- State: string (nullable = true)
 |-- ZipCode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Continent: string (nullable = true)
 |-- DOB: date (nullable = true)
 
 df_customers_transformed.createOrReplaceTempView("practice")
 
 ii. You are tasked with verifying the ZIP code format for customers.
Specifically, you need to find customers whose ZIP codes are exactly 3
digits long. Retrieve all customers from the Customer table with ZIP
codes that consist of exactly 3 digits.
===========================================================================
a. df_customers_zip = df_customers_transformed.filter(col("ZipCode").like("___"))
df_customers_zip.show(truncate=False)
df_customers_zip.printSchema()

b. df_customers_zip = spark.sql("""select * from practice
                                where ZipCode like '___'
                            """)
df_customers_zip.show(truncate=False)
df_customers_zip.printSchema()

o/p:
===========
+----------+------+------------+-----------+---------+------------------+-------+---------+---------+----------+
|CustomerID|Gender|CustomerName|City       |StateCode|State             |ZipCode|Country  |Continent|DOB       |
+----------+------+------------+-----------+---------+------------------+-------+---------+---------+----------+
|1314      |Male  |Isaac Israel|EDITH RIVER|NT       |Northern Territory|852    |Australia|Australia|1965-12-21|
+----------+------+------------+-----------+---------+------------------+-------+---------+---------+----------+

root
 |-- CustomerID: integer (nullable = true)
 |-- Gender: string (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 |-- StateCode: string (nullable = true)
 |-- State: string (nullable = true)
 |-- ZipCode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Continent: string (nullable = true)
 |-- DOB: date (nullable = true)
 
 iii. Find all distinct cities from the Customers table.
 ============================================================
 a. df_customers_cities = df_customers_transformed.dropDuplicates(["City"])
df_customers_cities.show(truncate=False)
df_customers_cities.printSchema()
o/p:
=========
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|CustomerID|Gender|CustomerName     |City          |StateCode|State             |ZipCode|Country  |Continent|DOB       |
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
|3012      |Female|Grace Hall       |BUNBURY       |WA       |Western Australia |6230   |Australia|Australia|1993-06-13|
|1789      |Male  |Ethan Brown      |CAIRNS        |QLD      |Queensland        |4870   |Australia|Australia|1990-02-14|
|2789      |Male  |Lucas Harris     |ROCKHAMPTON   |QLD      |Queensland        |4700   |Australia|Australia|1974-05-16|
|1256      |Male  |Lincoln Jenks    |KULLOGUM      |QLD      |Queensland        |4660   |Australia|Australia|1950-03-12|
|2480      |Female|Mia Anderson     |MACKAY        |QLD      |Queensland        |4740   |Australia|Australia|1992-03-05|
|1042      |Male  |Aidan Pankhurst  |TAWONGA SOUTH |VIC      |Victoria          |3698   |Australia|Australia|1965-11-19|
|1675      |Female|Sophia Turner    |BALLARAT      |VIC      |Victoria          |3350   |Australia|Australia|1985-08-11|
|2599      |Male  |Benjamin Thomas  |PORT LINCOLN  |SA       |South Australia   |5606   |Australia|Australia|1981-07-27|
|554       |Female|Claire Ferres    |WINJALLOK     |VIC      |Victoria          |3380   |Australia|Australia|1947-05-26|
|2245      |Female|Charlotte White  |TOOWOOMBA     |QLD      |Queensland        |4350   |Australia|Australia|1978-01-17|
|1945      |Male  |Noah Wilson      |DARWIN        |NT       |Northern Territory|0800   |Australia|Australia|1972-06-30|
|2678      |Female|Harper Lee       |BENDIGO       |VIC      |Victoria          |3550   |Australia|Australia|1987-11-09|
|1822      |Female|Olivia Smith     |BROOME        |WA       |Western Australia |6725   |Australia|Australia|1988-12-03|
|786       |Male  |Jai Poltpalingada|MIDDLE RIVER  |SA       |South Australia   |5223   |Australia|Australia|1957-09-17|
|1133      |Male  |Nicholas Caffyn  |JUBILEE POCKET|QLD      |Queensland        |4802   |Australia|Australia|1969-11-22|
|2056      |Female|Amelia Johnson   |HOBART        |TAS      |Tasmania          |7000   |Australia|Australia|1995-09-19|
|2198      |Male  |William Taylor   |GEELONG       |VIC      |Victoria          |3220   |Australia|Australia|1983-04-21|
|2890      |Female|Ella Walker      |KALGOORLIE    |WA       |Western Australia |6430   |Australia|Australia|1998-08-28|
|2956      |Male  |Henry Young      |MILDURA       |VIC      |Victoria          |3500   |Australia|Australia|1962-12-22|
|1314      |Male  |Isaac Israel     |EDITH RIVER   |NT       |Northern Territory|852    |Australia|Australia|1965-12-21|
+----------+------+-----------------+--------------+---------+------------------+-------+---------+---------+----------+
only showing top 20 rows

root
 |-- CustomerID: integer (nullable = true)
 |-- Gender: string (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 |-- StateCode: string (nullable = true)
 |-- State: string (nullable = true)
 |-- ZipCode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Continent: string (nullable = true)
 |-- DOB: date (nullable = true)
 
 b. df_customers_cities = df_customers_transformed.select(col("City")).distinct()
df_customers_cities.show(truncate=False)
df_customers_cities.printSchema()


c. df_customers_cities = spark.sql("""select distinct City from practice""")
df_customers_cities.show(truncate=False)
df_customers_cities.printSchema()
o/p:
============
+--------------+
|City          |
+--------------+
|BUNBURY       |
|CAIRNS        |
|ROCKHAMPTON   |
|KULLOGUM      |
|MACKAY        |
|TAWONGA SOUTH |
|BALLARAT      |
|PORT LINCOLN  |
|WINJALLOK     |
|TOOWOOMBA     |
|DARWIN        |
|BENDIGO       |
|BROOME        |
|MIDDLE RIVER  |
|JUBILEE POCKET|
|HOBART        |
|GEELONG       |
|KALGOORLIE    |
|MILDURA       |
|TEMPLERS      |
+--------------+
only showing top 20 rows

root
 |-- City: string (nullable = true)
 
 iv. Write a query to find all customers from the Customers table whose City
starts with the letter 'A' using regex. Display CustomerKey, Name, and
City.
================================================================================
a. df_customers_final = df_customers_transformed.filter(col("City").like("A%"))\
                                             .select(col("CustomerID"),col("CustomerName"),col("City"))
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

b. df_customers_final = spark.sql("""select CustomerID,CustomerName,City
                                  from practice
                                  where City like 'A%'
                                  """)
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

c. df_customers_final = df_customers_transformed.filter(col("City").rlike("^[A]"))\
                                             .select(col("CustomerID"),col("CustomerName"),col("City"))
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

d. df_customers_final = spark.sql("""select CustomerID,CustomerName,City
                                  from practice
                                  where City REGEXP '^[A]' 
                                """)
df_customers_final.show(truncate=False)
df_customers_final.printSchema()
o/p:
==========
+----------+------------+------+
|CustomerID|CustomerName|City  |
+----------+------------+------+
|2376      |James Martin|ALBANY|
+----------+------------+------+

root
 |-- CustomerID: integer (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 
 v. Write a query to find all customers from the Customers table whose City
end with the letter 'A' using regex. Display CustomerKey, Name, and
City.
===============================================================================
a. df_customers_final = df_customers_transformed.filter(col("City").like("%A"))\
                                             .select(col("CustomerID"),col("CustomerName"),col("City"))
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

b. df_customers_final = spark.sql("""select CustomerID,CustomerName,City
                                  from practice
                                  where City like '%A'
                                  """)
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

c. df_customers_final = df_customers_transformed.filter(col("City").rlike("[A]$"))\
                                             .select(col("CustomerID"),col("CustomerName"),col("City"))
df_customers_final.show(truncate=False)
df_customers_final.printSchema()

d. df_customers_final = spark.sql("""select CustomerID,CustomerName,City
                                  from practice
                                  where City REGEXP '[A]$' 
                                """)
df_customers_final.show(truncate=False)
df_customers_final.printSchema()
o/p:
============
+----------+---------------+---------+
|CustomerID|CustomerName   |City     |
+----------+---------------+---------+
|1568      |Luke Virtue    |KOTTA    |
|2245      |Charlotte White|TOOWOOMBA|
|2956      |Henry Young    |MILDURA  |
+----------+---------------+---------+

root
 |-- CustomerID: integer (nullable = true)
 |-- CustomerName: string (nullable = true)
 |-- City: string (nullable = true)
 
 
 vi. Retrieve the number of customers whose city name contains exactly
5 letters and starts with 'A'. Display the city name and the count of such
customers, ordering the results by city name in ascending order.
================================================================================
a. df_customers_final_city = df_customers_final.filter(col("City").like("A___"))\
                                            .groupBy(col("City"))\
                                            .agg(count("*").alias("total_count"))\
                                            .orderBy(col("City"))
df_customers_final_city.show(truncate=False)
df_customers_final_city.printSchema()

b. df_customers_final_city = spark.sql("""
    SELECT City,
           COUNT(*) AS total_count
    FROM practice
    WHERE City LIKE 'A___'
    GROUP BY City
    ORDER BY City
""")
df_customers_final_city.show(truncate=False)
df_customers_final_city.printSchema()
o/p:
============
+----+-----------+
|City|total_count|
+----+-----------+
+----+-----------+

root
 |-- City: string (nullable = true)
 |-- total_count: long (nullable = false)
 
 
 43. Pyspark/sparksql interview question:
===================================================
From a given csv file , calculate Expiry date as shown in o/p df by adding RechargeDate column with Remaining_days column:
================================================================================================================================
i/p:
=====
+----------+------------+--------------+--------+
|RechargeId|RechargeDate|Remaining_days|Validity|
+----------+------------+--------------+--------+
|R201623   |20200511    |1             |online  |
|R201873   |20200119    |110           |online  |
|R201999   |20200105    |35            |online  |
|R201951   |20191105    |215           |online  |
+----------+------------+--------------+--------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)


o/p:
=========
+----------+------------+--------------+--------+-----------+
|RechargeId|RechargeDate|Remaining_days|Validity|Expiry_date|
+----------+------------+--------------+--------+-----------+
|R201623   |20200511    |1             |online  |2020-05-12 |
|R201873   |20200119    |110           |online  |2020-05-08 |
|R201999   |20200105    |35            |online  |2020-02-09 |
|R201951   |20191105    |215           |online  |2020-06-07 |
+----------+------------+--------------+--------+-----------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)
 |-- Expiry_date: date (nullable = true)
 
 Solution:
 ==================
 from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [("R201623",20200511,1,"online"),\
        ("R201873",20200119,110,"online"),\
        ("R201999",20200105,35,"online"),\
        ("R201951",20191105,215,"online")]
        
schema_ddl = "RechargeId string,RechargeDate int,Remaining_days int,Validity string"

schema_prog = StructType([\
                         StructField("RechargeId",StringType(),True),\
                         StructField("RechargeDate",StringType(),True),\
                         StructField("Remaining_days",IntegerType(),True),\
                         StructField("Validity",StringType(),True)])
                         
df = spark.createDataFrame(data=data,schema=schema_prog)
df.show(truncate=False)
df.printSchema()
o/p:
==========
+----------+------------+--------------+--------+
|RechargeId|RechargeDate|Remaining_days|Validity|
+----------+------------+--------------+--------+
|R201623   |20200511    |1             |online  |
|R201873   |20200119    |110           |online  |
|R201999   |20200105    |35            |online  |
|R201951   |20191105    |215           |online  |
+----------+------------+--------------+--------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)
 
 df.createOrReplaceTempView("practice")
 
 i. Using df():
==================================

 df_final = df.withColumn("date_s",to_date(col("RechargeDate").cast("string"),'yyyyMMdd'))
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+----------+------------+--------------+--------+----------+
|RechargeId|RechargeDate|Remaining_days|Validity|date_s    |
+----------+------------+--------------+--------+----------+
|R201623   |20200511    |1             |online  |2020-05-11|
|R201873   |20200119    |110           |online  |2020-01-19|
|R201999   |20200105    |35            |online  |2020-01-05|
|R201951   |20191105    |215           |online  |2019-11-05|
+----------+------------+--------------+--------+----------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)
 |-- date_s: date (nullable = true)
 
 df_final_1 = df_final.withColumn("Expiry_date",expr("date_add(date_s,Remaining_days)"))\
                     .drop(col("date_s"))
df_final_1.show(truncate=False)
df_final_1.printSchema()
o/p:
=======
+----------+------------+--------------+--------+-----------+
|RechargeId|RechargeDate|Remaining_days|Validity|Expiry_date|
+----------+------------+--------------+--------+-----------+
|R201623   |20200511    |1             |online  |2020-05-12 |
|R201873   |20200119    |110           |online  |2020-05-08 |
|R201999   |20200105    |35            |online  |2020-02-09 |
|R201951   |20191105    |215           |online  |2020-06-07 |
+----------+------------+--------------+--------+-----------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)
 |-- Expiry_date: date (nullable = true)
 
 
 ii. Using sparksql():
 ============================
 df_final_1 = spark.sql("""
WITH cte1 AS (
    SELECT *,
           TO_DATE(CAST(RechargeDate AS STRING), 'yyyyMMdd') AS date_s
    FROM practice
),
cte2 AS (
    SELECT *,
           DATE_ADD(date_s, Remaining_days) AS Expiry_date
    FROM cte1
)
SELECT RechargeId, RechargeDate, Remaining_days, Validity, Expiry_date
FROM cte2
""")

df_final_1.show(truncate=False)
df_final_1.printSchema()

o/p:
=========
+----------+------------+--------------+--------+-----------+
|RechargeId|RechargeDate|Remaining_days|Validity|Expiry_date|
+----------+------------+--------------+--------+-----------+
|R201623   |20200511    |1             |online  |2020-05-12 |
|R201873   |20200119    |110           |online  |2020-05-08 |
|R201999   |20200105    |35            |online  |2020-02-09 |
|R201951   |20191105    |215           |online  |2020-06-07 |
+----------+------------+--------------+--------+-----------+

root
 |-- RechargeId: string (nullable = true)
 |-- RechargeDate: string (nullable = true)
 |-- Remaining_days: integer (nullable = true)
 |-- Validity: string (nullable = true)
 |-- Expiry_date: date (nullable = true)

    
 44. Pyspark / sparksql coding challenge:
=========================================================
i/p:
=======
+---+----+---+--------+
|ID |NAME|Age|Marks   |
+---+----+---+--------+
|1  |A   |20 |31|32|34|
|2  |B   |21 |21|32|43|
|3  |C   |22 |21|32|11|
|4  |D   |23 |10|12|12|
+---+----+---+--------+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Marks: string (nullable = true)
 
o/p 1:
===================
+---+----+---+-------+---------+----+
|ID |NAME|Age|Physics|Chemistry|Math|
+---+----+---+-------+---------+----+
|1  |A   |20 |31     |32       |34  |
|2  |B   |21 |21     |32       |43  |
|3  |C   |22 |21     |32       |11  |
|4  |D   |23 |10     |12       |12  |
+---+----+---+-------+---------+----+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Physics: string (nullable = true)
 |-- Chemistry: string (nullable = true)
 |-- Math: string (nullable = true)
 
o/p 2:
===========
+---+----+---+-----+
|ID |NAME|AGE|Marks|
+---+----+---+-----+
|1  |A   |20 |31   |
|1  |A   |20 |32   |
|1  |A   |20 |34   |
|2  |B   |21 |21   |
|2  |B   |21 |32   |
|2  |B   |21 |43   |
|3  |C   |22 |21   |
|3  |C   |22 |32   |
|3  |C   |22 |11   |
|4  |D   |23 |10   |
|4  |D   |23 |12   |
|4  |D   |23 |12   |
+---+----+---+-----+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- AGE: integer (nullable = true)
 |-- Marks: string (nullable = true)
 
 
 Solution:
 ==================
 from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


data = [
    (1, 'A', 20, '31|32|34'),
    (2, 'B', 21, '21|32|43'),
    (3, 'C', 22, '21|32|11'),
    (4, 'D', 23, '10|12|12')
]

schema = "ID int, NAME string, Age int, Marks string"

df = spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()
o/p:
============
+---+----+---+--------+
|ID |NAME|Age|Marks   |
+---+----+---+--------+
|1  |A   |20 |31|32|34|
|2  |B   |21 |21|32|43|
|3  |C   |22 |21|32|11|
|4  |D   |23 |10|12|12|
+---+----+---+--------+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Marks: string (nullable = true)
 
 df.createOrReplaceTempView("practice")
 
 i. O/P 1 solution:
===================================
a.  Using df():
=============================
df_final = df.withColumn("Physics", split(col("Marks"), "\\|")[0]) \
             .withColumn("Chemistry", split(col("Marks"), "\\|")[1]) \
             .withColumn("Math", split(col("Marks"), "\\|")[2]) \
             .select("ID", "NAME", "Age", "Physics", "Chemistry", "Math")

df_final.show(truncate=False)
df_final.printSchema()


 b. Using sparksql():
==============================
df_final = spark.sql("""
SELECT
    ID,
    NAME,
    AGE,
    split(Marks,'\\\\|')[0] AS Physics,
    split(Marks,'\\\\|')[1] AS Chemistry,
    split(Marks,'\\\\|')[2] AS Math
FROM practice
""")
df_final.show(truncate=False)
df_final.printSchema()

o/p:
============
+---+----+---+-------+---------+----+
|ID |NAME|AGE|Physics|Chemistry|Math|
+---+----+---+-------+---------+----+
|1  |A   |20 |31     |32       |34  |
|2  |B   |21 |21     |32       |43  |
|3  |C   |22 |21     |32       |11  |
|4  |D   |23 |10     |12       |12  |
+---+----+---+-------+---------+----+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- AGE: integer (nullable = true)
 |-- Physics: string (nullable = true)
 |-- Chemistry: string (nullable = true)
 |-- Math: string (nullable = true)
 
 ii. O/P 2 solution:
 =============================
 a. Using df():
====================================
 df_final_1 = df.select(col("ID"),col("NAME"),col("AGE"),explode(split(col("Marks"),'\\|')).alias("Marks"))
df_final_1.show(truncate=False)
df_final_1.printSchema()


b. Using sparksql():
===================================
df_final_1 = spark.sql("""
SELECT
    ID,
    NAME,
    AGE,
    explode(split(Marks,'\\\\|')) AS Marks
FROM practice
""")

df_final_1.show(truncate=False)
df_final_1.printSchema()

o/p:
===========
+---+----+---+-----+
|ID |NAME|AGE|Marks|
+---+----+---+-----+
|1  |A   |20 |31   |
|1  |A   |20 |32   |
|1  |A   |20 |34   |
|2  |B   |21 |21   |
|2  |B   |21 |32   |
|2  |B   |21 |43   |
|3  |C   |22 |21   |
|3  |C   |22 |32   |
|3  |C   |22 |11   |
|4  |D   |23 |10   |
|4  |D   |23 |12   |
|4  |D   |23 |12   |
+---+----+---+-----+

root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- AGE: integer (nullable = true)
 |-- Marks: string (nullable = true)


45. Pyspark / sparksql coding question:
==================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
(1, "Contoso 512MB MP3 Player E51 Silver", "Contoso", "Silver", 6.62, 12.99, 101, "MP4&MP3", 1, "Audio"),
(2, "Contoso 512MB MP3 Player E51 Blue", "Contoso", "Blue", 7.40, 14.52, 101, "MP4&MP3", 1, "Audio"),
(3, "Contoso 1G MP3 Player E100 White", "Contoso", "White", 11.00, 21.57, 101, "MP4&MP3", 1, "Audio"),
(4, "Contoso 2G MP3 Player E200 Silver", "Contoso", "Silver", 11.00, 21.57, 101, "MP4&MP3", 1, "Audio"),
(5, "Contoso 2G MP3 Player E200 Red", "Contoso", "Red", 11.00, 21.57, 101, "MP4&MP3", 1, "Audio"),
(6, "Contoso 2G MP3 Player E200 Black", "Contoso", "Black", 11.00, 21.57, 101, "MP4&MP3", 1, "Audio"),
(7, "Contoso 2G MP3 Player E200 Blue", "Contoso", "Blue", 30.58, 59.99, 101, "MP4&MP3", 1, "Audio"),
(8, "Contoso 4G MP3 Player E400 Silver", "Contoso", "Silver", 30.58, 59.99, 101, "MP4&MP3", 1, "Audio"),
(9, "Contoso 4G MP3 Player E400 Black", "Contoso", "Black", 30.58, 59.99, 101, "MP4&MP3", 1, "Audio"),
(10, "Contoso 4G MP3 Player E400 Green", "Contoso", "Green", 30.58, 59.99, 101, "MP4&MP3", 1, "Audio"),
(11, "Contoso 4G MP3 Player E400 Orange", "Contoso", "Orange", 35.72, 77.68, 101, "MP4&MP3", 1, "Audio"),
(12, "Contoso 4GB Flash MP3 Player E401 Blue", "Contoso", "Blue", 35.72, 77.68, 101, "MP4&MP3", 1, "Audio"),
(13, "Contoso 4GB Flash MP3 Player E401 Black", "Contoso", "Black", 35.72, 77.68, 101, "MP4&MP3", 1, "Audio"),
(14, "Contoso 4GB Flash MP3 Player E401 Silver", "Contoso", "Silver", 35.72, 77.68, 101, "MP4&MP3", 1, "Audio"),
(15, "Contoso 4GB Flash MP3 Player E401 White", "Contoso", "White", 50.56, 109.95, 101, "MP4&MP3", 1, "Audio"),
(16, "Contoso 8GB Super-Slim MP3/Video Player M800 White", "Contoso", "White", 50.56, 109.95, 101, "MP4&MP3", 1, "Audio"),
(17, "Contoso 8GB Super-Slim MP3/Video Player M800 Red", "Contoso", "Red", 50.56, 109.95, 101, "MP4&MP3", 1, "Audio"),
(18, "Contoso 8GB Super-Slim MP3/Video Player M800 Green", "Contoso", "Green", 50.56, 109.95, 101, "MP4&MP3", 1, "Audio"),
(19, "Contoso 8GB Super-Slim MP3/Video Player M800 Pink", "Contoso", "Pink", 61.62, 134.00, 101, "MP4&MP3", 1, "Audio"),
(20, "Contoso 8GB MP3 Player new model M820 Black", "Contoso", "Black", 61.62, 134.00, 101, "MP4&MP3", 1, "Audio")
]

schema_ddl = """
ProductKey int,
ProductName string,
Brand string,
Color string,
UnitCostUSD float,
UnitPriceUSD float,
SubcategoryKey int,
Subcategory string,
CategoryKey int,
Category string
"""

schema_prog = StructType([
    StructField("ProductKey", IntegerType(), True),
    StructField("ProductName", StringType(), True),
    StructField("Brand", StringType(), True),
    StructField("Color", StringType(), True),
    StructField("UnitCostUSD", FloatType(), True),
    StructField("UnitPriceUSD", FloatType(), True),
    StructField("SubcategoryKey", IntegerType(), True),
    StructField("Subcategory", StringType(), True),
    StructField("CategoryKey", IntegerType(), True),
    StructField("Category", StringType(), True)
])

df = spark.createDataFrame(data=data,schema=schema_prog)
df.show(truncate=False)
df.printSchema()
o/p:
===========
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+
|ProductKey|ProductName                                       |Brand  |Color |UnitCostUSD|UnitPriceUSD|SubcategoryKey|Subcategory|CategoryKey|Category|
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+
|1         |Contoso 512MB MP3 Player E51 Silver               |Contoso|Silver|6.62       |12.99       |101           |MP4&MP3    |1          |Audio   |
|2         |Contoso 512MB MP3 Player E51 Blue                 |Contoso|Blue  |7.4        |14.52       |101           |MP4&MP3    |1          |Audio   |
|3         |Contoso 1G MP3 Player E100 White                  |Contoso|White |11.0       |21.57       |101           |MP4&MP3    |1          |Audio   |
|4         |Contoso 2G MP3 Player E200 Silver                 |Contoso|Silver|11.0       |21.57       |101           |MP4&MP3    |1          |Audio   |
|5         |Contoso 2G MP3 Player E200 Red                    |Contoso|Red   |11.0       |21.57       |101           |MP4&MP3    |1          |Audio   |
|6         |Contoso 2G MP3 Player E200 Black                  |Contoso|Black |11.0       |21.57       |101           |MP4&MP3    |1          |Audio   |
|7         |Contoso 2G MP3 Player E200 Blue                   |Contoso|Blue  |30.58      |59.99       |101           |MP4&MP3    |1          |Audio   |
|8         |Contoso 4G MP3 Player E400 Silver                 |Contoso|Silver|30.58      |59.99       |101           |MP4&MP3    |1          |Audio   |
|9         |Contoso 4G MP3 Player E400 Black                  |Contoso|Black |30.58      |59.99       |101           |MP4&MP3    |1          |Audio   |
|10        |Contoso 4G MP3 Player E400 Green                  |Contoso|Green |30.58      |59.99       |101           |MP4&MP3    |1          |Audio   |
|11        |Contoso 4G MP3 Player E400 Orange                 |Contoso|Orange|35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|12        |Contoso 4GB Flash MP3 Player E401 Blue            |Contoso|Blue  |35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|13        |Contoso 4GB Flash MP3 Player E401 Black           |Contoso|Black |35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|14        |Contoso 4GB Flash MP3 Player E401 Silver          |Contoso|Silver|35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|15        |Contoso 4GB Flash MP3 Player E401 White           |Contoso|White |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
|16        |Contoso 8GB Super-Slim MP3/Video Player M800 White|Contoso|White |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
|17        |Contoso 8GB Super-Slim MP3/Video Player M800 Red  |Contoso|Red   |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
|18        |Contoso 8GB Super-Slim MP3/Video Player M800 Green|Contoso|Green |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
|19        |Contoso 8GB Super-Slim MP3/Video Player M800 Pink |Contoso|Pink  |61.62      |134.0       |101           |MP4&MP3    |1          |Audio   |
|20        |Contoso 8GB MP3 Player new model M820 Black       |Contoso|Black |61.62      |134.0       |101           |MP4&MP3    |1          |Audio   |
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+

root
 |-- ProductKey: integer (nullable = true)
 |-- ProductName: string (nullable = true)
 |-- Brand: string (nullable = true)
 |-- Color: string (nullable = true)
 |-- UnitCostUSD: float (nullable = true)
 |-- UnitPriceUSD: float (nullable = true)
 |-- SubcategoryKey: integer (nullable = true)
 |-- Subcategory: string (nullable = true)
 |-- CategoryKey: integer (nullable = true)
 |-- Category: string (nullable = true)
 
 
 df.createOrReplaceTempView("practice")
 
 i. Find the minimum and maximum price of products from the Products table.
 ===============================================================================
 a. Using df():
=========================
df_max_min_price = df.agg(max(col("UnitPriceUSD")).alias("max_unit_pprice"),\
                          min(col("UnitPriceUSD")).alias("min_unit_price"))
df_max_min_price.show(truncate=False)
df_max_min_price.printSchema()

b. Using sparksql:
============================
df_max_min_price = spark.sql("""select max(UnitPriceUSD) as max_unit_pprice,
                                       min(UnitPriceUSD) as min_unit_price
                                       from practice
                             """)
df_max_min_price.show(truncate=False)
df_max_min_price.printSchema()
o/p:
=========
+---------------+--------------+
|max_unit_pprice|min_unit_price|
+---------------+--------------+
|134.0          |12.99         |
+---------------+--------------+

root
 |-- max_unit_pprice: float (nullable = true)
 |-- min_unit_price: float (nullable = true)


ii. Retrieve the top 5 most expensive products from the Products table,showing only product names and prices.
==================================================================================================================
a. Using df():
========================
df_expensive_product = df.sort(col("UnitPriceUSD").desc())\
                         .limit(5)\
                         .select(col("ProductName"),col("UnitPriceUSD"))
df_expensive_product.show(truncate=False)
df_expensive_product.printSchema()


b. Using sparksql():
==================================
df_expensive_product = spark.sql("""select ProductName,UnitPriceUSD
                                    from practice
                                    order by UnitPriceUSD desc
                                    limit 5
                                """)
df_expensive_product.show(truncate=False)
df_expensive_product.printSchema()
o/p:
=========
+--------------------------------------------------+------------+
|ProductName                                       |UnitPriceUSD|
+--------------------------------------------------+------------+
|Contoso 8GB MP3 Player new model M820 Black       |134.0       |
|Contoso 8GB Super-Slim MP3/Video Player M800 Pink |134.0       |
|Contoso 4GB Flash MP3 Player E401 White           |109.95      |
|Contoso 8GB Super-Slim MP3/Video Player M800 Red  |109.95      |
|Contoso 8GB Super-Slim MP3/Video Player M800 White|109.95      |
+--------------------------------------------------+------------+

root
 |-- ProductName: string (nullable = true)
 |-- UnitPriceUSD: float (nullable = true)
 
 iii. Write a query to find the average Unit Cost USD of products by Brand
from the Products table where the average cost is greater than 5.
Display Brand and the average Unit Cost USD.
=============================================================================
a. Using df():
==================
df_avg_unit = df.groupBy(col("Brand"))\
                .agg(avg(col("UnitCostUSD")).alias("avg_unit_cost_price"))\
                .filter(col("avg_unit_cost_price")>5)

df_avg_unit.show(truncate=False)
df_avg_unit.printSchema()

b. Using sparksql:
=============================
df_avg_unit = spark.sql("""select Brand,avg(UnitCostUSD) as avg_unit_cost_price
                           from practice
                           group by Brand
                           having avg_unit_cost_price>5
                           """)
df_avg_unit.show(truncate=False)
df_avg_unit.printSchema()
o/p:
==========
+-------+-------------------+
|Brand  |avg_unit_cost_price|
+-------+-------------------+
|Contoso|32.43500039577484  |
+-------+-------------------+

root
 |-- Brand: string (nullable = true)
 |-- avg_unit_cost_price: double (nullable = true)
 
 
 iv.  Retrieve all products whose names contain at least two vowels. Also,
ensure that the product name ends with a vowel. Order the results by
product name in ascending order.
===========================================================================
a. Using df():
======================
result_df = (
    df.filter(
        col("ProductName").rlike(r"(?i)(?=(?:.*[aeiou]){2,}).*[aeiou]$")
    )
    .orderBy("ProductName")
)

result_df.show(truncate=False)
result_df.printSchema()

b. Using sparksql:
=========================
result_df = spark.sql("""select * from practice
                         where ProductName REGEXP '(?i)(?=(?:.*[aeiou]){2,}).*[aeiou]$'
                         order by ProductName asc
                         """)
result_df.show(truncate=False)
result_df.printSchema()
o/p:
============
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+
|ProductKey|ProductName                                       |Brand  |Color |UnitCostUSD|UnitPriceUSD|SubcategoryKey|Subcategory|CategoryKey|Category|
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+
|3         |Contoso 1G MP3 Player E100 White                  |Contoso|White |11.0       |21.57       |101           |MP4&MP3    |1          |Audio   |
|7         |Contoso 2G MP3 Player E200 Blue                   |Contoso|Blue  |30.58      |59.99       |101           |MP4&MP3    |1          |Audio   |
|11        |Contoso 4G MP3 Player E400 Orange                 |Contoso|Orange|35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|12        |Contoso 4GB Flash MP3 Player E401 Blue            |Contoso|Blue  |35.72      |77.68       |101           |MP4&MP3    |1          |Audio   |
|15        |Contoso 4GB Flash MP3 Player E401 White           |Contoso|White |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
|2         |Contoso 512MB MP3 Player E51 Blue                 |Contoso|Blue  |7.4        |14.52       |101           |MP4&MP3    |1          |Audio   |
|16        |Contoso 8GB Super-Slim MP3/Video Player M800 White|Contoso|White |50.56      |109.95      |101           |MP4&MP3    |1          |Audio   |
+----------+--------------------------------------------------+-------+------+-----------+------------+--------------+-----------+-----------+--------+

root
 |-- ProductKey: integer (nullable = true)
 |-- ProductName: string (nullable = true)
 |-- Brand: string (nullable = true)
 |-- Color: string (nullable = true)
 |-- UnitCostUSD: float (nullable = true)
 |-- UnitPriceUSD: float (nullable = true)
 |-- SubcategoryKey: integer (nullable = true)
 |-- Subcategory: string (nullable = true)
 |-- CategoryKey: integer (nullable = true)
 |-- Category: string (nullable = true)


v. Find the maximum, minimum, and average unit price of products in
each category. Display the results ordered by the average price in
descending order.
==========================================================================
a. Using df():
====================
df_final = df.groupBy(col("Category"))\
             .agg(max(col("UnitPriceUSD")).alias("max_unit_price"),\
                  min(col("UnitPriceUSD")).alias("min_unit_price"),\
                  avg(col("UnitPriceUSD")).alias("avg_unit_price"))\
             .sort(col("avg_unit_price").desc())
df_final.show(truncate=False)
df_final.printSchema()


b. Using sparksql():
======================================
df_final = df.groupBy(col("Category"))\
             .agg(max(col("UnitPriceUSD")).alias("max_unit_price"),\
                  min(col("UnitPriceUSD")).alias("min_unit_price"),\
                  avg(col("UnitPriceUSD")).alias("avg_unit_price"))\
             .sort(col("avg_unit_price").desc())
df_final.show(truncate=False)
df_final.printSchema()
o/p:
===========
+--------+--------------+--------------+-----------------+
|Category|max_unit_price|min_unit_price|avg_unit_price   |
+--------+--------------+--------------+-----------------+
|Audio   |134.0         |12.99         |68.61349973678588|
+--------+--------------+--------------+-----------------+

root
 |-- Category: string (nullable = true)
 |-- max_unit_price: float (nullable = true)
 |-- min_unit_price: float (nullable = true)
 |-- avg_unit_price: double (nullable = true)
 
 
 vi. Retrieve the ProductKey and Product Name of all products where
the Product Name contains the pattern "MP3 Player". Sort the results by
Product Name in ascending order.
==============================================================================
a. Using df():
======================
df_final_1 = df.filter(col("ProductName").like("%MP3 Player%"))\
               .sort(col("ProductName"))\
               .select(col("ProductKey"),col("ProductName"))
df_final_1.show(truncate=False)
df_final_1.printSchema() 


b.Using sparksql:
========================
df_final_1 = df.filter(col("ProductName").like("%MP3 Player%"))\
               .sort(col("ProductName"))\
               .select(col("ProductKey"),col("ProductName"))
df_final_1.show(truncate=False)
df_final_1.printSchema() 
o/p:
=========
+----------+-------------------------------------------+
|ProductKey|ProductName                                |
+----------+-------------------------------------------+
|3         |Contoso 1G MP3 Player E100 White           |
|6         |Contoso 2G MP3 Player E200 Black           |
|7         |Contoso 2G MP3 Player E200 Blue            |
|5         |Contoso 2G MP3 Player E200 Red             |
|4         |Contoso 2G MP3 Player E200 Silver          |
|9         |Contoso 4G MP3 Player E400 Black           |
|10        |Contoso 4G MP3 Player E400 Green           |
|11        |Contoso 4G MP3 Player E400 Orange          |
|8         |Contoso 4G MP3 Player E400 Silver          |
|13        |Contoso 4GB Flash MP3 Player E401 Black    |
|12        |Contoso 4GB Flash MP3 Player E401 Blue     |
|14        |Contoso 4GB Flash MP3 Player E401 Silver   |
|15        |Contoso 4GB Flash MP3 Player E401 White    |
|2         |Contoso 512MB MP3 Player E51 Blue          |
|1         |Contoso 512MB MP3 Player E51 Silver        |
|20        |Contoso 8GB MP3 Player new model M820 Black|
+----------+-------------------------------------------+

root
 |-- ProductKey: integer (nullable = true)
 |-- ProductName: string (nullable = true)
 
 
 vii. You want to analyze the performance of different brands based on
their products' average selling price and total sales. You need to
find which brands have an average unit price greater than $50 and
ensure that each brand has more than 5 products in the dataset.
Retrieve the Brand, the average Unit Price USD, and the total
number of products for each brand. Only include brands with an
average unit price greater than $50 and having more than 5
products in the dataset. Order the results by the average unit price
in descending order.
================================================================================
a. df_final_2 = df.groupBy(col("Brand"))\
               .agg(avg(col("UnitPriceUSD")).alias("avg_unit_price"),\
                    count(col("ProductKey")).alias("total_sales"))\
               .filter((col("avg_unit_price")>50) & (col("total_sales")>5))\
               .sort(col("avg_unit_price").desc())
df_final_2.show(truncate=False)
df_final_2.printSchema()

b. df_final_2 = spark.sql("""select Brand,avg(UnitPriceUSD) as avg_unit_price,
                                       count(ProductKey) as total_sales
                                       from practice
                                       group by Brand
                                       having avg_unit_price>50 and total_sales>5
                                       order by avg_unit_price desc
                        """)
df_final_2.show(truncate=False)
df_final_2.printSchema()
o/p:
===========
+-------+-----------------+-----------+
|Brand  |avg_unit_price   |total_sales|
+-------+-----------------+-----------+
|Contoso|68.61349973678588|20         |
+-------+-----------------+-----------+

root
 |-- Brand: string (nullable = true)
 |-- avg_unit_price: double (nullable = true)
 |-- total_sales: long (nullable = false)
 
 
 
46. deposits ( user_id, deposit_id, deposit_date, deposit_amount )
Find out which user made the highest number of deposits in a single day.
Also shows the total number of deposits made by all users on that same day.
Result:- user_id | deposits_date | deposits_by_user | deposits_made_that_day
   1              | 2019-01-01       | 5                       | 13
================================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


data = [
    (1, 101, '2019-01-01', 100.00),\
    (1, 102, '2019-01-01',150.00),\
    (1, 103, '2019-01-01',200.00),\
    (1, 104, '2019-01-01',120.00),\
    (1, 105, '2019-01-01',130.00),\
    (2, 201, '2019-01-01',300.00),\
    (2, 202, '2019-01-01',220.00),\
    (2, 203, '2019-01-01',180.00),\
    (2, 204, '2019-01-01',160.00),
    (3, 301, '2019-01-01',90.00),\
    (3, 302, '2019-01-01',110.00),\
    (3, 303, '2019-01-01',130.00),\
    (4, 401, '2019-01-01',500.00),\
    (1, 106, '2019-01-02',200.00),\
    (2, 205, '2019-01-02',300.00)
]

schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("deposit_id", IntegerType(), True),
    StructField("deposit_date", StringType(), True),
    StructField("deposit_amount", FloatType(), True)
])

df_deposits = spark.createDataFrame(data, schema)

df_deposits.show(truncate=False)
df_deposits.printSchema()
o/p:
==========
+-------+----------+------------+--------------+
|user_id|deposit_id|deposit_date|deposit_amount|
+-------+----------+------------+--------------+
|1      |101       |2019-01-01  |100.0         |
|1      |102       |2019-01-01  |150.0         |
|1      |103       |2019-01-01  |200.0         |
|1      |104       |2019-01-01  |120.0         |
|1      |105       |2019-01-01  |130.0         |
|2      |201       |2019-01-01  |300.0         |
|2      |202       |2019-01-01  |220.0         |
|2      |203       |2019-01-01  |180.0         |
|2      |204       |2019-01-01  |160.0         |
|3      |301       |2019-01-01  |90.0          |
|3      |302       |2019-01-01  |110.0         |
|3      |303       |2019-01-01  |130.0         |
|4      |401       |2019-01-01  |500.0         |
|1      |106       |2019-01-02  |200.0         |
|2      |205       |2019-01-02  |300.0         |
+-------+----------+------------+--------------+

root
 |-- user_id: integer (nullable = true)
 |-- deposit_id: integer (nullable = true)
 |-- deposit_date: string (nullable = true)
 |-- deposit_amount: float (nullable = true)
 
 
 df_deposits.createOrReplaceTempView("practice")
 
 i. Using df():
======================
df_deposit_per_day = df_deposits.groupBy(col("user_id"),col("deposit_date"))\
                                .agg(count(col("deposit_id")).alias("deposits_by_user"))
                                     
df_deposit_per_day.show(truncate=False)
df_deposit_per_day.printSchema()
o/p:
==========
+-------+------------+----------------+
|user_id|deposit_date|deposits_by_user|
+-------+------------+----------------+
|1      |2019-01-02  |1               |
|2      |2019-01-02  |1               |
|2      |2019-01-01  |4               |
|4      |2019-01-01  |1               |
|3      |2019-01-01  |3               |
|1      |2019-01-01  |5               |
+-------+------------+----------------+

root
 |-- user_id: integer (nullable = true)
 |-- deposit_date: string (nullable = true)
 |-- deposits_by_user: long (nullable = false)
 
 winspec = Window.partitionBy("deposit_date")

df_result = df_deposit_per_day.withColumn(
    "deposits_made_that_day",
    sum("deposits_by_user").over(winspec)
)

df_result.show()
o/p:
========
+-------+------------+----------------+----------------------+
|user_id|deposit_date|deposits_by_user|deposits_made_that_day|
+-------+------------+----------------+----------------------+
|      4|  2019-01-01|               1|                    13|
|      3|  2019-01-01|               3|                    13|
|      2|  2019-01-01|               4|                    13|
|      1|  2019-01-01|               5|                    13|
|      1|  2019-01-02|               1|                     2|
|      2|  2019-01-02|               1|                     2|
+-------+------------+----------------+----------------------+

winspec1 = Window.orderBy(col("deposits_by_user").desc())
df_highest_deposit = df_result.withColumn("rn",row_number().over(winspec1))\
                              .filter(col("rn")==1)\
                              .drop(col("rn"))
df_highest_deposit.show(truncate=False)
df_highest_deposit.printSchema()
o/p:
=========
+-------+------------+----------------+----------------------+
|user_id|deposit_date|deposits_by_user|deposits_made_that_day|
+-------+------------+----------------+----------------------+
|1      |2019-01-01  |5               |13                    |
+-------+------------+----------------+----------------------+

root
 |-- user_id: integer (nullable = true)
 |-- deposit_date: string (nullable = true)
 |-- deposits_by_user: long (nullable = false)
 |-- deposits_made_that_day: long (nullable = true)
 
 
 ii. Using sparksql():
==============================
df_highest_deposit = spark.sql("""
WITH cte1 AS (
    SELECT
        user_id,
        deposit_date,
        COUNT(deposit_id) AS deposits_by_user
    FROM practice
    GROUP BY user_id, deposit_date
),
cte2 AS (
    SELECT
        *,
        SUM(deposits_by_user) OVER (PARTITION BY deposit_date) AS deposits_made_that_day
    FROM cte1
),
cte3 AS (
    SELECT
        *,
        ROW_NUMBER() OVER (ORDER BY deposits_by_user DESC) AS rn
    FROM cte2
)
SELECT
    user_id,
    deposit_date,
    deposits_by_user,
    deposits_made_that_day
FROM cte3
WHERE rn = 1
""")
df_highest_deposit.show(truncate=False)
df_highest_deposit.printSchema()
o/p:
==========
+-------+------------+----------------+----------------------+
|user_id|deposit_date|deposits_by_user|deposits_made_that_day|
+-------+------------+----------------+----------------------+
|1      |2019-01-01  |5               |13                    |
+-------+------------+----------------+----------------------+

root
 |-- user_id: integer (nullable = true)
 |-- deposit_date: string (nullable = true)
 |-- deposits_by_user: long (nullable = false)
 |-- deposits_made_that_day: long (nullable = true)
 
 
47. Find the largest store (MAX(Square Meters)) for each country. Order the results by the¶
country name in ascending order.
========================================================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data_store = [
(1,"Australia","Australian Capital Territory",595,"2008-01-01"),
(2,"Australia","Northern Territory",665,"2008-01-12"),
(3,"Australia","South Australia",2000,"2012-01-07"),
(4,"Australia","Tasmania",2000,"2010-01-01"),
(5,"Australia","Victoria",2000,"2015-12-09"),
(6,"Australia","Western Australia",2000,"2010-01-01"),
(7,"Canada","New Brunswick",1105,"2007-05-07"),
(8,"Canada","Newfoundland and Labrador",2105,"2014-07-02"),
(9,"Canada","Northwest Territories",1500,"2005-03-04"),
(10,"Canada","Nunavut",1210,"2015-04-04"),
(11,"Canada","Yukon",1210,"2009-06-03"),
(12,"France","Basse-Normandie",350,"2012-06-06"),
(13,"France","Corse",245,"2013-06-07"),
(14,"France","Franche-Comté",350,"2009-12-15"),
(15,"France","La Réunion",400,"2015-01-01"),
(16,"France","Limousin",385,"2010-06-03"),
(17,"France","Martinique",350,"2007-07-08"),
(18,"France","Mayotte",310,"2012-08-08"),
(19,"Germany","Berlin",1295,"2015-04-04"),
(20,"Germany","Brandenburg",1715,"2012-12-15"),
(21,"Germany","Freie Hansestadt Bremen",560,"2018-06-03"),
(22,"Germany","Freistaat Thüringen",2000,"2008-03-06"),
(23,"Germany","Hamburg",1365,"2010-01-01"),
(24,"Germany","Hessen",1855,"2012-12-15"),
(25,"Germany","Mecklenburg-Vorpommern",1610,"2010-01-01"),
(26,"Germany","Saarland",350,"2019-03-05"),
(27,"Germany","Sachsen-Anhalt",2000,"2008-08-08"),
(28,"Italy","Caltanissetta",1200,"2012-12-15"),
(29,"Italy","Enna",1000,"2008-01-01"),
(30,"Italy","Pesaro",2100,"2008-01-12"),
(31,"Netherlands","Drenthe",1085,"2012-01-07"),
(32,"Netherlands","Flevoland",910,"2010-01-01"),
(33,"Netherlands","Friesland",1540,"2015-12-09"),
(34,"Netherlands","Groningen",1365,"2010-01-01"),
(35,"Netherlands","Zeeland",1225,"2007-05-07"),
(36,"United Kingdom","Armagh",1300,"2014-07-02"),
(37,"United Kingdom","Ayrshire",2100,"2005-03-04"),
(38,"United Kingdom","Belfast",1800,"2015-04-04"),
(39,"United Kingdom","Blaenau Gwent",2100,"2009-06-03"),
(40,"United Kingdom","Dungannon and South Tyrone",1300,"2012-06-06"),
(41,"United Kingdom","Fermanagh",2100,"2013-06-07"),
(42,"United Kingdom","North Down",1900,"2009-12-15"),
(43,"United States","Alaska",1190,"2015-01-01"),
(44,"United States","Arkansas",2000,"2010-06-03"),
(45,"United States","Connecticut",2000,"2007-07-08"),
(46,"United States","Delaware",1015,"2012-08-08"),
(47,"United States","Hawaii",1120,"2015-04-04"),
(48,"United States","Idaho",1540,"2012-12-15"),
(49,"United States","Iowa",2000,"2018-06-03"),
(50,"United States","Kansas",2000,"2008-03-06"),
(51,"United States","Maine",1295,"2010-01-01"),
(52,"United States","Mississippi",2000,"2009-06-03"),
(53,"United States","Montana",1260,"2012-06-06"),
(54,"United States","Nebraska",2000,"2013-06-07"),
(55,"United States","Nevada",2000,"2009-12-15"),
(56,"United States","New Hampshire",1260,"2015-01-01"),
(57,"United States","New Mexico",1645,"2010-06-03"),
(58,"United States","North Dakota",1330,"2007-07-08"),
(59,"United States","Oregon",2000,"2012-08-08"),
(60,"United States","Rhode Island",1260,"2005-04-04"),
(61,"United States","South Carolina",2000,"2012-12-15"),
(62,"United States","South Dakota",1120,"2018-06-03"),
(63,"United States","Utah",2000,"2008-03-06"),
(64,"United States","Washington DC",1330,"2010-01-01"),
(65,"United States","West Virginia",1785,"2012-01-01"),
(66,"United States","Wyoming",840,"2014-01-01"),
(0,"Online","Online",None,"2010-01-01")
]

schema_store_ddl = "StoreKey int,Country string,State string,SquareMeters int,OpenDate string"

schema_store_prog = StructType([\
                               StructField("StoreKey",IntegerType(),True),\
                               StructField("Country",StringType(),True),\
                               StructField("State",StringType(),True),\
                               StructField("SquareMeters",IntegerType(),True),\
                               StructField("OpenDate",StringType(),True)])

df_stores = spark.createDataFrame(data=data_store,schema=schema_store_prog)
df_stores.show(truncate=False)
df_stores.printSchema()
o/p:
==========
+--------+---------+----------------------------+------------+----------+
|StoreKey|Country  |State                       |SquareMeters|OpenDate  |
+--------+---------+----------------------------+------------+----------+
|1       |Australia|Australian Capital Territory|595         |2008-01-01|
|2       |Australia|Northern Territory          |665         |2008-01-12|
|3       |Australia|South Australia             |2000        |2012-01-07|
|4       |Australia|Tasmania                    |2000        |2010-01-01|
|5       |Australia|Victoria                    |2000        |2015-12-09|
|6       |Australia|Western Australia           |2000        |2010-01-01|
|7       |Canada   |New Brunswick               |1105        |2007-05-07|
|8       |Canada   |Newfoundland and Labrador   |2105        |2014-07-02|
|9       |Canada   |Northwest Territories       |1500        |2005-03-04|
|10      |Canada   |Nunavut                     |1210        |2015-04-04|
|11      |Canada   |Yukon                       |1210        |2009-06-03|
|12      |France   |Basse-Normandie             |350         |2012-06-06|
|13      |France   |Corse                       |245         |2013-06-07|
|14      |France   |Franche-Comté               |350         |2009-12-15|
|15      |France   |La Réunion                  |400         |2015-01-01|
|16      |France   |Limousin                    |385         |2010-06-03|
|17      |France   |Martinique                  |350         |2007-07-08|
|18      |France   |Mayotte                     |310         |2012-08-08|
|19      |Germany  |Berlin                      |1295        |2015-04-04|
|20      |Germany  |Brandenburg                 |1715        |2012-12-15|
+--------+---------+----------------------------+------------+----------+
only showing top 20 rows

root
 |-- StoreKey: integer (nullable = true)
 |-- Country: string (nullable = true)
 |-- State: string (nullable = true)
 |-- SquareMeters: integer (nullable = true)
 |-- OpenDate: string (nullable = true)
 
 
df_stores.createOrReplaceTempView("practice")


i. Using df():
============================
df_largest_store = df_stores.groupBy(col("Country"))\
                            .agg(max(col("SquareMeters")).alias("max_squares_meter"))\
                            .sort(col("Country").asc())
df_largest_store.show(truncate=False)
df_largest_store.printSchema()


ii. Using sparksql:
================================
df_largest_store = spark.sql("""select Country,max(SquareMeters) as max_squares_meter
                                from practice
                                group by Country
                                order by Country asc
                            """)
df_largest_store.show(truncate=False)
df_largest_store.printSchema()

o/p:
==============
+--------------+-----------------+
|Country       |max_squares_meter|
+--------------+-----------------+
|Australia     |2000             |
|Canada        |2105             |
|France        |400              |
|Germany       |2000             |
|Italy         |2100             |
|Netherlands   |1540             |
|Online        |null             |
|United Kingdom|2100             |
|United States |2000             |
+--------------+-----------------+

root
 |-- Country: string (nullable = true)
 |-- max_squares_meter: integer (nullable = true)
 
 
 48. Pyspark/sparksql coding question:
===========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


data = [('Lucky Kumar',),\
        ('Raj Singh',),\
        ('Vivek Yadav',)]

schema_ddl = "Full_name string"
df = spark.createDataFrame(data=data,schema=schema_ddl)
df.show(truncate=False)
df.printSchema()
o/p:
==========
+-----------+
|Full_name  |
+-----------+
|Lucky Kumar|
|Raj Singh  |
|Vivek Yadav|
+-----------+

root
 |-- Full_name: string (nullable = true)
 
 df.createOrReplaceTempView("practice")
 
 i. Using df():
=================================
df_final = df.withColumn("First_name",split(col("Full_name"),' ')[0])\
             .withColumn("Last_name",split(col("Full_name"),' ')[1])

df_final.show(truncate=False)
df_final.printSchema()


ii. Using sparksql:
==============================
df_final = spark.sql("""select Full_name,
                               split(Full_name,' ')[0] as First_name,
                               split(Full_name,' ')[1] as Last_name
                        from practice
                    """)
df_final.show(truncate=False)
df_final.printSchema()

o/p:
===========
+-----------+----------+---------+
|Full_name  |First_name|Last_name|
+-----------+----------+---------+
|Lucky Kumar|Lucky     |Kumar    |
|Raj Singh  |Raj       |Singh    |
|Vivek Yadav|Vivek     |Yadav    |
+-----------+----------+---------+

root
 |-- Full_name: string (nullable = true)
 |-- First_name: string (nullable = true)
 |-- Last_name: string (nullable = true)


49. Pyspark/sparksql coding question:
===========================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
============
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data_state = [('Bihar',),\
              ('Assam',),\
              ('Orissa',)]

schema_state = "State string"

df_state = spark.createDataFrame(data=data_state,schema=schema_state)
df_state.show(truncate=False)
df_state.printSchema()
o/p:
============
+------+
|State |
+------+
|Bihar |
|Assam |
|Orissa|
+------+

root
 |-- State: string (nullable = true)
 
 df_state.createOrReplaceTempView("practice")
 
i.  df_final = df_state.selectExpr(
    "*",
    """
    CASE
        WHEN State = 'Bihar' THEN 101
        WHEN State = 'Assam' THEN 102
        WHEN State = 'Orissa' THEN 103
        ELSE NULL
    END AS Std_code
    """
)
df_final.show(truncate=False)
df_final.printSchema()


ii. df_final = df_state.select("State",expr("""CASE 
                                               WHEN State = 'Bihar' THEN 101
                                               WHEN State = 'Assam' THEN 102
                                               WHEN State = 'Orissa' THEN 103
                                               ELSE NULL
                                            END AS Std_code
                                        """))
df_final.show(truncate=False)
df_final.printSchema()



iii. df_final = df_state.withColumn(
    "Std_code",
    when(col("State") == "Bihar", 101)
    .when(col("State") == "Assam", 102)
    .when(col("State") == "Orissa", 103)
    .otherwise(None)
)

df_final.show(truncate=False)
df_final.printSchema()



iv. Using sparksql:
==========================
df_final = spark.sql("""
SELECT *,
       CASE
           WHEN State = 'Bihar' THEN 101
           WHEN State = 'Assam' THEN 102
           WHEN State = 'Orissa' THEN 103
           ELSE NULL
       END AS Std_code
FROM practice
""")

df_final.show(truncate=False)
df_final.printSchema()

o/p:
===========
+------+--------+
|State |Std_code|
+------+--------+
|Bihar |101     |
|Assam |102     |
|Orissa|103     |
+------+--------+

root
 |-- State: string (nullable = true)
 |-- Std_code: integer (nullable = true)



50. Pyspark/spark sql coding question:
=====================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()

spark
o/p:
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data = [
("2015-01-01","USD",1.0000),
("2015-01-01","CAD",1.1583),
("2015-01-01","AUD",1.2214),
("2015-01-01","EUR",0.8237),
("2015-01-01","GBP",0.6415),

("2015-01-02","USD",1.0000),
("2015-01-02","CAD",1.1682),
("2015-01-02","AUD",1.2323),
("2015-01-02","EUR",0.8304),
("2015-01-02","GBP",0.6477),

("2015-01-03","USD",1.0000),
("2015-01-03","CAD",1.1682),
("2015-01-03","AUD",1.2323),
("2015-01-03","EUR",0.8304),
("2015-01-03","GBP",0.6477),

("2015-01-04","USD",1.0000),
("2015-01-04","CAD",1.1682),
("2015-01-04","AUD",1.2323),
("2015-01-04","EUR",0.8304),
("2015-01-04","GBP",0.6477),

("2015-01-05","USD",1.0000),
("2015-01-05","CAD",1.1784),
("2015-01-05","AUD",1.2384),
("2015-01-05","EUR",0.8393),
("2015-01-05","GBP",0.6569),

("2015-01-06","USD",1.0000),
("2015-01-06","CAD",1.1763),
("2015-01-06","AUD",1.2288),
("2015-01-06","EUR",0.8393),
("2015-01-06","GBP",0.6582),

("2015-01-07","USD",1.0000),
("2015-01-07","CAD",1.1830),
("2015-01-07","AUD",1.2391),
("2015-01-07","EUR",0.8452),
("2015-01-07","GBP",0.6612),

("2015-01-08","USD",1.0000),
("2015-01-08","CAD",1.1816),
("2015-01-08","AUD",1.2337),
("2015-01-08","EUR",0.8498),
("2015-01-08","GBP",0.6637),

("2015-01-09","USD",1.0000),
("2015-01-09","CAD",1.1820),
("2015-01-09","AUD",1.2280),
("2015-01-09","EUR",0.8465),
("2015-01-09","GBP",0.6602),

("2015-01-10","USD",1.0000),
("2015-01-10","CAD",1.1820),
("2015-01-10","AUD",1.2280),
("2015-01-10","EUR",0.8465),
("2015-01-10","GBP",0.6602),

("2015-01-11","USD",1.0000),
("2015-01-11","CAD",1.1820),
("2015-01-11","AUD",1.2280),
("2015-01-11","EUR",0.8465),
("2015-01-11","GBP",0.6602),

("2015-01-12","USD",1.0000),
("2015-01-12","CAD",1.1897),
("2015-01-12","AUD",1.2282),
("2015-01-12","EUR",0.8472),
("2015-01-12","GBP",0.6586),

("2015-01-13","USD",1.0000),
("2015-01-13","CAD",1.1835),
("2015-01-13","AUD",1.2230),
("2015-01-13","EUR",0.8488),
("2015-01-13","GBP",0.6538),

("2015-01-14","USD",1.0000),
("2015-01-14","CAD",1.1789),
("2015-01-14","AUD",1.2245),
("2015-01-14","EUR",0.8495),
("2015-01-14","GBP",0.6516),

("2015-01-15","USD",1.0000),
("2015-01-15","CAD",1.2032),
("2015-01-15","AUD",1.2387),
("2015-01-15","EUR",0.8607),
("2015-01-15","GBP",0.6609),

("2015-01-16","USD",1.0000),
("2015-01-16","CAD",1.2097),
("2015-01-16","AUD",1.2375),
("2015-01-16","EUR",0.8621),
("2015-01-16","GBP",0.6582),

("2015-01-17","USD",1.0000),
("2015-01-17","CAD",1.2097),
("2015-01-17","AUD",1.2375),
("2015-01-17","EUR",0.8621),
("2015-01-17","GBP",0.6582),

("2015-01-18","USD",1.0000),
("2015-01-18","CAD",1.2097),
("2015-01-18","AUD",1.2375),
("2015-01-18","EUR",0.8621),
("2015-01-18","GBP",0.6582),

("2015-01-19","USD",1.0000),
("2015-01-19","CAD",1.2067),
("2015-01-19","AUD",1.2346),
("2015-01-19","EUR",0.8612),
("2015-01-19","GBP",0.6571),

("2015-01-20","USD",1.0000),
("2015-01-20","CAD",1.2074),
("2015-01-20","AUD",1.2304),
("2015-01-20","EUR",0.8635),
("2015-01-20","GBP",0.6608)
]

schema = StructType([
    StructField("Date", StringType(), True),
    StructField("Currency", StringType(), True),
    StructField("Exchange", DoubleType(), True)
])

df = spark.createDataFrame(data, schema)

print(df.count())  # 100
df.show(truncate=False)
df.printSchema()
o/p:
=========
100
+----------+--------+--------+
|Date      |Currency|Exchange|
+----------+--------+--------+
|2015-01-01|USD     |1.0     |
|2015-01-01|CAD     |1.1583  |
|2015-01-01|AUD     |1.2214  |
|2015-01-01|EUR     |0.8237  |
|2015-01-01|GBP     |0.6415  |
|2015-01-02|USD     |1.0     |
|2015-01-02|CAD     |1.1682  |
|2015-01-02|AUD     |1.2323  |
|2015-01-02|EUR     |0.8304  |
|2015-01-02|GBP     |0.6477  |
|2015-01-03|USD     |1.0     |
|2015-01-03|CAD     |1.1682  |
|2015-01-03|AUD     |1.2323  |
|2015-01-03|EUR     |0.8304  |
|2015-01-03|GBP     |0.6477  |
|2015-01-04|USD     |1.0     |
|2015-01-04|CAD     |1.1682  |
|2015-01-04|AUD     |1.2323  |
|2015-01-04|EUR     |0.8304  |
|2015-01-04|GBP     |0.6477  |
+----------+--------+--------+
only showing top 20 rows

root
 |-- Date: string (nullable = true)
 |-- Currency: string (nullable = true)
 |-- Exchange: double (nullable = true)
 
 
df.createOrReplaceTempView("parctice")

i. Finding the Highest Exchange Rate for Each Currency¶
You want to identify the highest exchange rate recorded for each
currency across different dates. This will help you understand the
peak value for each currency during the given period.
Retrieve the maximum exchange rate (MAX(Exchange)) for each
currency.
==========================================================================
a. Using df():
======================
df_highest_exchng_rate = df.groupBy(col("Currency"))\
                           .agg(max(col("Exchange")).alias("max_exchange_rate"))

df_highest_exchng_rate.show(truncate=False)
df_highest_exchng_rate.printSchema()


b. Using sparksql:
============================
df_highest_exchng_rate = spark.sql("""select Currency,max(Exchange) as max_exchange_rate
                                      from parctice
                                      group by Currency
                                      """)

df_highest_exchng_rate.show(truncate=False)
df_highest_exchng_rate.printSchema()

o/p:
===========
+--------+-----------------+
|Currency|max_exchange_rate|
+--------+-----------------+
|GBP     |0.6637           |
|CAD     |1.2097           |
|EUR     |0.8635           |
|AUD     |1.2391           |
|USD     |1.0              |
+--------+-----------------+

root
 |-- Currency: string (nullable = true)
 |-- max_exchange_rate: double (nullable = true)
 
 
 ii. Analyzing Exchange Rate Trends Over Time¶
You want to find out how many days each currency had an
exchange rate higher than 1.0. This will give you insight into the
frequency of stronger currencies compared to the USD.
Count the number of days (COUNT(Date)) where the exchange rate
for each currency was greater than 1.0. Only include currencies
where the count is more than 3 days. Order the results by the count
in descending order
================================================================================
a. Using df():
==========================================
df_final = df.filter(col("Exchange")>1.0)\
             .groupBy(col("Currency"))\
             .agg(count(col("Date")).alias("num_of_days"))\
             .filter(col("num_of_days")>3)\
             .sort(col("num_of_days").desc())

df_final.show(truncate=False)
df_final.printSchema()


b. Using sparksql:
===========================
df_final = spark.sql("""select Currency,count(Date) as num_of_days
                        from parctice
                        where Exchange > 1.0
                        group by Currency
                        having num_of_days > 3
                        order by num_of_days desc
                        """)
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=========
+--------+-----------+
|Currency|num_of_days|
+--------+-----------+
|AUD     |20         |
|CAD     |20         |
+--------+-----------+

root
 |-- Currency: string (nullable = true)
 |-- num_of_days: long (nullable = false)
 
 
 
 
 
 
 
 
 
 
 50. Write an SQL query/ Pyspark  to report the customer ids from the Customer table that bought all the products in the Product table.
 ===============================================================================================================================================
 
Customer table:
 
+-------------+-------------+
 
| customer_id | product_key |
 
+-------------+-------------+
 
| 1           | 5           |
 
| 2           | 6           |
 
| 3           | 5           |
 
| 3           | 6           |
 
| 1           | 6           |
 
| 1           | 5           |
 
+-------------+-------------+
 
  
 
Product table:
 
+-------------+
 
| product_key |
 
+-------------+
 
| 5           |
 
| 6           |
 
+-------------+
 
  
 
Output:  
 
+-------------+
 
| customer_id |
 
+-------------+
 
| 1           |
 
| 3           |

 solution:
================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        
spark
o/p:
========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


data = [
    (1, 5),
    (2, 6),
    (3, 5),
    (3, 6),
    (1, 6),
    (1, 5)
]

columns = ["customer_id", "product_key"]

df_customer = spark.createDataFrame(data, columns)

df_customer.show()
df_customer.printSchema()
o/p:
===========
+-----------+-----------+
|customer_id|product_key|
+-----------+-----------+
|          1|          5|
|          2|          6|
|          3|          5|
|          3|          6|
|          1|          6|
|          1|          5|
+-----------+-----------+

root
 |-- customer_id: long (nullable = true)
 |-- product_key: long (nullable = true)



df_customer.createOrReplaceTempView("customers")

product_data = [
    (5,),
    (6,)
]

product_columns = ["product_key"]

df_product = spark.createDataFrame(product_data, product_columns)

df_product.show()
o/p:
========
+-----------+
|product_key|
+-----------+
|          5|
|          6|
+-----------+


df_product.createOrReplaceTempView("products")

i. Using df():
=======================
df_result = df_customer.alias("c") \
    .join(
        df_product.alias("p"),
        on="product_key",
        how="inner"
    ) \
    .select("customer_id") \
    .distinct()

df_result.show()
o/p:
=======
+-----------+
|customer_id|
+-----------+
|          1|
|          3|
|          2|
+-----------+


df_result = df_customer.alias("c") \
    .join(
        df_product.alias("p"),
        on="product_key",
        how="inner"
    ) \
    .groupBy(col("c.customer_id"))\
    .agg(count("*").alias("count"))\
    .where(col("count")>1)\
    .select(col("customer_id"))

df_result.show()
o/p:
========
+-----------+
|customer_id|
+-----------+
|          1|
|          3|
+-----------+


ii. Using sparksql:
=========================
df_result = spark.sql("""with cte as (select c.customer_id,count(*) as total_count from customers c
                                      inner join products p 
                                      on c.product_key = p.product_key
                                      group by c.customer_id
                                      having total_count>1
                                      )
                                      select customer_id from cte
                                      """)
df_result.show()
o/p:
=======
+-----------+
|customer_id|
+-----------+
|          1|
|          3|
+-----------+


51. Pyspark/spark sql coding problem:
===================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass
username = getpass.getuser()
spark = SparkSession.\
        builder.\
        config("spark.ui.port",'0').\
        config("spark.sql.warehouse.dir",f"/user/{username}/warehouse").\
        enableHiveSupport().\
        master('yarn').\
        getOrCreate()
        

spark
o/p:
============================
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


sales_data = [("2024-01-01",20000),\
              ("2024-01-02",10000),\
              ("2024-01-03",150000),\
              ("2024-01-04",10000),\
              ("2024-01-05",210000)]


sales_schema_ddl = "sales_date string,sales_amount int"

sales_schema_prog = StructType([\
                               StructField("sales_date",StringType(),True),\
                               StructField("sales_amount",IntegerType(),True)])
                               
                               
sales_df = spark.createDataFrame(data=sales_data,schema=sales_schema_prog)
sales_df.show(truncate=False)
sales_df.printSchema()
o/p:
===========
+----------+------------+
|sales_date|sales_amount|
+----------+------------+
|2024-01-01|20000       |
|2024-01-02|10000       |
|2024-01-03|150000      |
|2024-01-04|10000       |
|2024-01-05|210000      |
+----------+------------+

root
 |-- sales_date: string (nullable = true)
 |-- sales_amount: integer (nullable = true)
 
sales_df_new = sales_df.withColumn("sales_date",to_date(col("sales_date"),'yyyy-MM-dd'))
sales_df_new.show(truncate=False)
sales_df_new.printSchema()
o/p:
==========
+----------+------------+
|sales_date|sales_amount|
+----------+------------+
|2024-01-01|20000       |
|2024-01-02|10000       |
|2024-01-03|150000      |
|2024-01-04|10000       |
|2024-01-05|210000      |
+----------+------------+

root
 |-- sales_date: date (nullable = true)
 |-- sales_amount: integer (nullable = true)


sales_df_new.createOrReplaceTempView("practice")


i. Find out cummulative sales or running total sales:
=============================================================
a. Using df():
=====================
winspec = Window.orderBy(col("sales_date"))

df_cummulative_sales = sales_df_new.withColumn("running_total",sum(col("sales_amount")).over(winspec))
df_cummulative_sales.show(truncate=False)
df_cummulative_sales.printSchema()


b. using sparksql:
=======================
df_cummulative_sales = spark.sql("""select *,sum(sales_amount) over(order by sales_date asc) as  running_total
                                    from practice
                                """)
df_cummulative_sales.show(truncate=False)
df_cummulative_sales.printSchema()

o/p:
============
+----------+------------+-------------+
|sales_date|sales_amount|running_total|
+----------+------------+-------------+
|2024-01-01|20000       |20000        |
|2024-01-02|10000       |30000        |
|2024-01-03|150000      |180000       |
|2024-01-04|10000       |190000       |
|2024-01-05|210000      |400000       |
+----------+------------+-------------+

root
 |-- sales_date: date (nullable = true)
 |-- sales_amount: integer (nullable = true)
 |-- running_total: long (nullable = true)
 
 
 ii. Find out the previous sales:
 =========================================
 a. Using df():
=====================
winspec = Window.orderBy(col("sales_date"))

df_previous_sales = sales_df_new.withColumn("previous_sales",lag(col("sales_amount")).over(winspec))
df_previous_sales.show(truncate=False)
df_previous_sales.printSchema()


b. using sparksql:
=======================
df_previous_sales = spark.sql("""select *,lag(sales_amount) over(order by sales_date asc) as  previous_sales
                                    from practice
                                """)
df_previous_sales.show(truncate=False)
df_previous_sales.printSchema()

o/p:
============
+----------+------------+--------------+
|sales_date|sales_amount|previous_sales|
+----------+------------+--------------+
|2024-01-01|20000       |null          |
|2024-01-02|10000       |20000         |
|2024-01-03|150000      |10000         |
|2024-01-04|10000       |150000        |
|2024-01-05|210000      |10000         |
+----------+------------+--------------+

root
 |-- sales_date: date (nullable = true)
 |-- sales_amount: integer (nullable = true)
 |-- previous_sales: integer (nullable = true)
 
 
 iii. Find out the next sales:
=======================================
 a. Using df():
=====================
winspec = Window.orderBy(col("sales_date"))

df_next_sales = sales_df_new.withColumn("next_sales",lead(col("sales_amount")).over(winspec))
df_next_sales.show(truncate=False)
df_next_sales.printSchema()


b. using sparksql:
=======================
df_next_sales = spark.sql("""select *,lead(sales_amount) over(order by sales_date asc) as  next_sales
                                    from practice
                                """)
df_next_sales.show(truncate=False)
df_next_sales.printSchema()

o/p:
============
+----------+------------+----------+
|sales_date|sales_amount|next_sales|
+----------+------------+----------+
|2024-01-01|20000       |10000     |
|2024-01-02|10000       |150000    |
|2024-01-03|150000      |10000     |
|2024-01-04|10000       |210000    |
|2024-01-05|210000      |null      |
+----------+------------+----------+

root
 |-- sales_date: date (nullable = true)
 |-- sales_amount: integer (nullable = true)
 |-- next_sales: integer (nullable = true)

  
    






