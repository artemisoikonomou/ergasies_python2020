import sys
import os
import json
from collections import Counter

# Διαβάζω το όνομα του χρήστη από τα command-line arguments
user = sys.argv[1]
authors = []

# Καλώ τον instagram-crawler με παράμετρο το όνομα του χρήστη και σώζω τα αποτελέσματα σε ένα JSON αρχείο
os.system("python ./instagram-crawler-master/crawler.py posts_full -u " + user + " -n 100 --fetch_comments -o results.json")

# Διαβάζω το JSON αρχείο και βρίσκω από τα comments τον χρήστη με τα περισσότερα σχόλια

fp = open('results.json','r', 1,'utf-8')
x = json.dumps(json.load(fp))
myJson = json.loads(x)

for rec in myJson:
    for comment in rec["comments"]:
        authors.append(comment["author"])

authKeys = Counter(authors).keys()
authCounts = Counter(authors).values()
m = max(authCounts)

for key, value in Counter(authors).items():
    if value==m:
        print("User with most comments is: " + key)
        break


