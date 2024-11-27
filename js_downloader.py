import os
import requests

folder_name = "js_files"
os.makedirs(folder_name, exist_ok=True)

with open("jsfiles.txt", "r") as file:
    urls = file.read().splitlines()

for url in urls:
    try:
        filename = os.path.join(folder_name, url.split('/')[-1])
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
