class Skill:

    def __init__(self, description, rate):
        self.description = description
        self.rate = rate

    def printAll2(self):
        print(f"skill: {self.description} rate: {self.rate}")


class Address:

    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __lt__(self, other):
        return self.city < other.city

    def printAll(self):
        print(f"street: {self.street} city: {self.city} state: {self.state} zip: {self.zip}")


class Person:

    def __init__(self, name):
        self.name = name
        self.addressList = []
        self.skillList = []

    def __lt__(self, other):
        return self.name < other.name

    def addAddress(self, address):
        self.addressList.append(address)

    def addSkill(self, skill):
        self.skillList.append(skill)

    def printAll(self):
        print("--- start ---")
        print(f"person, name: {self.name}")
        for ad in sorted(self.addressList):
            ad.printAll()

        for sk in self.skillList:
            sk.printAll2()

        print("--- end ---")



myPeople = [] #list()

p1 = Person("Robert")
myPeople.append(p1) #append(person)

address1 = Address("str", "ci", "state", "9999")
p1.addAddress(address1)

add3 = Address("44/3", "hang dong", "Thailand", "50230")
p1.addAddress(add3)

add4 = Address("str2", "Amsterdam", "Holland", "8888")
p1.addAddress(add4)

p1.addAddress(Address("str3", "buuuhausen", "Germany", "37124"))


skill = Skill("bier saufen", 10)
p1.addSkill(skill)

p2 = Person("Markus")
myPeople.append(p2)

add2 = Address("2542 10th", "Oakland", "Ca", "94606")
p2.addAddress(add2)

skill1 = Skill("senf ", 3)
p2.addSkill(skill1)

skill3 = Skill("C++", 10)
p2.addSkill(skill3)

skill4 = Skill("Python and AI", 8)
p2.addSkill(skill4)

for x in sorted(myPeople):
    x.printAll()