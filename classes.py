class Product:
    def __init__(self, uid, name, price, type, stock, size):
        self.uid = uid
        self.name = name
        self.price = price
        self.type = type
        self.size = size
        self.stock = stock

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name
    
    def getEnable(self):
        return self.stock > 0

newProduct = Product('ARC203', 'Think Python', 40, 'book', 12, 'medium')
newProduct.setName('Computer Vision')

print(newProduct.getName())

