import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import reader
import pandas as pd
import csv
import re
from urllib.request import urlopen

url = ""

counter = 0

with open('topmillion.csv', newline='') as csvfile:

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

                #print("COUNTER" + str(counter))

                html = page.read().decode("utf-8")
                print(html)
                pattern = "/"
                match_results = re.search(pattern, html, re.IGNORECASE)
                title = match_results.group()
                title = re.sub("<.*?>", "", title) # Remove HTML tags


                file.write("~"*30 + "\r\n")

                file.write(url + "\r\n")


                file.write(html + "\r\n")
                print("Writing: " + html)

                file.write("~"*30)


                counter += 1

            except Exception as inst:
                print("Error opening: " + url)
                print(type(inst))    # the exception instance
                print(inst.args)     # arguments stored in .args
                print(inst)
                counter += 1














