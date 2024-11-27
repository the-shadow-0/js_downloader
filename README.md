Description

This Python script downloads JavaScript files from a list of URLs provided in a text file (jsfiles.txt). The script automatically creates a folder named js_files (if it doesn't already exist) and saves the downloaded JavaScript files into that folder. If a download fails, it catches the error and prints a message detailing which URL failed to download.
Requirements

To run this script, you need to have Python 3.x installed along with the requests library. If you don't have the requests library installed, you can install it via pip:

pip install requests

Files

    jsfiles.txt: This file should contain one URL per line. The URLs should point to raw JavaScript files (e.g., https://example.com/script.js).
    js_files/: This folder is created by the script and will store all the downloaded JavaScript files.

How it Works

    The script reads the URLs from jsfiles.txt, which should be placed in the same directory as the script.
    For each URL in the list, the script:
        Fetches the JavaScript file using an HTTP GET request.
        Saves the file into the js_files folder using the filename derived from the URL (the part after the last /).
        If the file is successfully downloaded, a message is printed with the filename.
        If the download fails (due to a network issue or invalid URL), an error message is printed.

How to Run

    Place the jsfiles.txt file with the list of URLs in the same directory as the script.
    Run the script with Python:

python download_js_files.py

    After the script runs, check the js_files folder for the downloaded files.

Example
jsfiles.txt:

https://example.com/script1.js
https://example.com/script2.js
https://example.com/script3.js

Output:

Downloaded: js_files/script1.js
Downloaded: js_files/script2.js
Failed to download https://example.com/script3.js: 404 Client Error: Not Found for url: https://example.com/script3.js
