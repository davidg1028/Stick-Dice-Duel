
class Fighters():
    
    def __init__(self, *args):
        
        length = len(args)
        if length == 6: #overload constructor
            self.name = args[0]
            self.hpBar = args[1]
            self.super = args[2]
            self.roll1 = args[3]
            self.basic = args[4]
            self.roll2 = args[5]
        elif length == 0: #default constructor
            self.name = ""
            self.hpBar = 0
            self.super = ""
            self.roll1 = 0
            self.basic = ""
            self.roll2 = 0

    #--------getters--------
    def getName(self):
        return self.name
        
    def getHpBar(self):
        return self.hpBar
    
    def getSuper(self):
        return self.super
        
    def getRoll1(self):
        return self.roll1
        
    def getBasic(self):
        return self.basic
    
    def getRoll2(self):
        return self.roll2
        
    def getItem(self):
        return self.item
    #----------setters--------  
    def setName(self, name):
        self.name = name
        
    def setHpBar(self, hpBar):
        self.hpBar = hpBar
        
    def setSuper(self, super):
        self.super = super
    
    def setRoll1(self, roll1):
        self.roll1 = roll1
        
    def setBasic(self, basic):
        self.basic = basic
        
    def setRoll2(self, roll2):
        self.roll2 = roll2
        
    def setItem(self, item):
        self.item = item
    #---------str----------
    def __str__(self):
        return "Name: " + self.name + \
               "\nHP Bar: " + self.hpBar + \
               "\nSuper: " + self.super + \
               "\nCost: " + str(self.roll1) + \
               "\nBasic: " + self.basic + \
               "\nCost: " + str(self.roll2)
