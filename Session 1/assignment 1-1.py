def calculateVAT(amount):
    totalAmount = float(amount) * 1.21
    return totalAmount

amount = input("Enter amount to calculate VAT: ") # can put line in calculateVAT function 
print(int(calculateVAT(amount)))