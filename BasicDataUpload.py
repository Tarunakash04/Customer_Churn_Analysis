# Import necessary libraries
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("CSV Import").getOrCreate()

# Load the CSV file
df = spark.read.csv(r"path_to_your_file.csv", header=True, inferSchema=True)

# Show the first few rows
df.show()
