1. Get column wise Null record count using Pyspark/sparksql:
================================================================
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
employee_data = [
(1,'John','Doe','john.doe@gmail.com',9876543210,101,1001,50000,10,201,1),
(2,'Jane','Smith','jane.smith@gmail.com',9876543211,102,1002,60000,15,202,2),
(3,'Mike','Brown','mike.brown@gmail.com',9876543212,103,1003,45000,None,201,1),
(4,'Sara','Wilson','sara.wilson@gmail.com',9876543213,104,1004,70000,20,203,3),
(5,'David','Lee','david.lee@gmail.com',9876543214,105,1005,52000,None,None,2),
(6,'Chris','Evans','chris.evans@gmail.com',9876543215,106,1001,48000,5,202,1),
(7,'Emma','Watson','emma.watson@gmail.com',9876543216,107,1002,65000,10,203,3),
(8,'Robert','Downey','robert@gmail.com',None,108,1003,80000,25,204,4),
(9,'Scarlett','Johansson','scarlett@gmail.com',9876543218,109,1004,72000,None,204,4),
(10,'Tom','Holland','tom@gmail.com',9876543219,110,1005,55000,12,None,2),
(11,'Bruce','Wayne','bruce@gmail.com',9876543220,111,1001,90000,30,205,5),
(12,'Clark','Kent','clark@gmail.com',9876543221,112,1002,88000,None,205,5),
(13,'Diana','Prince','diana@gmail.com',9876543222,113,1003,77000,18,None,3),
(14,'Barry','Allen','barry@gmail.com',None,114,1004,68000,15,206,3),
(15,'Arthur','Curry','arthur@gmail.com',9876543224,115,1005,62000,None,206,4),
(16,'Tony','Stark','tony@gmail.com',9876543225,116,1001,95000,35,None,5),
(17,'Steve','Rogers','steve@gmail.com',9876543226,117,1002,87000,22,207,5),
(18,'Natasha','Romanoff','natasha@gmail.com',None,118,1003,73000,None,207,4),
(19,'Peter','Parker','peter@gmail.com',9876543228,119,1004,50000,8,None,2),
(20,'Wanda','Maximoff','wanda@gmail.com',9876543229,120,1005,78000,None,208,3)
]
employee_schema = StructType([
StructField("Employee_id", IntegerType(), True),
StructField("First_name", StringType(), True),
StructField("Last_name", StringType(), True),
StructField("Email", StringType(), True),
StructField("Phone_number", LongType(), True),
StructField("Hire_id", IntegerType(), True),
StructField("Job_id", LongType(), True),
StructField("Salary", IntegerType(), True),
StructField("Commisssion_pct", IntegerType(), True),
StructField("Manager_Id", IntegerType(), True),
StructField("department_id", IntegerType(), True)
])

df_employee = spark.createDataFrame(employee_data, schema=employee_schema)

df_employee.show(truncate=False)
df_employee.printSchema()
o/p:
===========
+-----------+----------+---------+---------------------+------------+-------+------+------+---------------+----------+-------------+
|Employee_id|First_name|Last_name|Email                |Phone_number|Hire_id|Job_id|Salary|Commisssion_pct|Manager_Id|department_id|
+-----------+----------+---------+---------------------+------------+-------+------+------+---------------+----------+-------------+
|1          |John      |Doe      |john.doe@gmail.com   |9876543210  |101    |1001  |50000 |10             |201       |1            |
|2          |Jane      |Smith    |jane.smith@gmail.com |9876543211  |102    |1002  |60000 |15             |202       |2            |
|3          |Mike      |Brown    |mike.brown@gmail.com |9876543212  |103    |1003  |45000 |null           |201       |1            |
|4          |Sara      |Wilson   |sara.wilson@gmail.com|9876543213  |104    |1004  |70000 |20             |203       |3            |
|5          |David     |Lee      |david.lee@gmail.com  |9876543214  |105    |1005  |52000 |null           |null      |2            |
|6          |Chris     |Evans    |chris.evans@gmail.com|9876543215  |106    |1001  |48000 |5              |202       |1            |
|7          |Emma      |Watson   |emma.watson@gmail.com|9876543216  |107    |1002  |65000 |10             |203       |3            |
|8          |Robert    |Downey   |robert@gmail.com     |null        |108    |1003  |80000 |25             |204       |4            |
|9          |Scarlett  |Johansson|scarlett@gmail.com   |9876543218  |109    |1004  |72000 |null           |204       |4            |
|10         |Tom       |Holland  |tom@gmail.com        |9876543219  |110    |1005  |55000 |12             |null      |2            |
|11         |Bruce     |Wayne    |bruce@gmail.com      |9876543220  |111    |1001  |90000 |30             |205       |5            |
|12         |Clark     |Kent     |clark@gmail.com      |9876543221  |112    |1002  |88000 |null           |205       |5            |
|13         |Diana     |Prince   |diana@gmail.com      |9876543222  |113    |1003  |77000 |18             |null      |3            |
|14         |Barry     |Allen    |barry@gmail.com      |null        |114    |1004  |68000 |15             |206       |3            |
|15         |Arthur    |Curry    |arthur@gmail.com     |9876543224  |115    |1005  |62000 |null           |206       |4            |
|16         |Tony      |Stark    |tony@gmail.com       |9876543225  |116    |1001  |95000 |35             |null      |5            |
|17         |Steve     |Rogers   |steve@gmail.com      |9876543226  |117    |1002  |87000 |22             |207       |5            |
|18         |Natasha   |Romanoff |natasha@gmail.com    |null        |118    |1003  |73000 |null           |207       |4            |
|19         |Peter     |Parker   |peter@gmail.com      |9876543228  |119    |1004  |50000 |8              |null      |2            |
|20         |Wanda     |Maximoff |wanda@gmail.com      |9876543229  |120    |1005  |78000 |null           |208       |3            |
+-----------+----------+---------+---------------------+------------+-------+------+------+---------------+----------+-------------+

root
 |-- Employee_id: integer (nullable = true)
 |-- First_name: string (nullable = true)
 |-- Last_name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Phone_number: long (nullable = true)
 |-- Hire_id: integer (nullable = true)
 |-- Job_id: long (nullable = true)
 |-- Salary: integer (nullable = true)
 |-- Commisssion_pct: integer (nullable = true)
 |-- Manager_Id: integer (nullable = true)
 |-- department_id: integer (nullable = true)
df_employee.createOrReplaceTempView("null_count")

i. Approach 1st To get null count for each column one by one:
==============================================================
a. Using df:
=====================
print("Employee_id:", df_employee.filter(col("Employee_id").isNull()).count())
print("First_name:", df_employee.filter(col("First_name").isNull()).count())
print("Last_name:", df_employee.filter(col("Last_name").isNull()).count())
print("Email:", df_employee.filter(col("Email").isNull()).count())
print("Phone_number:", df_employee.filter(col("Phone_number").isNull()).count())
print("Hire_id:", df_employee.filter(col("Hire_id").isNull()).count())
print("Job_id:", df_employee.filter(col("Job_id").isNull()).count())
print("Salary:", df_employee.filter(col("Salary").isNull()).count())
print("Commisssion_pct:", df_employee.filter(col("Commisssion_pct").isNull()).count())
print("Manager_Id:", df_employee.filter(col("Manager_Id").isNull()).count())
print("department_id:", df_employee.filter(col("department_id").isNull()).count())  
o/p:
=======
Employee_id: 0
First_name: 0
Last_name: 0
Email: 0
Phone_number: 3
Hire_id: 0
Job_id: 0
Salary: 0
Commisssion_pct: 7
Manager_Id: 5
department_id: 0

