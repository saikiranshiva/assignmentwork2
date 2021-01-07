units=int(input("Number of unit consumed: "))
if(units>0 and units<=50):
    payAmount=units*3.0
    fixedcharge=25.00
elif(units>51 and units<=100):
    payAmount=(51*3.0)+(units-51)*6
    fixedcharge=50.00
elif(units>101 and units<=150):
    payAmount=(51*3.0)+(101-51)*6.0+(units-101)*9.0
    fixedcharge=75.00
elif(units>151 and units<=200):
    payAmount=(51*3.0)+(101*6)*6.0+(151-101)*9.0+(units-151)*12.0
    fixedcharge=100.00
elif(units>201):
    payAmount=2500;
    fixedcharge=125.00
else:
    payAmount=0;
    
Total= payAmount+fixedcharge
print("\nElecticity bill pay=%.2f: " %Total);