# robot-skimmer


This is a robots.txt scraper spider scripted in Python.


For now, it will only look for the robots.txt file in the world’s top million websites and writes every line containing the char ```/```. This allows the analysis and later tweaking of the code to search for specific strings of phrases of interest.

The code can be found below:

```Python

from urllib.request import urlopen
from csv import reader
import csv
import re
from urllib.request import urlopen

url = ""
counter = 0
with open('topmillion.csv', newline='') as csvfile: # Allows top million url's to be read directly from and excel sheet or .csv file
    with open('scraped_robots.txt', 'w') as file:
        data = csv.DictReader(csvfile)
        print("|--------------------------|")
        print("| ~~~~~ Scrape Time! ~~~~~ |")
        print("|--------------------------|")
        for row in data:
            if counter == 10:
                break
            url = "https://www." + row['URL'] + '/robots.txt'
            try:
                page = urlopen(url)
                html = page.read().decode("utf-8")
                print(html)
                pattern = "/"
                match_results = re.search(pattern, html, re.IGNORECASE)
                title = match_results.group()
                title = re.sub("<.*?>", "", title) # Remove HTML tags
                file.write("~"*30 + "\r\n")
                file.write(url + "\r\n")  # Simple formating to view contents of robots.txt files by site much easier
                file.write(html + "\r\n")
                print("Writing: " + html)
                file.write("~"*30)
                counter += 1
            except Exception as inst:
                print("Error opening: " + url)
                counter += 1


```