b. Using sparksql:
=========================
i. Using case statement + sum():
================================
df_null_count = spark.sql("""SELECT 
    SUM(CASE WHEN Employee_id IS NULL THEN 1 ELSE 0 END) AS Employee_id,
    SUM(CASE WHEN First_name IS NULL THEN 1 ELSE 0 END) AS First_name,
    SUM(CASE WHEN Last_name IS NULL THEN 1 ELSE 0 END) AS Last_name,
    SUM(CASE WHEN Email IS NULL THEN 1 ELSE 0 END) AS Email,
    SUM(CASE WHEN Phone_number IS NULL THEN 1 ELSE 0 END) AS Phone_number,
    SUM(CASE WHEN Hire_id IS NULL THEN 1 ELSE 0 END) AS Hire_id,
    SUM(CASE WHEN Job_id IS NULL THEN 1 ELSE 0 END) AS Job_id,
    SUM(CASE WHEN Salary IS NULL THEN 1 ELSE 0 END) AS Salary,
    SUM(CASE WHEN Commisssion_pct IS NULL THEN 1 ELSE 0 END) AS Commisssion_pct,
    SUM(CASE WHEN Manager_Id IS NULL THEN 1 ELSE 0 END) AS Manager_Id,
    SUM(CASE WHEN department_id IS NULL THEN 1 ELSE 0 END) AS department_id
FROM null_count""")
df_null_count.show()
o/p:
=======
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+
|Employee_id|First_name|Last_name|Email|Phone_number|Hire_id|Job_id|Salary|Commisssion_pct|Manager_Id|department_id|
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+
|          0|         0|        0|    0|           3|      0|     0|     0|              7|         5|            0|
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+

ii.Using union all + count():
================================
df_null_count = spark.sql("""
SELECT 'Employee_id' AS column_name, COUNT(*) AS total_null_count
FROM null_count
WHERE Employee_id IS NULL

UNION ALL

SELECT 'First_name', COUNT(*)
FROM null_count
WHERE First_name IS NULL

UNION ALL

SELECT 'Last_name', COUNT(*)
FROM null_count
WHERE Last_name IS NULL

UNION ALL

SELECT 'Email', COUNT(*)
FROM null_count
WHERE Email IS NULL

UNION ALL

SELECT 'Phone_number', COUNT(*)
FROM null_count
WHERE Phone_number IS NULL

UNION ALL

SELECT 'Hire_id', COUNT(*)
FROM null_count
WHERE Hire_id IS NULL

UNION ALL

SELECT 'Job_id', COUNT(*)
FROM null_count
WHERE Job_id IS NULL

UNION ALL

SELECT 'Salary', COUNT(*)
FROM null_count
WHERE Salary IS NULL

UNION ALL

SELECT 'Commisssion_pct', COUNT(*)
FROM null_count
WHERE Commisssion_pct IS NULL

UNION ALL

SELECT 'Manager_Id', COUNT(*)
FROM null_count
WHERE Manager_Id IS NULL

UNION ALL

SELECT 'department_id', COUNT(*)
FROM null_count
WHERE department_id IS NULL
""")

df_null_count.show()
o/p:
=======
+---------------+----------------+
|    column_name|total_null_count|
+---------------+----------------+
|    Employee_id|               0|
|     First_name|               0|
|      Last_name|               0|
|          Email|               0|
|   Phone_number|               3|
|        Hire_id|               0|
|         Job_id|               0|
|         Salary|               0|
|Commisssion_pct|               7|
|     Manager_Id|               5|
|  department_id|               0|
+---------------+----------------+

ii. Approach 2nd To get null count dynamically for every column:
==================================================================
a. Using df():
===============
col1 = df_employee.columns
for i in col1:
    print(i)
o/p:
=======
Employee_id
First_name
Last_name
Email
Phone_number
Hire_id
Job_id
Salary
Commisssion_pct
Manager_Id
department_id

df_null_count = df_employee.select([
    count(when(col(i).isNull(), i)).alias(i)
    for i in col1
])

df_null_count.show()
o/p:
=====
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+
|Employee_id|First_name|Last_name|Email|Phone_number|Hire_id|Job_id|Salary|Commisssion_pct|Manager_Id|department_id|
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+
|          0|         0|        0|    0|           3|      0|     0|     0|              7|         5|            0|
+-----------+----------+---------+-----+------------+-------+------+------+---------------+----------+-------------+


2. How to find Data Skewness in spark/How to get count of rows from each partition in spark:
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
df = spark.read.format("csv")\
          .option("header",True)\
          .option("inferSchema",True)\
          .option("sep",",")\
          .option("path","/public/trendytech/orders_wh")\
          .load()
df.show(truncate=False)
o/p:
======
+--------+---------------------+-----------+---------------+
|order_id|order_date           |customer_id|order_status   |
+--------+---------------------+-----------+---------------+
|1       |2013-07-25 00:00:00.0|11599      |CLOSED         |
|2       |2013-07-25 00:00:00.0|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00.0|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00.0|8827       |CLOSED         |
|5       |2013-07-25 00:00:00.0|11318      |COMPLETE       |
|6       |2013-07-25 00:00:00.0|7130       |COMPLETE       |
|7       |2013-07-25 00:00:00.0|4530       |COMPLETE       |
|8       |2013-07-25 00:00:00.0|2911       |PROCESSING     |
|9       |2013-07-25 00:00:00.0|5657       |PENDING_PAYMENT|
|10      |2013-07-25 00:00:00.0|5648       |PENDING_PAYMENT|
|11      |2013-07-25 00:00:00.0|918        |PAYMENT_REVIEW |
|12      |2013-07-25 00:00:00.0|1837       |CLOSED         |
|13      |2013-07-25 00:00:00.0|9149       |PENDING_PAYMENT|
|14      |2013-07-25 00:00:00.0|9842       |PROCESSING     |
|15      |2013-07-25 00:00:00.0|2568       |COMPLETE       |
|16      |2013-07-25 00:00:00.0|7276       |PENDING_PAYMENT|
|17      |2013-07-25 00:00:00.0|2667       |COMPLETE       |
|18      |2013-07-25 00:00:00.0|1205       |CLOSED         |
|19      |2013-07-25 00:00:00.0|9488       |PENDING_PAYMENT|
|20      |2013-07-25 00:00:00.0|9198       |PROCESSING     |
+--------+---------------------+-----------+---------------+
df.printSchema()
o/p:
=======
root
 |-- order_id: integer (nullable = true)
 |-- order_date: string (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
df.count()
o/p:
========
68883
df.rdd.getNumPartitions()
o/p:
=======
1
df_count1 = df.select(spark_partition_id().alias("partition_id"))\
              .groupBy(col("partition_id"))\
              .count()
df_count1.show(truncate=False)
o/p:
=======
+------------+-----+
|partition_id|count|
+------------+-----+
|0           |68883|
+------------+-----+
From above output we conclude a single partition (partition 0) is holding entire data that is 68883 records, so it is skewwed partition,
so to resolve this we will use repartition().

df_repartition = df.repartition(8)
df_repartition.rdd.getNumPartitions()
o/p:
========
8
df_count = df_repartition.select(spark_partition_id().alias("partition_id"))\
                         .groupBy(col("partition_id"))\
                         .count()
df_count.show(truncate=False)
o/p:
=======
+------------+-----+
|partition_id|count|
+------------+-----+
|1           |8610 |
|6           |8611 |
|3           |8610 |
|5           |8610 |
|4           |8610 |
|7           |8611 |
|2           |8610 |
|0           |8611 |
+------------+-----+

3. Total no of partitions and total rows in each partitions:
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


4.  distinct() vs dropDuplicates():
===============================================
i. distinct(): To remove duplicate from entire row but not subset of columns.
ii. dropDuplicates(): To remove duplicate from entire row + subset of columns:

soln:
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
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

mylist = [(1,"Kapil",34),\
           (1,"Kapil",34),\
           (1,"Sathish",26),\
           (2,"Sathish",26)]

df = spark.createDataFrame(data=mylist).toDF("id","name","age")
df.show(truncate=False)
df.printSchema()
o/p:
=========
+---+-------+---+
|id |name   |age|
+---+-------+---+
|1  |Kapil  |34 |
|1  |Kapil  |34 |
|1  |Sathish|26 |
|2  |Sathish|26 |
+---+-------+---+

root
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- age: long (nullable = true)


i. To remove duplicate from entire row but not subset of columns:
==========================================================================
df1 = df.distinct()
df1.show(truncate=False)
o/p:
=========
+---+-------+---+
|id |name   |age|
+---+-------+---+
|1  |Sathish|26 |
|1  |Kapil  |34 |
|2  |Sathish|26 |
+---+-------+---+

ii. To remove duplicate from entire row + subset of columns:
========================================================================
a. df1 = df.dropDuplicates()
df1.show(truncate=False)
o/p:
=========
+---+-------+---+
|id |name   |age|
+---+-------+---+
|1  |Sathish|26 |
|1  |Kapil  |34 |
|2  |Sathish|26 |
+---+-------+---+

b. df1 = df.dropDuplicates(["name","age"])
df1.show(truncate=False)
o/p:
=========
+---+-------+---+
|id |name   |age|
+---+-------+---+
|1  |Sathish|26 |
|1  |Kapil  |34 |
+---+-------+---+

c. df1 = df.dropDuplicates(["id"])
df1.show(truncate=False)
o/p:
=======
+---+-------+---+
|id |name   |age|
+---+-------+---+
|1  |Sathish|26 |
|2  |Sathish|26 |
+---+-------+---+


5. Ambiguoty error problem:
=======================================
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

emp_data = [
    (1, "John", 101),
    (2, "Alice", 102),
    (3, "Bob", 103)
]

emp_df = spark.createDataFrame(emp_data, ["id", "name", "dept_id"])
emp_df.show(truncate=False)
emp_df.printSchema()
o/p:
========
+---+-----+-------+
|id |name |dept_id|
+---+-----+-------+
|1  |John |101    |
|2  |Alice|102    |
|3  |Bob  |103    |
+---+-----+-------+

root
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- dept_id: long (nullable = true)

dept_data = [
    (101, "HR"),
    (102, "IT"),
    (103, "Finance")
]

dept_df = spark.createDataFrame(dept_data, ["dept_id", "name"])
dept_df.show(truncate=False)
dept_df.printSchema()
o/p:
==========
+-------+-------+
|dept_id|name   |
+-------+-------+
|101    |HR     |
|102    |IT     |
|103    |Finance|
+-------+-------+

root
 |-- dept_id: long (nullable = true)
 |-- name: string (nullable = true)

i. Ambiguoty error problem:
===================================
df_joined = emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'inner')\
                  .select("id","name","dept_id")
