from numpy import arange, mean, median


# numba jit did not help here due to mean(axis) keyword
def realtime_normalization(raw_arr, cnt_samples, normalize_samples, fs,
                           norm_type='mean'):

    if cnt_samples == 0:
        return raw_arr
    if cnt_samples < normalize_samples:
        n_idx = arange(0, cnt_samples, 1)
    else:
        n_idx = arange(cnt_samples - normalize_samples, cnt_samples+1, 1)

    if norm_type == "mean":
        norm_previous = mean(raw_arr[:, n_idx], axis=1)
    elif norm_type == "median":
        norm_previous = median(raw_arr[:, n_idx], axis=1)
    else: 
        raise TypeError("only median and mean are supported as normalization "
                        "method")
    raw_norm = (raw_arr[:, -fs:].T - norm_previous) / norm_previous.T

    return raw_norm.T
