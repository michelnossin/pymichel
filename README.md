# PyMichel

Basic PySpark project including test and Egg library

# Create the library (python v3)
python setup.py bdist_egg

# For all next steps log in Docker first:
docker run --rm -it -p 8080:8080 -v /home/michel/git/pymichel:/tmp/pymichel spark /bin/bash

# Test Spark on Docker (in our case dylanmei/zeppelin image) 
/usr/spark-2.2.0/bin/spark-submit --master local[8] /usr/spark-2.2.0/bin/examples/src/main/python/pi.py

# Test the egg file manually
/usr/spark-2.2.0/bin/pyspark --py-files /tmp/pymichel/dist/pymichel-0.0.1-py3.7.egg
<execute any step>

# Submit job
/usr/spark-2.2.0/bin/spark-submit --py-files /tmp/pymichel/dist/pymichel-0.0.1-py3.7.egg /tmp/pymichel/main/main.py
Or
chmod 700 /tmp/pymichel/docker/deploy-spark-job.sh
. /tmp/pymichel/docker/deploy-spark-job.sh

# Deploy via docker
Not tested yet: 
docker build  -t pymichel  -f /home/michel/git/pymichel/docker/dockerfile_pymichel /home/michel/git/pymichel/
