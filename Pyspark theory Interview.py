WEEK 4TH:
====================
1. HOW TO CHECK NO OF PARTITION IN A DF OR RDD:
=======================================================
df.rdd.getNumPartitions()

2. When you parallelize your data than no of partition is decided by a property:
================================================================================
spark.sparkContext.defaultParallelism

3. When you are reading the data from textFile and creating the rdd than no of partitions is:
=============================================================================================
a. First we will see the size of the fie.
b. load the file and create rdd.
c. check no of partitions:
rdd.getNumPartitions().
d.spark.sparkContext.defaultMinPartitions.

4. Difference b/t reduceByKey() vs countByValue():
===================================================
i. reduceByKey():
========================
a. It is an transformation so it is an lazy evaluated.
b. when we use recuceByKey() on our data so we will get parallelism as our code will run on multiple node cluster.
c. we will use recuceByKey() when we want to apply more transformation after this.
d. Code:
===========
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
======
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
=======
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
results = mapped_rdd.reduceByKey(lambda x,y:x+y)
results.take(10)
o/p:
======
[('CLOSED', 7556),
 ('CANCELED', 1428),
 ('COMPLETE', 22899),
 ('PENDING_PAYMENT', 15030),
 ('SUSPECTED_FRAUD', 1558),
 ('PENDING', 7610),
 ('ON_HOLD', 3798),
 ('PROCESSING', 8275),
 ('PAYMENT_REVIEW', 729)]
 
ii. countByValue():
=============================
a. It is an action so it is an eager operation.
b. so when we apply countByValue() on our data than we will not get parallelism beacuse our code will run on a local machine.
c. we will use countByValue() on our data when we dont want to use another transformation after this.
d. we will use countByValue() in place of map+reduceByKey().
e.Code:
===============
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
======
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
mapped_rdd = orders_rdd.map(lambda x:(x.split(",")[3]))
mapped_rdd.take(10)
o/p:
======
['CLOSED',
 'PENDING_PAYMENT',
 'COMPLETE',
 'CLOSED',
 'COMPLETE',
 'COMPLETE',
 'COMPLETE',
 'PROCESSING',
 'PENDING_PAYMENT',
 'PENDING_PAYMENT']
mapped_rdd.countByValue()
0/p:
=======
defaultdict(int,
            {'CLOSED': 7556,
             'PENDING_PAYMENT': 15030,
             'COMPLETE': 22899,
             'PROCESSING': 8275,
             'PAYMENT_REVIEW': 729,
             'PENDING': 7610,
             'ON_HOLD': 3798,
             'CANCELED': 1428,
             'SUSPECTED_FRAUD': 1558})
             
5. Difference b/t wide transformation and narrow transformation:
=========================================================================
i. Narrow Transformation:
================================
a. A transformation that does not involve shuffle of data is referred as Narrow Transformation.
b. In this case no new stages are created.
c. For example: filter(),map(),flatmap().

ii. Wide Transformation:
=========================================
a. A transformation that involve shuffle of data is referred as Wide Transformation.
b. In this case new stage is created because stages are marked by shuffle boundary.
c. For example: reduceByKey(), groupByKey().

Note: Try to minimise the use of wide transformation because it involve complete shuffle of data and shuffling is costlier operation.
try to use more narrow transformation like filter() to discard umwanted data and than try to apply wide transformation so that we have to shuffle less data.

6. Impt Concept to remember:
==================================
i. Job:
================
a. Job is dependent on no of action called in the code.
b. No of job = No of Action executed.
c. For example : If there are 5 action executed in your code than:
                 No of Jobs = 5(As there are 5 Action executed).
Action = collect(),take(),reduce(),countByValue(),diplay(),show().

ii. Stages:
=============
a. Stages are marked by shuffle boundaries that means stages are dependent on shuffle.
b. No of stages = No of wide transformation + 1.
c. For example : If we use 1 wide transformation like reduceByKey() than in this case :
    No Of stages = No of wide transformation + 1
                    1+1=2 stages
    stage 0--> o/p of stage 0 is written to disk.
    stage 1---> stage 1 take the result from disk.
    
iii. Task:
===================
a. Task depend on no of partition in a df/rdd.
b. Task = No of partition in your rdd/df.
c. No of partitions = Size of the file in HDFS.
Each partition size is 128 mb by default.

Note:
===========
i. First we have Job-> Inside Job we have stage(Shuffle) ->3rd Inside each stage we have task(partition).

7. Diffrenece b/t reduceByKey() vs reduce():
============================================
i. reduceByKey():
=========================
a. It ia an transformation which means it is lazy evaluated.
b. It works on pair rdd(K,V).
c. When we use reduceByKey() than we get multiple value as output.
d. In this case we get parallelism.

ii. reduce():
==================
a. It is an Action which means it is an eager operation.
b. It works on normal rdd.
c. when we use reduce() than we get single value as output.
d. In this case we will not get parallelism.
e. Code:
=================
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
my_list = [1,4,6,8,9,10,12]
based_rdd = spark.sparkContext.parallelize(my_list)
based_rdd.reduce(lambda x,y:x+y)
o/p:
======
50

8. Difference b/t reduceByKey() vs groupByKey():
===================================================
i. reduceByKey():
====================
a. It perform local aggregation just like combiner acting at the mapper end, so the benefit of local aggregation is:
    i. Less (K,V) pair need to be shuffled so shuffling is minimised.
    ii. And more work is done in parallel, so we get parallelism.
b. So it does not lead to out of memory error issue.
c. Resource utilisation is good.
d. Code:
=================
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
base_rdd = spark.sparkContext.textFile("/public/trendytech/orders/orders.csv")
base_rdd.take(10)
o/p:
========
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
mapped_rdd = base_rdd.map(lambda x:(x.split(",")[3],1))
mapped_rdd.take(10)
o/p:
====
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
=======
[('PENDING', 9512500),
 ('PROCESSING', 10343750),
 ('CANCELED', 1785000),
 ('COMPLETE', 28623750),
 ('SUSPECTED_FRAUD', 1947500),
 ('CLOSED', 9445000),
 ('ON_HOLD', 4747500),
 ('PAYMENT_REVIEW', 911250),
 ('PENDING_PAYMENT', 18787500)]
 
ii. groupByKey():
=====================
a. It does not perform local aggregation, so the demerit of this is:
    i. Entire (K,V) pair need to be shuffled.
    ii. Less work is done in parallel.
b. It lead to OOM error issue.
c. It leads to underutilisation of cluster, so resource utilisation is not good.
d. Code:
=============
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
base_rdd = spark.sparkContext.textFile("/public/trendytech/orders/orders.csv")
base_rdd.take(10)
o/p:
=======
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
mapped_rdd = base_rdd.map(lambda x:(x.split(",")[3],x.split(",")[2]))
mapped_rdd.take(10)
o/p:
=======
[('CLOSED', '11599'),
 ('PENDING_PAYMENT', '256'),
 ('COMPLETE', '12111'),
 ('CLOSED', '8827'),
 ('COMPLETE', '11318'),
 ('COMPLETE', '7130'),
 ('COMPLETE', '4530'),
 ('PROCESSING', '2911'),
 ('PENDING_PAYMENT', '5657'),
 ('PENDING_PAYMENT', '5648')]
grouped_rdd = mapped_rdd.groupByKey()
result = grouped_rdd.map(lambda x:(x[0],len(x[1])))
result.collect()
o/p:
========
[('PENDING', 9512500),
 ('PROCESSING', 10343750),
 ('CANCELED', 1785000),
 ('COMPLETE', 28623750),
 ('SUSPECTED_FRAUD', 1947500),
 ('CLOSED', 9445000),
 ('ON_HOLD', 4747500),
 ('PAYMENT_REVIEW', 911250),
 ('PENDING_PAYMENT', 18787500)]
 
 Note: In production it is recommended to use reduceByKey() instead of groupByKey() due to above reason.
 
 Similarity b/t reduceByKey() vs groupByKey():
====================================================
i. Both works on pair rdd (K,V).
ii. Both are wide transformation so shuffling takes place.

8. Challenges with Normal Join:
===================================
i. It involve complete shuffle of data.
ii. Code:
================
Using rdd:
===============
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
orders_base = spark.sparkContext.textFile("/public/trendytech/orders/orders_1gb.csv")
orders_base.take(10)
o/p:
======
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
customers_base = spark.sparkContext.textFile("/public/trendytech/retail_db/customers/part-00000")
customers_base.take(10)
o/p:
=====
['1,Richard,Hernandez,XXXXXXXXX,XXXXXXXXX,6303 Heather Plaza,Brownsville,TX,78521',
 '2,Mary,Barrett,XXXXXXXXX,XXXXXXXXX,9526 Noble Embers Ridge,Littleton,CO,80126',
 '3,Ann,Smith,XXXXXXXXX,XXXXXXXXX,3422 Blue Pioneer Bend,Caguas,PR,00725',
 '4,Mary,Jones,XXXXXXXXX,XXXXXXXXX,8324 Little Common,San Marcos,CA,92069',
 '5,Robert,Hudson,XXXXXXXXX,XXXXXXXXX,"10 Crystal River Mall ",Caguas,PR,00725',
 '6,Mary,Smith,XXXXXXXXX,XXXXXXXXX,3151 Sleepy Quail Promenade,Passaic,NJ,07055',
 '7,Melissa,Wilcox,XXXXXXXXX,XXXXXXXXX,9453 High Concession,Caguas,PR,00725',
 '8,Megan,Smith,XXXXXXXXX,XXXXXXXXX,3047 Foggy Forest Plaza,Lawrence,MA,01841',
 '9,Mary,Perez,XXXXXXXXX,XXXXXXXXX,3616 Quaking Street,Caguas,PR,00725',
 '10,Melissa,Smith,XXXXXXXXX,XXXXXXXXX,8598 Harvest Beacon Plaza,Stafford,VA,22554']
orders_mapped = orders_base.map(lambda x:(x.split(",")[2],x.split(",")[3]))
orders_mapped.take(10)
o/p:
========
[('11599', 'CLOSED'),
 ('256', 'PENDING_PAYMENT'),
 ('12111', 'COMPLETE'),
 ('8827', 'CLOSED'),
 ('11318', 'COMPLETE'),
 ('7130', 'COMPLETE'),
 ('4530', 'COMPLETE'),
 ('2911', 'PROCESSING'),
 ('5657', 'PENDING_PAYMENT'),
 ('5648', 'PENDING_PAYMENT')]
customers_mapped = customers_base.map(lambda x:(x.split(",")[0],x.split(",")[8]))
customers_mapped.take(10)
o/p:
======
[('1', '78521'),
 ('2', '80126'),
 ('3', '00725'),
 ('4', '92069'),
 ('5', '00725'),
 ('6', '07055'),
 ('7', '00725'),
 ('8', '01841'),
 ('9', '00725'),
 ('10', '22554')]
joined_rdd = customers_mapped.join(orders_mapped)
joined_rdd.take(10)
o/p:
========
[('8442', ('46307', 'CLOSED')),
 ('8442', ('46307', 'CLOSED')),
 ('8442', ('46307', 'PROCESSING')),
 ('8442', ('46307', 'PENDING')),
 ('8442', ('46307', 'PROCESSING')),
 ('8442', ('46307', 'PENDING_PAYMENT')),
 ('8442', ('46307', 'ON_HOLD')),
 ('8442', ('46307', 'CLOSED')),
 ('8442', ('46307', 'CLOSED')),
 ('8442', ('46307', 'PROCESSING'))]
 
ii. Using Df:
====================
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
schema1 = "order_id int,order_date timestamp,customer_id int,order_status string"
df1 = spark.read.format("csv")\
           .option("header","True")\
           .schema(schema1)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/orders/orders_1gb.csv")\
           .load()
df1.show(truncate=False)
o/p:
========
+--------+-------------------+-----------+---------------+
|order_id|order_date         |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
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
|21      |2013-07-25 00:00:00|2711       |PENDING        |
+--------+-------------------+-----------+---------------+
schema2 = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("email", StringType(), True),
    StructField("street", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("customer_id", IntegerType(), True)
])
df2 = spark.read.format("csv")\
           .option("header","True")\
           .schema(schema2)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/retail_db/customers/part-00000")\
           .load()
df2.show(truncate=False)
o/p:
=======
+---+-----------+---------+---------+---------+---------------------------+-------------+-----+-----------+
|id |first_name |last_name|phone    |email    |street                     |city         |state|customer_id|
+---+-----------+---------+---------+---------+---------------------------+-------------+-----+-----------+
|2  |Mary       |Barrett  |XXXXXXXXX|XXXXXXXXX|9526 Noble Embers Ridge    |Littleton    |CO   |80126      |
|3  |Ann        |Smith    |XXXXXXXXX|XXXXXXXXX|3422 Blue Pioneer Bend     |Caguas       |PR   |725        |
|4  |Mary       |Jones    |XXXXXXXXX|XXXXXXXXX|8324 Little Common         |San Marcos   |CA   |92069      |
|5  |Robert     |Hudson   |XXXXXXXXX|XXXXXXXXX|10 Crystal River Mall      |Caguas       |PR   |725        |
|6  |Mary       |Smith    |XXXXXXXXX|XXXXXXXXX|3151 Sleepy Quail Promenade|Passaic      |NJ   |7055       |
|7  |Melissa    |Wilcox   |XXXXXXXXX|XXXXXXXXX|9453 High Concession       |Caguas       |PR   |725        |
|8  |Megan      |Smith    |XXXXXXXXX|XXXXXXXXX|3047 Foggy Forest Plaza    |Lawrence     |MA   |1841       |
|9  |Mary       |Perez    |XXXXXXXXX|XXXXXXXXX|3616 Quaking Street        |Caguas       |PR   |725        |
|10 |Melissa    |Smith    |XXXXXXXXX|XXXXXXXXX|8598 Harvest Beacon Plaza  |Stafford     |VA   |22554      |
|11 |Mary       |Huffman  |XXXXXXXXX|XXXXXXXXX|3169 Stony Woods           |Caguas       |PR   |725        |
|12 |Christopher|Smith    |XXXXXXXXX|XXXXXXXXX|5594 Jagged Embers By-pass |San Antonio  |TX   |78227      |
|13 |Mary       |Baldwin  |XXXXXXXXX|XXXXXXXXX|7922 Iron Oak Gardens      |Caguas       |PR   |725        |
|14 |Katherine  |Smith    |XXXXXXXXX|XXXXXXXXX|5666 Hazy Pony Square      |Pico Rivera  |CA   |90660      |
|15 |Jane       |Luna     |XXXXXXXXX|XXXXXXXXX|673 Burning Glen           |Fontana      |CA   |92336      |
|16 |Tiffany    |Smith    |XXXXXXXXX|XXXXXXXXX|6651 Iron Port             |Caguas       |PR   |725        |
|17 |Mary       |Robinson |XXXXXXXXX|XXXXXXXXX|1325 Noble Pike            |Taylor       |MI   |48180      |
|18 |Robert     |Smith    |XXXXXXXXX|XXXXXXXXX|2734 Hazy Butterfly Circle |Martinez     |CA   |94553      |
|19 |Stephanie  |Mitchell |XXXXXXXXX|XXXXXXXXX|3543 Red Treasure Bay      |Caguas       |PR   |725        |
|20 |Mary       |Ellis    |XXXXXXXXX|XXXXXXXXX|4703 Old Route             |West New York|NJ   |7093       |
|21 |William    |Zimmerman|XXXXXXXXX|XXXXXXXXX|3323 Old Willow Mall       |Caguas       |PR   |725        |
+---+-----------+---------+---------+---------+---------------------------+-------------+-----+-----------+
df_joined = df1.join(df2,df1.customer_id==df2.customer_id,"inner")
df_joined.show(truncate=False)
o/p:
=======
+--------+-------------------+-----------+---------------+-----+----------+----------+---------+---------+--------------------------+--------+-----+-----------+
|order_id|order_date         |customer_id|order_status   |id   |first_name|last_name |phone    |email    |street                    |city    |state|customer_id|
+--------+-------------------+-----------+---------------+-----+----------+----------+---------+---------+--------------------------+--------+-----+-----------+
|81      |2013-07-25 00:00:00|674        |PROCESSING     |12393|Mary      |Smith     |XXXXXXXXX|XXXXXXXXX|6567 High Lagoon Heath    |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |12014|Samantha  |Smith     |XXXXXXXXX|XXXXXXXXX|6097 Dewy Treasure Farm   |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |11522|Roy       |Smith     |XXXXXXXXX|XXXXXXXXX|9202 Clear Highway        |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |11284|Sarah     |Sherman   |XXXXXXXXX|XXXXXXXXX|7668 Fallen Orchard       |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |11035|Evelyn    |Fritz     |XXXXXXXXX|XXXXXXXXX|8477 Middle Court         |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |10607|Matthew   |Romero    |XXXXXXXXX|XXXXXXXXX|623 Round Bluff Cape      |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |10078|Mary      |Jones     |XXXXXXXXX|XXXXXXXXX|5282 Silent Landing       |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |8892 |Russell   |Dennis    |XXXXXXXXX|XXXXXXXXX|318 Blue Log Loop         |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |8157 |Mary      |Marshall  |XXXXXXXXX|XXXXXXXXX|4940 Silver Autumn Terrace|Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |5261 |Jennifer  |Suarez    |XXXXXXXXX|XXXXXXXXX|9600 Velvet Horse Freeway |Manati  |PR   |674        |
|81      |2013-07-25 00:00:00|674        |PROCESSING     |4666 |Mary      |Smith     |XXXXXXXXX|XXXXXXXXX|340 Velvet Barn Gate      |Manati  |PR   |674        |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|8525 |Mary      |Smith     |XXXXXXXXX|XXXXXXXXX|1846 Wishing Gate Green   |New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|8510 |Roger     |Smith     |XXXXXXXXX|XXXXXXXXX|1744 Shady Dale           |New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|7798 |James     |Smith     |XXXXXXXXX|XXXXXXXXX|257 Thunder Lane          |New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|5214 |Mary      |Poole     |XXXXXXXXX|XXXXXXXXX|346 Silver Hickory Village|New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|3606 |Joan      |Strickland|XXXXXXXXX|XXXXXXXXX|2319 Fallen Impasse       |New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|753  |Sandra    |Stafford  |XXXXXXXXX|XXXXXXXXX|7557 Wishing Falls        |New York|NY   |10033      |
|314     |2013-07-26 00:00:00|10033      |PENDING_PAYMENT|610  |Mary      |Smith     |XXXXXXXXX|XXXXXXXXX|6759 Foggy Limits         |New York|NY   |10033      |
|341     |2013-07-26 00:00:00|10128      |CLOSED         |11594|Mary      |Smith     |XXXXXXXXX|XXXXXXXXX|5257 Umber Field          |New York|NY   |10128      |
|341     |2013-07-26 00:00:00|10128      |CLOSED         |11460|Richard   |Payne     |XXXXXXXXX|XXXXXXXXX|1156 Silver Sky Line      |New York|NY   |10128      |
+--------+-------------------+-----------+---------------+-----+----------+----------+---------+---------+--------------------------+--------+-------------------

9. Broadcast join:
=====================
i. In Broadcast join we have one small table and one large table , the smaller table is broadcasted from driver machine across all executor and a complete copy of this smaller table is
present on each executor and the larger table is distributed across all executor so same key is present on all machine so join takes place and shuffling is minimised.
ii. Shuffling is minimised.
iii. Code:
==============
a. Using lower level API:
=============================
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
orders_base = spark.sparkContext.textFile("/public/trendytech/orders/orders_1gb.csv")
orders_base.take(10)
o/p:
=======
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
customers_base = spark.sparkContext.textFile("/public/trendytech/retail_db/customers/part-00000")
customers_base.take(10)
o/p:
======
['1,Richard,Hernandez,XXXXXXXXX,XXXXXXXXX,6303 Heather Plaza,Brownsville,TX,78521',
 '2,Mary,Barrett,XXXXXXXXX,XXXXXXXXX,9526 Noble Embers Ridge,Littleton,CO,80126',
 '3,Ann,Smith,XXXXXXXXX,XXXXXXXXX,3422 Blue Pioneer Bend,Caguas,PR,00725',
 '4,Mary,Jones,XXXXXXXXX,XXXXXXXXX,8324 Little Common,San Marcos,CA,92069',
 '5,Robert,Hudson,XXXXXXXXX,XXXXXXXXX,"10 Crystal River Mall ",Caguas,PR,00725',
 '6,Mary,Smith,XXXXXXXXX,XXXXXXXXX,3151 Sleepy Quail Promenade,Passaic,NJ,07055',
 '7,Melissa,Wilcox,XXXXXXXXX,XXXXXXXXX,9453 High Concession,Caguas,PR,00725',
 '8,Megan,Smith,XXXXXXXXX,XXXXXXXXX,3047 Foggy Forest Plaza,Lawrence,MA,01841',
 '9,Mary,Perez,XXXXXXXXX,XXXXXXXXX,3616 Quaking Street,Caguas,PR,00725',
 '10,Melissa,Smith,XXXXXXXXX,XXXXXXXXX,8598 Harvest Beacon Plaza,Stafford,VA,22554']
orders_mapped = orders_base.map(lambda x:(x.split(",")[2],x.split(",")[3]))
orders_mapped.take(10)
o/p:
======
[('11599', 'CLOSED'),
 ('256', 'PENDING_PAYMENT'),
 ('12111', 'COMPLETE'),
 ('8827', 'CLOSED'),
 ('11318', 'COMPLETE'),
 ('7130', 'COMPLETE'),
 ('4530', 'COMPLETE'),
 ('2911', 'PROCESSING'),
 ('5657', 'PENDING_PAYMENT'),
 ('5648', 'PENDING_PAYMENT')]
customers_mapped = customers_base.map(lambda x:(x.split(",")[0],x.split(",")[8]))
customers_mapped.take(10)
o/p:
=====
[('1', '78521'),
 ('2', '80126'),
 ('3', '00725'),
 ('4', '92069'),
 ('5', '00725'),
 ('6', '07055'),
 ('7', '00725'),
 ('8', '01841'),
 ('9', '00725'),
 ('10', '22554')]
customers_broadcast = spark.sparkContext.broadcast(customers_mapped.collect())
def get_pincode(customer_id):
    try:
        return customers_broadcast.value[customer_id]
    except:
        return "-1"
joined_rdd = orders_mapped.map(lambda x:(get_pincode(int(x[0])),x[1]))
joined_rdd.take(10)
o/p:
======
[(('11600', '00725'), 'CLOSED'),
 (('257', '00791'), 'PENDING_PAYMENT'),
 (('12112', '00725'), 'COMPLETE'),
 (('8828', '00725'), 'CLOSED'),
 (('11319', '00612'), 'COMPLETE'),
 (('7131', '92129'), 'COMPLETE'),
 (('4531', '78046'), 'COMPLETE'),
 (('2912', '93063'), 'PROCESSING'),
 (('5658', '78550'), 'PENDING_PAYMENT'),
 (('5649', '00725'), 'PENDING_PAYMENT')]
