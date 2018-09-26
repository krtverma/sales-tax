class Bill():
    sumuation=0
    def product_detail(self):
        product_price=float(input("enter the normal product which tax is 10%"))
        with_tax_product_price=(product_price*(10/100))
        print(with_tax_product_price)
        self.sumuation+=with_tax_product_price
       

    def Tax_Free_Product(self):
        tax_free_price=float(input("enter the product which tax is free"))
        self.sumuation+=tax_free_price
        print(tax_free_price)

    def Imported_Product(self):
        imported_Product=float(input("enter the price"))
        with_tax_Imported_product_price=(imported_Product*(5/100))
        self.sumuation+=with_tax_Imported_product_price
        print(with_tax_Imported_product_price)

    def summ(self):
        print(self.sumuation)

b=Bill()
b.product_detail()
b.Tax_Free_Product()
b.Imported_Product()
b.summ()






 