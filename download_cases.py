import requests
import os
import csv

# CSV file containing URLs
csv_file_path = "court_cases.csv"

output_folder = "court_cases"
os.makedirs(output_folder, exist_ok=True)

# read URLs from the CSV file, 
# skipping the first, second-to-last, and last lines
# first line contains column names, last two 
# lines contains data for Table 1 in the paper
urls = []
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    for row in rows[1:-2]:  # Skip first, second-to-last, and last rows
        url = row[0].strip()
        # just sanity check below
        if url.startswith("http://") or url.startswith("https://"):
            urls.append(url)

for url in urls:
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        # use last part of the URL as the filename
        filename = url.split('/')[-1]  
        filepath = os.path.join(output_folder, filename)

        # save the content to file
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {url} to {filepath}")

    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

