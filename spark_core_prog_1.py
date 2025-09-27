print("We are learning spark core programming")
#parts (2,3,4 of this learning is not much important in our realtime environment now a days
#parts (1 and 5) is very very important
#1. How to create spark session object (leveraging all possible features/options) -Imporant (core/sql/streaming)
#2. How to create and manage (partitioning & Caching/persisting) RDDs (foreground)
#3. How to transform RDDs
#4. How to produce/store the result of the RDDs (transformed) into console/storage layers by performing some actions
#5. Spark Arch/terminologies, Performance Optimization, Job Submission, Spark Cluster concept (VV Important) - not used only for core, used in SQL & Streaming also

#def main(args): - Lets consider we are writing the further lines of code inside main method

print("IMPORTANT - 1. How to create spark session object (leveraging all possible features/options) -Imporant")
#How to create spark session object (leveraging all possible features) -Imporant
#Spark session object is the entry point for accessing the spark cluster
#lets learn in detail about the spark session object creation
from pyspark.sql.session import SparkSession
#builder is a factory pattern which is responsible for instantiating the sparksession class with more options like additional config, appname,
# master(local[2]), enableHiveSupport().. getOrCreate()
#getOrCreate() - Get an existing spark session object or create a new object if the spark session object is stopped/closed or not present
spark=SparkSession.builder.master("local[2]").appName("WD32_Spark_Core_App").enableHiveSupport().getOrCreate()
print(spark)
rdd1=spark.sparkContext.parallelize(range(1,100))
print(rdd1.getNumPartitions())
#spark.stop()
spark1=SparkSession.builder.master("local[4]").appName("WE43_Spark_Core_App").enableHiveSupport().getOrCreate()
print(spark1)

#To write spark core program follow all these.....
#a. import required libraries
from pyspark.sql.session import SparkSession

#b. Create spark session object (internally it will create spark context (sc), sqlContext/hiveContext)
spark1=SparkSession.builder.master("local[*]").appName("WE43_Spark_Core_App").enableHiveSupport().getOrCreate()

#c. Define the sparkcontext for writing rdd programs in the below way..
sc=spark1.sparkContext#define sc which is like an alias/renamed spark.sparkContext object

#d. Show only the error, dont display information or warning
sc.setLogLevel("ERROR")

#e. Start write the lines of code
rdd1=sc.parallelize(range(1,100))
print(rdd1.collect())
print(rdd1.getNumPartitions())

###############################################################################################
print("Not IMPORTANT - 2. How to create and manage RDDs (not important)")
#Not IMPORTANT - 2. How to create and manage RDDs (not important)
#What are the possible ways of Createing RDDs
#RDD -
# Resilient (Rebuild (fault tolerance) in case if the data in the memory is lost using the concept of lineage in DAG)
# Distributed (across multiple memory of different computers using concept of partitions)
# Dataset (using files/sources/programaticaly/other rdd/memory)
#1. RDDs can be created from some sources (FS/DB/any other sources)
#2. RDDs can be created from another RDD
#3. RDDs can be created from memory
#4. RDDs can be created programatically

#1. RDDs can be created from some sources (FS/DB/any other sources) - If we need to create resilient distributed dataset in memory for computation
file_rdd=sc.textFile("file:///home/hduser/hive/data/txns")
hadoop_rdd=sc.textFile("hdfs://127.0.0.1:54310/user/hduser/txns")
print(file_rdd.take(5))
#print(hadoop_rdd.take(5))

#2. RDDs can be created from another RDD (refreshed memory) (because the given RDD is IMMUTABLE)
#map_rdd created from file_rdd
map_rdd=file_rdd.map(lambda row:row.split(","))#Convert every row (string) of the data present in the file_rdd to list(values) - Higher Order Function
print(map_rdd.take(5))
#or
split_func=lambda row:row.split(",")
map_rdd=file_rdd.map(split_func)#Convert every row (string) of the data present in the file_rdd to list(values) - Higher Order Function
print(map_rdd.take(5))
#or
def split_met(row):
    return row.split(",")
map_rdd=file_rdd.map(split_met)#Convert every row (string) of the data present in the file_rdd to list(values) - Higher Order Function
print(map_rdd.take(5))

