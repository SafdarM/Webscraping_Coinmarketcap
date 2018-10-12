# Webscrapping_Coinmarketcap
This public repository performs web scrapping on the worlds largest "cryptocurrency-trend-analyser" website, www.coinmarketcap.com.

# About Coinmarketcap?
CoinMarketCap is a website that tracks most of the alternative coins that has hit the market as well as Bitcoins and shows users the current value in dollars and Bitcoins for each coin. Also, featues including top gainers/top losers over a 1hr/24hr/7d timeline can be analysed. Currentlt there exists over 2000 cryptocurrencies on CMC portal.

# What does this repo has to do with CMC?
Computer science is all about trends, analysis, prediction and ofcourse logic. To perform such analysis develops seeks for data. The world largest data storage mechanism is the World Wide Web! The Internet. Unfortunate for the developers, this kind of data is not program ready. The Internet data is not relational, and hence there is a need to pre process the raw and ugly data into ready-to-use format.

# Webscrapping_Coinmarketcap - Crutches for prediction algorithms:
Webscrapping_Coinmarketcap is a simple web scrapper which fetches information not only about top gainers/top losers over a 1hr/24hr/7d timeline, but also about thousands of currently trading altcoins. Using Webscrapping_Coinmarketcap you can get information about changes in:
- Price
- Volume
- Percentage

over a range of timelines. This data can be formed as the crux of predicting algorithms. 

# Libraries used:
- Pandas
- bs4 (BeautifulSoup)

# Python version:
- 2.7.8

# Sample output dataframe of cryptocurrency_get():
After successfully importing CoinMarketCapScrapper
```python
ob = CoinMarketCapScrapper()
print ob.trending_currency_get()
```
![image](https://user-images.githubusercontent.com/14060853/46869725-57c17c80-ce4a-11e8-9100-39317aa3da60.png)

**Note: The actual API gives 100's of rows.**
