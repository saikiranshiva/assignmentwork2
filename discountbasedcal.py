amt = int(input("Enter Parchases Amount: "))
if(amt>0):
    if amt<=1000:
       disc = amt
    elif amt<=2000:
        disc=amt*0.10
    elif amt<=3000:
        disc=0.2 * amt
    else:
         disc=0.25 * amt

    print("Discount : ",disc)
    print("Total_bill Pay  : ",amt-disc)
else:
    print("Invalid Amount")
