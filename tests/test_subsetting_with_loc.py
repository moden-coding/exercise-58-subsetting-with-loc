#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd

from src.subsetting_with_loc import subsetting_with_loc


class TestSubsettingWithLoc(unittest.TestCase):

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

    def test_returns_a_dataframe(self):
        df = subsetting_with_loc()
        self.assertIsInstance(
            df,
            pd.DataFrame,
            msg="subsetting_with_loc() must return a pandas DataFrame, not "
            "%r." % (type(df),),
        )


if __name__ == "__main__":
    unittest.main()
