# -*- coding: utf-8 -*-
import os
import pandas as pd
import string
import numpy as np


def load_raw_data(path: string) -> pd.DataFrame:
    """
    Load csv data using pandas and return a dataframe
    """

    df = pd.read_csv(path, sep=",", decimal=".", index_col='Data',
                     parse_dates=['Data'])

    return df


# --------------------------------------------
# Load data
path = r"/Users/<your_user>/xxx/xxx/data/"
final_path = os.path.join(path, "xxxx.csv")

df_raw = load_raw_data(path=final_path)
df_raw = df_raw.sort_index()
