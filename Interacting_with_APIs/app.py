import time
from libs.openexchange import OpenExchangeClient

APP_ID = "b0febbe1946241fc88b113656f3e1290"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

for _ in range(100):
    start = time.time()
    gbp_amount = client.convert(usd_amount, "USD", "GBP")
    end = time.time()
    print(end - start)

print(f'USD: {usd_amount:.2f}, GBP: {gbp_amount:.2f}')