#3. RDDs can be created from memory (retained)
#Find the total sales happened?
#Lazy Transformations happens in the below lines
file_rdd=sc.textFile("file:///home/hduser/hive/data/txns")#Rdd created from file/disk/sources
map_rdd=file_rdd.map(lambda row:row.split(","))#RDD created from another RDD
map_rdd.cache()#Garbage collector pls don't clean the data from map_rdd, pls allow me to retain for later usage
#Action happens from the below line
print(map_rdd.count())
amt_rdd=map_rdd.map(lambda split_row:float(split_row[3]))#RDD can created from memory
print(amt_rdd.take(3))
city_rdd=map_rdd.map(lambda split_row:split_row[7])#RDD can created from memory
print(city_rdd.take(3))
print("Total sales is ",amt_rdd.sum())

#4. RDDs can be created programatically (learning & analysis) using the parallelize function
#RDDs are resilient distributed dataset
lst=list(range(1,101))
even_lst=[]
for i in lst:#map will run for loop
    if i%2==0:
        even_lst.append(i)
print(even_lst)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
rdd_lst=sc.parallelize(lst)
filter_even_rdd=rdd_lst.filter(lambda i:i%2==0)#Filter (select + where clause in sql) is a transformation that act like a map (for loop) to iterate on every element
# and apply any condition like a (if condition)
filter_even_rdd.collect()

#Use parallelize or programatic rdd creation to understand the datascruture and rdd transformations and actions concept easily..
lst1=["1,irfan,42","2,bala,35"]
for i in lst1:
    print(i.split(","))

print(sc.parallelize(lst1).glom().collect())
print(sc.parallelize(lst1).map(lambda x:x.split(",")).collect())
print(sc.parallelize(lst1).map(lambda x:x.split(",")[0]).collect())

print("3. How to Transform/process RDDs - Not much important")
#Interview Question: How to identify the given function is a transformation or an action?
#Ans: function return another RDD is a transformation, function return result/value is action
#some of the Transformation (function that returns another RDD) functions asked in interviews (rarely) -> map, filter, flatmap, reduceByKey, zipWithIndex, mappartition, join etc.,
#Interview Question: Transformation are of 2 categories -
# 1. Passive - If the output elements is equal to the input elements of an RDD
# 2. Active transformation - If the output elements is NOT equal to the input elements of an RDD
#How to do you identify a given function is a transformation or action?
#In python A variable can hold values or programs(object) or functions(anonymous/lambda function) or data object (rdd)
lines_rdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt")#rdd returned (lazily) of type list[string]
#map method (select statement) - Passive transformation
map_rdd=lines_rdd.map(lambda row_str:row_str.split(','))
formatted_rdd=map_rdd.map(lambda row_str_cols:(row_str_cols[0],row_str_cols[1],int(row_str_cols[2]),row_str_cols[3],float(row_str_cols[4])))
amt_rdd=formatted_rdd.map(lambda x:x[4])#no. of columns returned is 5th column
sum_of_amt=amt_rdd.sum()#Minimum one Action is must needed for every spark application

#Filter (select and where)- Active transformation
filter_rdd=map_rdd.filter(lambda x:x[1]=='chennai')#no. of columns returned is all
filter_rdd.collect()

city_rdd=map_rdd.map(lambda x:x[1]).filter(lambda x:x=='chennai')#better?yes (secondarily) projection pushdown
print("filter1 output")
print(city_rdd.collect())
city_rdd=map_rdd.filter(lambda x:x[1]=='chennai').map(lambda x:x[1])#better?yes (primarily) - predicate pushdown
print("filter2 output")

#flatMap -#flatmap is a higher order function that iterate on each row of the given dataset of an rdd as like a map transformation
#used to convert unstructured text data into structured data
# It will work like a nested for loop or it will work like select with explode function
# and then it will flatten the row further down into elements
#'hi team goodmorning','lets learn spark' -> map(lambda x:x.split(' ')) -> [[hi,team,goodmorning],[lets,learn,spark]]
#'hi team goodmorning','lets learn spark' -> flatMap(lambda x:x.split(' ')) -> [[hi,team,goodmorning],[lets,learn,spark]] -> [hi,team,goodmorning,lets,learn,spark]

#Interview Question: Difference between map and flatMap?
#Map will iterate at the row level in a given dataset of multiple rows
#flatMap will iterate at the row level (map) in a given dataset of multiple rows, then flatten at the every element of the row
for i in ['hi team goodmorning', 'lets learn spark']:
 for j in i.split(" "):
  print(j.upper())

