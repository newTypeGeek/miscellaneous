from pprint import pprint

import numpy as np
import pandas as pd

from consec_nan import get_consecutive_nan

if __name__ == '__main__':

    data = [np.nan, np.nan, np.nan,
            1, 2, 3, 4, 5, 6, 7, 8,
            np.nan, np.nan, -1, -2,
            9, np.nan, 10, np.nan, np.nan
            ]

    index = pd.period_range(start="2019-03-01", periods=len(data), freq="1T").to_timestamp()

    time_series = pd.Series(data=data, index=index)
    result_nan = get_consecutive_nan(time_series)

    print("----- Input Time Series -----")
    print(time_series)

    print("\n----- Results -----")

    pprint(result_nan)