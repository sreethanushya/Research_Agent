import yfinance as yf
import wikipedia
def company_data(company):
    info={}
    ticker_map={"apple":"AAPL","tesla":"TSLA","microsoft":"MSFT","google":"GOOGL","amazon":"AMZN","meta":"META","nvidia":"NVDA"}
    symbol=ticker_map.get(company.lower(),company)
    try:
        ticker=yf.Ticker(symbol)
        info=ticker.info
    except Exception as e:
        print(e)
    try:
        summary=wikipedia.summary(company,sentences=3)
    except:
        summary="Summary unavailable"
    data={"company":company,"industry":info.get("industry","unknown"),"employees":info.get("fullTimeEmployees","unknown"),"market_cap":info.get("marketCap","unknown"),"revenue":info.get("totalRevenue","unknown"),"website":info.get("website","unknown"),"gross_profit":info.get("grossProfits","unknown"),"operating_expense":info.get("operatingExpense","unknown"),"summary":summary}
    return data