df_joined.show(truncate=False)
df_joined.printSChema()
o/p:
==========
AnalysisException: Reference 'name' is ambiguous, could be: name, name.


There are two ways to resolve ambiguous problem:
1. Using .withColumnRenamed(), before joining the df rename the ambigous column name in one of the df.
2. After joining and before selecting the column , try to drop the ambiguous column from one of the df.


1. Using .withColumnRenamed(), before joining the df rename the ambigous column name in one of the df:
============================================================================================================
emp_df = emp_df.withColumnRenamed("name","name_new")\
               .withColumnRenamed("dept_id","dept_id_new")

df_joined = emp_df.join(dept_df,emp_df.dept_id_new==dept_df.dept_id,'inner')\
                  .select("id","name","dept_id")
df_joined.show(truncate=False)
df_joined.printSchema()
o/p:
=========
+---+-------+-------+
|id |name   |dept_id|
+---+-------+-------+
|3  |Finance|103    |
|1  |HR     |101    |
|2  |IT     |102    |
+---+-------+-------+

root
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- dept_id: long (nullable = true)

2.  After joining and before selecting the column , try to drop the ambiguous column from one of the df:
===============================================================================================================
df_joined = emp_df.join(
    dept_df,
    emp_df.dept_id == dept_df.dept_id,
    "inner"
).drop(dept_df["dept_id"], dept_df["name"]) \
 .select("id", "name", "dept_id")

df_joined.show(truncate=False)
o/p:
======
output will be displayed.


6. Use of union(),unionAll(),unionByName(),distinct(),intersect(),interesctAll(),substract(),exceptAll():
======================================================================================================================
i. Use of union():¶
===========================================
a. This is used when both dataframe that is df1 and df2 have same schema that is column name and datatype.
b. It preserve duplicate in case of pyspark but in case of sql it removes duplicates.
c. To remove duplicate we should use distinct / dropDuplicates().

Impt Note to remember about union() in case of df and spark sql:
========================================================================
a. In case of pyspark df() union() behaves as unionall() and it does not remove duplicate record by default , to remove duplicate we should use distinct()/dropDuplicates() , so in terms of performance it is fast in case of pyspark df().
b. In case of sparksql union() behaves as sql union() and removes duplicate record automatically by default , we do not have to use distinct()/dropDuplicates explicitly so here performance wise union() in case of sparksql is low/slow.

Code:
=============
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

data1 = [(1,"maheer","male"),\
         (2,"wafa","male")]

schema_ddl_1 = "id integer,name string,gender string"
schema_prog_1 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("gender",StringType(),True)])

df1 = spark.createDataFrame(data=data1,schema=schema_ddl_1)
df1.show(truncate=False)
df1.printSchema()
o/p:
========
+---+------+------+
|id |name  |gender|
+---+------+------+
|1  |maheer|male  |
|2  |wafa  |male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)

data2 = [(3,"asi","female"),\
         (4,"ayesha","female"),\
         (1,"maheer","male")]

schema_ddl_2 = "id integer,name string,gender string"
schema_prog_2 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("gender",StringType(),True)])

df2 = spark.createDataFrame(data=data2,schema=schema_ddl_2)
df2.show(truncate=False)
df2.printSchema()
o/p:
========
+---+------+------+
|id |name  |gender|
+---+------+------+
|3  |asi   |female|
|4  |ayesha|female|
|1  |maheer|male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)

df1.createOrReplaceTempView("practice1")
df2.createOrReplaceTempView("practice2")

df_final_union = df1.union(df2)
df_final_union.show(truncate=False)
df_final_union.printSchema()
o/p:
========
+---+------+------+
|id |name  |gender|
+---+------+------+
|1  |maheer|male  |
|2  |wafa  |male  |
|3  |asi   |female|
|4  |ayesha|female|
|1  |maheer|male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)

To remove duplicate using distinct()/dropDuplicates():
==========================================================================
df_final_union.distinct().show(truncate=False)
o/p:
=========
+---+------+------+
|id |name  |gender|
+---+------+------+
|4  |ayesha|female|
|2  |wafa  |male  |
|1  |maheer|male  |
|3  |asi   |female|
+---+------+------+

df_final_union.dropDuplicates().show()
o/p:
=========
+---+------+------+
| id|  name|gender|
+---+------+------+
|  4|ayesha|female|
|  2|  wafa|  male|
|  1|maheer|  male|
|  3|   asi|female|
+---+------+------+


df_final_union = spark.sql("""select id,name,gender from practice1
                              union 
                              select id,name,gender from practice2""")
df_final_union.show(truncate=False)
df_final_union.printSchema()
o/p:
=========
+---+------+------+
|id |name  |gender|
+---+------+------+
|4  |ayesha|female|
|2  |wafa  |male  |
|1  |maheer|male  |
|3  |asi   |female|
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)


ii. Use of unionAll():
===========================================
i. This is used when both dataframe that is df1 and df2 have same schema that is column name and datatype.
ii. It preserve duplicate in case of pyspark but in case of sql it removes duplicates.
iii. To remove duplicate we should use distinct / dropDuplicates().
Impt Note to remember about union() in case of df and spark sql:¶
i. In case of pyspark df() unionAll() behaves as unionall() and it does not remove duplicate record by default , to remove duplicate we should use distinct()/dropDuplicates() , so in terms of performance it is fast in case of pyspark df().
ii. In case of sparksql union() behaves as sql unionAll() does not removes duplicate record automatically by default , we have to use distinct()/dropDuplicates explicitly so here performance wise unionAll() in case of sparksql is high/fast

