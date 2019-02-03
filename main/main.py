
from pymichel.spark import get_spark
from pymichel.app import winner_or_loser

if __name__ == "__main__":
    """
        Usage: pymichel
    """
    source_data = [
            ("michel", 1),
            ("piet", 2)
        ]
    source_df = get_spark().createDataFrame(
            source_data,
            ["name", "salary"]
        )

    actual_df = winner_or_loser(source_df)

    actual_df.show()
