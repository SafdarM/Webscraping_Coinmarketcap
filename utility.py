from bs4 import BeautifulSoup

def start_stop(mode, time):
    start = None
    stop = None
    if mode.lower() == 'gainer':
        if time.lower() == '1h':
            start = 0
            stop = 31
        elif time.lower() == '7d':
            start = 31
            stop = 62
        elif time.lower() == '24h':
            start = 62
            stop = 93
        else:
            raise AssertionError('Invalid time parameter. time can be 1h or 24h or 7d.')
    elif mode.lower() == 'loser':
        if time.lower() == '1h':
            start = 93
            stop = 124
        elif time.lower() == '7d':
            start = 124
            stop = 155
        elif time.lower() == '24h':
            start = 155
            stop = 186
    else:
        raise AssertionError('Invalid mode. Mode can either be "gainer" or "loser"')
    if start is not None and stop is not None:
        return start, stop
    else:
        raise AssertionError('Error encountered in indexing gainer loser page.')


def soup_maker(page):
    try:
        soup = BeautifulSoup(page, 'html.parser')
        return soup
    except:
        raise AssertionError('IncompleteRead error. File too larger to handle')