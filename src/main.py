from data.downloader import download_stock

apple = download_stock("AAPL")

print(apple.head())