#Interview Question: When do we use flatmap in realtime? Whether you know spark core programming? Yes
# Can you write word count program using spark core?
# Can you let me know the total occurance of the given keyword in an unstructured data?
#how many people shown interest in learning spark
'''
hadoop spark hadoop spark kafka datascience
spark hadoop spark datascience
informatica java aws gcp
gcp aws azure spark
gcp pyspark hadoop hadoop
'''
sc.textFile("file:///home/hduser/mrdata/courses.log").flatMap(lambda x:x.split(" ")).filter(lambda x:x=='spark').count()

#zip, zipWithIndex - HOF that returns the zipped result of two rdds contains (same number of partition elements)
emp_basic_rdd = sc.textFile("file:/home/hduser/sparkdata/empbasicinfo.txt").map(lambda x:x.split(","))
emp_addon_rdd = sc.textFile("file:/home/hduser/sparkdata/empaddoninfoId.txt").map(lambda x:x.split(","))
#zip (joins rdds horizontally without any join conditions)-> Zips this RDD with another one, returning key-value pairs with the first element in each RDD second element in each RDD, etc. Assumes
# rules: The two RDDs have the same number of partitions and the same number of elements in each partition
print(emp_basic_rdd.zip(emp_addon_rdd).collect())

emp_basic_rdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt").map(lambda x:x.split(","))
emp_addon_rdd = sc.textFile("file:/home/hduser/sparkdata/empaddoninfo.txt").map(lambda x:x.split(","))
print(emp_basic_rdd.zip(emp_addon_rdd).map(lambda x:[x[0][0],x[0][1],x[0][2],x[1][0]]).collect())

#Zipwithindex - HOF returns the rdd output adding index value for every element of the given rdd
#Realtime usage of zipwithindex
#Interview question: How to do you remove the header from a given dataset?
emprdd = sc.textFile("file:/home/hduser/sparkdata/empdata_header.txt")
print('zipwithindexed original data',emprdd.zipWithIndex().collect())
print('zipwithindexed original data',emprdd.zipWithIndex().filter(lambda x:x[1]>0).collect())

header=emprdd.first()
print('using first action to filter header data',emprdd.filter(lambda x:x!=header).collect())

#union, subtract, intersection, distinct (set functions)
#union (merge rdds vertically without any join conditions) - For detail description refer /usr/local/spark/python/pyspark/rdd.py
# rules:
# Not a strict rule, but we have to ensure to apply this rule programatically
# All set operators will say - number of columns, datatype should be same between the 2 datasets going to be operated
#Union will return duplicates
#rdd1-1,a,10
#rdd2-2,b,20
#rdd3-rdd1+rdd2

emprdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt")
emprdd1 = sc.textFile("file:/home/hduser/sparkdata/empdata1.txt")
print(emprdd.count())
print(emprdd1.count())

#union includes duplicate also
union_rdd=emprdd.union(emprdd1) #union (will retain duplicates) in spark core is union all in sql databases
print(union_rdd.collect())
print(union_rdd.count())

#union will not place a strict rules of same number of columns and datatype in both rdds
emprdd2 = sc.textFile("file:/home/hduser/sparkdata/empdata2.txt")#4 columns data
union_rdd=emprdd.union(emprdd2) #will this work? it works because we are unioning list(str)+list(str)
print(union_rdd.collect())

#union will not place a strict rules of same number of columns and datatype in both rdds, but we have to apply the rules programatically by
#converting the given rdd into tuples
#Data strandardization
emprdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt").map(lambda x:x.split(",")).map(lambda x:(x[0],x[1],int(x[2]),x[3],x[4]))
emprdd2 = sc.textFile("file:/home/hduser/sparkdata/empdata2.txt").map(lambda x:x.split(",")).map(lambda x:(x[0],'Unknown',int(x[1]),x[2],x[3]))
union_rdd=emprdd.union(emprdd2)
print(union_rdd.collect())
print(union_rdd.map(lambda x:x[1]).collect())

emprdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt")
emprdd1 = sc.textFile("file:/home/hduser/sparkdata/empdata1.txt")
intersect_rdd=emprdd.intersection(emprdd1)#intersection shows only the common data between the given rdds
#Show me the employees working in both regions?
print(intersect_rdd.collect())

subtract_rdd=emprdd.subtract(emprdd1)#subtract shows difference between rdd1 minus rdd2 or vice versa
print(subtract_rdd.collect())

#I want to deduplicate the duplicate data in the given RDD or I wanted to implement union (deduplicated) rather than union all?
union_rdd=emprdd.union(emprdd1)
print(union_rdd.collect())#union all
print(union_rdd.distinct().collect())#union (de duplicated)

