#Program Name: custom-object.py
#Assignment Module 3
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210521

class Purchase(object):
    def __init__(self,amount):
        self.amount = amount
    def calculateTax(self, taxPercent):
            return self.amount * taxPercent/100

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100 + tipPercent/100)

        
