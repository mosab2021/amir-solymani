class Car:    

    def __init__(self, model, name, color):
        self.__model = model
        self.__name = name
        self.__color = color
    
    def getModel(self):
        return self.__model
    
    @property
    def name(self):
        return self.__name

    # def getName(self):
    #     return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # def setName(self, name)  :
    #     self.__name = name

    @name.deleter
    def name(self):
        del self.__name
    
    def getColor(self):
        return self.__color 
    
    def setModel(self, model):
        self.__model = model  

    
    
    def setColor(self, color):
        self.__color = color

    

prideObj = Car("2020", "PRIDE", "Black")

sahandObj = Car("2024", "sahand", "White")

# prideObj.setName("pride111")
# print(prideObj.getName())


prideObj.name = "pride132"
del prideObj.name
# print(prideObj.name)


print(prideObj.getColor())

prideObj.setModel("1400")
print(prideObj.getModel())
        

sahandObj.name = "sahandIrani"
print(sahandObj.name)