Code:
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
o/p:
=========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data1 = [(1,"maheer","male"),\
         (2,"wafa","male")]

schema_ddl_1 = "id integer,name string,gender string"
schema_prog_1 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("gender",StringType(),True)])

df1 = spark.createDataFrame(data=data1,schema=schema_ddl_1)
df1.show(truncate=False)
df1.printSchema()
o/p:
=========
+---+------+------+
|id |name  |gender|
+---+------+------+
|1  |maheer|male  |
|2  |wafa  |male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)

data2 = [(3,"asi","female"),\
         (4,"ayesha","female"),\
         (1,"maheer","male")]

schema_ddl_2 = "id integer,name string,gender string"
schema_prog_2 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("gender",StringType(),True)])

df2 = spark.createDataFrame(data=data2,schema=schema_ddl_2)
df2.show(truncate=False)
df2.printSchema()
o/p:
=======
+---+------+------+
|id |name  |gender|
+---+------+------+
|3  |asi   |female|
|4  |ayesha|female|
|1  |maheer|male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)

df1.createOrReplaceTempView("practice1")
df2.createOrReplaceTempView("practice2")

df_final_unionAll = df1.unionAll(df2)
df_final_unionAll.show(truncate=False)
df_final_unionAll.printSchema()
o/p:
=========
+---+------+------+
|id |name  |gender|
+---+------+------+
|1  |maheer|male  |
|2  |wafa  |male  |
|3  |asi   |female|
|4  |ayesha|female|
|1  |maheer|male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)


To remove duplicate using distinct()/dropDuplicates():
==========================================================================
df_final_unionAll.distinct().show(truncate=False)
o/p:
=======
+---+------+------+
|id |name  |gender|
+---+------+------+
|4  |ayesha|female|
|2  |wafa  |male  |
|1  |maheer|male  |
|3  |asi   |female|
+---+------+------+

df_final_unionAll.dropDuplicates().show(truncate=False)
o/p:
=======
+---+------+------+
|id |name  |gender|
+---+------+------+
|4  |ayesha|female|
|2  |wafa  |male  |
|1  |maheer|male  |
|3  |asi   |female|
+---+------+------+

df_final_unionAll = spark.sql("""select id,name,gender from practice1
                              UNION ALL
                              select id,name,gender from practice2""")
df_final_unionAll.show(truncate=False)
df_final_unionAll.printSchema()
o/p:
=======
+---+------+------+
|id |name  |gender|
+---+------+------+
|1  |maheer|male  |
|2  |wafa  |male  |
|3  |asi   |female|
|4  |ayesha|female|
|1  |maheer|male  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- gender: string (nullable = true)


Final Note about union() and unionAll() in pyspark and spark sql:
================================================================================
i. In case of pyspark df() union() and unionAll() both preserve duplicate record that means it does not remove duplicate record , to remove duplicate record use distinct() and dropDuplicates()
ii. In case of pyspark df() union() and unionAll() gives good performance (fast).
iii. In case of sparksql() union() removes duplicate record and does not give good performance.
iv. In case of sparksql() unionAll() preserve duplicate record and give good performance.



iii. Use of unionByName():
===================================
i. It is used to merge two df with different schema.

code:
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
o/p:
===========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

data1 = [(1,"maheer",31)]

schema_ddl_1 = "id integer,name string,age integer"
schema_prog_1 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("age",IntegerType(),True)])

df1 = spark.createDataFrame(data=data1,schema=schema_ddl_1)
df1.show(truncate=False)
df1.printSchema()
o/p:
=================
+---+------+---+
|id |name  |age|
+---+------+---+
|1  |maheer|31 |
+---+------+---+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- age: integer (nullable = true)

data2 = [(1,"maheer",2000)]

schema_ddl_2 = "id integer,name string,salary integer"
schema_prog_2 = StructType([\
                           StructField("id",IntegerType(),True),\
                           StructField("name",StringType(),True),\
                           StructField("salary",IntegerType(),True)])

df2 = spark.createDataFrame(data=data2,schema=schema_ddl_2)
df2.show(truncate=False)
df2.printSchema()
o/p:
=========
+---+------+------+
|id |name  |salary|
+---+------+------+
|1  |maheer|2000  |
+---+------+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- salary: integer (nullable = true)

df1.createOrReplaceTempView("practice1")
df2.createOrReplaceTempView("practice2")

df_final_unionByName = df1.unionByName(df2,allowMissingColumns=True)
df_final_unionByName.show(truncate=False)
df_final_unionByName.printSchema()
o/p:
===========
+---+------+----+------+
|id |name  |age |salary|
+---+------+----+------+
|1  |maheer|31  |null  |
|1  |maheer|null|2000  |
+---+------+----+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- age: integer (nullable = true)
 |-- salary: integer (nullable = true)


df_final_unionByName = spark.sql("""
select 
       id,
       name,
       age,
       null as salary
from practice1

UNION ALL

select 
       id,
       name,
       null as age,
       salary
from practice2
""")

df_final_unionByName.show(truncate=False)
df_final_unionByName.printSchema()
o/p:
=======
+---+------+----+------+
|id |name  |age |salary|
+---+------+----+------+
|1  |maheer|31  |null  |
|1  |maheer|null|2000  |
+---+------+----+------+

root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- age: integer (nullable = true)
 |-- salary: integer (nullable = true)


7. How to deal with null record in df/sparksql:
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
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

schema = "Id int, Name string,Marks double"
data = [(1,"Sagar",None),\
        (2,None,23.5),\
        (None,None,45.2),\
        (4,"Alex",46.7)]

df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show(truncate=False)
o/p:
========
root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Marks: double (nullable = true)

+----+-----+-----+
|Id  |Name |Marks|
+----+-----+-----+
|1   |Sagar|null |
|2   |null |23.5 |
|null|null |45.2 |
|4   |Alex |46.7 |
+----+-----+-----+


df.createOrReplaceTempView("practice1")

i. df_null_count = df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
])

df_null_count.show()
o/p:
=========
+---+----+-----+
| Id|Name|Marks|
+---+----+-----+
|  1|   2|    1|
+---+----+-----+

ii. df_null_count = spark.sql("""select 'Id' as column_name,count(*) as total_null_count
                             from practice1
                             where Id is null
                             
                             UNION ALL
                             
                             select 'Name',count(*) as null_count
                             from practice1
                             where Name is null
                             
                             UNION ALL 
                             
                             select 'Marks',count(*) as null_count
                             from practice1
                             where Marks is null
                             """)
df_null_count.show()
o/p:
========
+-----------+----------------+
|column_name|total_null_count|
+-----------+----------------+
|         Id|               1|
|       Name|               2|
|      Marks|               1|
+-----------+----------------+

iii. df_null_count = spark.sql("""
SELECT
       SUM(CASE WHEN Id IS NULL THEN 1 ELSE 0 END) AS Id,
       SUM(CASE WHEN Name IS NULL THEN 1 ELSE 0 END) AS Name,
       SUM(CASE WHEN Marks IS NULL THEN 1 ELSE 0 END) AS Marks
FROM practice1
""")
df_null_count.show()
o/p:
==========
+---+----+-----+
| Id|Name|Marks|
+---+----+-----+
|  1|   2|    1|
+---+----+-----+

Approach 1st using .dropna():
============================================================
i. This will delete(drop) entire row where null value is present in any of the column.

df.dropna().show(truncate=False)
o/p:
==========
+---+----+-----+
|Id |Name|Marks|
+---+----+-----+
|4  |Alex|46.7 |
+---+----+-----+

