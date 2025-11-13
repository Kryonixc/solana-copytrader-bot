def dynamic_stoploss(price, trail_percent=0.2):
    stop = price * (1 - trail_percent)
    return stop
