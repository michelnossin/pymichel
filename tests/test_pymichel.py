import pytest

from pymichel.spark import get_spark
from pymichel.app import winner_or_loser

class TestPyMichel(object):

    def test_winner_or_loser(self):
        source_data = [
            ("michel", 1),
            ("piet", 2)
        ]
        source_df = get_spark().createDataFrame(
            source_data,
            ["name", "salary"]
        )

        actual_df = winner_or_loser(source_df)

        expected_data = [
            ("michel", 1, "winner"),
            ("piet", 2, "loser")
        ]
        expected_df = get_spark().createDataFrame(
            expected_data,
            ["name", "salary", "winner_or_loser"]
        )
        actual_df.show()

        assert(expected_df.collect() == actual_df.collect())