#reduce (action)
#Calculate the sum of salary of the given employees working in chennai? select sum(sal) from table where city='chennai';
#lets write a map reduce program to achieve this
#map(collect, filter, convert) -> shuffle (data copy from mapper to reducer containers) -> reducer (merge, sort, group, aggregate) consolidation
emprdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt").map(lambda x:x.split(",")).filter(lambda x:x[1]=='chennai').map(lambda x:(int(x[4])))
#collect, conversion and filter
sum_fun=lambda brain_accumulator,finger_increment:brain_accumulator+finger_increment#school days mind and finger game
#[100000, 10000, 100000]
reducer=emprdd.reduce(sum_fun)

#python way of doing reduction
from functools import reduce
reduce(lambda x,y:x+y,[100000, 10000, 100000])

#paired RDD - If we can perform operations on the rdd data if it is in a key,value pair format, then it is a paired rdd
#select city,sum(sal) from table group by city;
#reduceByKey (paired RDD functions) - Important transformation as like map, filter, flatmap
#Calculate the city wise sum of salary of the given employees? chennai,210000, hyd,115000
emp_paired_rdd = sc.textFile("file:/home/hduser/sparkdata/empdata.txt").map(lambda x:x.split(","))\
    .map(lambda x:(x[1],int(x[4])))
reducer_by_key=emp_paired_rdd.reduceByKey(sum_fun)

#Can you write word count program using spark core? we can achieve using reduceByKey function
'''
hadoop spark hadoop spark kafka datascience
spark hadoop spark datascience
informatica java aws gcp
gcp aws azure spark
gcp pyspark hadoop hadoop
'''
#import libraries
#spark session #1. Spark session object creation
unstructured_rdd=sc.textFile("file:///home/hduser/mrdata/courses.log")#2. RDD Creation
structured_rdd=unstructured_rdd.flatMap(lambda x:x.split(" "))#3. Transformation
paired_rdd=structured_rdd.map(lambda course:(course,1))#3. Transformation
reduced_by_key_rdd=paired_rdd.reduceByKey(lambda x,y:x+y)#3. Transformation
print(reduced_by_key_rdd.collect())#4. Action

#join transformation (paired RDD functions) - joins are Not suggested literally using rdd functions
emp_paired_rdd = sc.textFile("file:/home/hduser/sparkdata/empdata_id.txt").map(lambda x:x.split(",")).map(lambda x:(int(x[6]),(int(x[0]),x[1],x[2])))
dept_paired_rdd = sc.textFile("file:/home/hduser/sparkdata/dept_id.txt").map(lambda x:x.split(",")).map(lambda x:(int(x[0]),x[1]))
print(emp_paired_rdd.join(dept_paired_rdd).collect())
print(emp_paired_rdd.leftOuterJoin(dept_paired_rdd).collect())

#Vignesh
#One basic doubt Irfan, In dataframe spark, the transformations will happen logical table view and physical rdd (background) -> sql (logical table)-> rdd trans -> rdd data
# and in RDD the transformations will happen on the physical rdd directly -> rdd trans -> rdd data

print("4. How to Materialize/Actions RDDs - Not much important")
#some of the Actions (function that returns the result) functions asked in interviews (rarely) -> map, filter, flatmap, reduceByKey, zipWithIndex, mappartition, join etc.,

#Spark core application to perform word count operation
#import libraries
from pyspark.sql.session import *
#spark session #1. Spark session object creation
spark=SparkSession.builder.getOrCreate()
sc=spark.sparkContext
#sc.setLogLevel("INFO")
unstructured_rdd=sc.textFile("file:///home/hduser/mrdata/courses.log")#2. RDD Creation
structured_rdd=unstructured_rdd.flatMap(lambda x:x.split(" "))#3. Transformation
print(structured_rdd.collect())
paired_rdd=structured_rdd.map(lambda course:(course,1))#3. Transformation
print(paired_rdd.collect())#4. Action1 -> entire lineage executed (line# 8 to 10 will be executed)
reduced_by_key_rdd=paired_rdd.reduceByKey(lambda x,y:x+y)#3. Transformation

print(reduced_by_key_rdd.collect())#4. Action2 -> entire lineage executed (line# 8 to 12 will be executed)
#collect action - Collect from different executor (container) memory and return all items to the driver memory
#Interview Question: Is it good to use collect in a spark core application? No
# collect is a top costly action, hence it should be causiously used for dev purpose or avoided using in an application until it is inevitable
#This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory

print(reduced_by_key_rdd.count())#4. Action1 -> entire lineage executed (line# 8 to 12 will be executed)
#count action is preferred than collect
#count action - Count number of elements in the rdd partition from different executor (container) memory and return the total count to the driver memory
#Will not happen like this....>  collect all the data from the executors and Count number of elements in the driver memory

#quick usecase to understand all 4 parts of spark core?
#Develop a spark core application to identify the total number of errors and warnings (column 2) available in the hadoop-hduser-namenode-localhost.localdomain.log file
#/usr/local/hadoop/logs
from pyspark.sql import *
spark=SparkSession.builder.getOrCreate()
sc=spark.sparkContext
rdd=sc.textFile("/user/hduser/dir1/*")
split_rdd=rdd.map(lambda x:x.split(" "))
#Interview Question: If I give a data file with variable number of columns and you are supposed to consider 4 columns only, how do you handle it?
#answer: After splitting, i will filter the data contains less than 4 columns, then will go with further transformation or action
split_rdd_filtered_min3_cols=split_rdd.filter(lambda x:len(x)>2)
print("Total log entries in the given log file=",rdd.count())
err_rdd=split_rdd_filtered_min3_cols.filter(lambda x:x[2]=='ERROR')
print("Total error log entries in the given log file=",err_rdd.count())
warn_rdd=split_rdd_filtered_min3_cols.filter(lambda x:x[2]=='WARN')
print("Total warning log entries in the given log file=",warn_rdd.count())

print("running take,first, top, sample, countbyvalue,countbykey etc.,")
#Data sampling actions (preferred rather than using collect)
print(err_rdd.take(3))
print(err_rdd.first())
print(err_rdd.top(3))
print("running sample, countbyvalue,countbykey etc.,")
#Random sampling
err_rdd.sample(True,.2).collect()#collect only 20% of overall data
reduced_by_key_rdd.sample(True,.3)
err_rdd.sample(True,.3,2)#param1:replace if duplicate output produced, param2: percent fraction of overall volume, param3: seed value to change the sample output
reduced_by_key_rdd.sample(True,.3,4)

#countByValue action is used to do a count of the given value by itself produced as key value pair output (dictionary)
#reduced_by_key_rdd.countByValue()
print(split_rdd_filtered_min3_cols.map(lambda x:x[2]).countByValue())
#Try implement countByValue for the wordcount program? [hadoop,spark,hadoop] -> hadoop->2,spark->1

print("running sample, countbyvalue,countbykey etc.,")
reduced_by_key_rdd.countByKey()
print(split_rdd_filtered_min3_cols.map(lambda x:(x[2],'dummy value')).countByKey())

#reduce() action help us reduce the result in any way we needed
fun1=lambda x,y:x+y
fun2=lambda x,y:x if x>y else y
fun3=lambda x,y:x*y
fun4=lambda x,y:x-y
sal_lst=[10000,20000,15000,30000,40000]
sal_rdd1=sc.parallelize(sal_lst)
amt_lst_rdd1=sc.textFile("file:///home/hduser/hive/data/txns").map(lambda x:float(x.split(",")[3]))
reduced_result=amt_lst_rdd1.reduce(fun1)
print("total sales happened",reduced_result)
reduced_result=amt_lst_rdd1.reduce(fun2)
print("max amount transacted",reduced_result)
reduced_result=amt_lst_rdd1.reduce(fun3)
print("multiplication of all amt",reduced_result)
reduced_result=amt_lst_rdd1.reduce(fun4)
print("subraction of all amount",reduced_result)

'''reduced_by_key_rdd.reduce()
reduced_by_key_rdd.sum()
reduced_by_key_rdd.max()
reduced_by_key_rdd.min()'''
reduced_by_key_rdd.saveAsTextFile("hdfs:///user/hduser/sparkappdata")
print("last line of the spark application")

#Can you write word count program in spark core?

#Important - 5. Spark Arch/terminologies, Performance Optimization, Job Submission, Spark Cluster concept (VV Important) - not used only for core, used in SQL & Streaming also
print("5. Spark Arch/terminologies, Performance Optimization, Job Submission, Spark Cluster concept (VV Important) - not used only for core, used in SQL & Streaming also")
#Performance Optimization - primary activity
#Remove all unwanted (costly) actions performed while doing the development like collect & print/take/count...


#Interview Question: How to do count the number of elements at the partition level