Approach 2nd using fillna():
=========================================================================
df.show(truncate=False)
o/p:
=========
+----+-----+-----+
|Id  |Name |Marks|
+----+-----+-----+
|1   |Sagar|null |
|2   |null |23.5 |
|null|null |45.2 |
|4   |Alex |46.7 |
+----+-----+-----+

df_final = df.fillna(0,['Id','Marks'])\
             .fillna('NA',['Name'])

df_final.show(truncate=False)
df_final.printSchema()
o/p:
=======
+---+-----+-----+
|Id |Name |Marks|
+---+-----+-----+
|1  |Sagar|0.0  |
|2  |NA   |23.5 |
|0  |NA   |45.2 |
|4  |Alex |46.7 |
+---+-----+-----+

root
 |-- Id: integer (nullable = true)
 |-- Name: string (nullable = false)
 |-- Marks: double (nullable = false)

df_final = spark.sql("""select coalesce(Id,0) as Id,coalesce(Name,'NA') as Name,coalesce(Marks,0) as Marks
                        from practice1""")

df_final.show(truncate=False)
o/p:
===========
+---+-----+-----+
|Id |Name |Marks|
+---+-----+-----+
|1  |Sagar|0.0  |
|2  |NA   |23.5 |
|0  |NA   |45.2 |
|4  |Alex |46.7 |
+---+-----+-----+

Approach 3rd using mean() + fillna():
======================================================
mean_value = df.select(mean(col("Marks"))).collect()[0][0]
print(mean_value)
o/p:
========
38.46666666666667

df_final = df.fillna(mean_value,['Id','Marks'])\
             .fillna('NA',['Name'])

df_final.show(truncate=False)
o/p:
==========
+---+-----+-----------------+
|Id |Name |Marks            |
+---+-----+-----------------+
|1  |Sagar|38.46666666666667|
|2  |NA   |23.5             |
|38 |NA   |45.2             |
|4  |Alex |46.7             |
+---+-----+-----------------+


df_final = spark.sql("""
WITH cte AS (
    SELECT *,
           AVG(Marks) OVER() AS mean_marks
    FROM practice1
)

SELECT 
       COALESCE(Id,0) AS Id,
       COALESCE(Name,'NA') AS Name,
       COALESCE(Marks,mean_marks) AS Marks
FROM cte
""")
df_final.show(truncate=False)
o/p:
=======
+---+-----+-----------------+
|Id |Name |Marks            |
+---+-----+-----------------+
|1  |Sagar|38.46666666666667|
|2  |NA   |23.5             |
|0  |NA   |45.2             |
|4  |Alex |46.7             |
+---+-----+-----------------+


8. How to deal with null record in df/sparksql:
===========================================================
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
o/p:
==============
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

sepal_schema_ddl = "sepal_length float,sepal_width float,petal_length float,petal_width float,class string"
sepal_schema_prog = StructType([\
                               StructField("sepal_length",FloatType(),True),\
                               StructField("sepal_width",FloatType(),True),\
                               StructField("petal_length",FloatType(),True),\
                               StructField("petal_width",FloatType(),True),\
                               StructField("class",StringType(),True)])
                               
data = [(5.1,3.5,1.4,0.2,"Iris_setosa"),\
        (4.9,3.0,1.4,0.2,"Iris_setosa"),\
        (4.7,3.2,1.3,None,"Iris_setosa"),\
        (4.6,None,1.5,0.2,"Iris_setosa"),\
        (5.0,3.6,1.4,0.2,None),\
        (5.4,3.9,1.7,0.4,"Iris_setosa"),\
        (None,None,None,None,None),\
        (None,None,None,None,None)]
        
iris_df = spark.createDataFrame(data=data,schema=sepal_schema_prog)
iris_df.show(truncate=False)
iris_df.printSchema()
o/p:
=============
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |null       |Iris_setosa|
|4.6         |null       |1.5         |0.2        |Iris_setosa|
|5.0         |3.6        |1.4         |0.2        |null       |
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
|null        |null       |null        |null       |null       |
|null        |null       |null        |null       |null       |
+------------+-----------+------------+-----------+-----------+

root
 |-- sepal_length: float (nullable = true)
 |-- sepal_width: float (nullable = true)
 |-- petal_length: float (nullable = true)
 |-- petal_width: float (nullable = true)
 |-- class: string (nullable = true)
 
 
i. Total null count column wise:
========================================================
print("Total null count in sepal_length column: ",iris_df.filter(col("sepal_length").isNull()).count())
print("Total null count in sepal_width column: ",iris_df.filter(col("sepal_width").isNull()).count())
print("Total null count in petal_length column: ",iris_df.filter(col("petal_length").isNull()).count())
print("Total null count in petal_width column: ",iris_df.filter(col("petal_width").isNull()).count())
print("Total null count in class column: ",iris_df.filter(col("class").isNull()).count())
o/p:
===============
Total null count in sepal_length column:  2
Total null count in sepal_width column:  3
Total null count in petal_length column:  2
Total null count in petal_width column:  3
Total null count in class column:  3

ii. iris_df_null_count = spark.sql("""
select 'sepal_length' as column_name, count(*) as total_null_count
from practice
where sepal_length is null

UNION ALL

select 'sepal_width', count(*)
from practice
where sepal_width is null

UNION ALL 

select 'petal_length', count(*)
from practice
where petal_length is null

UNION ALL

select 'petal_width', count(*)
from practice
where petal_width is null

UNION ALL 

select 'class', count(*)
from practice
where class is null
""")

iris_df_null_count.show(truncate=False)
o/p:
===========
+------------+----------------+
|column_name |total_null_count|
+------------+----------------+
|sepal_length|2               |
|sepal_width |3               |
|petal_length|2               |
|petal_width |3               |
|class       |3               |
+------------+----------------+


Total null count for each column dynamically:
========================================================
i. iris_df_null_count = iris_df.select(
    [
        count(when(col(i).isNull(), i)).alias(i)
        for i in iris_df.columns
    ]
)

iris_df_null_count.show(truncate=False)
o/p:
===========
+------------+-----------+------------+-----------+-----+
|sepal_length|sepal_width|petal_length|petal_width|class|
+------------+-----------+------------+-----------+-----+
|2           |3          |2           |3          |3    |
+------------+-----------+------------+-----------+-----+

ii. iris_df_null_count = spark.sql("""SELECT
                                      SUM(CASE WHEN sepal_length IS NULL THEN 1 ELSE 0 END) AS sepal_length,
                                      SUM(CASE WHEN sepal_width IS NULL THEN 1 ELSE 0 END) AS sepal_width,
                                      SUM(CASE WHEN petal_length IS NULL THEN 1 ELSE 0 END) AS petal_length,
                                      SUM(CASE WHEN petal_width IS NULL THEN 1 ELSE 0 END) AS petal_width,
                                      SUM(CASE WHEN class IS NULL THEN 1 ELSE 0 END) AS class
                                      FROM practice
                                """) 
iris_df_null_count.show(truncate=False) 
o/p:
===========
+------------+-----------+------------+-----------+-----+
|sepal_length|sepal_width|petal_length|petal_width|class|
+------------+-----------+------------+-----------+-----+
|2           |3          |2           |3          |3    |
+------------+-----------+------------+-----------+-----+

1. To drop the null values:
=========================================================
i. iris_df.dropna(how='any').show(truncate=False)
o/p:
=============
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
+------------+-----------+------------+-----------+-----------+

Note -: In above code By default how='any' in dropna() , so how='any' means if a single column contain null value in entire row than that entire row will be dropped.


ii. iris_df.dropna(how='all').show(truncate=False)
o/p:
==========

+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |null       |Iris_setosa|
|4.6         |null       |1.5         |0.2        |Iris_setosa|
|5.0         |3.6        |1.4         |0.2        |null       |
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
+------------+-----------+------------+-----------+-----------+



Note -: In above code we are using how='all' in dropna() , so how='all' means if all the columns contain null value in entire row than that entire row will be dropped.


