# Created By Baghas at 5th Mei 2021

from bs4 import BeautifulSoup as bs
from requests.api import get
import sys
import os

DOMAIN = "https://www.wavsource.com"
TIPEFILE = ".wav"
sys.stdout = open("link.txt", "w")

folder = "C:\\Users\\Baghas\\Documents\\MRIS\\web_scraping\\tugas2"
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        fname = os.path.join(folder, filename)
        # print("Filename: {}".format(fname))

        with open(fname, "r") as f:
            soup = bs(f.read(), "html.parser")
            info = soup.find_all("a", href=True)

        for i in info:
            new = i.get("href")
            if "https://www.wavsource.com/snds_2020-10-01" in new:
                print(new)


# file = open("page1.html", "r")
# sys.stdout = open("test.txt", "w")
# soup = bs(file, "html.parser")
# for a in soup.find_all("a", href=True):


sys.stdout.close()