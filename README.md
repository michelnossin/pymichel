# PyMichel

Basic PySpark project including test and Egg library
No local Spark is required as we will use Spark.
The used Docker image uses Spark 2.2, and Python 3.4

# Build and run docker image (from your own pc)
docker build --no-cache  -t pymichel  -f docker/dockerfile_pymichel /home/michel/git/pymichel

# Optional step below: if you want to develop on your docker environment

## For all next steps log in Docker first:
docker run --rm -it -p 8080:8080 -v /home/michel/git/pymichel:/tmp/pymichel spark /bin/bash

## Create the library
cd /tmp/pymichel
python setup.py bdist_egg

## Test Spark on Docker (in our case dylanmei/zeppelin image) 
/usr/spark-2.2.0/bin/spark-submit --master local[8] /usr/spark-2.2.0/bin/examples/src/main/python/pi.py

## Test the egg file manually
/usr/spark-2.2.0/bin/pyspark --py-files /tmp/pymichel/dist/pymichel-0.0.1-py3.4.egg
<execute any step>

## Submit job
```
/usr/spark-2.2.0/bin/spark-submit --py-files /tmp/pymichel/dist/pymichel-0.0.1-py3.4.egg /tmp/pymichel/main/main.py
Or
chmod 700 /tmp/pymichel/docker/deploy-spark-job.sh
. /tmp/pymichel/docker/deploy-spark-job.sh
```
