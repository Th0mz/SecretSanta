from random import shuffle

class Entities:

    def __init__(self):
        self.entities = {}
        self.shuffledEntities = {}

        self.numberOfEntities = 0

    def addEntity(self, name, email):
        """ Add a new entity to the entities dictionary """ 
        self.entities[email] = name

        self.numberOfEntities = len(self.entities)

    def printEntries(self):
        print(str(self.numberOfEntities) + " Registered Entries :")

        for email in self.entities:
            print("   -> Name : " + self.entities[email] + "  E-mail : " + email)
    
    def printShuffledEntries(self):
        print(str(self.numberOfEntities) + " Registered Entries :")

        for email in self.shuffledEntities:
            print("   -> Name : " + self.shuffledEntities[email] + "  E-mail : " + email)


    def shuffleEntries(self):
        def derangement(keys):
            if self.numberOfEntities <= 1:
                raise ValueError("Cant shuffle dict with less than 1 entry")

            shuffledKeys = list(keys)
            while any(x == y for x, y in zip(keys, shuffledKeys)):
                shuffle(shuffledKeys)

            return shuffledKeys

        self.shuffledEntities = {x : self.entities[y] for x, y in zip(self.entities, derangement(self.entities))}


