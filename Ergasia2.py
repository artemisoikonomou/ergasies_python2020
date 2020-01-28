words = []
letters = ['f','c','k','r'] 

def readFile():
    fp=open('words.txt','r')
    lines = fp.readlines()
    for line in lines:
        for word in line.split(" "):
            words.append(word.replace('\n',''))

def returnthesums(word):
    goodLetters = 0
    badLetters  = 0
    
    for c in word:
        badLetterFound = False
        for l in letters:
            if c.lower()==l:
                badLetterFound = True    # Bad letter found 
                break
            else:
                badLetterFound = False   # Normal letter

        if not badLetterFound :
          goodLetters += 1
        else:
          badLetters += 1

    return badLetters, goodLetters

def findthebadorgoodword():
    for word in words:
        badLetters, goodLetters = returnthesums(word)
        if badLetters > goodLetters :
            print("Bad word: " + word)
        else:
            print("Good word: " + word)

readFile()
findthebadorgoodword()
