class product:
    def __init__(self, productName="codetree", productCode=50):
        self.productName = productName
        self.productCode = productCode
    

product1 = product()
print(f'product {product1.productCode} is {product1.productName}')
productName, productCode = input().split()
product1 = product(productName, productCode)
print(f'product {product1.productCode} is {product1.productName}')