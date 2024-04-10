class Weapon():
    name = "name"
    type = ""
    damage = 0
    cost = 0
    critical = 0
    range = ""
    weight = 0
    usage = ""
    special =[]

    def __init__(self,name,type,damage,cost,critical,special):
        self.name = name
        self.type = type
        self.damage = damage
        self.cost = cost
        self.critical = critical
        self.special = special

    def Information(self):
        print("""
        Weapon Details:
            Weapon Name = {}
            Weapon Type = {}
            Weapon Damage = {}
            Weapon Cost = {}
            Weapon Critical = {}
        """.format(self.name,self.type,self.damage,self.cost,self.critical))

    def addEnchantment(self,enchant):
        print("Enchanting the Weapon...")
        self.damage += enchant

    def newSpecialAbility(self,newAbility):
        print("Magical Ability Adding...")
        self.special.append(newAbility)

weapon1 = Weapon()
weapon2 = Weapon()
greatsword = Weapon("TwoHanded",12,50,2)
dagger = Weapon("OneHandLight",4,5,2)

print(greatsword.cost)