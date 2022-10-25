from tqdm import tqdm
from zipfile import ZipFile
import requests
import os

url = "https://www.axiory.com/jp/assets/download/historical/mt4_standard/2022/XAUUSD.zip" #big file test
filepath = "historical_data/xauusd2022.zip"

if not os.path.isfile(filepath):
    # Streaming, so we can iterate over the response.
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(filepath, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

with ZipFile(filepath, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    zipObj.extractall("historical_data")

