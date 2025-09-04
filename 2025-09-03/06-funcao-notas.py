def rfm_score(x, quantiles, col, reverse=False):
    if x <= quantiles[col][0.25]:
        score = 1
    elif x <= quantiles[col][0.5]:
        score = 2
    elif x <= quantiles[col][0.75]:
        score = 3
    else:
        score = 4
    return 5 - score if reverse else score