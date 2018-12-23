import requests
import json
import pandas as pd

url = "https://www.bestproducts.com/ajax/contentmedia/?id=da8cafb3-4124-4da3-abbd-4bfbe843b026&start=0&limit=101&fbclid=IwAR3OxS9lmdq9YueSDwd0sz_fA8vkvcNYNFXkwtvSsLUOZ18FkkCdt0kG7fs"
r = requests.get(url)

content = json.loads(r.text)

prod_names = [content[i]['data']['product']['name'] for i in range(len(content)-1)]

data_price = [content[i]['data']['product']['priceNoSymbol'] for i in range(len(content)-1)]
data = pd.DataFrame(
    {'prod_names':prod_names,
    'prod_price': data_price}
    )

data.to_csv('100.csv', encoding='utf-8-sig')