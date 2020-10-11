import pandas as pd
from typing import List, Dict, Union


def get_consecutive_nan(ts: pd.Series) -> List[Dict[str, Union[pd.Timestamp, pd.Timedelta]]]:
    """
    Get the consecutive NaN timestamps and durations of the input time series ts

    Args:
        ts (pd.Series):  a time series with index formatted as DatetimeIndex
                         Note that we require the timestamps are evenly spaced,
                         otherwise the result could be misleading

    Returns:
        results (List[Dict[str, Union[pd.Timestamp, pd.Timedelta]]]): each element in a list is a dictionary which
        contain the result of consecutive NaN timestamps, durations result.
        In each dictionary, we have:
            "start" --> pd.Timestamp (the starting timestamp of consecutive NaN)
            "end" --> pd.Timestamp (the ending timestamp of consecutive NaN)
            "duration" --> pd.Timedelta (the duration of this particular consecutive NaN time series segment)
    """

    has_issue = ts.isna()
    has_no_issue = ~ has_issue

    # https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas
    # consec_count is a series, containing the consecutive count of NaN.
    # However at this stage, we do not know which timestamps do these NaN correspond to
    consec_count = has_issue.astype(int).groupby(has_no_issue.astype(int).cumsum()).sum()  # type: pd.Series
    consec_count = consec_count[consec_count != 0]

    # Now, we begin to infer the correct timestamp range of the consecutive count of NaN
    consec_cucount = consec_count.cumsum()
    shifted_index = list(consec_cucount.index[1:] + consec_cucount.values[:-1])
    shifted_index.insert(0, consec_cucount.index[0])
    start_timestamps = has_issue.index[shifted_index]

    # interval is the duration between consecutive_count data points
    # we assume evenly spaced timestamps
    interval = ts.index[1] - ts.index[0]
    interval_seconds = interval.total_seconds()

    durations = pd.to_timedelta(consec_count.values * interval_seconds, unit='s')
    end_timestamps = start_timestamps + durations - pd.to_timedelta(interval_seconds, unit='s')

    # Combine the result to a List of Tuple
    results = []
    for start, end, duration in zip(start_timestamps, end_timestamps, durations):
        results.append({
            "start": start,
            "end": end,
            "duration": duration,
        })

    return results
