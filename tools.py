import yfinance as yf
from yahoo_fin import stock_info as si

def getPriceByDate(ticker,date):
    try:  
        data = yf.download(ticker, start=date, end=date)
    except:
        # print("ticker not found")
        return -1
        
    if data is None:
        # print("ticker not found data value is None")
        return -1
    if data['Close'] is None:
        # print("data close value is None")
        return -1
    if len(data['Close'].values) == 0:
        # print("data close value empty")
        return -1
        
    return data['Close'].values[0]

def getPriceChangePercent(ticker,startDate,endDate):
    # ticker = 'SPY'
    # startDate='2020-02-19'
    # endDate='2020-05-20'
    startDatePriceValue = getPriceByDate(ticker,startDate)
    if startDatePriceValue == -1:
        print("startDatePriceValue not exist")
        return -1000
    
    endDatePriceValue = getPriceByDate(ticker,endDate)
    if endDatePriceValue == -1:
        print("endDatePriceValue not exist")
        return -1000
    priceChangePercent= ((endDatePriceValue-startDatePriceValue)/startDatePriceValue)*100
    return priceChangePercent

def getTickersListSP500():
    return si.tickers_sp500()

def getTickersListNasdq():
    return si.tickers_nasdaq()

def getTickersListDow():
    return si.tickers_dow()

def getTickersListOthers():
    return si.tickers_other()
