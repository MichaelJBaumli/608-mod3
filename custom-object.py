#Program Name: custom-object.py
#Assignment Module 3
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210521

#This is a copy and paste from https://nwmissouri.instructure.com/courses/37830/pages/module-3-project-purchase-object-methods

class Purchase(object):
    def __init__(self,amount):
        self.amount = amount
    def calculateTax(self, taxPercent):
            return self.amount * taxPercent/100

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100 + tipPercent/100)

        
#Create Purchase object given an amount
purchase = Purchase(100.0)

# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Set the object to aclculate the tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Display some useful information

print(f'Tax: ${tax:0.2f}')
print(f'Tip: ${tip:0.2f}')
print(f'Total: ${purchase.calculateTotal(taxPercent,tipPercent):0.2f}')