iii. iris_df.dropna(thresh=3).show(truncate=False)
o/p:
==========
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |null       |Iris_setosa|
|4.6         |null       |1.5         |0.2        |Iris_setosa|
|5.0         |3.6        |1.4         |0.2        |null       |
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
+------------+-----------+------------+-----------+-----------+

Note -: In above code we are using thresh=3 in dropna() , so thresh=3 means if in a row three column contain non null value than that will not be dropped and whichever rows are having more than 3 null valuecolumns than that will be dropped

iv. iris_df.dropna(subset=['class']).show(truncate=False)
o/p:
===========
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |null       |Iris_setosa|
|4.6         |null       |1.5         |0.2        |Iris_setosa|
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
+------------+-----------+------------+-----------+-----------+

Note -: In above code we are using subset=['class'] in dropna() , so subset=['class'] means if column class contain null value in any of the row than that entire row will be dropped.


2. Use of fillna() to handle null values in a column:
=============================================================
i. iris_df.fillna(0.0,subset = ['sepal_length','sepal_width','petal_length','petal_width'])\
       .fillna("Iris_setosa",subset=['class']).show(truncate=False)
o/p:
===========
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |0.0        |Iris_setosa|
|4.6         |0.0        |1.5         |0.2        |Iris_setosa|
|5.0         |3.6        |1.4         |0.2        |Iris_setosa|
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
|0.0         |0.0        |0.0         |0.0        |Iris_setosa|
|0.0         |0.0        |0.0         |0.0        |Iris_setosa|
+------------+-----------+------------+-----------+-----------+

ii. iris_df_null_handler = spark.sql("""select coalesce(sepal_length,0.0) as sepal_length,
                                           coalesce(sepal_width,0.0) as sepal_width,
                                           coalesce(petal_length,0.0) as petal_length,
                                           coalesce(petal_width,0.0) as petal_width,
                                           coalesce(class,'Iris_setosa') as class
                                    from practice
                                """)
iris_df_null_handler.show()
o/p:
=========
+-----------------+------------------+------------------+-------------------+-----------+
|     sepal_length|       sepal_width|      petal_length|        petal_width|      class|
+-----------------+------------------+------------------+-------------------+-----------+
|5.099999904632568|               3.5| 1.399999976158142|0.20000000298023224|Iris_setosa|
|4.900000095367432|               3.0| 1.399999976158142|0.20000000298023224|Iris_setosa|
|4.699999809265137| 3.200000047683716|1.2999999523162842|                0.0|Iris_setosa|
|4.599999904632568|               0.0|               1.5|0.20000000298023224|Iris_setosa|
|              5.0|3.5999999046325684| 1.399999976158142|0.20000000298023224|Iris_setosa|
|5.400000095367432|3.9000000953674316|1.7000000476837158| 0.4000000059604645|Iris_setosa|
|              0.0|               0.0|               0.0|                0.0|Iris_setosa|
|              0.0|               0.0|               0.0|                0.0|Iris_setosa|
+-----------------+------------------+------------------+-------------------+-----------+

3. Handle null using mean() values + fillna():
==============================================
i. mean_value = iris_df.select(
    mean(col("sepal_length"))
).collect()[0][0]

print(mean_value)

iris_df.fillna(mean_value,subset = ['sepal_length','sepal_width','petal_length','petal_width'])\
       .fillna("Iris_setosa",subset=['class']).show(truncate=False)
o/p:
==========
+------------+-----------+------------+-----------+-----------+
|sepal_length|sepal_width|petal_length|petal_width|class      |
+------------+-----------+------------+-----------+-----------+
|5.1         |3.5        |1.4         |0.2        |Iris_setosa|
|4.9         |3.0        |1.4         |0.2        |Iris_setosa|
|4.7         |3.2        |1.3         |4.95       |Iris_setosa|
|4.6         |4.95       |1.5         |0.2        |Iris_setosa|
|5.0         |3.6        |1.4         |0.2        |Iris_setosa|
|5.4         |3.9        |1.7         |0.4        |Iris_setosa|
|4.95        |4.95       |4.95        |4.95       |Iris_setosa|
|4.95        |4.95       |4.95        |4.95       |Iris_setosa|
+------------+-----------+------------+-----------+-----------+


ii. iris_df_null_handler = spark.sql("""with cte as (
                                     select *,avg(sepal_length) over() mean_value
                                     from practice)
                                     select coalesce(sepal_length,mean_value) as sepal_length,
                                           coalesce(sepal_width,mean_value) as sepal_width,
                                           coalesce(petal_length,mean_value) as petal_length,
                                           coalesce(petal_width,mean_value) as petal_width,
                                           coalesce(class,'Iris_setosa') as class
                                    from cte
                                    """)
iris_df_null_handler.show(truncate=False)
o/p:
=========
+-----------------+------------------+------------------+-------------------+-----------+
|sepal_length     |sepal_width       |petal_length      |petal_width        |class      |
+-----------------+------------------+------------------+-------------------+-----------+
|5.099999904632568|3.5               |1.399999976158142 |0.20000000298023224|Iris_setosa|
|4.900000095367432|3.0               |1.399999976158142 |0.20000000298023224|Iris_setosa|
|4.699999809265137|3.200000047683716 |1.2999999523162842|4.949999968210856  |Iris_setosa|
|4.599999904632568|4.949999968210856 |1.5               |0.20000000298023224|Iris_setosa|
|5.0              |3.5999999046325684|1.399999976158142 |0.20000000298023224|Iris_setosa|
|5.400000095367432|3.9000000953674316|1.7000000476837158|0.4000000059604645 |Iris_setosa|
|4.949999968210856|4.949999968210856 |4.949999968210856 |4.949999968210856  |Iris_setosa|
|4.949999968210856|4.949999968210856 |4.949999968210856 |4.949999968210856  |Iris_setosa|
+-----------------+------------------+------------------+-------------------+-----------+


9. Use of unionByName():
=====================================
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
=================
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell


data1 = [('Azarudeen,Shahul',25),\
         ('Michael,Clarke',26),\
         ('Virat,Kohli',28),\
         ('Andrew,Simon',37)]

schema1 = 'Name string,Age int'
df1 = spark.createDataFrame(data=data1,schema=schema1)
df1.show(truncate=False)
df1.printSchema()
o/p:
=========
+----------------+---+
|Name            |Age|
+----------------+---+
|Azarudeen,Shahul|25 |
|Michael,Clarke  |26 |
|Virat,Kohli     |28 |
|Andrew,Simon    |37 |
+----------------+---+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 
 data2 = [('Rabindranath,Tagore',32,'Male'),\
         ('Mandone,Lawre',59,'Female'),\
         ('Flintoff,David',12,'Male'),\
         ('Ammie,James',20,'Female')]

schema2 = 'Name string,Age int,Gender string'
df2 = spark.createDataFrame(data=data2,schema=schema2)
df2.show(truncate=False)
df2.printSchema()
o/p:
======
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 Different approaches to merge 2 df having different schema:
====================================================================
1. Approach 1st Using unionByName():
===============================================
df_final = df1.unionByName(df2,allowMissingColumns=True)
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=======
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Azarudeen,Shahul   |25 |null  |
|Michael,Clarke     |26 |null  |
|Virat,Kohli        |28 |null  |
|Andrew,Simon       |37 |null  |
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 2. Approach 2nd Using explicit schema():
====================================================
data1 = [('Azarudeen,Shahul',25,None),\
         ('Michael,Clarke',26,None),\
         ('Virat,Kohli',28,None),\
         ('Andrew,Simon',37,None)]

schema1 = 'Name string,Age int,Gender string'
df1 = spark.createDataFrame(data=data1,schema=schema1)
df1.show(truncate=False)
df1.printSchema()
o/p:
==============
+----------------+---+------+
|Name            |Age|Gender|
+----------------+---+------+
|Azarudeen,Shahul|25 |null  |
|Michael,Clarke  |26 |null  |
|Virat,Kohli     |28 |null  |
|Andrew,Simon    |37 |null  |
+----------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
data2 = [('Rabindranath,Tagore',32,'Male'),\
         ('Mandone,Lawre',59,'Female'),\
         ('Flintoff,David',12,'Male'),\
         ('Ammie,James',20,'Female')]

