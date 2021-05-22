from bs4 import BeautifulSoup as bs
from requests.api import get
import sys
import os

# sys.stdout = open("link.txt", "w")

folder = "./content/Tugas-Besar-Bs4-1914311046/"
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

# sys.stdout.close()