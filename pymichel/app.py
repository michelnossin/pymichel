import pyspark.sql.functions as F

def winner_or_loser(df):
    return df.withColumn("winner_or_loser",
                         (F.when(F.col("name") == 'michel', 'winner')
                          .otherwise('loser'))

    )