schema2 = 'Name string,Age int,Gender string'
df2 = spark.createDataFrame(data=data2,schema=schema2)
df2.show(truncate=False)
df2.printSchema()
o/p
=====
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)


df_final_1 = df1.union(df2)
df_final_1.show(truncate=False)
df_final_1.printSchema()
o/p:
============
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Azarudeen,Shahul   |25 |null  |
|Michael,Clarke     |26 |null  |
|Virat,Kohli        |28 |null  |
|Andrew,Simon       |37 |null  |
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
3. Approach 3rd Using .withColumn(),union():
======================================================
data1 = [('Azarudeen,Shahul',25),\
         ('Michael,Clarke',26),\
         ('Virat,Kohli',28),\
         ('Andrew,Simon',37)]

schema1 = 'Name string,Age int'
df1 = spark.createDataFrame(data=data1,schema=schema1)
df1.show(truncate=False)
df1.printSchema()
o/p:
=========
+----------------+---+
|Name            |Age|
+----------------+---+
|Azarudeen,Shahul|25 |
|Michael,Clarke  |26 |
|Virat,Kohli     |28 |
|Andrew,Simon    |37 |
+----------------+---+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 
 df1_new = df1.withColumn("Gender",lit("null"))
df1_new.show(truncate=False)
df1_new.printSchema()
o/p:
=========
+----------------+---+------+
|Name            |Age|Gender|
+----------------+---+------+
|Azarudeen,Shahul|25 |null  |
|Michael,Clarke  |26 |null  |
|Virat,Kohli     |28 |null  |
|Andrew,Simon    |37 |null  |
+----------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = false)
 
df_final_2 = df1_new.union(df2)
df_final_2.show(truncate=False)
df_final_2.printSchema()
o/p:
=========
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Azarudeen,Shahul   |25 |null  |
|Michael,Clarke     |26 |null  |
|Virat,Kohli        |28 |null  |
|Andrew,Simon       |37 |null  |
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 
 4. Approach 4th Using outer join:
 ============================================
 data1 = [('Azarudeen,Shahul',25),\
         ('Michael,Clarke',26),\
         ('Virat,Kohli',28),\
         ('Andrew,Simon',37)]

schema1 = 'Name string,Age int'
df1 = spark.createDataFrame(data=data1,schema=schema1)
df1.show(truncate=False)
df1.printSchema()
o/p:
========
+----------------+---+
|Name            |Age|
+----------------+---+
|Azarudeen,Shahul|25 |
|Michael,Clarke  |26 |
|Virat,Kohli     |28 |
|Andrew,Simon    |37 |
+----------------+---+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 
data2 = [('Rabindranath,Tagore',32,'Male'),\
         ('Mandone,Lawre',59,'Female'),\
         ('Flintoff,David',12,'Male'),\
         ('Ammie,James',20,'Female')]

schema2 = 'Name string,Age int,Gender string'
df2 = spark.createDataFrame(data=data2,schema=schema2)
df2.show(truncate=False)
df2.printSchema()
o/p:
========
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 df_final_3 = df1.join(df2,df1['Name']==df2['Age'],'outer')
df_final_3.show(truncate=False)
df_final_3.printSchema()
o/p:
=========
+----------------+----+-------------------+----+------+
|Name            |Age |Name               |Age |Gender|
+----------------+----+-------------------+----+------+
|null            |null|Flintoff,David     |12  |Male  |
|Virat,Kohli     |28  |null               |null|null  |
|Andrew,Simon    |37  |null               |null|null  |
|Azarudeen,Shahul|25  |null               |null|null  |
|Michael,Clarke  |26  |null               |null|null  |
|null            |null|Ammie,James        |20  |Female|
|null            |null|Mandone,Lawre      |59  |Female|
|null            |null|Rabindranath,Tagore|32  |Male  |
+----------------+----+-------------------+----+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 Note: The above outer join approach is not recommended approach as it involves complete shuffle of data.
 
 5. Approach 5th using Automated Approach:
 =================================================
 col1 = df1.columns
print(col1)
o/p:
========
['Name', 'Age']

col2 = df2.columns
print(col2)
o/p:
=========
['Name', 'Age', 'Gender']

listA = list(set(col1) - set(col2))
print(listA)
o/p:
========
[]

listB = list(set(col2) - set(col1))
print(listB)
o/p:
=======
['Gender']

for i in listB:
    df1 = df1.withColumn(i,lit("null"))
df1.printSchema()
df1.show(truncate=False)
o/p:
========
root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = false)

+----------------+---+------+
|Name            |Age|Gender|
+----------------+---+------+
|Azarudeen,Shahul|25 |null  |
|Michael,Clarke  |26 |null  |
|Virat,Kohli     |28 |null  |
|Andrew,Simon    |37 |null  |
+----------------+---+------+

df_final_4 = df1.union(df2)
df_final_4.show(truncate=False)
df_final_4.printSchema()
o/p:
============
+-------------------+---+------+
|Name               |Age|Gender|
+-------------------+---+------+
|Azarudeen,Shahul   |25 |null  |
|Michael,Clarke     |26 |null  |
|Virat,Kohli        |28 |null  |
|Andrew,Simon       |37 |null  |
|Rabindranath,Tagore|32 |Male  |
|Mandone,Lawre      |59 |Female|
|Flintoff,David     |12 |Male  |
|Ammie,James        |20 |Female|
+-------------------+---+------+

root
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Gender: string (nullable = true)
 
 Conclusion:
 ======================
 There are 4 ways to merge two df's with different schema:
 ===============================================================
 1. Approach 1st Using unionByName().
 2. Approach 2nd Using explicit schema().
 3. Approach 3rd Using .withColumn(),union().
 4. Approach 4th Using outer join.
 5. Approach 5th using Automated Approach.
 
 
 10. Use of create_map(),map_keys(),map_values(),explode():
 ============================================================================
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

data = [(1,'Sagar',25),\
        (2,'Alex',30),\
        (3,'David',35)]

schema_ddl = "ID int,Name string,Age int"

schma_prog = StructType([\
                        StructField("ID",IntegerType(),True),\
                        StructField("Name",StringType(),True),\
                        StructField("Age",IntegerType(),True)])
                        

df = spark.createDataFrame(data=data,schema=schma_prog)
df.show(truncate=False)
df.printSchema()
o/p:
==========
+---+-----+---+
|ID |Name |Age|
+---+-----+---+
|1  |Sagar|25 |
|2  |Alex |30 |
|3  |David|35 |
+---+-----+---+

root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Age: integer (nullable = true)

i. Use of create_map():
===============================================
df_map_result = df.withColumn("map_column",create_map(lit("Name"),col("Name"),lit("Age"),col("Age")))\
                  .drop("Name","Age")

df_map_result.show(truncate=False)
df_map_result.printSchema()

o/p:
===========
+---+--------------------------+
|ID |map_column                |
+---+--------------------------+
|1  |{Name -> Sagar, Age -> 25}|
|2  |{Name -> Alex, Age -> 30} |
|3  |{Name -> David, Age -> 35}|
+---+--------------------------+

root
 |-- ID: integer (nullable = true)
 |-- map_column: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 
 
ii. Use of map_keys() and map_values:
================================================
df_map_result_keys = df_map_result.withColumn("keys",map_keys(col("map_column")))\
                                  .withColumn("values",map_values(col("map_column")))

df_map_result_keys.show(truncate=False)
df_map_result_keys.printSchema()

