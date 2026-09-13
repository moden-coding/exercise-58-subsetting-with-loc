#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd

from src.subsetting_with_loc import subsetting_with_loc


class TestSubsettingWithLoc(unittest.TestCase):

    def test_returns_a_dataframe(self):
        df = subsetting_with_loc()
        self.assertIsInstance(
            df,
            pd.DataFrame,
            msg="subsetting_with_loc() must return a pandas DataFrame, not "
            "%r." % (type(df),),
        )

    def test_shape(self):
        df = subsetting_with_loc()
        self.assertEqual(
            df.shape,
            (311, 3),
            msg="subsetting_with_loc() should return a DataFrame with shape "
            "(311, 3): 311 municipalities and the 3 selected columns. Got "
            "%r." % (df.shape,),
        )

    def test_columns_and_indices(self):
        df = subsetting_with_loc()
        np.testing.assert_array_equal(
            df.columns,
            [
                "Population",
                "Share of Swedish-speakers of the population, %",
                "Share of foreign citizens of the population, %",
            ],
            err_msg="The DataFrame's columns should be exactly "
            "['Population', 'Share of Swedish-speakers of the population, "
            "%%', 'Share of foreign citizens of the population, %%'] in "
            "that order. Got %r." % (list(df.columns),),
        )
        self.assertEqual(
            df.index[0],
            "Akaa",
            msg="The first row's index should be 'Akaa'. Got %r." % (
                df.index[0],
            ),
        )
        self.assertEqual(
            df.index[-1],
            "Äänekoski",
            msg="The last row's index should be 'Äänekoski'. Got "
            "%r." % (df.index[-1],),
        )

    def test_aggregate_rows_excluded(self):
        df = subsetting_with_loc()
        self.assertNotIn(
            "WHOLE COUNTRY",
            df.index,
            msg="'WHOLE COUNTRY' is a nationwide aggregate row that comes "
            "before 'Akaa' in the file - it should not be part of the "
            "'Akaa' to 'Äänekoski' selection.",
        )
        self.assertNotIn(
            "Äänekoski sub-regional unit",
            df.index,
            msg="'Äänekoski sub-regional unit' is a region-level aggregate "
            "row that comes after the municipality 'Äänekoski' in the "
            "file - the selection should stop at the municipality itself.",
        )

    def test_akaa_row_values(self):
        df = subsetting_with_loc()
        row = df.loc["Akaa"]
        self.assertEqual(
            row["Population"],
            16769,
            msg="Akaa's Population should be 16769. Got %r." % (
                row["Population"],
            ),
        )
        self.assertAlmostEqual(
            row["Share of Swedish-speakers of the population, %"],
            0.2,
            msg="Akaa's share of Swedish-speakers should be 0.2%%. Got "
            "%r." % (row["Share of Swedish-speakers of the population, %"],),
        )
        self.assertAlmostEqual(
            row["Share of foreign citizens of the population, %"],
            1.6,
            msg="Akaa's share of foreign citizens should be 1.6%%. Got "
            "%r." % (row["Share of foreign citizens of the population, %"],),
        )

    def test_aanekoski_row_values(self):
        df = subsetting_with_loc()
        row = df.loc["Äänekoski"]
        self.assertEqual(
            row["Population"],
            19144,
            msg="Äänekoski's Population should be 19144. Got %r." % (
                row["Population"],
            ),
        )
        self.assertAlmostEqual(
            row["Share of Swedish-speakers of the population, %"],
            0.1,
            msg="Äänekoski's share of Swedish-speakers should be 0.1%%. "
            "Got %r."
            % (row["Share of Swedish-speakers of the population, %"],),
        )
        self.assertAlmostEqual(
            row["Share of foreign citizens of the population, %"],
            1.2,
            msg="Äänekoski's share of foreign citizens should be 1.2%%. "
            "Got %r."
            % (row["Share of foreign citizens of the population, %"],),
        )


if __name__ == "__main__":
    unittest.main()
