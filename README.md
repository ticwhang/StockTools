# StockTools

## Prerequisite
安裝yfinance

```
pip install yfinance --upgrade --no-cache-dir
```

安裝yahoo_fin
```
pip install yahoo-fin --upgrade --no-cache-dir
```


## 使用方式

取得S&P 500股票清單：

```
import tools
SP500Tickers = tools.getTickersListSP500()
```
```
print(SP500Tickers)

['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD
...
```

取得那斯達克股票清單
```
import tools
SP500Tickers = tools.getTickersListNasdq()
```
```
print(NasdqaTickers)

['AACG', 'AACI', 'AACIU', 'AACIW', 'AADI', 'AADR', 'AAL', 'AAME', 'AAOI', 'AAON', 'AAPB', 'AAPD', 'AAPL', 'AAPU', 'AATC', 'AAWW', 'AAXJ', 'ABCB', 'ABCL', 'ABCM', 'ABEO', 'ABGI', 'ABIO', 'ABMD', 'ABNB', 'ABOS', 'ABSI', 'ABST', 'ABTX', 'ABUS', 'ABVC', 'ACAB', 'ACABU', 'ACABW', 'ACAC', 'ACACU', 'ACA
...
```

取得道瓊指數成份股清單
```
import tools
Dowickers = tools.getTickersListDow()
```
```
print(Dowickers)
['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
```

取得股票指定日期的價格(當日收盤價)
```
import tools

price = tools.getPriceByDate('SPY','2020-02-22')
print(price)

[*********************100%***********************]  1 of 1 completed
333.4800109863281
```
取得股票在指定時間內價格變化百分比

```
import tools

priceChangePercent = tools.getPriceChangePercent('SPY','2020-02-19','2020-05-20')
print(priceChangePercent)
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
-13.292551392885008
```


