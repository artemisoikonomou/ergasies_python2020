import sys
import os

# Διαβάζω το όνομα του χρήστη από τα command-line arguments
user = sys.argv[1]

# Καλώ τον instagram-crawler με παράμετρο το όνομα του χρήστη και σώζω τα αποτελέσματα σε ένα JSON αρχείο
os.system("python ./instagram-crawler-master/crawler.py posts_full -u " + user + " -n 4 --fetch_comments -o results.json")

# Διαβάζω το JSON αρχείο και βρίσκω από τα comments τον χρήστη με τα περισσότερα

