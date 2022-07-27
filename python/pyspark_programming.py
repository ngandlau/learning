from pyspark.sql import SparkSession

data = [
    ('nils', 23, None),
    ('hans', None, None),
    ('sira', None, 'female')
]
columns = ['name', 'age', 'gender']

spark = SparkSession.builder.master('local').getOrCreate()
df = spark.createDataFrame(data=data, schema=columns)

# None Filter
df.filter("age is NULL and gender is NULL").show()
df.filter("age is NULL and gender is not NULL").show()
df.filter("NOT age is NULL").show()
df.filter("age is NULL or age == 23").show()

# Equal filters
df.filter("name == 'nils'").show()
df.filter("name == 'nils' or name == 'sira'").show()
df.filter("name <> 'nils'").show()

spark.stop()