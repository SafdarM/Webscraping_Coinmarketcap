from bs4 import BeautifulSoup
from pandas import DataFrame
import re
import urllib2
import utility


class CoinMarketCapScrapper:
    def __init__(self):
        self.MARKET_PAGE = 'https://coinmarketcap.com/currencies/bitcoin/#markets'
        self.CRYPTOCURRENCY = 'https://coinmarketcap.com/all/views/all/'
        self.GAINER_LOSER = 'https://coinmarketcap.com/gainers-losers/'

    def bitcoin_market_get(self):
        """
        This method returns information about bitcoin market as per coinmarket.com

        :return: Bitcoin market details in the form of a dataframe.
        """
        data_frame_input_list = []

        try:
            page = urllib2.urlopen(self.MARKET_PAGE)
        except:
            raise AssertionError('https://coinmarketcap.com/currencies/bitcoin/#markets is currently unreachable.')

        soup = BeautifulSoup(page, 'html.parser')
        ROW_DATA_LIST = soup.find_all('tr')
        row_header = ROW_DATA_LIST[0].get_text().strip().lower().replace(' ','_').replace('#','sno').encode('utf-8').split()

        if isinstance(ROW_DATA_LIST, list):
            for row in ROW_DATA_LIST[1:]:
                text = re.sub(r'\n+','\n',row.get_text().encode('utf-8').strip().replace('*','').replace(' ','_'))
                data_frame_input_list.append(text.split()[:-1])
        df = DataFrame.from_records(data_frame_input_list, columns=row_header, nrows=False)
        df.reset_index(drop=True, inplace=True)
        return df

    def cryptocurrency_get(self):
        """
        This method returns information of all the cryptyocurrencies trading on coimarketcap.com

        :return: Cryptocurrency details in the form of a dataframe
        """
        data_frame_input_list = []
        try:
            page = urllib2.urlopen(self.CRYPTOCURRENCY)
        except:
            raise AssertionError('https://coinmarketcap.com is currently unreachable.')

        soup = utility.soup_maker(page)
        ROW_DATA_LIST = soup.find_all('tr')
        row_header = ROW_DATA_LIST[0].get_text().strip().lower().replace('#','sno').replace(' ','_').encode('utf-8').split()
        row_header.insert(1, 'symbol')
        row_header.pop(3)
        if isinstance(ROW_DATA_LIST, list):
            for row in ROW_DATA_LIST[1:]:
                text = ' '.join(re.sub('\n+', '\n', row.get_text().encode('utf-8').replace('*','').
                                       replace('Vol','').replace('Low','Low_Volume')).split()[:-19]).split()
                text.pop(3)
                if len(text)>len(row_header):
                    for index, item in enumerate(text):
                        if 'low' in item.lower() and len(text)==11:
                            text[index:index+2] = ['_'.join(text[index:index+2])]
                        if list(item)[0] != '$':
                            continue
                        else:
                            text[2:index] = ['_'.join(text[2:index])]
                        break
                null_checker = text
                if '?' not in ''.join(null_checker) and len(text)==len(row_header):
                    data_frame_input_list.append(text)

        df = DataFrame.from_records(data_frame_input_list, columns=row_header, nrows=False)
        df.reset_index(drop=True, inplace=True)
        return df

    def trending_currency_get(self, mode='gainer', time='7d'):
        """
        This method fetched the gainers/losers details.

        *Parameters*:
        :param mode: Possible values are <gainer/loser>
        :param time: Possible value are <1h/24h/7d>

        :return:    Dataframe containing loser/gainer details
        """
        data_frame_input_list = []
        try:
            page = urllib2.urlopen(self.GAINER_LOSER)
        except:
            raise AssertionError('https://coinmarketcap.com/gainers-losers/ is currently unreachable.')

        soup = BeautifulSoup(page, 'html.parser')
        ROW_DATA_LIST = soup.find_all('tr')

        start, stop = utility.start_stop(mode, time)

        row_header = ROW_DATA_LIST[start].get_text().strip().lower().replace('#','sno').replace(' ','_').encode('utf-8').split()
        if isinstance(ROW_DATA_LIST, list):
            for row in ROW_DATA_LIST[start+1:stop]:
                text = ' '.join(re.sub('\n+', '\n', row.get_text().encode('utf-8').replace('*', '')).split()).split()
                if len(text)>len(row_header):
                    for index, item in enumerate(text):
                        if list(item)[0] != '$':
                            continue
                        else:
                            text[1:index-1] = ['_'.join(text[1:index-1])]
                            break
                data_frame_input_list.append(text)

        df = DataFrame.from_records(data_frame_input_list, columns=row_header, nrows=False)
        df.reset_index(drop=True, inplace=True)
        return df
