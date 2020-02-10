import random

# Φτιάχνω μια λίστα με 3 στοιχεία που αποτελούν τα φανάρια
# --> κάθε στοιχείο της λίστας θα έχει 3 τιμές "name" : "fanari 1", "cars": 10, "isGreen": True
fanaria = [ { "name":"fanari1", "cars":10, "isGreen": False}, 
            { "name":"fanari2", "cars":20, "isGreen": False},
            { "name":"fanari3", "cars":30, "isGreen": False} ]

def maxCars():
    maxCars = fanaria[0]["cars"]
    fanariMax = 0
    for i in range(1,3):
        if fanaria[i]["cars"] > maxCars:
            maxCars = fanaria[i]["cars"]
            fanariMax = i
    
    return fanariMax

def comeGo(isGreen):
    come=0
    go=0
    if isGreen==True:
        go = random.randrange(5, 10)
    else:
        come = random.randrange(0, 5)

    return come,go


def populateCars():
    for fanari in fanaria:
        fanari["cars"] = random.randrange(1, 20)

def printFanaria():
    print("FANARIA STATUS --------------------------------------------------------")
    for fanari in fanaria:
        print(f'Name: {fanari["name"]}, Cars: {fanari["cars"]}, Is Green: {fanari["isGreen"]}')
    print("FANARIA STATUS END --------------------------------------------------------")

# Ξεκινάει το πρόγραμμα
random.seed()

# Βάζω σε κάθε φανάρι τυχαίο αριθμό αυτοκινήτων (από 1 έως 100)
populateCars()

# Επανέλαβε για όσο κανένα φανάρι δεν έχει μηδέν αυτοκίνητα:
while fanaria[0]["cars"]!=0 and fanaria[1]["cars"] !=0 and fanaria[2]["cars"]!=0 :
    
    # printFanaria() --> Για να ελέγξουμε τον αλγόριθμο σε κάθε στάδιο
    
    #     Βρές ποιο είναι το φανάρι με τα περισσότερα αυτοκίνητα
    fanariMax = maxCars()  

    #     --> Κάντο πράσινο
    fanaria[fanariMax]["isGreen"] = True

    #     --> Να φύγουν τυχαία από 5-10 αυτοκίνητα από το πράσινο φανάρι
    come, go = comeGo(fanaria[fanariMax]["isGreen"])
    print(f'Name: {fanaria[fanariMax]["name"]}, Cars: {fanaria[fanariMax]["cars"]}, Is Green: {fanaria[fanariMax]["isGreen"]}, Cars coming: {come}, Cars Leaving: {go}')
    if fanaria[fanariMax]["cars"] - go >= 0:
        fanaria[fanariMax]["cars"] = fanaria[fanariMax]["cars"] - go

    #     --> Να μπουν τυχαία από 0-5 αυτοκίνητα στα άλλα φανάρια
    for i in range(0,3):
        if(i!=fanariMax):
            come, go = comeGo(fanaria[i]["isGreen"])
            print(f'Name: {fanaria[i]["name"]}, Cars: {fanaria[i]["cars"]}, Is Green: {fanaria[i]["isGreen"]}, Cars coming: {come}, Cars Leaving: {go}')
            fanaria[i]["cars"] = fanaria[i]["cars"] + come
    
    fanaria[fanariMax]["isGreen"] = False

