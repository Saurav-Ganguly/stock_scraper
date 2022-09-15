import requests
from datetime import datetime
import time

# from_date = input("Enter start date in yyyy/mm/dd format: ")
# to_date = input("Enter end date in yyyy/mm/dd format: ")
tickers = ["TCS.NS", "AAPL", "GOOG"]
from_date = '2021/09/13'
to_date = '2022/09/13'

from_date_format = datetime.strptime(from_date, '%Y/%m/%d')
to_date_format = datetime.strptime(to_date, '%Y/%m/%d')
#epoch time
epoch_from_date = int(time.mktime(from_date_format.timetuple()))
epoch_to_date = int(time.mktime(to_date_format.timetuple()))

#forbidden as script is not allowed to download file
#imporsonate a browser
headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

#write the file
for ticker in tickers:
  url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={epoch_from_date}&period2={epoch_to_date}&interval=1d&events=history&includeAdjustedClose=true"
  content = requests.get(url, headers=headers).content
  with open(f"{ticker}.csv", "wb") as file:
    file.write(content)