b. Using Df:
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
schema1 = "order_id int,order_date timestamp,customer_id int,order_status string"
df1 = spark.read.format("csv")\
           .option("header","True")\
           .schema(schema1)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/orders/orders_1gb.csv")\
           .load()
df1.show(truncate=False)
o/p:
======


schema2 = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("email", StringType(), True),
    StructField("street", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("customer_id", IntegerType(), True)
])
df2 = spark.read.format("csv")\
           .option("header","True")\
           .schema(schema2)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/retail_db/customers/part-00000")\
           .load()
df2.show(truncate=False)
df_joined = df1.join(
    broadcast(df2),
    df1.customer_id == df2.customer_id,
    "inner"
)
df_joined.show(truncate=False)


10. Repartition vs Coalesce:
===================================
i. Repartition():
=====================
a. It can increase the no of partitions and it can also decrease the no of partitions.
b. But decrease of partition is not recommended because it gives resultant partition of equal size so to do so it involve complete shuffle of data.
c. It gives resultant partition of equal size.
d. It  involve complete shuffle of data.
e. It does not give skewed partition.
Note: It is mainly recommended to increase the no of partition.

ii. Coalesce():
====================
a. It can only decrease the no of partition.
b. It does not give resultant partition of equal size.
c. It minimize shuffling of data.
d. It cannot increase no of partitions.
e. It leads to skewwed partitions.

Impt point to Remember:
i. You might want to increase the no of partitions to get more parallelism.
ii. You might want to decrease the no of partition after transformation like filter where you know that each partition is holding very less data.

 Code:
===============
a. Using rdd():
=========================
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
orders_base = spark.sparkContext.textFile("/public/trendytech/orders/orders_1gb.csv")
orders_base.getNumPartitions()
o/p:
========
9
new_rdd = orders_base.repartition(15)
orders_base.getNumPartitions()
o/p:
========
9
new_rdd = orders_base.coalesce(30)
orders_base.getNumPartitions()
o/p:
======
9
new_rdd = orders_base.coalesce(5)
new_rdd.getNumPartitions()
o/p:
========
5

b. a. Using df():
=========================
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
schema1 = "order_id int,order_date timestamp,customer_id int,order_status string"
df1 = spark.read.format("csv")\
           .option("header","True")\
           .schema(schema1)\
           .option("delimeter",",")\
           .option("path","/public/trendytech/orders/orders_1gb.csv")\
           .load()
df1.show(truncate=False)
0/p:
=======
+--------+-------------------+-----------+---------------+
|order_id|order_date         |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
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
|21      |2013-07-25 00:00:00|2711       |PENDING        |
+--------+-------------------+-----------+---------------+
df1.printSchema()
o/p:
=======
root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)

df1.rdd.getNumPartitions()
o/p:
=======
9
new_df1 = df1.repartition(15)
new_df1.rdd.getNumPartitions()
o/p:
=========
15
new_df1 = df1.coalesce(30)
new_df1.rdd.getNumPartitions()
o/p:
=========
9
new_df1 = df1.coalesce(5)
new_df1.rdd.getNumPartitions()
o/p:
=========
5

11. cache() vs persist():
================================
i. cache():
===============
a. It is a transformation which means it is an lazy operation.
b. We should apply cache() on resultant rdd so that we can reuse that rdd again and again and our application will run faster.
c. cache is always in memory.
d. If we apply cache on resultant rdd and we call multiple action on our resultant rdd than for the first action all the transformation from beginning to end will be executed
   and cache will store the intermediate result in memory and when we call the 2nd action it will take the intermediate result from memory and execute result of the operation 
   in a faster mamnner so this will make our application run faster.
e. we should not apply cache() on base_rdd.
f. code:
=============
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
orders_filtered = orders_base.filter(lambda x:x.split(",")[3]!="PENDING_PAYMENT")
orders_mapped = orders_filtered.map(lambda x:(x.split(",")[2],1))
orders_reduced = orders_mapped.reduceByKey(lambda x,y:x+y)
result = orders_reduced.filter(lambda x:int(x[0])<501)
result.cache()
o/p:
=========
PythonRDD[6] at RDD at PythonRDD.scala:53
result.collect()
o/p:
=======
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
 ('315', 1125),
 ('106', 750),
 ('247', 2625),
 ('100', 2250),
 ('291', 1500),
 ('227', 1500),
 ('498', 1500),
 ('124', 1500),
 ('452', 1500),
 ('43', 750),
 ('134', 1500),
 ('448', 1500),
 ('295', 750),
 ('476', 375),
 ('294', 1125),
 ('441', 1125),
 ('225', 1875),
 ('33', 750),
 ('293', 750),
 ('178', 375),
 ('31', 1125),
 ('173', 3000),
 ('457', 2625),
 ('460', 1875),
 ('444', 1875),
 ('48', 3000),
 ('464', 1875),
 ('478', 2250),
 ('109', 1875),
 ('157', 750),
 ('114', 1500),
 ('226', 1500),
 ('96', 1875),
 ('355', 1500),
 ('60', 1875),
 ('359', 1500),
 ('208', 1500),
 ('36', 1125),
 ('302', 375),
 ('231', 2625),
 ('93', 1875),
 ('50', 1875),
 ('411', 1500),
 ('305', 1500),
 ('317', 1125),
 ('479', 375),
 ('8', 2250),
 ('327', 1875),
 ('269', 375),
 ('356', 2250),
 ('335', 3750),
 ('408', 1875),
 ('92', 1875),
 ('155', 1500),
 ('35', 1125),
 ('367', 1875),
 ('449', 1125),
 ('257', 2625),
 ('224', 1875),
 ('425', 1875),
 ('465', 2625),
 ('332', 2250),
 ('229', 2250),
 ('321', 3000),
 ('85', 2250),
 ('152', 1125),
 ('198', 1500),
 ('84', 750),
 ('170', 1125),
 ('329', 2250),
 ('3', 2625),
 ('237', 750),
 ('435', 1875),
 ('190', 1875),
 ('311', 1500),
 ('421', 1125),
 ('394', 1500),
 ('346', 1125),
 ('412', 1500),
 ('261', 750),
 ('140', 1875),
 ('10', 750),
 ('253', 375),
 ('153', 375),
 ('396', 1875),
 ('254', 2250),
 ('232', 1500),
 ('11', 1125),
 ('484', 1875),
 ('442', 2625),
 ('172', 2625),
 ('17', 1875),
 ('46', 1875),
 ('38', 2250),
 ('422', 1875),
 ('467', 3000),
 ('437', 3750),
 ('47', 1125),
 ('205', 1875),
 ('216', 1125),
 ('482', 3750),
 ('221', 4500),
 ('347', 1125),
 ('292', 750),
 ('312', 2625),
 ('490', 750),
 ('284', 1500),
 ('51', 3000),
 ('148', 1125),
 ('406', 1500),
 ('296', 3000),
 ('414', 750),
 ('164', 1500),
 ('26', 1875),
 ('373', 1875),
 ('277', 1500),
 ('447', 1500),
 ('368', 1500),
 ('182', 1125),
 ('87', 1500),
 ('385', 750),
 ('25', 750),
 ('116', 750),
 ('95', 2250),
 ('306', 1875),
 ('255', 2250),
 ('251', 1500),
 ('136', 750),
 ('6', 750),
 ('310', 750),
 ('419', 1500),
 ('345', 2250),
 ('195', 750),
 ('207', 2250),
 ('230', 1875),
 ('324', 1500),
 ('454', 2250),
 ('430', 2625),
 ('197', 3000),
 ('450', 3000),
 ('44', 1125),
 ('440', 1875),
 ('378', 1500),
 ('429', 1500),
 ('119', 3000),
 ('23', 1875),
 ('313', 375),
 ('147', 1500),
 ('13', 2250),
 ('16', 2250),
 ('27', 1875),
 ('233', 1875),
 ('471', 1500),
 ('113', 1500),
 ('71', 3000),
 ('101', 1875),
 ('258', 2625),
 ('20', 1875),
 ('279', 1125),
 ('297', 2625),
 ('282', 1500),
 ('456', 750),
 ('438', 1125),
 ('451', 375),
 ('127', 1125),
 ('319', 2250),
 ('432', 1125),
 ('364', 3375),
 ('63', 2250),
 ('445', 1500),
 ('90', 1500),
 ('443', 3000),
 ('342', 1500),
 ('111', 750),
 ('107', 1875),
 ('262', 1875),
 ('349', 1500),
 ('66', 1125),
 ('337', 1500),
 ('74', 2625),
 ('278', 750),
 ('322', 750),
 ('160', 1125),
 ('301', 375),
 ('135', 375),
 ('94', 2250),
 ('272', 3000),
 ('179', 1500),
 ('371', 1875),
 ('426', 1875),
 ('223', 1125),
 ('241', 2250),
 ('58', 2625),
 ('488', 1500),
 ('409', 2625),
 ('458', 1875),
 ('267', 1125),
 ('15', 1125),
 ('480', 1125),
 ('475', 1875),
 ('187', 1875),
 ('439', 1500),
 ('354', 3750),
 ('141', 2250),
 ('264', 1125),
 ('62', 1500),
 ('194', 1500),
 ('472', 2250),
 ('185', 1875),
 ('139', 1125),
 ('340', 2250),
 ('314', 3375),
 ('176', 1875),
 ('500', 1125),
 ('401', 1125),
 ('64', 750),
 ('375', 1500),
 ('110', 1875),
 ('320', 1875),
 ('252', 1875),
 ('433', 2250),
 ('413', 750),
 ('234', 1125),
 ('9', 1125),
 ('181', 1125),
 ('86', 1125),
 ('477', 2250),
 ('386', 1125),
 ('167', 750),
 ('145', 2250),
 ('485', 750),
 ('330', 1500),
 ('161', 1500),
 ('239', 1875),
 ('249', 750),
 ('350', 1500),
 ('81', 750),
 ('42', 1875),
 ('59', 1500),
 ('325', 1125),
 ('466', 375),
 ('461', 1125),
 ('405', 750),
 ('29', 375),
 ('146', 1500),
 ('497', 2250),
 ('273', 2250),
 ('377', 2250),
 ('308', 2250),
 ('455', 3000),
 ('379', 1875),
 ('188', 1500),
 ('126', 1875),
 ('263', 750),
 ('75', 1875),
 ('418', 375)]
 
result.count()
o/p:
=====
492

spark.stop()


ii. persist():
====================
a. persist comes with various storage level like persist on disk,persist in memeory, persist on memeory and disk.

12. How to find Data Skewness in spark/How to get count of rows from each partition in spark:
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

13. RDD vs Dataframe vs sparksql:
=====================================
i. RDD (Resilient Distributed Dataset):
============================================
a. RDD stands for Resilient Distributed Dataset.
b. It is a lower level API.
c. Defination:
==================
. The basic unit which holds data in spark is referred to as RDD.
ii. Combination of distributed partitions in memory together form a RDD.
iii. It is simply raw data without any schema.

d. There is no schema attached with data.
e. It does not give optimization because spark engine does not optimize the rdd code using catalyst optimizer.
f. It is immutable which means we cannot change the content of RDD.
g. It is more flexible as compared to df and sparksql.
RDD > DF > sparksql
Flexibility means not every solution you can code in sql style, but everything can be done in RDD style.
h. In terms of complexity RDD is toughest.
Easy: sparksql > df > RDD.
i. It is not developer friendly. because using RDD developer cannot use sql way of writing the code.
j. It is not so efficient which means it does not give good performance.
k. RDD is resilient to failure which means it is fault tolerant so we can recover failed RDD using lineage graph and RDD immutability.
l. In case of RDD the data is stored in memory in form of partitions so as soon as you stop the sparksession/sparkcontext you data will be lost
so it is not persistent.
m. To check no of partitions: rdd.getNumPartitions().
n. It uses sparkcontext.
o. There are multiple way to create rdd:
   a. 1st Using local variable like list:
      =======================================
       my_list = [1,2,3,4,5,6,7,8,9,10]
       rdd1 = spark.sparkContext.parallelize(my_list)
       rdd1.collect()
       o/p:
       ======
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   b. 2nd Using textFile:
      ===========================
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

ii. df (Dataframe):
=======================
a. Df is a higher level API so it is a wrapper on top of lower level api.
higher level API = schema + lower level API.
b. Defination:
======================
i. Dataframe is a distributed collection of data organised into named column.
ii. In case of dataframe schema is attached with data so it gives a tabular view.
iii. It is similar like myssql table but distributed across multiple machines.
c. In case of Df, schema is attached with data.
Df = schema + rdd(raw data).
d. In terms of complexity it is less complex than RDD but it is more complex than sparksql.
Easy: sparksql > df > RDD.
e. In terms of flexibility it is less flexible than RDD but more flexible than sparksql.
RDD > DF > sparksql
f. It is also immutable and distributed.
g. It gives optimization because spark engine internally optimize the df code using catalyst optimizer.
h. It is more efficeint than Rdd but less efficient than sparksql, because in terms of performance it is better than Rdd.
i. It is developer friendly.
j. In case of Df we have:
    i. Data that is stored in memory.
    ii. Metadata is stored in memory (temporary metadata catalog).
It is not persistent so as soon as we stop sparksession both data + metadata is lost.
k. It uses sparksession.
l. To check no of partitions : df.rdd.getNumPartitions().
m. There are multiple way to create a dataframe df():
    a. First using list of multiple tuple:
       =====================================
       data = [
    ("Work hard in #silence, let #success make the noise.",),
    ("Be #yourself; everyone else is already taken.",),
    ("The only way to do #greatwork is to #love what you do.",),
    ("#Believe you can and you're #halfway there.",),
    ("The #future belongs to those who #believe in the #beauty of their #dreams.",)
]
df = spark.createDataFrame(data, ["quote"])
df.show(truncate=False)
    b. 2nd Using different file format like csv,parquet,orc,avro,json,jdbc:
       =====================================================================
       syntax
    c. 3rd Using rdd:
       =========================
       df = rdd.toDF(["col1", "col2"])
       df = spark.createDataFrame(rdd, ["col1", "col2"])

iii. sparksql:
======================
a. It is higher level API.
b. To access sparksql from df we create a temporary or global temporary view:
   df.createOrReplaceTempView("orders")
   df.createTempView("orders1")
   df.createOrReplaceGlobalTempView("orders2").
c. In case of sparksql schema is attached with data, so we get tabular view similar like sql but the difference is 
it is dsitributed across multiple machines so we will get parallelism.
d. In terms of complexity it is easiest of all:
 Easy: sparksql > df > RDD.
e. In terms of fleixibity , it is least flexible. 
RDD > DF > sparksql
f. It is distributed and immutable.
g. It gives optimization because spark engine optimize sparksql code using catalyst optimizer.
h. It is more efficent than RDD but it terms of performance both df and sparksql are same.
i. It is developer friendly.
j. spark table that we access using sparksql is persistent:
    i. Data - stored in disk(s3/ADLS GEN2/GCS).
    ii. Meatadata - It is stored in permanent metastore.
so even we stop the sparksession still you can access data + metadata so spark table that we access using sparksql is persistent.
k. It uses sparksession.
l. To check no of partitions:
=================================
df.rdd.getNumPartitions().
m. Multiple ways to create sparktable out of df:
=====================================================
    a. df.createTempView("orders1")
    b. df.createOrReplaceTempView("orders")
    c. df.createOrReplaceGlobalTempView("orders2")

Similarity b/t df vs sparksql:
===============================
i. Both gives same performance.
ii. Both are developer friendly.
iii. Both uses spark session.
iv. Both gives optimization.

Note: Both df/sparksql gives good performance because it contains data + metadata(datatype,col_name) so spark engine uses this data + metdata information to internally 
optimize the code using catalyst optimizer, but in case of rdd we dont have metdata information so spark engine find it difficult to optimize the rdd code internally using
catalyst optimizer.

