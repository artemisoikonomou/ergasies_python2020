import random


# Φτιάχνω μια λίστα με 3 στοιχεία που αποτελούν τα φανάρια
# --> κάθε στοιχείο της λίστας θα έχει 3 τιμές "name" : "fanari 1", "cars": 10, "isGreen": True
fanaria = [ { "name":"fanari1", "cars":10, "isGreen": False}, 
            { "name":"fanari2", "cars":20, "isGreen": False},
            { "name":"fanari3", "cars":30, "isGreen": False} ]

def minmaxCars():
    minCars = fanaria[0]["cars"]
    maxCars = fanaria[0]["cars"]
    fanariMax = 0
    for i in range(1,3):
        if fanaria[i]["cars"] < minCars:
            minCars = fanaria[i]["cars"]
        if fanaria[i]["cars"] > maxCars:
            maxCars = fanaria[i]["cars"]
            fanariMax = i
    
    return minCars, maxCars, fanariMax


def populateCars():
    for fanari in fanaria:
        fanari["cars"] = random.randrange(1, 100)

def printFanaria():
    for fanari in fanaria:
        print(f'Name: {fanari["name"]}, Cars: {fanari["cars"]}, Is Green: {fanari["isGreen"]}')

# Ξεκινάει το πρόγραμμα

# Βάζω σε κάθε φανάρι τυχαίο αριθμό αυτοκινήτων (από 1 έως 100)
populateCars()

# Επανέλαβε για όσο κανένα φανάρι δεν έχει μηδέν αυτοκίνητα:
#     Βρές ποιο είναι το φανάρι με τα περισσότερα αυτοκίνητα  
#          --> Κάντο πράσινο
#          --> Να φύγουν τυχαία από 5-10 αυτοκίνητα
#          --> Να διαιρεθούν ακέραια / 2 τα αυτοκίνητα που φύγανε και να πάνε στα άλλα 2 φαναρια
#          --> Τύπωσε για όλα τα φανάρια το όνομα τους, την κατάσταση τους και τα αυτοκίνητα που τώρα έχουν

minCars, maxCars, fanariMax = minmaxCars()       
print(f"minCars {minCars}")
print(f"maxCars {maxCars}")
print(f"Fanari with max {fanariMax}")
printFanaria()