o/p:
================
+---+--------------------------+-----------+-----------+
|ID |map_column                |keys       |values     |
+---+--------------------------+-----------+-----------+
|1  |{Name -> Sagar, Age -> 25}|[Name, Age]|[Sagar, 25]|
|2  |{Name -> Alex, Age -> 30} |[Name, Age]|[Alex, 30] |
|3  |{Name -> David, Age -> 35}|[Name, Age]|[David, 35]|
+---+--------------------------+-----------+-----------+

root
 |-- ID: integer (nullable = true)
 |-- map_column: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 |-- keys: array (nullable = false)
 |    |-- element: string (containsNull = true)
 |-- values: array (nullable = false)
 |    |-- element: string (containsNull = true)
 

iii. Use of explode():
======================================
df_map_result_explode = df_map_result.select(col("ID"),col("map_column"),explode(col("map_column")))
df_map_result_explode.show(truncate=False)
df_map_result_explode.printSchema()

o/p:
========
+---+--------------------------+----+-----+
|ID |map_column                |key |value|
+---+--------------------------+----+-----+
|1  |{Name -> Sagar, Age -> 25}|Name|Sagar|
|1  |{Name -> Sagar, Age -> 25}|Age |25   |
|2  |{Name -> Alex, Age -> 30} |Name|Alex |
|2  |{Name -> Alex, Age -> 30} |Age |30   |
|3  |{Name -> David, Age -> 35}|Name|David|
|3  |{Name -> David, Age -> 35}|Age |35   |
+---+--------------------------+----+-----+

root
 |-- ID: integer (nullable = true)
 |-- map_column: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 |-- key: string (nullable = false)
 |-- value: string (nullable = true)
 
 
 
 11. Use of create_map(),map_keys(),map_values(),explode():
 ============================================================================
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

employee_data = [("Prem","Ojha","premsankarojha@gmail.com","8637879832"),\
                 ("Abhishek","Ojha","abhishekojha@gmail.com","8899604567"),\
                 ("Amit","Yadav","amityadav@gmail.com","8890786544")]

employee_ddl = "First_Name string,Last_Name string,Email string,Phone_Number string"

employee_prog = StructType([\
                           StructField("First_Name",StringType(),True),\
                           StructField("Last_Name",StringType(),True),\
                           StructField("Email",StringType(),True),\
                           StructField("Phone_Number",StringType(),True)])
                        

employee_df = spark.createDataFrame(data=employee_data,schema=employee_prog)
employee_df.show(truncate=False)
employee_df.printSchema()
o/p:
==========
+----------+---------+------------------------+------------+
|First_Name|Last_Name|Email                   |Phone_Number|
+----------+---------+------------------------+------------+
|Prem      |Ojha     |premsankarojha@gmail.com|8637879832  |
|Abhishek  |Ojha     |abhishekojha@gmail.com  |8899604567  |
|Amit      |Yadav    |amityadav@gmail.com     |8890786544  |
+----------+---------+------------------------+------------+

root
 |-- First_Name: string (nullable = true)
 |-- Last_Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Phone_Number: string (nullable = true)

i. Use of create_map():
===============================================
employee_df_map = employee_df.withColumn("employee_map",create_map(lit("First_Name"),("First_Name"),
                                                                   lit("Last_Name"),("Last_Name"),
                                                                   lit("Email"),("Email"),
                                                                   lit("Phone_Number"),col("Phone_Number")))\
                            .drop("First_Name","Last_Name","Email","Phone_Number")
employee_df_map.show(truncate=False)
employee_df_map.printSchema()

o/p:
===========
+--------------------------------------------------------------------------------------------------------+
|employee_map                                                                                            |
+--------------------------------------------------------------------------------------------------------+
|{First_Name -> Prem, Last_Name -> Ojha, Email -> premsankarojha@gmail.com, Phone_Number -> 8637879832}  |
|{First_Name -> Abhishek, Last_Name -> Ojha, Email -> abhishekojha@gmail.com, Phone_Number -> 8899604567}|
|{First_Name -> Amit, Last_Name -> Yadav, Email -> amityadav@gmail.com, Phone_Number -> 8890786544}      |
+--------------------------------------------------------------------------------------------------------+

root
 |-- employee_map: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 
 
ii. Use of map_keys() and map_values:
================================================
employee_df_map_keys_values = employee_df_map.withColumn("employee_keys",map_keys(col("employee_map")))\
                                      .withColumn("employee_values",map_values(col("employee_map")))\
                                      .drop("employee_map")
employee_df_map_keys_values.show(truncate=False)
employee_df_map_keys_values.printSchema()

o/p:
================
+--------------------------------------------+----------------------------------------------------+
|employee_keys                               |employee_values                                     |
+--------------------------------------------+----------------------------------------------------+
|[First_Name, Last_Name, Email, Phone_Number]|[Prem, Ojha, premsankarojha@gmail.com, 8637879832]  |
|[First_Name, Last_Name, Email, Phone_Number]|[Abhishek, Ojha, abhishekojha@gmail.com, 8899604567]|
|[First_Name, Last_Name, Email, Phone_Number]|[Amit, Yadav, amityadav@gmail.com, 8890786544]      |
+--------------------------------------------+----------------------------------------------------+

root
 |-- employee_keys: array (nullable = false)
 |    |-- element: string (containsNull = true)
 |-- employee_values: array (nullable = false)
 |    |-- element: string (containsNull = true)
 

iii. Use of explode():
======================================
employee_df_explode = employee_df_map.select(col("employee_map"),explode(col("employee_map")))
employee_df_explode.show(truncate=False)
employee_df_explode.printSchema()

o/p:
========
+--------------------------------------------------------------------------------------------------------+------------+------------------------+
|employee_map                                                                                            |key         |value                   |
+--------------------------------------------------------------------------------------------------------+------------+------------------------+
|{First_Name -> Prem, Last_Name -> Ojha, Email -> premsankarojha@gmail.com, Phone_Number -> 8637879832}  |First_Name  |Prem                    |
|{First_Name -> Prem, Last_Name -> Ojha, Email -> premsankarojha@gmail.com, Phone_Number -> 8637879832}  |Last_Name   |Ojha                    |
|{First_Name -> Prem, Last_Name -> Ojha, Email -> premsankarojha@gmail.com, Phone_Number -> 8637879832}  |Email       |premsankarojha@gmail.com|
|{First_Name -> Prem, Last_Name -> Ojha, Email -> premsankarojha@gmail.com, Phone_Number -> 8637879832}  |Phone_Number|8637879832              |
|{First_Name -> Abhishek, Last_Name -> Ojha, Email -> abhishekojha@gmail.com, Phone_Number -> 8899604567}|First_Name  |Abhishek                |
|{First_Name -> Abhishek, Last_Name -> Ojha, Email -> abhishekojha@gmail.com, Phone_Number -> 8899604567}|Last_Name   |Ojha                    |
|{First_Name -> Abhishek, Last_Name -> Ojha, Email -> abhishekojha@gmail.com, Phone_Number -> 8899604567}|Email       |abhishekojha@gmail.com  |
|{First_Name -> Abhishek, Last_Name -> Ojha, Email -> abhishekojha@gmail.com, Phone_Number -> 8899604567}|Phone_Number|8899604567              |
|{First_Name -> Amit, Last_Name -> Yadav, Email -> amityadav@gmail.com, Phone_Number -> 8890786544}      |First_Name  |Amit                    |
|{First_Name -> Amit, Last_Name -> Yadav, Email -> amityadav@gmail.com, Phone_Number -> 8890786544}      |Last_Name   |Yadav                   |
|{First_Name -> Amit, Last_Name -> Yadav, Email -> amityadav@gmail.com, Phone_Number -> 8890786544}      |Email       |amityadav@gmail.com     |
|{First_Name -> Amit, Last_Name -> Yadav, Email -> amityadav@gmail.com, Phone_Number -> 8890786544}      |Phone_Number|8890786544              |
+--------------------------------------------------------------------------------------------------------+------------+------------------------+

root
 |-- employee_map: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 |-- key: string (nullable = false)
 |-- value: string (nullable = true)
