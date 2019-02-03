import pytest

from pymichel import spark
from pymichel import app

class TestPyMichel(object):

    def test_winner_or_loser(self):
        source_data = [
            ("michel", 1),
            ("piet", 2)
        ]
        spark_session = spark.get_spark()
        source_df = spark_session.createDataFrame(
            source_data,
            ["name", "salary"]
        )

        actual_df = app.winner_or_loser(source_df)

        expected_data = [
            ("michel", 1, "winner"),
            ("piet", 2, "loser")
        ]
        expected_df = spark_session.createDataFrame(
            expected_data,
            ["name", "salary", "winner_or_loser"]
        )
        actual_df.show()

        assert(expected_df.collect() == actual_df.collect())

