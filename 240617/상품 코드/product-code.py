class product:
    def __init__(self, productName, productCode):
        self.productName = productName
        self.productCode = productCode
    

product1 = product("codetree", 50)
print(f'product {product1.productCode} is {product1.productName}')
productName, productCode = input().split()
product2 = product(productName, productCode)
print(f'product {product2.productCode} is {product2.productName}')