14. Use of inferSchema:
==============================
i. It does not give correct inference , so we will not get correct datatype.
ii. It takes lot of time because it scan entire file and try to infer the datatype so if file size is huge it takes lot of time.
iii. In production it is not recommended to use inferSchema.
iv. Instead of using inferSchema we can explicitly define a schema.
v. Code:
==============
orders_df = spark.read.format("csv")\
                 .option("header",True)\
                 .option("inferSchema",True)\
                 .option("delimeter",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()
orders_df.printSchema()
o/p:
========
root
 |-- order_id: integer (nullable = true)
 |-- order_date: string (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
 
vi. Explicit schema:
=======================
a. Programmatic style:
===========================
orders_schema = StructType([\
                           StructField("order_id",IntegerType(),True),\
                           StructField("order_date",TimestampType(),True),\
                           StructField("customer_id",IntegerType(),True),\
                           StructField("order_status",StringType(),True)])
orders_df = spark.read.format("csv")\
                 .option("header",True)\
                 .schema(orders_schema)\
                 .option("delimeter",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()
orders_df.printSchema()
o/p:
========
root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
 
 b. SQL Style:
=================
orders_schema = "order_id int,order_date timestamp,customer_id int,order_status string"
orders_df = spark.read.format("csv")\
                 .option("header",True)\
                 .schema(orders_schema)\
                 .option("delimeter",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()
orders_df.printSchema()
o/p:
=======
root
 |-- order_id: integer (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)
 
Note: In production we should enforce schema instead of using inferSchema.

15. Multiply way to read csv,json,parquet,orc,avro,table:
============================================================
i. CSV File(row based file format + partial schema + comma/pipe separated + faster write):
==========================================================================================
a. Standard Df reader API:
===============================
orders_df_csv = spark.read.format("csv")\
                 .option("header",True)\
                 .option("inferSchema",True)\
                 .option("delimeter",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()
b. 2nd way to read a csv file:
=================================
orders_df_csv = spark.read.csv(path = "/public/trendytech/orders_wh/orders_wh.csv",header = True,inferSchema = True,sep = ",")

ii. JSON File(row based file format + partial schema + K,V pair + faster write):
================================================================================
a. Standard Df reader API:
===============================
orders_df_json = spark.read.format("csv")\
                 .option("header",True)\
                 .option("inferSchema",True)\
                 .option("delimeter",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()
b. 2nd way to read a csv file:
=================================
orders_df_json = spark.read.csv(path = "/public/trendytech/orders_wh/orders_wh.csv",header = True,inferSchema = True,sep = ",")

iii. Parquet File Format(column based file format + binary format(not human readeable) + faster read + comsume less storage space + schema evolution + internally uses snappy
based compression technique):
=========================================================================================================================================================
a. Standard Df reader API:
===============================
orders_df_parquet = spark.read.format("parquet")\
                         .option("path","/public/trendytech/datasets/ordersparquet/*")\
                         .load()
orders_df_parquet.show(truncate = False)
orders_df_parquet.printSchema()
b. 2nd way to read a csv file:
=================================
orders_df_parquet = spark.read.parquet(path = "/public/trendytech/datasets/ordersparquet/")
orders_df_parquet.show(truncate = False)
orders_df_parquet.printSchema()
Note: Best compatible with spark.

iv. Orc File Format (column based file format + faster read + comsume less storage space + best suited for Hive + binary format(not human readeable) + internally uses snappy
based compression technique)):
==============================================================================================================================================================================
a. Standard Df reader API:
===============================
orders_df_orc = spark.read.format("orc")\
                     .option("path","/public/trendytech/datasets/ordersorc/*")\
                     .load()
orders_df_orc.show(truncate = False)
orders_df_orc.printSchema()
b. 2nd way to read a csv file:
=================================
orders_df_orc = spark.read.orc(path = "/public/trendytech/datasets/ordersorc/*")
                     
orders_df_orc.show(truncate = False)
orders_df_orc.printSchema()

Note: ORC supports schema evolution because it is self-describing and columnar, allowing addition/removal of columns without affecting existing data. 
It is best suited with Hive because it is natively integrated, supports predicate pushdown, compression, and Hive ACID transactions, handle complex datatype of hive.

 v. AVRO File Format (Row based file format + faster write + best suited for kafka + not human readable):
==============================================================================================================
i. By default avro is not not supported in spark so use this in spark we have to import a package based on our spark version:
=======================================================================================================================================
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
a. Standard Df reader API:
===============================
orders_df_avro = spark.read.format("avro")\
                     .option("path","/public/trendytech/datasets/orders_avro/*")\
                     .load()
orders_df_avro.show(truncate = False)
orders_df_avro.printSchema()

16. .where() vs .filter():
====================================
i. In terms of performance both are same.
syntax:
==============
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
orders_df_avro = spark.read.format("avro")\
                     .option("path","/public/trendytech/datasets/orders_avro/*")\
                     .load()
orders_df_avro.show(truncate = False)
orders_df_avro.printSchema()
o/p:
=========
+--------+---------------------+-------+---------------+
|order_id|order_date           |cust_id|order_status   |
+--------+---------------------+-------+---------------+
|51049   |2014-06-09 00:00:00.0|4983   |PROCESSING     |
|51050   |2014-06-09 00:00:00.0|1840   |ON_HOLD        |
|51051   |2014-06-09 00:00:00.0|8207   |COMPLETE       |
|51052   |2014-06-09 00:00:00.0|6254   |COMPLETE       |
|51053   |2014-06-09 00:00:00.0|348    |PENDING        |
|51054   |2014-06-09 00:00:00.0|1468   |COMPLETE       |
|51055   |2014-06-09 00:00:00.0|3843   |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00.0|7178   |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00.0|749    |COMPLETE       |
|51058   |2014-06-09 00:00:00.0|5146   |PENDING        |
|51059   |2014-06-09 00:00:00.0|4645   |CLOSED         |
|51060   |2014-06-09 00:00:00.0|247    |COMPLETE       |
|51061   |2014-06-09 00:00:00.0|6551   |PENDING        |
|51062   |2014-06-09 00:00:00.0|5548   |PROCESSING     |
|51063   |2014-06-09 00:00:00.0|7020   |CLOSED         |
|51064   |2014-06-09 00:00:00.0|909    |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00.0|7975   |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00.0|6494   |PENDING        |
|51067   |2014-06-09 00:00:00.0|1380   |CLOSED         |
|51068   |2014-06-09 00:00:00.0|5766   |COMPLETE       |
+--------+---------------------+-------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

transformed_df = orders_df_avro.withColumn("order_date_new",to_timestamp(col("order_date")))\
                               .withColumnRenamed("cust_id","customer_id")\
                               .select(col("order_id"),col("order_date_new"),col("customer_id"),col("order_status"))
transformed_df.show(truncate = False)
transformed_df.printSchema()
o/p:
=======
+--------+-------------------+-----------+---------------+
|order_id|order_date_new     |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|51049   |2014-06-09 00:00:00|4983       |PROCESSING     |
|51050   |2014-06-09 00:00:00|1840       |ON_HOLD        |
|51051   |2014-06-09 00:00:00|8207       |COMPLETE       |
|51052   |2014-06-09 00:00:00|6254       |COMPLETE       |
|51053   |2014-06-09 00:00:00|348        |PENDING        |
|51054   |2014-06-09 00:00:00|1468       |COMPLETE       |
|51055   |2014-06-09 00:00:00|3843       |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00|7178       |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00|749        |COMPLETE       |
|51058   |2014-06-09 00:00:00|5146       |PENDING        |
|51059   |2014-06-09 00:00:00|4645       |CLOSED         |
|51060   |2014-06-09 00:00:00|247        |COMPLETE       |
|51061   |2014-06-09 00:00:00|6551       |PENDING        |
|51062   |2014-06-09 00:00:00|5548       |PROCESSING     |
|51063   |2014-06-09 00:00:00|7020       |CLOSED         |
|51064   |2014-06-09 00:00:00|909        |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00|7975       |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00|6494       |PENDING        |
|51067   |2014-06-09 00:00:00|1380       |CLOSED         |
|51068   |2014-06-09 00:00:00|5766       |COMPLETE       |
+--------+-------------------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date_new: timestamp (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)

i. .filter():
===================
a. filtered_df = transformed_df.filter(col("customer_id")==11599).show(5, truncate = False)
b. filtered_df = transformed_df.filter("customer_id = 11599").show(5, truncate = False)
o/p:
=========
+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|53545   |2014-06-27 00:00:00|11599      |PENDING     |
|59911   |2013-10-17 00:00:00|11599      |PROCESSING  |
|1       |2013-07-25 00:00:00|11599      |CLOSED      |
|11397   |2013-10-03 00:00:00|11599      |COMPLETE    |
|23908   |2013-12-20 00:00:00|11599      |COMPLETE    |
+--------+-------------------+-----------+------------+
only showing top 5 rows

+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|53545   |2014-06-27 00:00:00|11599      |PENDING     |
|59911   |2013-10-17 00:00:00|11599      |PROCESSING  |
|1       |2013-07-25 00:00:00|11599      |CLOSED      |
|11397   |2013-10-03 00:00:00|11599      |COMPLETE    |
|23908   |2013-12-20 00:00:00|11599      |COMPLETE    |
+--------+-------------------+-----------+------------+
only showing top 5 rows

ii. .where():
==================
a. filtered_df = transformed_df.where(col("customer_id")==11599).show(5, truncate = False)
b. filtered_df = transformed_df.where("customer_id = 11599").show(5, truncate = False)
o/p:
=========
+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|53545   |2014-06-27 00:00:00|11599      |PENDING     |
|59911   |2013-10-17 00:00:00|11599      |PROCESSING  |
|1       |2013-07-25 00:00:00|11599      |CLOSED      |
|11397   |2013-10-03 00:00:00|11599      |COMPLETE    |
|23908   |2013-12-20 00:00:00|11599      |COMPLETE    |
+--------+-------------------+-----------+------------+
only showing top 5 rows

+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|53545   |2014-06-27 00:00:00|11599      |PENDING     |
|59911   |2013-10-17 00:00:00|11599      |PROCESSING  |
|1       |2013-07-25 00:00:00|11599      |CLOSED      |
|11397   |2013-10-03 00:00:00|11599      |COMPLETE    |
|23908   |2013-12-20 00:00:00|11599      |COMPLETE    |
+--------+-------------------+-----------+------------+
only showing top 5 rows

17. .createOrReplaceTempView() vs .createOrReplaceGlobalTempView() vs .createTempView() :
================================================================================================
i. .createOrReplaceTempView():
=======================================
a. It is accesible within the sparksession where it is created, it will not be accesible within other spark application(sparksession).
b. syntax:
==================
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
orders_df_avro = spark.read.format("avro")\
                     .option("path","/public/trendytech/datasets/orders_avro/*")\
                     .load()
orders_df_avro.show(truncate = False)
orders_df_avro.printSchema()
o/p:
========
+--------+---------------------+-------+---------------+
|order_id|order_date           |cust_id|order_status   |
+--------+---------------------+-------+---------------+
|51049   |2014-06-09 00:00:00.0|4983   |PROCESSING     |
|51050   |2014-06-09 00:00:00.0|1840   |ON_HOLD        |
|51051   |2014-06-09 00:00:00.0|8207   |COMPLETE       |
|51052   |2014-06-09 00:00:00.0|6254   |COMPLETE       |
|51053   |2014-06-09 00:00:00.0|348    |PENDING        |
|51054   |2014-06-09 00:00:00.0|1468   |COMPLETE       |
|51055   |2014-06-09 00:00:00.0|3843   |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00.0|7178   |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00.0|749    |COMPLETE       |
|51058   |2014-06-09 00:00:00.0|5146   |PENDING        |
|51059   |2014-06-09 00:00:00.0|4645   |CLOSED         |
|51060   |2014-06-09 00:00:00.0|247    |COMPLETE       |
|51061   |2014-06-09 00:00:00.0|6551   |PENDING        |
|51062   |2014-06-09 00:00:00.0|5548   |PROCESSING     |
|51063   |2014-06-09 00:00:00.0|7020   |CLOSED         |
|51064   |2014-06-09 00:00:00.0|909    |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00.0|7975   |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00.0|6494   |PENDING        |
|51067   |2014-06-09 00:00:00.0|1380   |CLOSED         |
|51068   |2014-06-09 00:00:00.0|5766   |COMPLETE       |
+--------+---------------------+-------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 transformed_df = orders_df_avro.withColumn("order_date_new",to_timestamp(col("order_date")))\
                               .withColumnRenamed("cust_id","customer_id")\
                               .select(col("order_id"),col("order_date_new"),col("customer_id"),col("order_status"))
                               
transformed_df.show(truncate = False)
transformed_df.printSchema()
o/p:
==========
+--------+-------------------+-----------+---------------+
|order_id|order_date_new     |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|51049   |2014-06-09 00:00:00|4983       |PROCESSING     |
|51050   |2014-06-09 00:00:00|1840       |ON_HOLD        |
|51051   |2014-06-09 00:00:00|8207       |COMPLETE       |
|51052   |2014-06-09 00:00:00|6254       |COMPLETE       |
|51053   |2014-06-09 00:00:00|348        |PENDING        |
|51054   |2014-06-09 00:00:00|1468       |COMPLETE       |
|51055   |2014-06-09 00:00:00|3843       |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00|7178       |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00|749        |COMPLETE       |
|51058   |2014-06-09 00:00:00|5146       |PENDING        |
|51059   |2014-06-09 00:00:00|4645       |CLOSED         |
|51060   |2014-06-09 00:00:00|247        |COMPLETE       |
|51061   |2014-06-09 00:00:00|6551       |PENDING        |
|51062   |2014-06-09 00:00:00|5548       |PROCESSING     |
|51063   |2014-06-09 00:00:00|7020       |CLOSED         |
|51064   |2014-06-09 00:00:00|909        |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00|7975       |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00|6494       |PENDING        |
|51067   |2014-06-09 00:00:00|1380       |CLOSED         |
|51068   |2014-06-09 00:00:00|5766       |COMPLETE       |
+--------+-------------------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date_new: timestamp (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)

transformed_df.createOrReplaceTempView("orders")
filtered_df = spark.sql("""select * from orders
                           where order_status = 'CLOSED'""")
filtered_df.show(5,truncate = False)
o/p:
=========
+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|51059   |2014-06-09 00:00:00|4645       |CLOSED      |
|51063   |2014-06-09 00:00:00|7020       |CLOSED      |
|51067   |2014-06-09 00:00:00|1380       |CLOSED      |
|51071   |2014-06-09 00:00:00|6502       |CLOSED      |
|51079   |2014-06-09 00:00:00|2031       |CLOSED      |
+--------+-------------------+-----------+------------+

If I am trying to acces this spark table "orders" from other sparksession(application) you will get error not able to access:
==================================================================================================================================
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
filtered_df = spark.sql("""select * from orders
                           """)
filtered_df.show(truncate = False)
o/p:
=========
Py4JJavaError: An error occurred while calling o50.sql.
: java.util.concurrent.ExecutionException: org.apache.hadoop.security.AccessControlException: 
Permission denied: user=itv022641, access=EXECUTE, inode="/user/itv024340":itv024340:supergroup:drwx------  

ii.  .createOrReplaceGlobalTempView():
=============================================
i. It we create a GlobalTempView() it will be accesible within the sparksession where it is created and also
   It will be accesible in other sparksession (spark application) also.
   
ii. syntax:
====================
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
orders_df_avro = spark.read.format("avro")\
                     .option("path","/public/trendytech/datasets/orders_avro/*")\
                     .load()
orders_df_avro.show(truncate = False)
orders_df_avro.printSchema()
o/p:
========
+--------+---------------------+-------+---------------+
|order_id|order_date           |cust_id|order_status   |
+--------+---------------------+-------+---------------+
|51049   |2014-06-09 00:00:00.0|4983   |PROCESSING     |
|51050   |2014-06-09 00:00:00.0|1840   |ON_HOLD        |
|51051   |2014-06-09 00:00:00.0|8207   |COMPLETE       |
|51052   |2014-06-09 00:00:00.0|6254   |COMPLETE       |
|51053   |2014-06-09 00:00:00.0|348    |PENDING        |
|51054   |2014-06-09 00:00:00.0|1468   |COMPLETE       |
|51055   |2014-06-09 00:00:00.0|3843   |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00.0|7178   |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00.0|749    |COMPLETE       |
|51058   |2014-06-09 00:00:00.0|5146   |PENDING        |
|51059   |2014-06-09 00:00:00.0|4645   |CLOSED         |
|51060   |2014-06-09 00:00:00.0|247    |COMPLETE       |
|51061   |2014-06-09 00:00:00.0|6551   |PENDING        |
|51062   |2014-06-09 00:00:00.0|5548   |PROCESSING     |
|51063   |2014-06-09 00:00:00.0|7020   |CLOSED         |
|51064   |2014-06-09 00:00:00.0|909    |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00.0|7975   |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00.0|6494   |PENDING        |
|51067   |2014-06-09 00:00:00.0|1380   |CLOSED         |
|51068   |2014-06-09 00:00:00.0|5766   |COMPLETE       |
+--------+---------------------+-------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 transformed_df = orders_df_avro.withColumn("order_date_new",to_timestamp(col("order_date")))\
                               .withColumnRenamed("cust_id","customer_id")\
                               .select(col("order_id"),col("order_date_new"),col("customer_id"),col("order_status"))
                               
transformed_df.show(truncate = False)
transformed_df.printSchema()
o/p:
==========
+--------+-------------------+-----------+---------------+
|order_id|order_date_new     |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|51049   |2014-06-09 00:00:00|4983       |PROCESSING     |
|51050   |2014-06-09 00:00:00|1840       |ON_HOLD        |
|51051   |2014-06-09 00:00:00|8207       |COMPLETE       |
|51052   |2014-06-09 00:00:00|6254       |COMPLETE       |
|51053   |2014-06-09 00:00:00|348        |PENDING        |
|51054   |2014-06-09 00:00:00|1468       |COMPLETE       |
|51055   |2014-06-09 00:00:00|3843       |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00|7178       |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00|749        |COMPLETE       |
|51058   |2014-06-09 00:00:00|5146       |PENDING        |
|51059   |2014-06-09 00:00:00|4645       |CLOSED         |
|51060   |2014-06-09 00:00:00|247        |COMPLETE       |
|51061   |2014-06-09 00:00:00|6551       |PENDING        |
|51062   |2014-06-09 00:00:00|5548       |PROCESSING     |
|51063   |2014-06-09 00:00:00|7020       |CLOSED         |
|51064   |2014-06-09 00:00:00|909        |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00|7975       |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00|6494       |PENDING        |
|51067   |2014-06-09 00:00:00|1380       |CLOSED         |
|51068   |2014-06-09 00:00:00|5766       |COMPLETE       |
+--------+-------------------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date_new: timestamp (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)

transformed_df.createOrReplaceGlobalTempView("orders")
filtered_df1 = spark.sql("""select * from orders
                           where order_status = 'CLOSED'""")
filtered_df1.show(5,truncate = False)

o/p:
=========
+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|51059   |2014-06-09 00:00:00|4645       |CLOSED      |
|51063   |2014-06-09 00:00:00|7020       |CLOSED      |
|51067   |2014-06-09 00:00:00|1380       |CLOSED      |
|51071   |2014-06-09 00:00:00|6502       |CLOSED      |
|51079   |2014-06-09 00:00:00|2031       |CLOSED      |
+--------+-------------------+-----------+------------+
only showing top 5 rows

If I am trying to acces this spark table "orders" from other sparksession(application) you will be able to access it:
==================================================================================================================================
filtered_df1 = spark.sql("""select * from orders
                           """)
filtered_df1.show(5, truncate = False)

o/p:
=========
output will be displayed.
   
iii. .createTempView():
==============================
i. If we use .createTempView() than in this case if table already exist , it will give error:
ii. syntax:
==================
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
orders_df_avro = spark.read.format("avro")\
                     .option("path","/public/trendytech/datasets/orders_avro/*")\
                     .load()
orders_df_avro.show(truncate = False)
orders_df_avro.printSchema()
o/p:
========
+--------+---------------------+-------+---------------+
|order_id|order_date           |cust_id|order_status   |
+--------+---------------------+-------+---------------+
|51049   |2014-06-09 00:00:00.0|4983   |PROCESSING     |
|51050   |2014-06-09 00:00:00.0|1840   |ON_HOLD        |
|51051   |2014-06-09 00:00:00.0|8207   |COMPLETE       |
|51052   |2014-06-09 00:00:00.0|6254   |COMPLETE       |
|51053   |2014-06-09 00:00:00.0|348    |PENDING        |
|51054   |2014-06-09 00:00:00.0|1468   |COMPLETE       |
|51055   |2014-06-09 00:00:00.0|3843   |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00.0|7178   |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00.0|749    |COMPLETE       |
|51058   |2014-06-09 00:00:00.0|5146   |PENDING        |
|51059   |2014-06-09 00:00:00.0|4645   |CLOSED         |
|51060   |2014-06-09 00:00:00.0|247    |COMPLETE       |
|51061   |2014-06-09 00:00:00.0|6551   |PENDING        |
|51062   |2014-06-09 00:00:00.0|5548   |PROCESSING     |
|51063   |2014-06-09 00:00:00.0|7020   |CLOSED         |
|51064   |2014-06-09 00:00:00.0|909    |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00.0|7975   |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00.0|6494   |PENDING        |
|51067   |2014-06-09 00:00:00.0|1380   |CLOSED         |
|51068   |2014-06-09 00:00:00.0|5766   |COMPLETE       |
+--------+---------------------+-------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 transformed_df = orders_df_avro.withColumn("order_date_new",to_timestamp(col("order_date")))\
                               .withColumnRenamed("cust_id","customer_id")\
                               .select(col("order_id"),col("order_date_new"),col("customer_id"),col("order_status"))
                               
transformed_df.show(truncate = False)
transformed_df.printSchema()
o/p:
==========
+--------+-------------------+-----------+---------------+
|order_id|order_date_new     |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|51049   |2014-06-09 00:00:00|4983       |PROCESSING     |
|51050   |2014-06-09 00:00:00|1840       |ON_HOLD        |
|51051   |2014-06-09 00:00:00|8207       |COMPLETE       |
|51052   |2014-06-09 00:00:00|6254       |COMPLETE       |
|51053   |2014-06-09 00:00:00|348        |PENDING        |
|51054   |2014-06-09 00:00:00|1468       |COMPLETE       |
|51055   |2014-06-09 00:00:00|3843       |PENDING_PAYMENT|
|51056   |2014-06-09 00:00:00|7178       |PENDING_PAYMENT|
|51057   |2014-06-09 00:00:00|749        |COMPLETE       |
|51058   |2014-06-09 00:00:00|5146       |PENDING        |
|51059   |2014-06-09 00:00:00|4645       |CLOSED         |
|51060   |2014-06-09 00:00:00|247        |COMPLETE       |
|51061   |2014-06-09 00:00:00|6551       |PENDING        |
|51062   |2014-06-09 00:00:00|5548       |PROCESSING     |
|51063   |2014-06-09 00:00:00|7020       |CLOSED         |
|51064   |2014-06-09 00:00:00|909        |PENDING_PAYMENT|
|51065   |2014-06-09 00:00:00|7975       |PENDING_PAYMENT|
|51066   |2014-06-09 00:00:00|6494       |PENDING        |
|51067   |2014-06-09 00:00:00|1380       |CLOSED         |
|51068   |2014-06-09 00:00:00|5766       |COMPLETE       |
+--------+-------------------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date_new: timestamp (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 
transformed_df.createTempView("orders")

o/p:
=============
AnalysisException: Temporary view 'orders' already exists

18. Important Concept:
===============================
i. Convert a df to sparktable/view:
============================================
a. transformed_df.createTempView("orders")
b. transformed_df.createOrReplaceTempView("orders")
c. transformed_df.createOrReplaceGlobalTempView("orders")

ii. Convert a sparktable/view to df:
===========================================
ordersdf = spark.read.table("orders")
ordersdf.show(5,truncate = False)
ordersdf.printSchema()

o/p:
============
+--------+-------------------+-----------+------------+
|order_id|order_date_new     |customer_id|order_status|
+--------+-------------------+-----------+------------+
|51049   |2014-06-09 00:00:00|4983       |PROCESSING  |
|51050   |2014-06-09 00:00:00|1840       |ON_HOLD     |
|51051   |2014-06-09 00:00:00|8207       |COMPLETE    |
|51052   |2014-06-09 00:00:00|6254       |COMPLETE    |
|51053   |2014-06-09 00:00:00|348        |PENDING     |
+--------+-------------------+-----------+------------+
only showing top 5 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date_new: timestamp (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)

19. Impt concept to remember about spark table:
=========================================================
i. First create a database if not exist:
ii. show databases.
iii. filter the database that you want to see using namespace.
iv. use <database_name>.
v. show tables.
vi.  create a table.
vii. insert record into table.
viii. select * from <table_name>.
ix. see the metdata of the table.
x. see the data of the table.

solution:
====================
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

i. First create a database if not exist:
=================================================
spark.sql("create database if not exists itv022641_retail")

ii. show databases:
=============================
spark.sql("show databases").show(truncate = False)

o/p:
==========
+-------------------------+
|namespace                |
+-------------------------+
|0000000000000_msdian     |
|0000000000000_naveen_db  |
|0000000009874_retail     |
|0000000_pavan            |
|0000001_sample_itv020476 |
|00000_2_db               |
|00000_aitv019314_anjitha |
|00000assg5_db            |
|00000assign5_db          |
|00000assign7_itv006450   |
|0000_0spark_tabbles_cache|
|0000_1itv025021_learning |
|0000_cache_spark111      |
|0000a5a5a5a5             |
|0001_av_ivy_tesco        |
|001_itv_grocery          |
|001_retail               |
|003402_hive1             |
|005198_ivy_tesco         |
|005212_ivy_tesco         |
+-------------------------+

iii. filter the database that you want to see using namespace:
=====================================================================
a. spark.sql("show databases").filter("namespace = 'itv022641_retail'").show(truncate = False)
b. spark.sql("show databases").filter("namespace like 'itv022641%'").show(truncate = False)

o/p:
==========
+----------------+
|namespace       |
+----------------+
|itv022641_retail|
+----------------+

iv. use <database_name>:
==================================
spark.sql("use itv022641_retail")

v. show tables:
=============================
spark.sql("show tables").show(truncate = False)
o/p:
========
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
+--------+---------+-----------+

vi.  create a table:
==============================
spark.sql("""
CREATE TABLE itv022641_retail.orders (
    order_id INT,
    order_date STRING,
    customer_id INT,
    order_status STRING
) using csv
""")
spark.sql("show tables").show(truncate = False)
o/p:
+----------------+---------+-----------+
|database        |tableName|isTemporary|
+----------------+---------+-----------+
|itv022641_retail|orders   |false      |
+----------------+---------+-----------+

vii. insert record into table:
======================================
spark.sql("""
INSERT INTO itv022641_retail.orders (order_id, order_date, customer_id, order_status)
VALUES 
(1, '2013-07-25 00:00:00', 11566, 'Processing'),
(2, '2013-07-25 00:00:00', 256, 'PENDING_PAYMENT'),
(3, '2013-07-25 00:00:00', 12111, 'COMPLETE'),
(4, '2013-07-25 00:00:00', 8827, 'CLOSED'),
(5, '2013-07-25 00:00:00', 11318, 'COMPLETE'),
(6, '2013-07-25 00:00:00', 7130, 'COMPLETE')
""")

viii. select the data of the table:
============================================
spark.sql("select * from itv022641_retail.orders").show(truncate = False)
o/p:
============
+--------+-------------------+-----------+---------------+
|order_id|order_date         |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|1       |2013-07-25 00:00:00|11566      |Processing     |
|2       |2013-07-25 00:00:00|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00|8827       |CLOSED         |
|5       |2013-07-25 00:00:00|11318      |COMPLETE       |
|6       |2013-07-25 00:00:00|7130       |COMPLETE       |
+--------+-------------------+-----------+---------------+


ix. see the metdata of the table:
=========================================
a. spark.sql("""describe table itv022641_retail.orders""").show(truncate = False)
o/p:
=========
+------------+---------+-------+
|col_name    |data_type|comment|
+------------+---------+-------+
|order_id    |int      |null   |
|order_date  |string   |null   |
|customer_id |int      |null   |
|order_status|string   |null   |
+------------+---------+-------+

b. spark.sql("""describe extended itv022641_retail.orders""").show(truncate = False)

o/p:
============

+----------------------------+---------------------------------------------------------------------------------+-------+
|col_name                    |data_type                                                                        |comment|
+----------------------------+---------------------------------------------------------------------------------+-------+
|order_id                    |int                                                                              |null   |
|order_date                  |string                                                                           |null   |
|customer_id                 |int                                                                              |null   |
|order_status                |string                                                                           |null   |
|                            |                                                                                 |       |
|# Detailed Table Information|                                                                                 |       |
|Database                    |itv022641_retail                                                                 |       |
|Table                       |orders                                                                           |       |
|Owner                       |itv022641                                                                        |       |
|Created Time                |Wed Mar 25 06:41:35 EDT 2026                                                     |       |
|Last Access                 |UNKNOWN                                                                          |       |
|Created By                  |Spark 3.1.2                                                                      |       |
|Type                        |MANAGED                                                                          |       |
|Provider                    |csv                                                                              |       |
|Location                    |hdfs://m01.itversity.com:9000/user/itv022641/warehouse/itv022641_retail.db/orders|       |
|Serde Library               |org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe                               |       |
|InputFormat                 |org.apache.hadoop.mapred.SequenceFileInputFormat                                 |       |
|OutputFormat                |org.apache.hadoop.hive.ql.io.HiveSequenceFileOutputFormat                        |       |
+----------------------------+---------------------------------------------------------------------------------+-------+


x. see the data of the table is present at :
=====================================================
i. [itv022641@g01 ~]$ hadoop fs -ls /user/itv022641/warehouse/itv022641_retail.db/orders
Found 3 items
-rwxr-xr-x   3 itv022641 supergroup        118 2026-03-24 02:21 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000
-rwxr-xr-x   3 itv022641 supergroup          0 2026-03-24 02:14 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-ef704571-5c9f-424e-8584-86bd4112e749-c000
-rwxr-xr-x   3 itv022641 supergroup        107 2026-03-24 02:21 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00001-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000
ii. [itv022641@g01 ~]$ hadoop fs -head /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000
12013-07-25 00:00:0011566Processing
22013-07-25 00:00:00256PENDING_PAYMENT
32013-07-25 00:00:0012111COMPLETE
iii. [itv022641@g01 ~]$ hadoop fs -head /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-ef704571-5c9f-424e-8584-86bd4112e749-c000
iv. [itv022641@g01 ~]$ hadoop fs -head /user/itv022641/warehouse/itv022641_retail.db/orders/part-00001-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000
42013-07-25 00:00:008827CLOSED
52013-07-25 00:00:0011318COMPLETE
62013-07-25 00:00:007130COMPLETE

v. [itv022641@g01 ~]$ hadoop fs -ls -h /user/itv022641/warehouse/itv022641_retail.db/orders
Found 3 items
-rwxr-xr-x   3 itv022641 supergroup        118 2026-03-24 02:21 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000
-rwxr-xr-x   3 itv022641 supergroup          0 2026-03-24 02:14 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00000-ef704571-5c9f-424e-8584-86bd4112e749-c000
-rwxr-xr-x   3 itv022641 supergroup        107 2026-03-24 02:21 /user/itv022641/warehouse/itv022641_retail.db/orders/part-00001-8e2fed60-9491-4d2c-85d2-63c87fb81275-c000

xi. After dropping the managed table "itv022641_retail.orders":
======================================================================
a. Both data + metadata will be lost.
b. syntax:
======================
i. spark.sql("""drop table itv022641_retail.orders""")
ii. metadata not found:
=============================
spark.sql("""describe extended itv022641_retail.orders""").show(truncate = False)
o/p:
=========
AnalysisException: Table or view not found for 'DESCRIBE TABLE': itv022641_retail.orders; line 1 pos 0;
'DescribeRelation true, [col_name#220, data_type#221, comment#222]
+- 'UnresolvedTableOrView [itv022641_retail, orders], DESCRIBE TABLE, true

iii. data also not found:
=====================================
a. spark.sql("select * from itv022641_retail.orders").show(truncate=False)
o/p:
==========
AnalysisException: Table or view not found: itv022641_retail.orders; line 1 pos 14;
'Project [*]
+- 'UnresolvedRelation [itv022641_retail, orders], [], false

b. [itv022641@g01 ~]$ hadoop fs -ls /user/itv022641/warehouse/itv022641_retail.db/orders
ls: `/user/itv022641/warehouse/itv022641_retail.db/orders': No such file or directory


20. Difference b/t Managed Table vs External Table in spark:
=======================================================================
i. Managed Table:
=========================
a. In case of Managed Table you are the complete owner of data + Meatadata because you create the table and also insert the data into the table using insert command.
b. syntax for Managed Table creation + Insert data into the managed table:
===============================================================================
i. spark.sql("""
CREATE TABLE itv022641_retail.orders (
    order_id INT,
    order_date STRING,
    customer_id INT,
    order_status STRING
) using csv
""")
spark.sql("show tables").show(truncate = False)
o/p:
+----------------+---------+-----------+
|database        |tableName|isTemporary|
+----------------+---------+-----------+
|itv022641_retail|orders   |false      |
+----------------+---------+-----------+ 

ii.  insert record into table:
======================================
spark.sql("""
INSERT INTO itv022641_retail.orders (order_id, order_date, customer_id, order_status)
VALUES 
(1, '2013-07-25 00:00:00', 11566, 'Processing'),
(2, '2013-07-25 00:00:00', 256, 'PENDING_PAYMENT'),
(3, '2013-07-25 00:00:00', 12111, 'COMPLETE'),
(4, '2013-07-25 00:00:00', 8827, 'CLOSED'),
(5, '2013-07-25 00:00:00', 11318, 'COMPLETE'),
(6, '2013-07-25 00:00:00', 7130, 'COMPLETE')
""")

iii. select the data of the table:
============================================
spark.sql("select * from itv022641_retail.orders").show(truncate = False)
o/p:
============
+--------+-------------------+-----------+---------------+
|order_id|order_date         |customer_id|order_status   |
+--------+-------------------+-----------+---------------+
|1       |2013-07-25 00:00:00|11566      |Processing     |
|2       |2013-07-25 00:00:00|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00|8827       |CLOSED         |
|5       |2013-07-25 00:00:00|11318      |COMPLETE       |
|6       |2013-07-25 00:00:00|7130       |COMPLETE       |
+--------+-------------------+-----------+---------------+

c. From above we can say that both insert + select command work well with Managed Table.
d. So In case of Managed Table if we drop the table both data + Metadata is lost.
syntax:
=================
After dropping the managed table "itv022641_retail.orders":
======================================================================
a. Both data + metadata will be lost.
b. syntax:
======================
i. spark.sql("""drop table itv022641_retail.orders""")
ii. metadata not found:
=============================
spark.sql("""describe extended itv022641_retail.orders""").show(truncate = False)
o/p:
=========
AnalysisException: Table or view not found for 'DESCRIBE TABLE': itv022641_retail.orders; line 1 pos 0;
'DescribeRelation true, [col_name#220, data_type#221, comment#222]
+- 'UnresolvedTableOrView [itv022641_retail, orders], DESCRIBE TABLE, true

iii. data also not found:
=====================================
a. spark.sql("select * from itv022641_retail.orders").show(truncate=False)
o/p:
==========
AnalysisException: Table or view not found: itv022641_retail.orders; line 1 pos 14;
'Project [*]
+- 'UnresolvedRelation [itv022641_retail, orders], [], false

b. [itv022641@g01 ~]$ hadoop fs -ls /user/itv022641/warehouse/itv022641_retail.db/orders
ls: `/user/itv022641/warehouse/itv022641_retail.db/orders': No such file or directory

e. It is mostly recommended for local practice purpose because you have full control over data + metadata.
f. Truncate command is supported in Managed Table.
syntax:
=================
spark.sql("Truncate table itv022641_retail.orders")
spark.sql("select * from itv022641_retail.orders").show(truncate = False)
o/p:
===============
+--------+----------+-----------+------------+
|order_id|order_date|customer_id|order_status|
+--------+----------+-----------+------------+
+--------+----------+-----------+------------+

g. Update and Delete is not supported in open version of spark in case of Managed Table.
   But in databricks Update and Delete are supported in case of Managed Table (because of Delta format/Delta Table which is Acid complaint).

Working of Delete + Update on open spark version:
==========================================================
spark.sql("DELETE FROM itv022641_retail.orders WHERE order_id=1")
o/p:
============
AnalysisException: DELETE is only supported with v2 tables
spark.sql("UPDATE itv022641_retail.orders SET order_status='COMPLETE' WHERE order_id = 2")
o/p:
=========
Getting error.

Note: In case of Managed Table you are sole owner of data + metadata.
      So if we drop the managed table both data + metadata is lost.
      Mainly recommended for local practice purpose.
      Insert is supported in case of Managed table.
      Truncate is also supported in case of Managed Table.
      Update + Delete are not supported as part of open spark version.
      But in databricks both Update + Delete is supported in case of managed table.

ii. External Table:
=============================
a. In case of External Table you are the complete owner of metadata but data is present at some external location so you dont have control over data.
b. Syntax for External Table creation:
==================================================
spark.sql("""
CREATE TABLE itv022641_retail_ext.orders_ext (
    order_id INT,
    order_date STRING,
    customer_id INT,
    order_status STRING
) using csv location '/public/trendytech/retail_db/orders'
""")
spark.sql("show tables").show(truncate = False)
o/p:
============
+--------------------+----------+-----------+
|database            |tableName |isTemporary|
+--------------------+----------+-----------+
|itv022641_retail_ext|orders_ext|false      |
+--------------------+----------+-----------+
To see data of external table:
=====================================
spark.sql("select * from itv022641_retail_ext.orders_ext").show(5, truncate = False)
o/p:
===========
+--------+---------------------+-----------+---------------+
|order_id|order_date           |customer_id|order_status   |
+--------+---------------------+-----------+---------------+
|1       |2013-07-25 00:00:00.0|11599      |CLOSED         |
|2       |2013-07-25 00:00:00.0|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00.0|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00.0|8827       |CLOSED         |
|5       |2013-07-25 00:00:00.0|11318      |COMPLETE       |
+--------+---------------------+-----------+---------------+
To see Metadata of External Table:
==========================================
spark.sql("describe extended itv022641_retail_ext.orders_ext").show(truncate = False)
o/p:
=============
+----------------------------+----------------------------------------------------------------+-------+
|col_name                    |data_type                                                       |comment|
+----------------------------+----------------------------------------------------------------+-------+
|order_id                    |int                                                             |null   |
|order_date                  |string                                                          |null   |
|customer_id                 |int                                                             |null   |
|order_status                |string                                                          |null   |
|                            |                                                                |       |
|# Detailed Table Information|                                                                |       |
|Database                    |itv022641_retail_ext                                            |       |
|Table                       |orders_ext                                                      |       |
|Owner                       |itv022641                                                       |       |
|Created Time                |Wed Mar 25 06:59:50 EDT 2026                                    |       |
|Last Access                 |UNKNOWN                                                         |       |
|Created By                  |Spark 3.1.2                                                     |       |
|Type                        |EXTERNAL                                                        |       |
|Provider                    |csv                                                             |       |
|Location                    |hdfs://m01.itversity.com:9000/public/trendytech/retail_db/orders|       |
|Serde Library               |org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe              |       |
|InputFormat                 |org.apache.hadoop.mapred.SequenceFileInputFormat                |       |
|OutputFormat                |org.apache.hadoop.hive.ql.io.HiveSequenceFileOutputFormat       |       |
+----------------------------+----------------------------------------------------------------+-------+
c. select is supported in case of external table.
synatx:
==============
spark.sql("select * from itv022641_retail_ext.orders_ext").show(5, truncate = False)
o/p:
===========
+--------+---------------------+-----------+---------------+
|order_id|order_date           |customer_id|order_status   |
+--------+---------------------+-----------+---------------+
|1       |2013-07-25 00:00:00.0|11599      |CLOSED         |
|2       |2013-07-25 00:00:00.0|256        |PENDING_PAYMENT|
|3       |2013-07-25 00:00:00.0|12111      |COMPLETE       |
|4       |2013-07-25 00:00:00.0|8827       |CLOSED         |
|5       |2013-07-25 00:00:00.0|11318      |COMPLETE       |
+--------+---------------------+-----------+---------------+

d. insert is supported in case of External table but not recommended to use because it will create a new file in that folder 
   and many people will be using that folder by saying (foldername/*).
syntax:
===================
spark.sql("""
INSERT INTO itv022641_retail_ext.orders_ext
VALUES (1111, '2023-02-12', 2222, 'CLOSED')
""")

e. Truncate is not supported in case of External Table:
===============================================================
syntax:
===============
spark.sql("truncate table itv022641_retail_ext.orders_ext").show(truncate = False)
o/p:
=========
AnalysisException: Operation not allowed: TRUNCATE TABLE on external tables: `itv022641_retail_ext`.`orders_ext`

f. If we drop the table in case of external table you metadata is lost but your data is not deleted.
syntax:
================
spark.sql("drop table itv022641_retail_ext.orders_ext")
Meatadata is lost:
=======================
spark.sql("describe extended itv022641_retail_ext.orders_ext").show(truncate = False)
o/p:
=========
AnalysisException: Table or view not found for 'DESCRIBE TABLE': itv022641_retail_ext.orders_ext; line 1 pos 0;
'DescribeRelation true, [col_name#346, data_type#347, comment#348]
+- 'UnresolvedTableOrView [itv022641_retail_ext, orders_ext], DESCRIBE TABLE, true

Data is not lost:
==========================
[itv022641@g01 ~]$ hadoop fs -ls /public/trendytech/retail_db/orders
Found 2 items
-rw-r--r--   3 itv005857 supergroup          0 2023-05-04 16:11 /public/trendytech/retail_db/orders/_SUCCESS
-rw-r--r--   3 itv005857 supergroup    2999944 2023-04-26 16:47 /public/trendytech/retail_db/orders/part-00000
[itv022641@g01 ~]$ hadoop fs -ls  /public/trendytech/retail_db/orders/part-00000
-rw-r--r--   3 itv005857 supergroup    2999944 2023-04-26 16:47 /public/trendytech/retail_db/orders/part-00000
[itv022641@g01 ~]$ hadoop fs -head  /public/trendytech/retail_db/orders/part-00000
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
8,2013-07-25 00:00:00.0,2911,PROCESSING
9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT
11,2013-07-25 00:00:00.0,918,PAYMENT_REVIEW
12,2013-07-25 00:00:00.0,1837,CLOSED
13,2013-07-25 00:00:00.0,9149,PENDING_PAYMENT
14,2013-07-25 00:00:00.0,9842,PROCESSING
15,2013-07-25 00:00:00.0,2568,COMPLETE
16,2013-07-25 00:00:00.0,7276,PENDING_PAYMENT
17,2013-07-25 00:00:00.0,2667,COMPLETE
18,2013-07-25 00:00:00.0,1205,CLOSED
19,2013-07-25 00:00:00.0,9488,PENDING_PAYMENT
20,2013-07-25 00:00:00.0,9198,PROCESSING
21,2013-07-25 00:00:00.0,2711,PENDING
22,2013-07-25 00:00:00.0,333,COMPLETE
23,2013-07-25 00:00:00.0,4367,PENDING_PAYMENT
24,2013-07-25 00:00:00.0,11441,CLOSED
25,2013-07-25 00:00:00.0,9503,CLOSED

g. Update and Delete is not supported in open version of spark in case of Managed Table.
   But in databricks Update and Delete are supported in case of Managed Table (because of Delta format/Delta Table which is Acid complaint).

Working of Delete + Update on open spark version:
==========================================================
spark.sql("DELETE FROM itv022641_retail_ext.orders_ext WHERE order_id=1")
o/p:
============
AnalysisException: DELETE is only supported with v2 tables

spark.sql("UPDATE itv022641_retail_ext.orders_ext SET order_status='COMPLETE' WHERE order_id = 2")
o/p:
=========
Getting error.

h. It is recommended when your data is kept at some central repository and multiple people are accessing the same data.

Note: In case of External Table you are sole owner of metadata but not data , it is kept at some external location.
      So if we drop the external table metadata is lost but not data.
      Mainly recommended when your data is kept at some central repository and multiple people are accessing the same data.
      Insert is supported in case of External table but not recommended to use because it will create a new file in that folder 
      and many people will be using that folder by saying (foldername/*) 
      Truncate is not supported in case of External Table.
      Update + Delete are not supported as part of open source spark version.
      But in databricks both Update + Delete is supported in case of External table.

21. Diff b/t use of count() with groupBy() vs use of count() with distinct() or df.count():
================================================================================================
i. count() with groupBy():
===================================
a. When we use count() with groupBy() function than in this case count() act as transformation
   because when we apply count() after groupBy() function we get huge result so we have to distribute this
   result on multiple machine to get more parallelism and also we can apply more transformation after that.
b. In this case count() is lazy evaluated , so to see the result we have to call an action.
c. syntax:
===================
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
=============
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

ii. count() with distinct() or df.count():
===============================================
a. In this case count() act as an action , so we get single value as output , so in this case no
   further transformation is required and also this value can be stored on a single machine as it is a single value,
   and also we will not get parallelism.
b. It is an eager operation.
c. syntax:
===============
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

23. Impt pt to remember:
===============================
Action:
==============
show()
head()
tail()
take()
collect()
count() with distinct() or df.count().

Utility function in pyspark (which is niether a action() nor a transformation():
=================================================================================
printSchema()
cache()
createOrReplaceTempView()


22. Performance tunning in spark is broadly categorised into 2 broad category:
======================================================================================
i. Application Code level optimization: Here we will mainly talk about how we can write our code in a efficient way For ex:
                                        We can use caache(),persist(), we can use reduceByKey() over groupByKey(), we can use
                                        optimized file format like parquet, We can optimize our join using broadcast join.

ii. Cluster Level optimization: Here we will talk about about the resources we can provide to our cluster so that it run efficiently
                                For ex: executor,executor memory,executor cores. 


23. Cluster Level Optimization:
==========================================
i. When we are talking about cluster level optimization our intention is to give more resources to our spark job so that it does not fail.
ii. Resources means CPU cores (compute) + Memory (RAM).
iii. Consider a scenario where we have 10 WN with each WN holding 16 cpu cores + 64 GB RAM, and we can create a multiple executor/container/JVM inside each WN.
iv. So there are multiple approaches to create Executors/Containers/JVM inside each WN:
    i. Thin/Tiny Executor: The Executor that contain minimum amount of resources(cpu core+RAM) is referred as Thin/Tiny Executor.
                           Using this approach our intention is to create maximum no of executors/containers inside each WN.
                           For ex: In above case we have 10 WN with each holding 16 cpu cores + 64 GB RAM, so using this thin 
                                   Executor approach inside each WN there will be 16 executors/containers with each holding
                                  1 cpu cores + 4GB RAM
                                  So Total Executors = 10*16 = 160 Executors with each executor holding 1 cpu cores + 4 GB RAM
                                  So Total CPU cores = 160*1 = 160 cpu cores
                                  So Total RAM       = 4*160 = 640 GB RAM
       Disadvantage of Thin Executor Approach is:
       =============================================
       i. We will lose the benefit of multithreading because each executor is holding only 1 Cpu cores and for multithreading to take place
          each executor should hold more than one cpu cores.
      ii. And also too many copies of shared variable(Broadcast variable/Accumulator variable) are required because each executor hold one complete copy of shared varaible,
          so in this case we have to maintain 160 copies of shared variable because we have 160 executors.

Note-: This approach is not recommended because we are losing the benefit of multithreading.

   ii. Fat Executor Approach: The Executor that hold maximum no of resources (CPU cores/RAM)  is referred as Fat Executor.
                              Using this approach our intention is to create maximum number of resources inside each WN.
                              For ex: In above case we have 10 WN with each holding 16 cpu cores + 64 GB RAM, so using this 
                                      Fat Executor approach inside each WN there will be 1 executor/container/jvm inside each
                                      WN with each executor holding 16 cpu cores + 64 GB RAM.
                                      So Total Executors = 1*10 = 10 Executors.
                                      So Total CPU cores = 10*16 = 160 CPU cores.
                                      So Total RAM       = 10*64 = 640 GB RAM.
      Disadvantage of Fat Executor Approach is:
      ==============================================
      i. Here we will get lot of multithreading so due to this our hdfs throughput suffer , it will slow down to pull the data from
         hdfs so this will degrade the performance.
      ii. if the executor holds very huge amount of memory then the garbage collection takes a lot of time.
          GC means removing unused objects from memory, so to remove unused object from memory GC takes lot of time.

Note-: This approach is not recommended because our hdfs throughput suffers because due to lot of multithreading.

So above two approach is not recommended due to following reasons:
    i. In case of Thin Executor we will lose the benefit of multithreading.
    ii. In case of Fat Executor our hdfs throughput slows down.
So From here we conclude that we need a balanced approach where we should have (1<cpu_cores<=5) , so each  executor should hold 5 cpu cores.

   iii. Balanced Executor Approach: In this approach each executor should hold 5 cpu cores .
                                    For ex: Consider we have 10 WN with each holding 16 cpu cores + 64 GB RAM
                                                     So out of this 16 cpu cores 1 cpu cores will go as part of background process , so we are left with 15 cpu cores
                                                     So out of this 64GB RAM 1 GB RAM will go as part of operating syatem, so we are left with 63 GB RAM.
                                                     So now we can create 3 executors inside each WN with each holding 5 cpu cores + 21 GB RAM.
                                                     So Total no of executors = 3*10 = 30 executors (each exector holds 21 gb ram + 5 cpu cores).
                                                     So this 21 GB RAM will divided into 2 parts :
                                                      i. On heap memory: The memory that is present inside executor/container/JVM is referreed as On heap memory.
                                                                         It does not give optimization because GC is required to remove unused object from memory.
                                                                         Here we dont have to manage memory by ourself system will take care of it.
                                                                         on heap memory = 21-1.5 ~ 19 GB
                                                      ii. Off heap memory: The memory that is present outside the executor/container/JVM is referred as off heap memory.
                                                                           It will give optimization because GC is not required.
                                                                           Here we have to manage the memory by ourself (programatically).
                                                                           off heap memory = max(384 mb / 7% of executor memory)
                                                                           so in above case off heap memory = 7% of 21 GB ~ 1.5 GB.

  Note-: From above we can conclude that each executor will hold 5 cpu cores + 19 GB RAM so this is balanced approach.
         Out of this 30 executors , 1 executor will be given for YARN Application Manager = 30 -1 = 29 executors.
         Total Cpu cores = 29*5 = 145 cpu cores.
         Total RAM       = 29*19 = 551 GB RAM.
         Advantage of this approach is:
         =======================================
         i. We will get benefit of multithreading because each executor holds more than 1 cpu cores.
         ii. Also too many copies of shared variable is not required.
         iii. Our hdfs throughtput will not suffer anymore.
         iv. GC will not be required to remove unused objects from memory.



24. How to handle date format datatype in spark:
====================================================
i. Use of inferSchema():
==========================
a. It gives incorrect datatype.
b. If the file size is huge (1TB/500 GB) it takes lot of time, because it scan entire file and try to infer the schema.
c. For example:
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
df = spark.read.format("csv")\
          .option("header",True)\
          .option("inferSchema",True)\
          .option("sep",",")\
          .option("path","/public/trendytech/orders_wh/*")\
          .load()
df.show(truncate=False)
df.printSchema()
o/p:
======+--------+---------------------+-----------+---------------+
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
only showing top 20 rows

root
 |-- order_id: integer (nullable = true)
 |-- order_date: string (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)

df.createOrReplaceTempView("date_conversion")

df_transformed = df.withColumn("order_date",to_timestamp(col("order_date"),'yyyy-MM-dd HH:mm:ss.S'))
df_transformed.show(truncate=False)
df_transformed.printSchema()


df_transformed = spark.sql("select order_id,to_timestamp(order_date,'yyyy-MM-dd HH:mm:ss.S') as order_date,customer_id,order_status from date_conversion")
df_transformed.show(truncate=False)
df_transformed.printSchema()
o/p:
=======
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

ii. Use of samplingRatio:
===============================
a. If we are using inferSchema than it scan entire file to infer the datatypes , so the major
   drawback is that it takes lot of time and degrade the performance of spark job.

b. so samplingRatio means instead of scanning entire file while using inferSchema , it scan portion of
   file and try to infer the schema/datatype.
   0.1 -> means 10% of the data scanned.
   0.2 -> means 20% of the data scanned.
   0.3% -> means 30% of the data scanned.
   .option("samplingRatio",0.1/0.2/0.3)

c. Code Example:
====================
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
          .option("samplingRatio",0.1)\
          .option("path","/public/yelp-dataset/yelp_user.csv")\
          .load()

df.printSchema()
o/p:
=====
root
 |-- user_id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- review_count: integer (nullable = true)
 |-- yelping_since: string (nullable = true)
 |-- friends: string (nullable = true)
 |-- useful: integer (nullable = true)
 |-- funny: integer (nullable = true)
 |-- cool: integer (nullable = true)
 |-- fans: integer (nullable = true)
 |-- elite: string (nullable = true)
 |-- average_stars: double (nullable = true)
 |-- compliment_hot: integer (nullable = true)
 |-- compliment_more: integer (nullable = true)
 |-- compliment_profile: integer (nullable = true)
 |-- compliment_cute: integer (nullable = true)
 |-- compliment_list: integer (nullable = true)
 |-- compliment_note: integer (nullable = true)
 |-- compliment_plain: integer (nullable = true)
 |-- compliment_cool: integer (nullable = true)
 |-- compliment_funny: integer (nullable = true)
 |-- compliment_writer: integer (nullable = true)
 |-- compliment_photos: integer (nullable = true)

Note-: Use of samplingRatio() makes spark job faster while infering datatype when scanning file while using inferSchema().

iii. If there is a datatype issue we will get column values as null:
=====================================================================
a. Code:
=========
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
orders_schema_prog = StructType([\
                                StructField("order_id",LongType(),True),\
                                StructField("order_date",DateType(),True),\
                                StructField("cust_id",LongType(),True),\
                                StructField("order_status",LongType(),True)])
orders_df_1 = spark.read.format("csv")\
                   .schema(orders_schema_prog)\
                   .option("sep",",")\
                   .option("path","/public/trendytech/datasets/orders_sample1.csv")\
                   .load()
orders_df_1.show(truncate=False)
orders_df_1.printSchema()
+--------+----------+-------+------------+
|order_id|order_date|cust_id|order_status|
+--------+----------+-------+------------+
|1       |2013-07-25|11599  |null        |
|2       |2013-07-25|256    |null        |
|3       |2013-07-25|12111  |null        |
|4       |2013-07-25|8827   |null        |
|5       |2013-07-25|11318  |null        |
|6       |2013-07-25|7130   |null        |
|7       |2013-07-25|4530   |null        |
|8       |2013-07-25|2911   |null        |
|9       |2013-07-25|5657   |null        |
|10      |2013-07-25|5648   |null        |
+--------+----------+-------+------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: date (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: long (nullable = true)

Note-: From Above we conclude that if there is a datatype issue we will get the column values as null

iv. How to deal with datetype:
==================================
a. Datetype are very hard to deal with and if not handled properly it will give error or it will give null values in entire column.
b. default date format: "YYYY-mm-dd"
c. Code Example:
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

! hadoop fs -cat /public/trendytech/datasets/orders_sample2.csv | head
o/p:
=======
1,07-25-2013,11599,CLOSED
2,07-25-2013,256,PENDING_PAYMENT
3,07-25-2013,12111,COMPLETE
4,07-25-2013,8827,CLOSED
5,07-25-2013,11318,COMPLETE
6,07-25-2013,7130,COMPLETE
7,07-25-2013,4530,COMPLETE
8,07-25-2013,2911,PROCESSING
9,07-25-2013,5657,PENDING_PAYMENT
10,07-25-2013,5648,PENDING_PAYMENT

orders_schema_ddl = "order_id long,order_date date,cust_id long,order_status string"

orders_schema_prog = StructType([\
                                StructField("order_id",LongType(),True),\
                                StructField("order_date",DateType(),True),\
                                StructField("cust_id",LongType(),True),\
                                StructField("order_status",StringType(),True)])

orders_df = spark.read.format("csv")\
                 .schema(orders_schema_ddl)\
                 .option("sep",",")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
=======
 Fail to parse '07-25-2013' in the new parser

d. To deal with above datetype issue , we have 2 options:
==========================================================
i. First use one option while reading csv file is:
   .option("dateFormat","mm-dd-YYYY")
   This option work in spark version 2.0 not in spark version 3.0.

   spark 3.0:
=======================
orders_df = spark.read.format("csv")\
                 .schema(orders_schema_ddl)\
                 .option("sep",",")\
                 .option("dateFormat","mm-dd-YYYY")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
======
Spark 3.0: Fail to recognize 'mm-dd-YYYY' pattern in the DateTimeFormatter. 1)

spark 2.0:
================
orders_df = spark.read.format("csv")\
                 .schema(orders_schema_ddl)\
                 .option("sep",",")\
                 .option("dateFormat","mm-dd-YYYY")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |2013-01-25|11599  |CLOSED         |
|2       |2013-01-25|256    |PENDING_PAYMENT|
|3       |2013-01-25|12111  |COMPLETE       |
|4       |2013-01-25|8827   |CLOSED         |
|5       |2013-01-25|11318  |COMPLETE       |
|6       |2013-01-25|7130   |COMPLETE       |
|7       |2013-01-25|4530   |COMPLETE       |
|8       |2013-01-25|2911   |PROCESSING     |
|9       |2013-01-25|5657   |PENDING_PAYMENT|
|10      |2013-01-25|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: date (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

ii. 2nd load the date as string and later convert it to datetype():
==========================================================================
a. This option works in both spark version 2.0,3.0.
b. code in spark 3.0:
========================
orders_schema_ddl = "order_id long,order_date string,cust_id long,order_status string"

orders_schema_prog = StructType([\
                                StructField("order_id",LongType(),True),\
                                StructField("order_date",StringType(),True),\
                                StructField("cust_id",LongType(),True),\
                                StructField("order_status",StringType(),True)])

orders_df = spark.read.format("csv")\
                 .schema(orders_schema_prog)\
                 .option("sep",",")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
==========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |07-25-2013|11599  |CLOSED         |
|2       |07-25-2013|256    |PENDING_PAYMENT|
|3       |07-25-2013|12111  |COMPLETE       |
|4       |07-25-2013|8827   |CLOSED         |
|5       |07-25-2013|11318  |COMPLETE       |
|6       |07-25-2013|7130   |COMPLETE       |
|7       |07-25-2013|4530   |COMPLETE       |
|8       |07-25-2013|2911   |PROCESSING     |
|9       |07-25-2013|5657   |PENDING_PAYMENT|
|10      |07-25-2013|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

transformed_df = orders_df.withColumn("order_date",to_date(col("order_date"),'mm-dd-yyyy'))
transformed_df.show(truncate=False)
transformed_df.printSchema()
o/p:
========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |2013-01-25|11599  |CLOSED         |
|2       |2013-01-25|256    |PENDING_PAYMENT|
|3       |2013-01-25|12111  |COMPLETE       |
|4       |2013-01-25|8827   |CLOSED         |
|5       |2013-01-25|11318  |COMPLETE       |
|6       |2013-01-25|7130   |COMPLETE       |
|7       |2013-01-25|4530   |COMPLETE       |
|8       |2013-01-25|2911   |PROCESSING     |
|9       |2013-01-25|5657   |PENDING_PAYMENT|
|10      |2013-01-25|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: date (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

c. Code in spark 2.0:
========================
orders_schema_ddl = "order_id long,order_date string,cust_id long,order_status string"

orders_schema_prog = StructType([\
                                StructField("order_id",LongType(),True),\
                                StructField("order_date",StringType(),True),\
                                StructField("cust_id",LongType(),True),\
                                StructField("order_status",StringType(),True)])

orders_df = spark.read.format("csv")\
                 .schema(orders_schema_prog)\
                 .option("sep",",")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
=======
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |07-25-2013|11599  |CLOSED         |
|2       |07-25-2013|256    |PENDING_PAYMENT|
|3       |07-25-2013|12111  |COMPLETE       |
|4       |07-25-2013|8827   |CLOSED         |
|5       |07-25-2013|11318  |COMPLETE       |
|6       |07-25-2013|7130   |COMPLETE       |
|7       |07-25-2013|4530   |COMPLETE       |
|8       |07-25-2013|2911   |PROCESSING     |
|9       |07-25-2013|5657   |PENDING_PAYMENT|
|10      |07-25-2013|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

transformed_df = orders_df.withColumn("order_date",to_date(col("order_date"),'mm-dd-yyyy'))
transformed_df.show(truncate=False)
transformed_df.printSchema()
o/p:
==========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |2013-01-25|11599  |CLOSED         |
|2       |2013-01-25|256    |PENDING_PAYMENT|
|3       |2013-01-25|12111  |COMPLETE       |
|4       |2013-01-25|8827   |CLOSED         |
|5       |2013-01-25|11318  |COMPLETE       |
|6       |2013-01-25|7130   |COMPLETE       |
|7       |2013-01-25|4530   |COMPLETE       |
|8       |2013-01-25|2911   |PROCESSING     |
|9       |2013-01-25|5657   |PENDING_PAYMENT|
|10      |2013-01-25|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: date (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

Impt pt to remember:
===========================
1. 
i. Default date format: YYYY-mm-dd (2013-07-25).(valid for spark version 2.0, version 3.0).
ii. mm-dd-yyyy (07-25-2013). (valid in spark 2.0, not spark 3.0).

2. The dates format are hard to deal sometimes and different spark versions might have different behaviour.
   To solve above problem there are 2 approach:
   i. Fisrt at the time of reading the data, we give:
      .option("dateFormat","mm-dd-YYYY")-> supported in spark version 2.0 not 3.0
       code:
       ==========
       spark 2.0
================
orders_df = spark.read.format("csv")\
                 .schema(orders_schema_ddl)\
                 .option("sep",",")\
                 .option("dateFormat","mm-dd-YYYY")\
                 .option("path","/public/trendytech/datasets/orders_sample2.csv")\
                 .load()
     ii. 2nd approach is to intially load the date column as string and then later apply transformation and
         convert the datatype of this column from string to date.-> (supported in spark version 2.0/3.0)
         Code:
         ==========
         transformed_df = orders_df.withColumn("order_date",to_date(col("order_date"),'mm-dd-yyyy'))
         transformed_df.show(truncate=False)
         transformed_df.printSchema()

3. whenever there is a datatype mismatch you will get in the o/p as null.


Impt note to remember:
========================
| Format | Remember like this              |
| ------ | ------------------------------- |
| `yyyy` | **Year** → always use small `y` |
| `MM`   | **Month = M for Month** 📅      |
| `mm`   | **m = minute (small thing ⏱️)** |
| `dd`   | **day (normal)**                |
| `DD`   | **Day of year (big count)**     |
👉 “Always use yyyy MM dd and you’re safe”


25. Read Modes in spark:
================================
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
=====
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets
o/p:
========
Found 31 items
-rw-r--r--   3 itv005857 supergroup 1675133810 2023-09-16 10:11 /public/trendytech/datasets/accepted_2007_to_2018Q4.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-08-21 19:29 /public/trendytech/datasets/compression-techniques-demo
-rw-r--r--   3 itv005857 supergroup 2362455918 2023-06-06 09:28 /public/trendytech/datasets/cust_transf.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-18 17:40 /public/trendytech/datasets/customer_nested
-rw-r--r--   3 itv005857 supergroup       1538 2023-07-20 07:25 /public/trendytech/datasets/customers_sample.csv
-rw-r--r--   3 itv005857 supergroup       1319 2023-05-23 13:04 /public/trendytech/datasets/hospital.csv
-rw-r--r--   3 itv005857 supergroup       5697 2023-06-05 02:31 /public/trendytech/datasets/hotel_data.csv
-rw-r--r--   3 itv005857 supergroup    6306330 2023-08-20 10:09 /public/trendytech/datasets/json_sample_multiline
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 10:20 /public/trendytech/datasets/json_sample_singleline
drwxr-xr-x   - itv005857 supergroup          0 2023-08-09 00:02 /public/trendytech/datasets/lending-club-project-datasets
-rw-r--r--   3 itv005857 supergroup        925 2023-05-23 13:05 /public/trendytech/datasets/library_data.json
-rw-r--r--   3 itv005857 supergroup   25487177 2023-06-11 04:35 /public/trendytech/datasets/logdata1m.csv
-rw-r--r--   3 itv005857 supergroup        118 2023-07-17 15:38 /public/trendytech/datasets/mapping_data
-rw-r--r--   3 itv005857 supergroup   46079587 2023-06-09 13:05 /public/trendytech/datasets/order_data.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-06-02 02:47 /public/trendytech/datasets/orders
-rw-r--r--   3 itv005857 supergroup    7064041 2023-05-04 07:46 /public/trendytech/datasets/orders.json
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 16:22 /public/trendytech/datasets/orders_avro
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 18:00 /public/trendytech/datasets/orders_orc_ff
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 17:40 /public/trendytech/datasets/orders_parquet_ff
-rw-r--r--   3 itv005857 supergroup        818 2023-07-20 07:25 /public/trendytech/datasets/orders_sample.csv
-rw-r--r--   3 itv005857 supergroup        292 2023-05-18 10:50 /public/trendytech/datasets/orders_sample1.csv
-rw-r--r--   3 itv005857 supergroup        292 2023-05-18 10:50 /public/trendytech/datasets/orders_sample2.csv
-rw-r--r--   3 itv005857 supergroup        296 2023-05-18 10:50 /public/trendytech/datasets/orders_sample3.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 07:54 /public/trendytech/datasets/ordersorc
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 07:58 /public/trendytech/datasets/ordersparquet
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 20:11 /public/trendytech/datasets/parquet-schema-evol-demo
drwxr-xr-x   - itv005857 supergroup          0 2023-08-21 07:15 /public/trendytech/datasets/parquet-schema-evol-demo1
-rw-r--r--   3 itv005857 supergroup       1602 2023-05-23 13:05 /public/trendytech/datasets/sales_data.json
-rw-r--r--   3 itv005857 supergroup        324 2023-05-23 13:04 /public/trendytech/datasets/train.csv
-rw-r--r--   3 itv005857 supergroup       1353 2023-06-09 16:01 /public/trendytech/datasets/windowdata.csv
-rw-r--r--   3 itv005857 supergroup       1317 2023-06-10 04:52 /public/trendytech/datasets/windowdatamodified.csv

! hadoop fs -cat /public/trendytech/datasets/orders_sample3.csv | head
o/p:
=======
1,2013-07-25,11599,CLOSED
2,2013-07-25,256,PENDING_PAYMENT
3,2013-07-25,12111,COMPLETE
4,2013-07-25,8827,CLOSED
5,2013-07-25,11318,COMPLETE
6,2013-07-25,7130,COMPLETE
7,2013-07-25,error,COMPLETE
8,2013-07-25,2911,PROCESSING
9,2013-07-25,unknown,PENDING_PAYMENT
10,2013-07-25,5648,PENDING_PAYMENT

There are 3 read modes in spark that is used to handle corrupt/malformed/ record:¶
1. PERMESSIVE.
2. DROPMALFORMED.
3. FAILFAST.


1. PERMESSIVE MODE.
============================

i. This is a default read mode in spark.
ii. Whenever it encounter any corrupt/malformed record or unable to parse due to datatype mismatch than it will set  the column/field to null without impacting the other results.

code:
=========
schema_permessive_ddl = "order_id long,order_date string,cust_id long,order_status string"

schema_permessive_programatic = StructType([\
                                StructField("order_id",LongType()),\
                                StructField("order_date",StringType()),\
                                StructField("cust_id",LongType()),\
                                StructField("order_status",StringType())])

df_permessive = spark.read.format("csv")\
                     .schema(schema_permessive_ddl)\
                     .option("sep",",")\
                     .option("path","/public/trendytech/datasets/orders_sample3.csv")\
                     .load()

df_permessive.show(truncate=False)
df_permessive.printSchema()
o/p:
========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |2013-07-25|11599  |CLOSED         |
|2       |2013-07-25|256    |PENDING_PAYMENT|
|3       |2013-07-25|12111  |COMPLETE       |
|4       |2013-07-25|8827   |CLOSED         |
|5       |2013-07-25|11318  |COMPLETE       |
|6       |2013-07-25|7130   |COMPLETE       |
|7       |2013-07-25|null   |COMPLETE       |
|8       |2013-07-25|2911   |PROCESSING     |
|9       |2013-07-25|null   |PENDING_PAYMENT|
|10      |2013-07-25|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

2. DROPMALFORMED MODE.
============================

i. It is not a default mode , to use this mode we have specify this at the time of reading the file.
ii. whenever it encounters any corrupt/malformed record or unable to parse due to datatype mismatch than it will delete this corrupt/malformed record without impacting the other result.

code:
========
schema_dropmalformed_ddl = "order_id long,order_date string,cust_id long,order_status string"

schema_dropmalformed_programatic = StructType([\
                                StructField("order_id",LongType()),\
                                StructField("order_date",StringType()),\
                                StructField("cust_id",LongType()),\
                                StructField("order_status",StringType())])

df_dropmalformed = spark.read.format("csv")\
                     .schema(schema_permessive_ddl)\
                     .option("mode","dropmalformed")\
                     .option("sep",",")\
                     .option("path","/public/trendytech/datasets/orders_sample3.csv")\
                     .load()

df_dropmalformed.show(truncate=False)
df_dropmalformed.printSchema()
o/p:
=========
+--------+----------+-------+---------------+
|order_id|order_date|cust_id|order_status   |
+--------+----------+-------+---------------+
|1       |2013-07-25|11599  |CLOSED         |
|2       |2013-07-25|256    |PENDING_PAYMENT|
|3       |2013-07-25|12111  |COMPLETE       |
|4       |2013-07-25|8827   |CLOSED         |
|5       |2013-07-25|11318  |COMPLETE       |
|6       |2013-07-25|7130   |COMPLETE       |
|8       |2013-07-25|2911   |PROCESSING     |
|10      |2013-07-25|5648   |PENDING_PAYMENT|
+--------+----------+-------+---------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)

3. FAILFAST MODE.
============================

i. It is not a default mode , to use this mode we have specify this at the time of reading the file.
ii. whenever it encounter any corrupt/malformed record or unable to parse due to datatype mismatch than it will give error and will not create the dataframe , so dataframe will not be created in this mode if malformed record is detected.

code:
========
schema_failfast_ddl = "order_id long,order_date string,cust_id long,order_status string"

schema_failfast_programatic = StructType([\
                                StructField("order_id",LongType()),\
                                StructField("order_date",StringType()),\
                                StructField("cust_id",LongType()),\
                                StructField("order_status",StringType())])

df_failfast = spark.read.format("csv")\
                     .schema(schema_permessive_ddl)\
                     .option("mode","failfast")\
                     .option("sep",",")\
                     .option("path","/public/trendytech/datasets/orders_sample3.csv")\
                     .load()

df_failfast.show(truncate=False)
df_failfast.printSchema()
o/p:
=======
Py4JJavaError: An error occurred while calling o103.showString.
: org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 2.0 failed 4 times, most recent failure: Lost task 0.3 in stage 2.0 (TID 5) (w01.itversity.com executor 2): org.apache.spark.SparkException: Malformed records are detected in record parsing. Parse Mode: FAILFAST. To process malformed records as null result, try setting the option 'mode' as 'PERMISSIVE'.

4. To store corrupt record in different column:
======================================================
schema_permessive_ddl = "order_id long,order_date string,cust_id long,order_status string,_corrupt_record string"

schema_permessive_programatic = StructType([\
                                StructField("order_id",LongType()),\
                                StructField("order_date",StringType()),\
                                StructField("cust_id",LongType()),\
                                StructField("order_status",StringType()),\
                                StructField("_corrupt_record",StringType())])

df_permissive_1 = spark.read.format("csv")\
    .schema(schema_permessive_ddl)\
    .option("mode","PERMISSIVE")\
    .option("columnNameOfCorruptRecord","_corrupt_record")\
    .option("sep",",")\
    .load("/public/trendytech/datasets/orders_sample3.csv")

df_permessive_1.show(truncate=False)
df_permessive_1.printSchema()
o/p:
==========
+--------+----------+-------+---------------+------------------------------------+
|order_id|order_date|cust_id|order_status   |_corrupt_record                     |
+--------+----------+-------+---------------+------------------------------------+
|1       |2013-07-25|11599  |CLOSED         |null                                |
|2       |2013-07-25|256    |PENDING_PAYMENT|null                                |
|3       |2013-07-25|12111  |COMPLETE       |null                                |
|4       |2013-07-25|8827   |CLOSED         |null                                |
|5       |2013-07-25|11318  |COMPLETE       |null                                |
|6       |2013-07-25|7130   |COMPLETE       |null                                |
|7       |2013-07-25|null   |COMPLETE       |7,2013-07-25,error,COMPLETE         |
|8       |2013-07-25|2911   |PROCESSING     |null                                |
|9       |2013-07-25|null   |PENDING_PAYMENT|9,2013-07-25,unknown,PENDING_PAYMENT|
|10      |2013-07-25|5648   |PENDING_PAYMENT|null                                |
+--------+----------+-------+---------------+------------------------------------+

root
 |-- order_id: long (nullable = true)
 |-- order_date: string (nullable = true)
 |-- cust_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 |-- _corrupt_record: string (nullable = true)

5. To see only the corrupt records:
==========================================
df_permessive_1.filter(col("_corrupt_record").isNotNull()).show(truncate=False)
o/p:
=========
_corrupt_record:
============================
7,2013-07-25,error,COMPLETE
9,2013-07-25,unknown,PENDING_PAYMENT


26. There are multiple ways to create a df:
===================================================

i. First from database and table, so there are 2 ways:
==============================================================

a. df = spark.sql("select * from database_name.table_name")
b. df = spark.table("database_name.table_name")
ii. 2nd from range() function we create df , this is used for testing purpose:
======================================================================================

a. df.range(0,10).
b. df.range(0,10,2).
iii. 3rd from local_list, so there are multiple ways to create a df from a locallist:
============================================================================================

a. df = spark.createDataFrame(local_list_name).toDF("col1","col2","col3","col4").
b. schema = ['col1','col2','col3','col4']
df = spark.createDataFrame(local_list_name).toDF(schema).
c. schema = ['col1','col2','col3','col4']
df = spark.createDataFrame(local_list_name,schema).
d. By enforcing schema, so there are 2 ways:
i. DDL String/SQL Style Approach:
===============================================

schema_ddl = "col1 datatype,col2 datatype,col3 datatype,col4 datatype".
ii. Programmatic Approach:
======================================

schema_programmatic = StructType([StructField("col1",datatype,True),\
StructField("col2",datatype,True),\
StructFiled("col3",datatype,True),\
StructField("col4,datatype,True)])
df = spark.createDataFrame(local_list_name,schema_ddl).
df = spark.createDataFrame(local_list_name,schema_programmtic).
iv. 4th Create df from different file format like csv,parquet,json,orc,avro,delta:
============================================================================================

v. Create df from rdd, so there are multiple ways to create df from a rdd:
======================================================================================

a. Create rdd from textFile and than convert it to df.
df = spark.createDataFrame(rdd,schema).
df = spark.createDataFrame(rdd).toDF(schema)


27. How to deal with nested schema in spark:
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
=======
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/datasets
o/p:
========
Found 31 items
-rw-r--r--   3 itv005857 supergroup 1675133810 2023-09-16 10:11 /public/trendytech/datasets/accepted_2007_to_2018Q4.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-08-21 19:29 /public/trendytech/datasets/compression-techniques-demo
-rw-r--r--   3 itv005857 supergroup 2362455918 2023-06-06 09:28 /public/trendytech/datasets/cust_transf.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-18 17:40 /public/trendytech/datasets/customer_nested
-rw-r--r--   3 itv005857 supergroup       1538 2023-07-20 07:25 /public/trendytech/datasets/customers_sample.csv
-rw-r--r--   3 itv005857 supergroup       1319 2023-05-23 13:04 /public/trendytech/datasets/hospital.csv
-rw-r--r--   3 itv005857 supergroup       5697 2023-06-05 02:31 /public/trendytech/datasets/hotel_data.csv
-rw-r--r--   3 itv005857 supergroup    6306330 2023-08-20 10:09 /public/trendytech/datasets/json_sample_multiline
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 10:20 /public/trendytech/datasets/json_sample_singleline
drwxr-xr-x   - itv005857 supergroup          0 2023-08-09 00:02 /public/trendytech/datasets/lending-club-project-datasets
-rw-r--r--   3 itv005857 supergroup        925 2023-05-23 13:05 /public/trendytech/datasets/library_data.json
-rw-r--r--   3 itv005857 supergroup   25487177 2023-06-11 04:35 /public/trendytech/datasets/logdata1m.csv
-rw-r--r--   3 itv005857 supergroup        118 2023-07-17 15:38 /public/trendytech/datasets/mapping_data
-rw-r--r--   3 itv005857 supergroup   46079587 2023-06-09 13:05 /public/trendytech/datasets/order_data.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-06-02 02:47 /public/trendytech/datasets/orders
-rw-r--r--   3 itv005857 supergroup    7064041 2023-05-04 07:46 /public/trendytech/datasets/orders.json
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 16:22 /public/trendytech/datasets/orders_avro
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 18:00 /public/trendytech/datasets/orders_orc_ff
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 17:40 /public/trendytech/datasets/orders_parquet_ff
-rw-r--r--   3 itv005857 supergroup        818 2023-07-20 07:25 /public/trendytech/datasets/orders_sample.csv
-rw-r--r--   3 itv005857 supergroup        292 2023-05-18 10:50 /public/trendytech/datasets/orders_sample1.csv
-rw-r--r--   3 itv005857 supergroup        292 2023-05-18 10:50 /public/trendytech/datasets/orders_sample2.csv
-rw-r--r--   3 itv005857 supergroup        296 2023-05-18 10:50 /public/trendytech/datasets/orders_sample3.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 07:54 /public/trendytech/datasets/ordersorc
drwxr-xr-x   - itv005857 supergroup          0 2023-05-04 07:58 /public/trendytech/datasets/ordersparquet
drwxr-xr-x   - itv005857 supergroup          0 2023-08-20 20:11 /public/trendytech/datasets/parquet-schema-evol-demo
drwxr-xr-x   - itv005857 supergroup          0 2023-08-21 07:15 /public/trendytech/datasets/parquet-schema-evol-demo1
-rw-r--r--   3 itv005857 supergroup       1602 2023-05-23 13:05 /public/trendytech/datasets/sales_data.json
-rw-r--r--   3 itv005857 supergroup        324 2023-05-23 13:04 /public/trendytech/datasets/train.csv
-rw-r--r--   3 itv005857 supergroup       1353 2023-06-09 16:01 /public/trendytech/datasets/windowdata.csv
-rw-r--r--   3 itv005857 supergroup       1317 2023-06-10 04:52 /public/trendytech/datasets/windowdatamodified.csv

! hadoop fs -ls /public/trendytech/datasets/customer_nested
o/p:
======
Found 3 items
-rw-r--r--   3 itv005857 supergroup          0 2023-05-18 17:40 /public/trendytech/datasets/customer_nested/_SUCCESS
-rw-r--r--   3 itv005857 supergroup         90 2023-05-18 17:40 /public/trendytech/datasets/customer_nested/part-00000-950ffc21-f8aa-4e00-8181-8ab726051097-c000.json
-rw-r--r--   3 itv005857 supergroup        173 2023-05-18 17:40 /public/trendytech/datasets/customer_nested/part-00001-950ffc21-f8aa-4e00-8181-8ab726051097-c000.json

! hadoop fs -cat /public/trendytech/datasets/customer_nested/part-00001-950ffc21-f8aa-4e00-8181-8ab726051097-c000.json | head
o/p:
=======
{"customer_id":2,"fullname":{"firstname":"ram","lastname":"kumar"},"city":"hyderabad"}
{"customer_id":3,"fullname":{"firstname":"vijay","lastname":"shankar"},"city":"pune"}

ddl_json = "customer_id int,fullname struct<firstname:string,lastname:string>,city string"

programmatic_json = StructType([\
                    StructField("customer_id",IntegerType(),True),\
                    StructField("fullname",StructType([StructField("firstname",StringType(),True),StructField("lastname",StringType(),True)])),\
                    StructField("city",StringType(),True)])

df_json = spark.read.format("json")\
               .schema(ddl_json)\
               .option("path","/public/trendytech/datasets/customer_nested/*")\
               .load()

df_json.show(truncate=False)
df_json.printSchema()
o/p:
========
+-----------+----------------+---------+
|customer_id|fullname        |city     |
+-----------+----------------+---------+
|2          |{ram, kumar}    |hyderabad|
|3          |{vijay, shankar}|pune     |
|1          |{sumit, mittal} |bangalore|
+-----------+----------------+---------+

root
 |-- customer_id: integer (nullable = true)
 |-- fullname: struct (nullable = true)
 |    |-- firstname: string (nullable = true)
 |    |-- lastname: string (nullable = true)
 |-- city: string (nullable = true)

df_json = spark.read.format("json")\
               .schema(programmatic_json)\
               .option("path","/public/trendytech/datasets/customer_nested/*")\
               .load()

df_json.show(truncate=False)
df_json.printSchema()
o/p:
======
+-----------+----------------+---------+
|customer_id|fullname        |city     |
+-----------+----------------+---------+
|2          |{ram, kumar}    |hyderabad|
|3          |{vijay, shankar}|pune     |
|1          |{sumit, mittal} |bangalore|
+-----------+----------------+---------+

root
 |-- customer_id: integer (nullable = true)
 |-- fullname: struct (nullable = true)
 |    |-- firstname: string (nullable = true)
 |    |-- lastname: string (nullable = true)
 |-- city: string (nullable = true)

df_json.createOrReplaceTempView("practice")

Find firstname and lastname:
=================================
i. df_final = df_json.withColumn("first_name",col("fullname.firstname"))\
                  .withColumn("last_name",col("fullname.firstname"))\
                  .drop(col("fullname"))

df_final.show(truncate=False)

ii. df_final = df_json.withColumn("first_name",col("fullname").getField("firstname"))\
                  .withColumn("last_name",col("fullname").getField("lastname"))\
                  .drop(col("fullname"))

df_final.show(truncate=False)
o/p:
=========
+-----------+---------+----------+---------+
|customer_id|city     |first_name|last_name|
+-----------+---------+----------+---------+
|2          |hyderabad|ram       |kumar    |
|3          |pune     |vijay     |shankar  |
|1          |bangalore|sumit     |mittal   |
+-----------+---------+----------+---------+

Using sparksql():
=========================
df_final = spark.sql("select customer_id,fullname.firstname as first_name,fullname.lastname as last_name,city from practice")
df_final.show(truncate=False)
df_final.printSchema()
o/p:
=======
+-----------+----------+---------+---------+
|customer_id|first_name|last_name|city     |
+-----------+----------+---------+---------+
|2          |ram       |kumar    |hyderabad|
|3          |vijay     |shankar  |pune     |
|1          |sumit     |mittal   |bangalore|
+-----------+----------+---------+---------+

root
 |-- customer_id: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- city: string (nullable = true)


28. distinct() vs dropDuplicates():
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


29. sparksession() vs sparkContext():
===============================================
i. SparkSession():
=============================
a. It is a unified session like umbrella that encapsulate all the other context like sparkcontext to deal with spark,hivecontext to deal with hive,sql context to deal with sql.
b. It is an entry point to spark cluster.
c. For one application there should be one sparksession.
d. It is mainly used when we are dealing with higher level API's like df/sparksql.
e. Code for sparksession:
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
==========
SparkSession - hive

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

a. .builder() - It is a method used to give two config i. One is appName ii. Other is master.
b. .appName() - It is used to give application name, for each application there should be one sparksession.
c. config("spark.sql.warehouse.dir",f"/user/{username}/warehouse") - This means whenever we create spark managed table than the data in case of managed table will
   be stored at this location ("/user/itv005857/warehouse").
d. .enableHiveSupport() - This maens we are able to accesss hive metastore .
e. master('yarn') - This means the reasource manager is yarn and our code will run on yarn managed hadoop cluster.
   master('local[*]') - This means our code will run on local machine.
f. .getOrCreate() - This means if the sparksession already exist it will give that or if it does not exist it will create that.

ii. sparkContext():
=============================
a. It is also an entry point to spark cluster.
b. It is mainly used to deal only with spark , to deal with hive or sql we need to create different context.
c. It is mainly used in case of lower level API's.
d. Code for sparkContext():
=======================================
spark = spark.sparkContext.textFile


iii. What is the need of sparksession() when we were having spark context already:
==========================================================================================
a. 1st If we create sparksession than we can deal with spark,hive,sql but when we create sparkcontext we mainly deal with spark only to deal with hive and sql 
   we need to create different context.

b. 2nd if we have two isolated environment that is two different environment in the same application.
   so in this case if we create two sparkcontext one in each environment within the same application 
   so if one spark context crashes than other spark context will also crash.

    so to resolve above issue we will create two sparksession one in each environment within same application
    and both sparksession will have same sparkcontext, both will sahre this same spark context.

Syntax to create two sparksession:
===========================================
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

sparkSession2 = spark.newSession()
print(sparkSession2)

iv. What is the need for 2 sparkSession():
=================================================
a. In extreme scenario there is requirement where we have two different isolated environment within one application and isnide each application we need to store some 
   temporary views, than in this case we will create 2 different sparksession.
   but each sparksession will share same sparkcontext.

b. Also if we create a temporary view in one sparksession and if we try to see that same temporary table in another sparksession than we will not be able to see that
   Also if we create a global temp view in one sparksession and if we try to see that same temporary view in another sparksession than we will be able to see that .
   for this case the code syntax is below.
   Syntax:
=======================
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
        master('yarn').\
        getOrCreate()
spark
o/p:
==========
SparkSession - in-memory

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

sparksession2 = spark.newSession()
sparksession2
o/p:
========
SparkSession - in-memory

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

orders_df = spark.read.format("csv")\
                 .option("header",True)\
                 .option("inferSchema",True)\
                 .option("sep",",")\
                 .option("path","/public/trendytech/orders_wh/orders_wh.csv")\
                 .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
========
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
only showing top 20 rows

root
 |-- order_id: integer (nullable = true)
 |-- order_date: string (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- order_status: string (nullable = true)

i. Using .createOrReplaceTempView():
========================================
orders_df.createOrReplaceTempView("orders_table1")
spark.sql("show tables").show(truncate=False)
o/p:
==========
+--------+-------------+-----------+
|database|tableName    |isTemporary|
+--------+-------------+-----------+
|        |orders_table1|true       |
+--------+-------------+-----------+
sparksession2.sql("show tables").show(truncate=False)
o/p:
=======
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
+--------+---------+-----------+

ii. Using .createOrReplaceGlobalTempView():
=================================================
orders_df.createOrReplaceGlobalTempView("orders_global_table")
spark.sql("select * from global_temp.orders_global_table").show(truncate=False)
o/p:
==========
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

sparksession2.sql("select * from global_temp.orders_global_table").show(truncate=False)
o/p:
=======
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


c. when we are using .enableHiveSupport() than in this case your sparksession will use the hive context , but if we remove this our sparksession will be in memory, so now 
   whatever the metastore will be in memory.
syntax:
===================
i.  Using .enableHiveSupport():
======================================
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

ii. Without using .enableHiveSupport():
==============================================
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
        master('yarn').\
        getOrCreate()
spark
o/p:
=========
SparkSession - in-memory

SparkContext

Spark UI

Versionv3.1.2MasteryarnAppNamepyspark-shell

30. Deployment mode in spark:
=====================================
i. There are 2 deployment mode in spark to deploy out spark application:
==============================================================================
a. client mode:
========================
i. In this mode our driver runs on the client machine/gateway node , so if we terminate our cluster or stop our spark session our driver will be terminated and we will not be able 
   to see our code.

ii. It is mainly recommended for testing/development purpose , so at the time of logic creation for our code we use this mode and once development is completed
    we will package our code and than deploy our code using cluster mode.
iii. In production it is not recommended.


b. cluster mode:
========================
i. In this mode our driver will run inside the cluster where executor is running.
ii. so even if we terminate the cluster or stop the sparksession our driver will not be terminated , it will still be running.
iii. In production this is the most recommended mode.
iv. In production we deploy our code using this mode.


30. cache() vs persist():
================================
i. cache():
===============
a. It is an lazy operation which means whenever we call an action this will be executed.
b. We should apply cache() on resultant rdd so that we can reuse that rdd again and again and our application will run faster.
c. cache is always in memory in case of rdd which means default storage level is (MEMORY_ONLY).
d. If we apply cache on resultant rdd and we call multiple action on our resultant rdd than for the first action all the transformation from beginning to end will be executed
   and cache will store the intermediate result in memory and when we call the 2nd action it will take the intermediate result from memory and execute result of the operation 
   in a faster mamnner so this will make our application run faster.
e. we should not apply cache() on base_rdd.
f. code:
=============
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
orders_filtered = orders_base.filter(lambda x:x.split(",")[3]!="PENDING_PAYMENT")
orders_mapped = orders_filtered.map(lambda x:(x.split(",")[2],1))
orders_reduced = orders_mapped.reduceByKey(lambda x,y:x+y)
result = orders_reduced.filter(lambda x:int(x[0])<501)
result.cache()
o/p:
=========
PythonRDD[6] at RDD at PythonRDD.scala:53
result.collect()
o/p:
=======
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
 ('315', 1125),
 ('106', 750),
 ('247', 2625),
 ('100', 2250),
 ('291', 1500),
 ('227', 1500),
 ('498', 1500),
 ('124', 1500),
 ('452', 1500),
 ('43', 750),
 ('134', 1500),
 ('448', 1500),
 ('295', 750),
 ('476', 375),
 ('294', 1125),
 ('441', 1125),
 ('225', 1875),
 ('33', 750),
 ('293', 750),
 ('178', 375),
 ('31', 1125),
 ('173', 3000),
 ('457', 2625),
 ('460', 1875),
 ('444', 1875),
 ('48', 3000),
 ('464', 1875),
 ('478', 2250),
 ('109', 1875),
 ('157', 750),
 ('114', 1500),
 ('226', 1500),
 ('96', 1875),
 ('355', 1500),
 ('60', 1875),
 ('359', 1500),
 ('208', 1500),
 ('36', 1125),
 ('302', 375),
 ('231', 2625),
 ('93', 1875),
 ('50', 1875),
 ('411', 1500),
 ('305', 1500),
 ('317', 1125),
 ('479', 375),
 ('8', 2250),
 ('327', 1875),
 ('269', 375),
 ('356', 2250),
 ('335', 3750),
 ('408', 1875),
 ('92', 1875),
 ('155', 1500),
 ('35', 1125),
 ('367', 1875),
 ('449', 1125),
 ('257', 2625),
 ('224', 1875),
 ('425', 1875),
 ('465', 2625),
 ('332', 2250),
 ('229', 2250),
 ('321', 3000),
 ('85', 2250),
 ('152', 1125),
 ('198', 1500),
 ('84', 750),
 ('170', 1125),
 ('329', 2250),
 ('3', 2625),
 ('237', 750),
 ('435', 1875),
 ('190', 1875),
 ('311', 1500),
 ('421', 1125),
 ('394', 1500),
 ('346', 1125),
 ('412', 1500),
 ('261', 750),
 ('140', 1875),
 ('10', 750),
 ('253', 375),
 ('153', 375),
 ('396', 1875),
 ('254', 2250),
 ('232', 1500),
 ('11', 1125),
 ('484', 1875),
 ('442', 2625),
 ('172', 2625),
 ('17', 1875),
 ('46', 1875),
 ('38', 2250),
 ('422', 1875),
 ('467', 3000),
 ('437', 3750),
 ('47', 1125),
 ('205', 1875),
 ('216', 1125),
 ('482', 3750),
 ('221', 4500),
 ('347', 1125),
 ('292', 750),
 ('312', 2625),
 ('490', 750),
 ('284', 1500),
 ('51', 3000),
 ('148', 1125),
 ('406', 1500),
 ('296', 3000),
 ('414', 750),
 ('164', 1500),
 ('26', 1875),
 ('373', 1875),
 ('277', 1500),
 ('447', 1500),
 ('368', 1500),
 ('182', 1125),
 ('87', 1500),
 ('385', 750),
 ('25', 750),
 ('116', 750),
 ('95', 2250),
 ('306', 1875),
 ('255', 2250),
 ('251', 1500),
 ('136', 750),
 ('6', 750),
 ('310', 750),
 ('419', 1500),
 ('345', 2250),
 ('195', 750),
 ('207', 2250),
 ('230', 1875),
 ('324', 1500),
 ('454', 2250),
 ('430', 2625),
 ('197', 3000),
 ('450', 3000),
 ('44', 1125),
 ('440', 1875),
 ('378', 1500),
 ('429', 1500),
 ('119', 3000),
 ('23', 1875),
 ('313', 375),
 ('147', 1500),
 ('13', 2250),
 ('16', 2250),
 ('27', 1875),
 ('233', 1875),
 ('471', 1500),
 ('113', 1500),
 ('71', 3000),
 ('101', 1875),
 ('258', 2625),
 ('20', 1875),
 ('279', 1125),
 ('297', 2625),
 ('282', 1500),
 ('456', 750),
 ('438', 1125),
 ('451', 375),
 ('127', 1125),
 ('319', 2250),
 ('432', 1125),
 ('364', 3375),
 ('63', 2250),
 ('445', 1500),
 ('90', 1500),
 ('443', 3000),
 ('342', 1500),
 ('111', 750),
 ('107', 1875),
 ('262', 1875),
 ('349', 1500),
 ('66', 1125),
 ('337', 1500),
 ('74', 2625),
 ('278', 750),
 ('322', 750),
 ('160', 1125),
 ('301', 375),
 ('135', 375),
 ('94', 2250),
 ('272', 3000),
 ('179', 1500),
 ('371', 1875),
 ('426', 1875),
 ('223', 1125),
 ('241', 2250),
 ('58', 2625),
 ('488', 1500),
 ('409', 2625),
 ('458', 1875),
 ('267', 1125),
 ('15', 1125),
 ('480', 1125),
 ('475', 1875),
 ('187', 1875),
 ('439', 1500),
 ('354', 3750),
 ('141', 2250),
 ('264', 1125),
 ('62', 1500),
 ('194', 1500),
 ('472', 2250),
 ('185', 1875),
 ('139', 1125),
 ('340', 2250),
 ('314', 3375),
 ('176', 1875),
 ('500', 1125),
 ('401', 1125),
 ('64', 750),
 ('375', 1500),
 ('110', 1875),
 ('320', 1875),
 ('252', 1875),
 ('433', 2250),
 ('413', 750),
 ('234', 1125),
 ('9', 1125),
 ('181', 1125),
 ('86', 1125),
 ('477', 2250),
 ('386', 1125),
 ('167', 750),
 ('145', 2250),
 ('485', 750),
 ('330', 1500),
 ('161', 1500),
 ('239', 1875),
 ('249', 750),
 ('350', 1500),
 ('81', 750),
 ('42', 1875),
 ('59', 1500),
 ('325', 1125),
 ('466', 375),
 ('461', 1125),
 ('405', 750),
 ('29', 375),
 ('146', 1500),
 ('497', 2250),
 ('273', 2250),
 ('377', 2250),
 ('308', 2250),
 ('455', 3000),
 ('379', 1875),
 ('188', 1500),
 ('126', 1875),
 ('263', 750),
 ('75', 1875),
 ('418', 375)]
 
result.count()
o/p:
=====
492

spark.stop()


ii. persist():
====================
a. persist comes with various storage level like persist on disk,persist in memeory, persist on memeory and disk.

Impt point to remember more about cache() and persist():
==============================================================
1. Cache and persist both are lazy operation which means whenever we call action this will be executed.
2. Both cache and persist are niether transformation nor action , both are utility function.
3. We should not cache base df , we should always try to cache or persist result df to get more benefit.
4. We should always try to cache() medium size df , not very large or niether very small df because if we use very large df than it will not fit into memory and we will get
   OOM error issue and if we use very small df than we will not get the benefit of caching.
5. We should try to cache the df that we want to use it again and again (lot of times).
6. In case of rdd the deafault storage level in cache is (MEMORY_ONLY) , but case of df/spark table the default storage level is (MEMORY_AND_DISK).
   So consider an example if we have 10 gb file so total no of partitions is 80 , so let say if there is not enough space in memory to accomodate this all 80 partitions
   than in case of rdd some of the partitions will get skipped (If 50 partitions are in memory than 30 partitions will be skipped) , but in case of df the storage level is
   (MEMORY_AND_DISK) so if 50 partitions is in memory than 30 partitions will be in disk .
7. Disk has two parts:
i. HDFS of WN: It will be slow and performance will be low.
ii. Local Disk: It will hold the cache/persist data(partitions) , this will be slightly faster than hdfs disk.
8. Cache will store the data in memory.
9. But persistt() comes with various storage level like (MEMORY_ONLY,MEMORY_AND_DISK,DISK_ONLY) and lot other.
10. Benefit of cache() and persist():
===============================================
i. It improves performance for ex Lets consider we are calling multiple action on our df , so if we use cache() on resultant df so when we will call the 1st action
   than all the transformation from begining to end will be executed and intermediate result will be stored in memory and than when we call action for 2nd time 
   than instead of executing all the transformation from begining to end it will take the intermediate result from memory and execute rest of the transformation
   so this will save computational cost and also make our application faster.
   For example psuedo code:
==========================================
df1 = read a orders file from the disk.
df2 = df1.transformation1
df3 = df2.transformation2
df4 = df3.transformation3
df4.cache()
df4.show()
df4.count()

For 1st action entire transformation from begining to end will be executed and the intermediate result will be cached in memory that is df4 result and when we call
    2nd action the entire transformation will not be executed it will take the intermediate result from memory and exceute rest of the result and application run faster
    and it also saves computational cost.

ii. It saves computational cost because we are avoiding some of the transformation when we are using cache().




i. Why to cache() a df() / rdd/ spark table if a df()/rdd/spark table is always in-memory?
=====================================================================================================
a. Lets consider a example code to understand this :
==================================================================
i. df1 = read a orders file from the disk.
   df2 = df1.transformation2
   df3 = df2.transformation3
   df3.show()
   df3.count()

In above example code  we are reading data from the disk and executing the transformation one by one whenever we are calling action1 that is "df3.show()" so entire thing is getting
executed and again when we ae calling 2nd action2 that is "df3.count()" again we are touching disk and the entire thing is getting executed from beginning to end so this degrade our
performance because we are reading data from the disk again and again and reading data from the disk takes a lot of time as data inside disk is stored in bytes/binary/serilaized format
so when we are reading it the byte data is converted to object form and due to which reading data from the disk becomes slow, so due to which we need to use cache the intermediate result while
calling 1st action so that when we call 2nd action we will take the intermediate result from memory and execute rest of the transformation result in speeding up the application.


ii. df1 = read a orders file from the disk.
    df1.cache()
   df2 = df1.transformation1
   df3 = df2.transformation2
   df3.show()
   df3.count()

So In above case when we are calling action for the 1st time the entire transformation is getting executed from beginning to end and the intermediate result is getting stored inside memory,
so when we call action for 2nd time instead of again reading from disk it will take the intermediate result from memory and exceute rest of the transformation making our application run faster.

So due to above two reasons we are using cache() though df()/rdd/spark table are in-memory.


ii. Why to use disk() when our data initially we are reading from disk so why we are caching the result in disk():
=============================================================================================================================
a. Disk has two parts:
i. HDFS of WN: It will be slow and performance will be low.
ii. Local Disk(Non-HDFS): It will hold the cache/persist data(partitions) , this will be slightly faster than hdfs disk.


So Initially the data that we are reading from disk was in hdfs of WN so it will be slow and low in performance.
and after caching th data will be on local disk / Non-hdfs of WN so this will be slightly faster .


iii. Where you can see your cached result in spark UI:
===============================================================
a. So to see cache result in spark UI we will go to storage tab.
b. We can see cache() result when our spark application(that is sparksession) is running , so whenever we stop the sparksession using (spark.stop()) we can't see our cached result.


31. Impt point to remember about cache() vs persist():
======================================================================
i. cache():
===========================
a. Whenever we perform cache() we get two benefit:
   i. It improve performance by speeding up the application beacuse after caching we are reading result from memory .
   ii. It reduces computational cost beacuse after caching the df when we call action again on cached df than in this case instaed of performing all the transformation it will take the 
       result from memory and perform rest of the operation making execution faster.

b. Always try to keep the result of cached df in other df(), For example:
   cached_df = orders_df.cache()
   cached_df.show()

c. cache() is an lazy operation whenver we call action it will be executed.

d. 

CASE I: So whenever we performed below operation on df before caching:
======================================================================================
   orders_df.count()
   =============================
i. So in above case we will get two stages , stage0 and stage1.
   In stage0 executor will give the  total local count of it, so here there will be 9 partitions two executor will work .
   In stage1  the final result of stage1 one will go to stage2  so here there will be 1 partition.
Here we are getting 2 stages because there is minimal shuffling involved.

ii. In above case count() took 6 sec before caching because it is reading data from disk().

iii. In cluster dynamic memory allocation is enabled so here initially when count() is executed it is acquiring 2 exceutors.
     In dynamic memory allocation:
==============================================
a. Min executors is 2
b. Max executors is 10

iv. In above case the df is not cached() so we can check this from our spark UI also:
    First from job tab -> Inside Job tab if we see NODE LOCAL so it means the df is not cached , so in Above case it is showing NODE LOCAL.
    2nd from SQL tab -> we will see INMEMORYTABLESCAN when df is cached but in above case we see Scan csv whic means it is not cached.

v. Again if we run "orders_df.count()" it is taking less time around 4 sec because here it is grapping more executor from the cluster as our dynamic memory allocation is enabled
   it will grap more executors that is 3 sec in this case so due to which it takes less time.


CASE II: So whenever we perform cached_df = orders_df.cache(), at the time of caching :
======================================================================================
   cached_df = orders_df.cache()
   =============================
a. So at the time of caching it will take around 17sec beacuse it is a intense heavy opeartion, at this time 9 partitions will be cached.

CASE III: So when we perform below operation:
===============================================================
   cached_df = orders_df.cache()
   cached_df.show()
=============================================
a. So in above case only 1 partition is cached because .show() will display only 20 records.

CASE IV: So when we perform below operation after caching for 1st time:
===========================================================================
    cached_df = orders_df.cache()
    cached_df.count()
============================================
a. In above case it is taking 20 sec because when we call count() for the 1st time after caching it will take time bacause as caching ia an lazy operation it takes lot of time 
   to  cache the df as there are 9 partitions .

b. In above case 8 executors will work.


CASE V: So when we perform below operation after caching for 2nd time:
===========================================================================
    cached_df = orders_df.cache()
    cached_df.count()
============================================
a. In above case it is taking only 0.2 sec because caching has take place and our data is in (MEMORY_AND_DISK) , so reading from memory will take less time.
b. In above case the df is  cached() so we can check this from our spark UI also:
    First from job tab -> Inside Job tab if we see PROCESS LOCAL so it means the df is  cached.
    2nd from SQL tab -> we will see INMEMORYTABLESCAN as our df is cached.

c. In above case 8 executors will work.

32. Impt concept in cache() and persist():
======================================================
i. Memory Deserialized 1*Replicated -> This means whatever it can keep in memory it will keep in memory and rest it will put to disk.

ii. Serialized:
==================================
Serialized means keeping it in binary format(byte format), so it consumes less storage space and it requires heavy computation because of format conversion (binary to object format).
Data is stored in disk in binary format(serilaized format) so due to which reading data from the disk is slow.


iii. Deserialized:
=============================
Deserialized means keeping it in object format, so it consume more storage space but in terms of computation this is fast.

iv. When we talk about caching:
=============================================
In case of -:
i. Disk -> It is always serialized (data is stored in binary format).
ii. Memory -> It can be serilaized or deserialized but deserilaized(memory) is prefered for memory.

v. In case of df we can't perform uncache() instead we will perform unpersist().


33. Another point to remember about cache() and persist():
========================================================================
i. Code1:
=========================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import getpass

username = getpass.getuser()

spark = SparkSession \
    .builder \
    .config("spark.sql.warehouse.dir", f"/user/{username}/warehouse") \
    .enableHiveSupport() \
    .master("yarn") \
    .getOrCreate()
    
spark
o/p:
=============
SparkSession - hive

SparkContext

Spark UI

Versionv2.4.7MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/orders
o/p:
==========
Found 3 items
-rw-r--r--   3 itv005857 supergroup 3749930000 2024-01-21 14:18 /public/trendytech/orders/orders.csv
-rw-r--r--   3 itv005857 supergroup 1124979000 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-28 05:02 /public/trendytech/orders/ordersparquet

! hadoop fs -ls /public/trendytech/orders/orders_1gb.csv
o/p:
=========
-rw-r--r--   3 itv005857 supergroup 1124979000 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv


! hadoop fs -head /public/trendytech/orders/orders_1gb.csv
o/p:
=========
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
8,2013-07-25 00:00:00.0,2911,PROCESSING
9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT
11,2013-07-25 00:00:00.0,918,PAYMENT_REVIEW
12,2013-07-25 00:00:00.0,1837,CLOSED
13,2013-07-25 00:00:00.0,9149,PENDING_PAYMENT
14,2013-07-25 00:00:00.0,9842,PROCESSING
15,2013-07-25 00:00:00.0,2568,COMPLETE
16,2013-07-25 00:00:00.0,7276,PENDING_PAYMENT
17,2013-07-25 00:00:00.0,2667,COMPLETE
18,2013-07-25 00:00:00.0,1205,CLOSED
19,2013-07-25 00:00:00.0,9488,PENDING_PAYMENT
20,2013-07-25 00:00:00.0,9198,PROCESSING
21,2013-07-25 00:00:00.0,2711,PENDING
22,2013-07-25 00:00:00.0,333,COMPLETE
23,2013-07-25 00:00:00.0,4367,PENDING_PAYMENT
24,2013-07-25 00:00:00.0,11441,CLOSED
25,2013-07-25 00:00:00.0,9503,CLOSED


orders_schema = "order_id long,order_date date,customer_id long,order_status string"

orders_df = spark.read \
                 .format("csv") \
                 .schema(orders_schema) \
                 .load("/public/trendytech/orders/orders_1gb.csv")

orders_df.cache()
o/p:
========
order_id	order_date	customer_id	order_status
1	2013-07-25	11599	CLOSED
2	2013-07-25	256	PENDING_PAYMENT
3	2013-07-25	12111	COMPLETE
4	2013-07-25	8827	CLOSED
5	2013-07-25	11318	COMPLETE
6	2013-07-25	7130	COMPLETE
7	2013-07-25	4530	COMPLETE
8	2013-07-25	2911	PROCESSING
9	2013-07-25	5657	PENDING_PAYMENT
10	2013-07-25	5648	PENDING_PAYMENT
11	2013-07-25	918	PAYMENT_REVIEW
12	2013-07-25	1837	CLOSED
13	2013-07-25	9149	PENDING_PAYMENT
14	2013-07-25	9842	PROCESSING
15	2013-07-25	2568	COMPLETE
16	2013-07-25	7276	PENDING_PAYMENT
17	2013-07-25	2667	COMPLETE
18	2013-07-25	1205	CLOSED
19	2013-07-25	9488	PENDING_PAYMENT
20	2013-07-25	9198	PROCESSING


a. This above code will hit cache() and one partition will be cached in above case as it will behave as .show().
b. This will behave as .show().
c. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "PROCESS_LOCAL" which indicate it has hit cache().
    iii. 3rd we will see Storage tab : So in above case it will show Cached Partitions as 1 and Fraction Cached as 11% .
d. In above case only one partition will be cached because it behaves like .show().


ii. Code 2:
=====================
filtered_df = orders_df.filter("customer_id == 10000000")
filtered_df.show()
o/p:
==========
+--------+----------+-----------+------------+
|order_id|order_date|customer_id|order_status|
+--------+----------+-----------+------------+
+--------+----------+-----------+------------+

a. In above case entire 9 partitions will be cached because as filter is a transformation it will try to scan entire partition in order to see the "customer_id = 10000000" exists or not.
b. This will behave as .show().
c. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "PROCESS_LOCAL" which indicate it has hit cache().
    iii. 3rd we will see Storage tab : So in above case it will show Cached Partitions as 9 and Fraction Cached as 100% .
    
 iii. Code3:
 =========================
 orders_df.select("order_id","order_status")\
         .filter("order_status == 'CLOSED'")\
         .cache()
o/p:
===========
order_id	order_status
1	CLOSED
4	CLOSED
12	CLOSED
18	CLOSED
24	CLOSED
25	CLOSED
37	CLOSED
51	CLOSED
57	CLOSED
61	CLOSED
62	CLOSED
87	CLOSED
90	CLOSED
101	CLOSED
116	CLOSED
129	CLOSED
133	CLOSED
191	CLOSED
201	CLOSED
211	CLOSED

a. The above code will hit cache() and it will cache only 1 partition and  Fraction Cached as 11% .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "PROCESS_LOCAL" which indicate it has hit cache().
c. To cache() entire 9 partitions we will use .count() which means we will call action .
Below Code:
===================
orders_df.select("order_id","order_status")\
         .filter("order_status == 'CLOSED'")\
         .count()
o/p:
=========
2833500

a. The above code will hit cache() and it will cache entire 9 partition and  Fraction Cached as 100% .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "PROCESS_LOCAL" which indicate it has hit cache().
    iii. 3rd we will see Storage tab : So in above case it will show Cached Partitions as 9 and Fraction Cached as 100% .
    
c. In above code case spark will use predicate pushdown optimization and will move filter ahead of select and it will remove unwanted data and we it will be left with less
   data and than work on it.
   
d. == Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#536L]
+- Filter (order_status#305 = CLOSED)
   +- Project [order_id#302L, order_status#305]
      +- Relation[order_id#302L,order_date#303,customer_id#304L,order_status#305] csv
In this case filter is moved ahead .
   

iv. code 4:
=======================
orders_df.filter("order_status == 'CLOSED'")\
         .select("order_id","order_status")\
         .count()
o/p:
=============
2833500

a. This above code will not hit cache() because this code has different Analyzed Logical Plan.
In this case filter is not  moved ahead .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "CSVSCAN" which indicate it has not hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "NODE_LOCAL" which indicate it has not hit cache().

    
    
Impt pt to remember about cache() and persist() in case of df():
======================================================================
a. filtered_df.unpersist() -> In case of df() we can't use .uncache() to uncache() the partitions , instead we will use .unpersist().
b. filtered_df.uncache() -> This is not supported in case of df() and rdd().
c. Predicate pushdown:
=================================
i. It means moving filter condition ahead so that the data gets limited in the initial stages.
ii. Let say you are performing lots of transformations and after that we are doing filter , so spark will see that can it move the filter up 
    so that basically you get the same result but first we filter the record so that we are left with less records and we process less record ,
    so this is one optimization thats called predicate pushdown.
iii. == Parsed Logical Plan ==
Aggregate [count(1) AS count#307L]
+- Project [order_id#0L, order_status#3]
   +- Filter (order_status#3 = CLOSED)
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#307L]
+- Project [order_id#0L, order_status#3]
   +- Filter (order_status#3 = CLOSED)
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#307L]
+- Project
   +- Filter (isnotnull(order_status#3) && (order_status#3 = CLOSED))
      +- InMemoryRelation [order_id#0L, order_date#1, customer_id#2L, order_status#3], StorageLevel(disk, memory, deserialized, 1 replicas)
            +- *(1) FileScan csv [order_id#0L,order_date#1,customer_id#2L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<order_id:bigint,order_date:date,customer_id:bigint,order_status:string>
            
            
            
v. code 5:
===================
orders_df.select("order_id","order_status").count()
o/p:
=========
25831125

i. The above code will not hit cache because this code  has different analyzed logical plan because here we are selecting entire order_status.


VI. Code 6:
==========================
orders_df.select("order_id","order_status")\
.filter("order_status == 'COMPLETE'")\
.count()
o/p:
==========
8587125

i. The above code will not hit cache because this code  has different analyzed logical plan because here we are using different filter condition.
   This will not hit cache because here we are selecting order_status == 'COMPLETE' , but when we are caching at that time we are selecting order_status == 'CLOSED' ,
   so here analyzed plan is different.


vii. code 7:
==========================
orders_df.select("order_id","order_status")\
         .filter("order_id > 10")\
         .cache()
o/p:
=========
order_id	order_status
11	PAYMENT_REVIEW
12	CLOSED
13	PENDING_PAYMENT
14	PROCESSING
15	COMPLETE
16	PENDING_PAYMENT
17	COMPLETE
18	CLOSED
19	PENDING_PAYMENT
20	PROCESSING
21	PENDING
22	COMPLETE
23	PENDING_PAYMENT
24	CLOSED
25	CLOSED
26	COMPLETE
27	PENDING_PAYMENT
28	COMPLETE
29	PROCESSING
30	PENDING_PAYMENT

a. This above code will hit the cache because here we are using different filter condition ("order_id > 10").
b. Here spark will use predicate pushdown and will push filter ahead and will remove unwanted data .
c. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has hit cache().
    ii. 2nd we will see JOB tab : So in aove case it will show "PROCESS_LOCAL" which indicate it has hit cache().


viii. Code 8:
====================
orders_df.select("order_id","order_status")\
         .filter("order_id > 100")\
         .count()
o/p:
=========
25793625

a. This above code will not hit the cache because here we are using different filter condition ("order_id > 100") .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "Scan csv" which indicate it has not hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "NODE_LOCAL" which indicate it has not hit cache(). 


ix. code 9:
==================
orders_df.select("order_status")\
         .filter("order_id > 10")\
         .count()
o/p:
=========
25827375

a. This will not hit  cache because analyzed plan is different .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "Scan csv" which indicate it has not hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "NODE_LOCAL" which indicate it has not hit cache(). 


x. Code 10:
====================
cached_df = orders_df.select("order_id","order_status")\
                     .filter("order_id>10")\
                     .cache()

cached_df.count()
o/p:
=======
25827375

a. This will hit  cache .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache(). 
    
c. This is most recommended approach .

xi. Code 11:
===================================
cached_df.select("order_id","order_status")\
         .filter("order_id > 100")\
         .count()
o/p:
===========
25793625


a. This will hit  cache .
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    
c. Here there is no issue if analyzed plan is different because we have kept the result of cached df into another df so in this case if your code matches
   or does not matches the analyzed plan than also it will hit cache().
   
   
Impt pt to remember about cache() and persist() in case of df():
======================================================================
a. filtered_df.unpersist() -> In case of df() we can't use .uncache() to uncache() the partitions , instead we will use .unpersist().
b. filtered_df.uncache() -> This is not supported in case of df() and rdd().
c. Predicate pushdown:
=================================
i. It means moving filter condition ahead so that the data gets limited in the initial stages.
ii. Let say you are performing lots of transformations and after that we are doing filter , so spark will see that can it move the filter up 
    so that basically you get the same result but first we filter the record so that we are left with less records and we process less record ,
    so this is one optimization thats called predicate pushdown.
iii. == Parsed Logical Plan ==
Aggregate [count(1) AS count#307L]
+- Project [order_id#0L, order_status#3]
   +- Filter (order_status#3 = CLOSED)
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#307L]
+- Project [order_id#0L, order_status#3]
   +- Filter (order_status#3 = CLOSED)
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#307L]
+- Project
   +- Filter (isnotnull(order_status#3) && (order_status#3 = CLOSED))
      +- InMemoryRelation [order_id#0L, order_date#1, customer_id#2L, order_status#3], StorageLevel(disk, memory, deserialized, 1 replicas)
            +- *(1) FileScan csv [order_id#0L,order_date#1,customer_id#2L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<order_id:bigint,order_date:date,customer_id:bigint,order_status:string>


iv. It is always recommended to keep the result of cached df into another dataframe so in this case if your code matches
   or does not matches the analyzed plan than also it will hit cache().
For example:
==================
df.cache()---------> Don't use
cached_df = df.cache()  ----------> Always recommended.  



34. Parsed / Analyzed / optimized Logical plan:
=======================================================
i. orders_df.select("order_status","order_id")\
         .filter("order_id>10")\
         .cache()
o/p:
==============
order_status	order_id
PAYMENT_REVIEW	11
CLOSED	12
PENDING_PAYMENT	13
PROCESSING	14
COMPLETE	15
PENDING_PAYMENT	16
COMPLETE	17
CLOSED	18
PENDING_PAYMENT	19
PROCESSING	20
PENDING	21
COMPLETE	22
PENDING_PAYMENT	23
CLOSED	24
CLOSED	25
COMPLETE	26
PENDING_PAYMENT	27
COMPLETE	28
PROCESSING	29
PENDING_PAYMENT	30

a. This will hit  cache  and it will behave like (.show()).
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 1
          Fraction Cached : 11% percent.
          Size in Memory : 9.0 MB.
          Size in Disk : 0 MB.
         

ii. orders_df.select("order_status","order_id")\
         .filter("order_id>10")\
         .count()
o/p:
============
25827375

a. This above code will hit cache() and here entire 9 partitions will be cached.  
b. So in above case we will get two stages , stage0 and stage1.
   In stage0 executor will give the  total local count of it, so here there will be 9 partitions two executor will work .
   In stage1  the final result of stage1 one will go to stage2  so here there will be 1 partition.
Here we are getting 2 stages because there is minimal shuffling involved.

c. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 9
          Fraction Cached : 100% percent.
          Size in Memory : 75.3 MB.
          Size in Disk : 0 MB.
          
          
iii. orders_df.select("order_status")\
         .filter("order_id>10")\
         .count()
o/p:
==========
25827375

a. This above code will hit cache() because it internally will add "order_id" at the end because we are doing filter on order_id , so it will 
   automatically come as part of the plan:
   Inside execution plan code will look like below:
   =====================================================
   orders_df.select("order_status","order_id")\
         .filter("order_id>10")\
         .count()
b. Execution plan diagram:
===================================
== Parsed Logical Plan ==
Aggregate [count(1) AS count#95L]
+- Project [order_status#3]
   +- Filter (order_id#0L > cast(10 as bigint))
      +- Project [order_status#]
         +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#95L]
+- Project [order_status#3]
   +- Filter (order_id#0L > cast(10 as bigint))
      +- Project [order_status#3, order_id#0L]
         +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#95L]
+- Project
   +- InMemoryRelation [order_status#3, order_id#0L], StorageLevel(disk, memory, deserialized, 1 replicas)
         +- *(1) Project [order_status#3, order_id#0L]
            +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
               +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>

== Physical Plan ==
*(2) HashAggregate(keys=[], functions=[count(1)], output=[count#95L])
+- Exchange SinglePartition
   +- *(1) HashAggregate(keys=[], functions=[partial_count(1)], output=[count#108L])
      +- InMemoryTableScan
            +- InMemoryRelation [order_status#3, order_id#0L], StorageLevel(disk, memory, deserialized, 1 replicas)
                  +- *(1) Project [order_status#3, order_id#0L]
                     +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
                        +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>
                        
c. So in above case we will get two stages , stage0 and stage1.
   In stage0 executor will give the  total local count of it, so here there will be 9 partitions two executor will work .
   In stage1  the final result of stage1 one will go to stage2  so here there will be 1 partition.
Here we are getting 2 stages because there is minimal shuffling involved.

c. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 9
          Fraction Cached : 100% percent.
          Size in Memory : 75.3 MB.
          Size in Disk : 0 MB.
          
          
 iv. orders_df.select("order_id","order_status")\
         .filter("order_id>10")\
         .cache()
o/p:
=========
order_id	order_status
11	PAYMENT_REVIEW
12	CLOSED
13	PENDING_PAYMENT
14	PROCESSING
15	COMPLETE
16	PENDING_PAYMENT
17	COMPLETE
18	CLOSED
19	PENDING_PAYMENT
20	PROCESSING
21	PENDING
22	COMPLETE
23	PENDING_PAYMENT
24	CLOSED
25	CLOSED
26	COMPLETE
27	PENDING_PAYMENT
28	COMPLETE
29	PROCESSING
30	PENDING_PAYMENT

a. This above code will hit cache() and will behave like .show() so here only 1 partition will be cached.
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 1
          Fraction Cached : 11% percent.
          Size in Memory :  MB.
          Size in Disk : 0 MB.
c. Logical plan:
=======================
== Parsed Logical Plan ==
GlobalLimit 21
+- LocalLimit 21
   +- Project [cast(order_id#0L as string) AS order_id#142, cast(order_status#3 as string) AS order_status#143]
      +- Filter (order_id#0L > cast(10 as bigint))
         +- Project [order_id#0L, order_status#3]
            +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
order_id: string, order_status: string
GlobalLimit 21
+- LocalLimit 21
   +- Project [cast(order_id#0L as string) AS order_id#142, cast(order_status#3 as string) AS order_status#143]
      +- Filter (order_id#0L > cast(10 as bigint))
         +- Project [order_id#0L, order_status#3]
            +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
GlobalLimit 21
+- LocalLimit 21
   +- Project [cast(order_id#0L as string) AS order_id#142, order_status#3]
      +- InMemoryRelation [order_id#0L, order_status#3], StorageLevel(disk, memory, deserialized, 1 replicas)
            +- *(1) Project [order_id#0L, order_status#3]
               +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
                  +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>

       
       
  v. orders_df.select("order_id","order_status")\
         .filter("order_id>10")\
         .count()
o/p:
=========
25827375

a. This above code will hit cache() and entire 9 partitions will be cached.
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 9
          Fraction Cached : 100% percent.
          Size in Memory : 75.3 MB.
          Size in Disk : 0 MB.
          
c. This code takes 6 secs.
d. Logical plan diagram:
=============================
== Parsed Logical Plan ==
Aggregate [count(1) AS count#162L]
+- Filter (order_id#0L > cast(10 as bigint))
   +- Project [order_id#0L, order_status#3]
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#162L]
+- Filter (order_id#0L > cast(10 as bigint))
   +- Project [order_id#0L, order_status#3]
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#162L]
+- Project
   +- InMemoryRelation [order_id#0L, order_status#3], StorageLevel(disk, memory, deserialized, 1 replicas)
         +- *(1) Project [order_id#0L, order_status#3]
            +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
               +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>




vi. orders_df.select("order_status")\
         .filter("order_id>10")\
         .count()
o/p:
==========
25827375

a. This above code will not hit cache because it will internally add "order_id" at the last as "order_id>10" is present in the filter so 
   Analyzed Plan will be different so due to which it will not hit cache().

b. In above code two stages will be created stage0 that will hold 9 tasks and stage1 holds 1 final task.



vii. orders_df.select("order_status","order_id")\
         .filter("order_id>10")\
         .cache()
o/p:
==========
order_status	order_id
PAYMENT_REVIEW	11
CLOSED	12
PENDING_PAYMENT	13
PROCESSING	14
COMPLETE	15
PENDING_PAYMENT	16
COMPLETE	17
CLOSED	18
PENDING_PAYMENT	19
PROCESSING	20
PENDING	21
COMPLETE	22
PENDING_PAYMENT	23
CLOSED	24
CLOSED	25
COMPLETE	26
PENDING_PAYMENT	27
COMPLETE	28
PROCESSING	29
PENDING_PAYMENT	30


a. The above code will hit cache() and in above case only 1 partitions will be cached because it will behave like .show().
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 1
          Fraction Cached : 11% percent.
          Size in Memory :  MB.
          Size in Disk : 0 MB.
          
          
viii. orders_df.select("order_status","order_id")\
         .filter("order_id>10")\
         .count()
o/p:
===========
25827375

a. This above code will hit cache() and entire 9 partitions will be cached.
b. The above code will take 0.2 sec.
c.  To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 9
          Fraction Cached : 100% percent.
          Size in Memory : 75.3 MB.
          Size in Disk : 0 MB.
d. Analyzed plan is same .
Execution plan diagram:
================================
== Parsed Logical Plan ==
Aggregate [count(1) AS count#234L]
+- Filter (order_id#0L > cast(10 as bigint))
   +- Project [order_status#3, order_id#0L]
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#234L]
+- Filter (order_id#0L > cast(10 as bigint))
   +- Project [order_status#3, order_id#0L]
      +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#234L]
+- Project
   +- InMemoryRelation [order_status#3, order_id#0L], StorageLevel(disk, memory, deserialized, 1 replicas)
         +- *(1) Project [order_status#3, order_id#0L]
            +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
               +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>
               




ix. orders_df.select("order_status")\
         .filter("order_id>10")\
         .count()
o/p:
=========
25827375

a. The above code will hit cahe() because internally it will add "order_id" at the end as it is present in filter condition "order_id>10"  so analyzed plan
   will be same.
   
b. To see if above code has hit cache() or not we will see two tab:
    i. 1st we will see SQL tab : So in above case it will show "InMemoryTableScan" which indicate it has  hit cache().
    ii. 2nd we will see JOB tab : So in above case it will show "PROCESS_LOCAL" which indicate it has  hit cache().
    iii. 3rd we will see STORAGE tab : So in above case it will show :
          Storage Level : Memory Deserialized 1x Replicated
          Cached Partitions : 9
          Fraction Cached : 100% percent.
          Size in Memory : 75.3 MB.
          Size in Disk : 0 MB.
c. Analyzed plan is same:
Execution plan diagram:
================================
== Parsed Logical Plan ==
Aggregate [count(1) AS count#251L]
+- Project [order_status#3]
   +- Filter (order_id#0L > cast(10 as bigint))
      +- Project [order_status#3, order_id#0L]
         +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Analyzed Logical Plan ==
count: bigint
Aggregate [count(1) AS count#251L]
+- Project [order_status#3]
   +- Filter (order_id#0L > cast(10 as bigint))
      +- Project [order_status#3, order_id#0L]
         +- Relation[order_id#0L,order_date#1,customer_id#2L,order_status#3] csv

== Optimized Logical Plan ==
Aggregate [count(1) AS count#251L]
+- Project
   +- InMemoryRelation [order_status#3, order_id#0L], StorageLevel(disk, memory, deserialized, 1 replicas)
         +- *(1) Project [order_status#3, order_id#0L]
            +- *(1) Filter (isnotnull(order_id#0L) && (order_id#0L > 10))
               +- *(1) FileScan csv [order_id#0L,order_status#3] Batched: false, Format: CSV, Location: InMemoryFileIndex[hdfs://m01.itversity.com:9000/public/trendytech/orders/orders_1gb.csv], PartitionFilters: [], PushedFilters: [IsNotNull(order_id), GreaterThan(order_id,10)], ReadSchema: struct<order_id:bigint,order_status:string>  


35. Cache and persist concept continue on df():
=================================================================
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

Versionv2.4.7MasteryarnAppNamepyspark-shell

! hadoop fs -ls /public/trendytech/orders
o/p:
=======
Found 3 items
-rw-r--r--   3 itv005857 supergroup 3749930000 2024-01-21 14:18 /public/trendytech/orders/orders.csv
-rw-r--r--   3 itv005857 supergroup 1124979000 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-28 05:02 /public/trendytech/orders/ordersparquet

! hadoop fs -head /public/trendytech/orders/orders_1gb.csv
o/p:
==========
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
8,2013-07-25 00:00:00.0,2911,PROCESSING
9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT
11,2013-07-25 00:00:00.0,918,PAYMENT_REVIEW
12,2013-07-25 00:00:00.0,1837,CLOSED
13,2013-07-25 00:00:00.0,9149,PENDING_PAYMENT
14,2013-07-25 00:00:00.0,9842,PROCESSING
15,2013-07-25 00:00:00.0,2568,COMPLETE
16,2013-07-25 00:00:00.0,7276,PENDING_PAYMENT
17,2013-07-25 00:00:00.0,2667,COMPLETE
18,2013-07-25 00:00:00.0,1205,CLOSED
19,2013-07-25 00:00:00.0,9488,PENDING_PAYMENT
20,2013-07-25 00:00:00.0,9198,PROCESSING
21,2013-07-25 00:00:00.0,2711,PENDING
22,2013-07-25 00:00:00.0,333,COMPLETE
23,2013-07-25 00:00:00.0,4367,PENDING_PAYMENT
24,2013-07-25 00:00:00.0,11441,CLOSED
25,2013-07-25 00:00:00.0,9503,CLOSED


! hadoop fs -ls -h  /public/trendytech/orders/orders_1gb.csv
o/p:
========
-rw-r--r--   3 itv005857 supergroup      1.0 G 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv

a. The above file named "orders_1gb.csv" is having size of 1.0 gb so total there will be 9 partitions  according to the  default size of 128 MB.


i. orders_df.count()
o/p:
========
25831125

a. The above code is taking 6 sec to execute beacause it is not hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see NODE_LOCAL which indicates the above code has not hit cache().
   ii. 2nd see Storage tab ->   You will see not a single partition is cached.
   iii. 3rd see SQL tab-> You will see "Scan csv" which means reading data from disk and not memory so this indicate it is not cached.

b. In above case total two stages will be created stage0 and stage1.
   i. stage0 -> In this stage total 9 executors will work and calculate local count .
   ii. stage1 -> In this stage only 1 executor will hold the final count.



ii. orders_df.distinct().count()
o/p:
========
68883


a. The above code is taking 15 sec to execute beacause it is not hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see NODE_LOCAL which indicates the above code has not hit cache().
   ii. 2nd see Storage tab ->   You will see not a single partition is cached.
   iii. 3rd see SQL tab-> You will see "Scan csv" which means reading data from disk and not memory so this indicate it is not cached.    
   
b. In above case total three stages will be created stage0,stage1 and stage2.
c. Whenever we invoke a wide transformation on higher level API than by default 200 partitions are created.
For ex:
============
9 tasks ->   200 tasks    -> Final distinct records (1 task).
            (Shuffling due to 
              distinct())
              
              


iii. cached_df = orders_df.cache()
     cached_df.count()
     o/p:
     ==========
     25831125
     
a. TThe above code is taking 20 sec to execute and it is  hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
   ii. 2nd see Storage tab ->   You will see entire 9 partition is cached.
   iii. 3rd see SQL tab-> You will see "InMemoryTableScan"  which means reading data from memory and not disk so this indicate it has hit cached. 
   

b. above case total two stages will be created stage0,stage1.



iv. cached_df.distinct().count()
    o/p:
    ===========
    68883

a. The above code is taking 2 sec to execute beacause it is  hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
   ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
   iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached.    
   
b. In above case total three stages will be created stage0,stage1 and stage2.
c. Whenever we invoke a wide transformation on higher level API than by default 200 partitions are created.
For ex:
============
9 tasks ->   200 tasks    -> Final distinct records (1 task).
            (Shuffling due to 
              distinct())
              
              
              
v. orders_df.count()
o/p:
=========
25831125


a. The above code is taking 0.2 sec to execute beacause it is  hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
   ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
   iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached. 


b. In above case total two stages will be created stage0,stage1.   











36. Cache vs Persist in case of spark managed table:
============================================================
i. In case of spark managed table data + metadata is owned by spark.
ii. Data is stored in warehouse director that is "/user/{username}/warehouse"
iii. Metadata is stored in hive metastore.
iv. So if we drop the table both data + metadata is lost.

In terms of caching:
===========================
i. Cache is a eager operation in terms of spark table to make it lazy we have to add a lazy keyword , but in case of df/rdd it is a lazy operation.
ii. We can perform uncache() on spark table but in case of df/rdd we cannot perform uncache() to perform uncache() we need to use .unpersist().

Code examples:
=======================
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

Versionv2.4.7MasteryarnAppNamepyspark-shell


! hadoop fs -ls /public/trendytech/orders
o/p:
=========
Found 3 items
-rw-r--r--   3 itv005857 supergroup 3749930000 2024-01-21 14:18 /public/trendytech/orders/orders.csv
-rw-r--r--   3 itv005857 supergroup 1124979000 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv
drwxr-xr-x   - itv005857 supergroup          0 2023-05-28 05:02 /public/trendytech/orders/ordersparquet

! hadoop fs -ls /public/trendytech/orders/orders_1gb.csv
o/p:
=========
-rw-r--r--   3 itv005857 supergroup 1124979000 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv

! hadoop fs -ls -h /public/trendytech/orders/orders_1gb.csv
o/p:
=========
-rw-r--r--   3 itv005857 supergroup      1.0 G 2023-04-29 14:10 /public/trendytech/orders/orders_1gb.csv

! hadoop fs -cat  /public/trendytech/orders/orders_1gb.csv | head
o/p:
===========
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
8,2013-07-25 00:00:00.0,2911,PROCESSING
9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT
cat: Unable to write to output stream.

orders_schema = "order_id long,order_date date,customer_id long,order_status string"

orders_df = spark.read.format("csv")\
                      .schema(orders_schema)\
                      .option("sep",",")\
                      .option("path","/public/trendytech/orders/orders_1gb.csv")\
                      .load()

orders_df.show(truncate=False)
orders_df.printSchema()
o/p:
=========
+--------+----------+-----------+---------------+
|order_id|order_date|customer_id|order_status   |
+--------+----------+-----------+---------------+
|1       |2013-07-25|11599      |CLOSED         |
|2       |2013-07-25|256        |PENDING_PAYMENT|
|3       |2013-07-25|12111      |COMPLETE       |
|4       |2013-07-25|8827       |CLOSED         |
|5       |2013-07-25|11318      |COMPLETE       |
|6       |2013-07-25|7130       |COMPLETE       |
|7       |2013-07-25|4530       |COMPLETE       |
|8       |2013-07-25|2911       |PROCESSING     |
|9       |2013-07-25|5657       |PENDING_PAYMENT|
|10      |2013-07-25|5648       |PENDING_PAYMENT|
|11      |2013-07-25|918        |PAYMENT_REVIEW |
|12      |2013-07-25|1837       |CLOSED         |
|13      |2013-07-25|9149       |PENDING_PAYMENT|
|14      |2013-07-25|9842       |PROCESSING     |
|15      |2013-07-25|2568       |COMPLETE       |
|16      |2013-07-25|7276       |PENDING_PAYMENT|
|17      |2013-07-25|2667       |COMPLETE       |
|18      |2013-07-25|1205       |CLOSED         |
|19      |2013-07-25|9488       |PENDING_PAYMENT|
|20      |2013-07-25|9198       |PROCESSING     |
+--------+----------+-----------+---------------+
only showing top 20 rows

root
 |-- order_id: long (nullable = true)
 |-- order_date: date (nullable = true)
 |-- customer_id: long (nullable = true)
 |-- order_status: string (nullable = true)
 
 
 ! hadoop fs -ls /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1
 o/p:
===========
Found 10 items
-rw-r--r--   3 itv025855 supergroup          0 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/_SUCCESS
-rw-r--r--   3 itv025855 supergroup  100316856 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00000-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316948 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00001-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316813 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00002-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100319652 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00003-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316854 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00004-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316945 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00005-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316734 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00006-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100319704 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00007-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup   38296119 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00008-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
 
 spark.sql("""
DESCRIBE EXTENDED  itv025855_cachingdemo_db_1.itv025855_orders1
""").show(truncate=False)
o/p:
=======
+----------------------------+------------------------------------------------------------------------------------------------------+-------+
|col_name                    |data_type                                                                                             |comment|
+----------------------------+------------------------------------------------------------------------------------------------------+-------+
|order_id                    |bigint                                                                                                |null   |
|order_date                  |date                                                                                                  |null   |
|customer_id                 |bigint                                                                                                |null   |
|order_status                |string                                                                                                |null   |
|                            |                                                                                                      |       |
|# Detailed Table Information|                                                                                                      |       |
|Database                    |itv025855_cachingdemo_db_1                                                                            |       |
|Table                       |itv025855_orders1                                                                                     |       |
|Owner                       |itv025855                                                                                             |       |
|Created Time                |Wed Jun 10 03:06:00 EDT 2026                                                                          |       |
|Last Access                 |Wed Dec 31 19:00:00 EST 1969                                                                          |       |
|Created By                  |Spark 2.4.7                                                                                           |       |
|Type                        |MANAGED                                                                                               |       |
|Provider                    |csv                                                                                                   |       |
|Table Properties            |[transient_lastDdlTime=1781075160]                                                                    |       |
|Statistics                  |840836625 bytes                                                                                       |       |
|Location                    |hdfs://m01.itversity.com:9000/user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1|       |
|Serde Library               |org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe                                                    |       |
|InputFormat                 |org.apache.hadoop.mapred.SequenceFileInputFormat                                                      |       |
|OutputFormat                |org.apache.hadoop.hive.ql.io.HiveSequenceFileOutputFormat                                             |       |
+----------------------------+------------------------------------------------------------------------------------------------------+-------+
only showing top 20 rows

Code1:
==============
spark.sql("""select count(*) as total_count from  itv025855_cachingdemo_db_1.itv025855_orders1""").show(truncate=False)
o/p
============
+-----------+
|total_count|
+-----------+
|25831125   |
+-----------+


a. The above code has not hit cache() so it is taking 6sec to execute, to chech that see below tab in spark UI:
   i. First see Job tab -> You will see NODE_LOCAL which indicates the above code has not hit cache().
   ii. 2nd see Storage tab ->   You will see not a single partition is cached.
   iii. 3rd see SQL tab-> You will see "Scancsv" which means reading data from  disk so this indicate it is not cached.



Code2:
===============
spark.sql("cache table itv025855_cachingdemo_db_1.itv025855_orders1")

a. The above code will hit cache() , in above case that is spark table cache() is not lazy, it is eager by default.
b. The above code took 0.2 sec beacause it is  hitting cache(), to chech that see below tab in spark UI:
   i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
   ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
   iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached.


code3: 
=================
spark.sql("select count(*) from itv025855_cachingdemo_db_1.itv025855_orders1").show(truncate=False)
o/p:
==========
+--------+
|count(1)|
+--------+
|25831125|
+--------+


a. The above code has hit cache so due to which it is taking less time to execute that is 0.2 sec.
b. To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached. 



Code 4:
===============
spark.sql("select distinct order_status from itv025855_cachingdemo_db_1.itv025855_orders1").show(truncate=False)
o/p:
==========
+---------------+
|order_status   |
+---------------+
|PENDING_PAYMENT|
|COMPLETE       |
|ON_HOLD        |
|PAYMENT_REVIEW |
|PROCESSING     |
|CLOSED         |
|SUSPECTED_FRAUD|
|PENDING        |
|CANCELED       |
+---------------+

a. This above code has hit cache so it will take less time 0.2 sec.
b. To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached. 

c. In above case as distinct is wide transformation so total there will 209 partitions.
============================================================================================
i. Intially there are 9 tasks.
ii. Than when we apply wide transformation there will be 200 partitions (tasks).
iii. There will 2 stages that is stage0 (holds 9 tasks) -> stage1 (holds 200 tasks).
                                                            (distinct())



Code 5:
==============
spark.sql("select count(distinct order_status) from itv025855_cachingdemo_db_1.itv025855_orders1").show(truncate=False)
o/p
==========
+----------------------------+
|count(DISTINCT order_status)|
+----------------------------+
|9                           |
+----------------------------+


a. The above code has hit cache so  it will take less time 1 sec.
b. To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
ii. 2nd see Storage tab ->   You will see entire 9 partitions is cached.
iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached.

c. In above case as distinct is wide transformation so total there will 210 partitions.
============================================================================================
i. Intially there are 9 tasks.
ii. Than when we apply wide transformation there will be 200 partitions (tasks).
iii. After Final count that will be 1 partition(task).
iii. There will 3 stages that is stage0 (holds 9 tasks) -> stage1 (holds 200 tasks)-> stage2 (holds 1 partition)
                                                            (distinct())               (count())
                                                            
                                                            
Code 6:
================
spark.sql("uncache table itv025855_cachingdemo_db_1.itv025855_orders1")
spark.sql("select count(distinct order_status) from itv025855_cachingdemo_db_1.itv025855_orders1").show(truncate=False)
o/p:
===========
+----------------------------+
|count(DISTINCT order_status)|
+----------------------------+
|9                           |
+----------------------------+


a. The above 1st code will uncache spark managed table .
b. The above 2nd code will not hit cache and it will take 4sec to execute.
b. To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see NODE_LOCAL which indicates the above code has NOT hit cache().
ii. 2nd see Storage tab ->   You will see not a single partition is cached.
iii. 3rd see SQL tab-> You will see "CSV scan" which means reading data from  disk so this indicate it is not cached. 

c. In above case as distinct is wide transformation so total there will 210 partitions.
============================================================================================
i. Intially there are 9 tasks.
ii. Than when we apply wide transformation there will be 200 partitions (tasks).
iii. After Final count that will be 1 partition(task).
iii. There will 3 stages that is stage0 (holds 9 tasks) -> stage1 (holds 200 tasks)-> stage2 (holds 1 partition)
                                                            (distinct())               (count())
                                                            
                                                            
Code 7:
==============
spark.sql("cache lazy table itv025855_cachingdemo_db_1.itv025855_orders1")
spark.sql("select count(distinct order_status) from itv025855_cachingdemo_db_1.itv025855_orders1").show(truncate=False)
o/p:
==========
+----------------------------+
|count(DISTINCT order_status)|
+----------------------------+
|9                           |
+----------------------------+


a. The above 1st  code will make the cache lazy in spark table by default cache is eager in spark table.
b. The above 2nd code will hit cache and it will take 11sec to execute because first cache is lazy so when we call action on that in below code it is taking time to cache that 
and than it is calculating the result.
 To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
ii. 2nd see Storage tab ->   You will see entire 9  partition is cached.
iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached. 

c. In above case as distinct is wide transformation so total there will 210 partitions.
============================================================================================
i. Intially there are 9 tasks.
ii. Than when we apply wide transformation there will be 200 partitions (tasks).
iii. After Final count that will be 1 partition(task).
iii. There will 3 stages that is stage0 (holds 9 tasks) -> stage1 (holds 200 tasks)-> stage2 (holds 1 partition)
                                                            (distinct())               (count())
                                                            
                                                            
! hadoop fs -ls /user/itv025855/warehouse
o/p:
=========
Found 2 items
drwxr-xr-x   - itv025855 supergroup          0 2026-06-10 02:57 /user/itv025855/warehouse/itv025855_cachingdemo_db.db
drwxr-xr-x   - itv025855 supergroup          0 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db


! hadoop fs -ls /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db
o/p:
===========
Found 1 items
drwxr-xr-x   - itv025855 supergroup          0 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1


! hadoop fs -ls /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1
o/p:
========
Found 10 items
-rw-r--r--   3 itv025855 supergroup          0 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/_SUCCESS
-rw-r--r--   3 itv025855 supergroup  100316856 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00000-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316948 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00001-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316813 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00002-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100319652 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00003-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316854 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00004-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316945 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00005-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100316734 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00006-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup  100319704 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00007-104047f5-b655-4c8a-b794-764e291ff298-c000.csv
-rw-r--r--   3 itv025855 supergroup   38296119 2026-06-10 03:05 /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1/part-00008-104047f5-b655-4c8a-b794-764e291ff298-c000.csv

! hadoop fs -du -h /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db
o/p:
=========
801.9 M  2.3 G  /user/itv025855/warehouse/itv025855_cachingdemo_db_1.db/itv025855_orders1



Impt point to remember :
===============================
i. There are 9 files so total there will 9 partitions will be have less than 128 MB data that is 95.7 MB data so thats where we get more partitions 
   though we have 801.9 MB file size.
   


Code 8:
=============
spark.sql("""select order_status,count(*) as total_count 
             from itv025855_cachingdemo_db_1.itv025855_orders1
             group by order_status
             """).show(truncate=False)
o/p:
===============
+---------------+-----------+
|order_status   |total_count|
+---------------+-----------+
|PENDING_PAYMENT|5636250    |
|COMPLETE       |8587125    |
|ON_HOLD        |1424250    |
|PAYMENT_REVIEW |273375     |
|PROCESSING     |3103125    |
|CLOSED         |2833500    |
|SUSPECTED_FRAUD|584250     |
|PENDING        |2853750    |
|CANCELED       |535500     |
+---------------+-----------+

a. The baove code has hit cache and the code took 75 ms .
 To check cache() see below tab:
==================================================   
i. First see Job tab -> You will see PROCESS_LOCAL which indicates the above code has  hit cache().
ii. 2nd see Storage tab ->   You will see entire 9  partition is cached.
iii. 3rd see SQL tab-> You will see "InMemoryTableScan" which means reading data from  memory so this indicate it is  cached. 









                                                                           
                                             
                                                                          
                                                     

   
      










    
